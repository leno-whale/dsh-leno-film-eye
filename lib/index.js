/**
 * dsh-leno-film-eye 0.1.0 — P0：用本地文件看一部片子的「连续、声音、节奏」。
 *
 * 它不判断好看，也不算分。它只把三样东西摆出来：
 *   1. 连续的画面（固定间隔拼图，不是只拍剪辑点）
 *   2. 声音的形状（哪几段静了、整体多响）
 *   3. 剪的节奏（切了几次、每段多长）
 *
 * 看片的判断仍然是人（我）来做。工具只负责别让我只看见摘要。
 */
export const VERSION = '0.2.1';
export const name = 'leno-film-eye';
export const inject = ['tools'];

// 宿主对 output 有两条硬要求（0.1.0 首装时踩过第一条：报 `content.some is not a function`）：
//   1) render 必须返回**内容数组**（[{ type:'text', text }]），返回字符串会在宿主侧炸；
//   2) schema 要声明自己返回的键，多余键靠 additionalProperties 放行。
const OUTPUT_SCHEMA = {
  type: 'object',
  additionalProperties: true,
  required: ['ok', 'text'],
  properties: {
    ok: { type: 'boolean' },
    text: { type: 'string' },
  },
};

function field(type, description, extra = {}) {
  const f = { type, description };
  if (extra.enumValues) f.enum = extra.enumValues;
  return f;
}

/** 属性级 required 宿主不认，统一收成顶层数组。 */
function normalize(properties) {
  const required = [];
  const out = {};
  for (const [k, v] of Object.entries(properties || {})) {
    const { required, ...rest } = v || {};
    if (required) required.push(k);
    out[k] = rest;
  }
  return { properties: out, required };
}

/** 宿主调 render(args, value)，必须拿到内容数组。 */
function render(_args, value) {
  return [{ type: 'text', text: String(value?.text ?? '') }];
}

function def(toolName, description, properties, execute) {
  const { properties: props, required } = normalize(properties);
  return {
    name: toolName,
    description,
    parameters: {
      type: 'object',
      additionalProperties: false,
      properties: props,
      ...(required.length ? { required } : {}),
    },
    output: { schema: OUTPUT_SCHEMA, render },
    execute,
  };
}

const pass = (text, extra = {}) => ({ ok: true, text, ...extra });
const fail = (text) => ({ ok: false, text });

export function apply(ctx, config = {}) {
  if (!ctx?.tools?.register) throw new Error('film-eye 需要 tools 段：inject 里必须有 "tools"');

  const defaultMax = Number(config.sheetsPerCall ?? 3);
  const defaultInterval = Number(config.intervalSec ?? 8);

  ctx.tools.register(
    def(
      'film_sheets',
      '把一段视频按固定间隔抽帧、九张拼一页（连续画面，不是只拍剪辑点）。写完返回图片路径，用 read_image 打开。',
      {
        file: field('string', '视频文件绝对路径', { required: true }),
        from: field('number', '从第几秒开始（默认 0）'),
        to: field('number', '到第几秒结束（默认片尾）'),
        interval: field('number', `每几秒抽一帧（默认 ${defaultInterval}）`),
        max: field('number', `最多出几页（默认 ${defaultMax}）`),
        outDir: field('string', '图片输出目录（默认 .film-eye-sheets）'),
      },
      async (args) => {
        const { sheets } = await import('./film.js');
        const r = sheets(String(args?.file ?? ''), {
          from: Number(args?.from ?? 0),
          to: args?.to == null ? null : Number(args.to),
          interval: Number(args?.interval ?? defaultInterval),
          max: Number(args?.max ?? defaultMax),
          outDir: args?.outDir ? String(args.outDir) : undefined,
        });
        if (!r.ok) return fail(`抽帧失败：${r.error}`);
        return pass(
          `出了 ${r.count} 页（每页 ${r.grid}×${r.grid}，约 ${r.interval * r.grid * r.grid} 秒/页，覆盖 ${r.coveredSec}/${r.totalSec} 秒）\n` +
            r.files.map((f) => `- ${f}`).join('\n') +
            (r.note ? `\n${r.note}` : ''),
          { files: r.files }
        );
      }
    )
  );

  ctx.tools.register(
    def(
      'film_audio',
      '量声音的形状：哪几段是静的（silencedetect）、整体多响（volumedetect）。文字转写里「他说不下去」和「他停了两秒」是同一句，在曲线上是两件事。',
      {
        file: field('string', '视频文件绝对路径', { required: true }),
        from: field('number', '从第几秒开始（默认 0）'),
        to: field('number', '到第几秒结束（默认片尾）'),
        noiseDb: field('number', '低于多少 dB 算静（默认 -40）'),
        minSilence: field('number', '至少静几秒才算一段（默认 0.5）'),
      },
      async (args) => {
        const { audioProfile } = await import('./film.js');
        const r = audioProfile(String(args?.file ?? ''), {
          from: Number(args?.from ?? 0),
          to: args?.to == null ? null : Number(args.to),
          noiseDb: Number(args?.noiseDb ?? -40),
          minSilence: Number(args?.minSilence ?? 0.5),
        });
        if (!r.ok) return fail(`量声音失败：${r.error}`);
        const lines = [
          `时长 ${r.duration} 秒｜平均 ${r.meanDb ?? '?'} dB｜峰值 ${r.maxDb ?? '?'} dB`,
          `静段 ${r.silences.length} 段：`,
          ...r.silences.slice(0, 12).map((s) => `- ${s.start}s → ${s.end ?? '到片尾'}s（${s.seconds ?? '?'} 秒静）`),
          r.silences.length > 12 ? `…还有 ${r.silences.length - 12} 段` : '',
        ];
        return pass(lines.filter(Boolean).join('\n'), { data: r });
      }
    )
  );

  ctx.tools.register(
    def(
      'film_shots',
      '数镜头：切在哪里、每段多长、每分钟切几次。节奏是能算的，不用猜。',
      {
        file: field('string', '视频文件绝对路径', { required: true }),
        threshold: field('number', '场景变化阈值 0–1（默认 0.3，越大越只抓硬切）'),
        from: field('number', '从第几秒开始（默认 0）'),
        to: field('number', '到第几秒结束（默认片尾）'),
      },
      async (args) => {
        const { shots } = await import('./film.js');
        const r = shots(String(args?.file ?? ''), {
          threshold: Number(args?.threshold ?? 0.3),
          from: Number(args?.from ?? 0),
          to: args?.to == null ? null : Number(args.to),
        });
        if (!r.ok) return fail(`数镜头失败：${r.error}`);
        return pass(
          `${r.shotCount} 个镜头 / ${r.duration} 秒（平均 ${r.avgShotSec} 秒，最长 ${r.longestShotSec} 秒，每分钟切 ${r.cutsPerMinute} 次）\n` +
            `切点：${r.cuts.slice(0, 24).join(', ')}${r.cuts.length > 24 ? ` …共 ${r.cuts.length} 个` : ''}`,
          { data: r }
        );
      }
    )
  );

  ctx.tools.register(
    def(
      'film_align',
      '把「时间 / 音量 / 切点 / 帧」放到同一张表上。单看画面会漏掉声音的变化，单看声音不知道画面在干什么；对齐之后才能看出它们是不是同一个动作。',
      {
        file: field('string', '视频文件绝对路径', { required: true }),
        interval: field('number', '每几秒一行（默认 4）'),
        from: field('number', '从第几秒开始（默认 0）'),
        to: field('number', '到第几秒结束（默认片尾）'),
        outDir: field('string', '输出目录（给了才落帧与 align.tsv；不给只出表）'),
        threshold: field('number', '场景变化阈值 0–1（默认 0.3）'),
      },
      async (args) => {
        const { align } = await import('./align.js');
        const r = await align(String(args?.file ?? ''), {
          interval: Number(args?.interval ?? 4),
          from: args?.from == null ? null : Number(args.from),
          to: args?.to == null ? null : Number(args.to),
          outDir: args?.outDir ? String(args.outDir) : '',
          threshold: Number(args?.threshold ?? 0.3),
        });
        if (!r.ok) return fail(`对齐失败：${r.error}`);
        return pass(r.text, { data: r });
      }
    )
  );

  return { version: VERSION };
}

export default { name, inject, apply, version: VERSION };
