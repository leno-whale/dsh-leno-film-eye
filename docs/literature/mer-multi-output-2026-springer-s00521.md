---
来源文件 / Source PDF: `mer-multi-output-2026-springer-s00521.pdf`
提取日期 / Extracted: 2026-10-30
提取方式 / Method: pdfplumber 文本层直接提取（非 OCR）
PDF 页数 / Pages: 38
总字符数 / Characters: 158635
DOI: 10.1007/s00521-026-12370-y
---
## 引用信息 / Citation (APA 7th)

> Mazzola, G., Seidita, V., & La Cascia, M. (2026). Benchmarking multi-output models for continuous music emotion prediction. *Neural Computing and Applications, 38*, Article 664. https://doi.org/10.1007/s00521-026-12370-y


## 正文（按页提取 / Extracted page by page）

### Page 1

Neural Computing and Applications (2026) 38:664
REVIEW
Benchmarking multi-output models for continuous
music emotion prediction
Giuseppe Mazzola · Valeria Seidita · Marco La Cascia
Received: 20 November 2025 / Accepted: 14 July 2026 / Published online: 17 August 2026
© The Author(s) 2026
Abstract
Predicting the emotional content of music is a long-standing challenge in audio signal processing and machine
learning, and although Music Emotion Recognition (MER) increasingly relies on deep learning, a systematic
comparison of audio descriptor families and of their integration through ensemble strategies and fusion lev-
els for continuous emotion prediction remains underexplored. This study addresses this gap within Russell’s
circumplex model of valence and arousal. Six machine learning paradigms (LSTM, MLP, Random Forest,
TabNet, PLSR, XGBoost) are evaluated across three theoretically diverse descriptor families: OpenSMILE
(signal-processing), PAA (psychoacoustic), and Librosa (MIR-standard). A ranking-based consistency criterion
identifies the four paradigms competitive across all families, and the resulting twelve base models are combined
at three fusion levels: late, early, and hybrid stacking. The framework is benchmarked against four state-of-
the-art architectures: three pre-trained audio Transformers (MERT, HuBERT, wav2vec 2.0) and a Conformer
trained from scratch. All experiments use 5-fold file-wise cross-validation, with Mean Euclidean Distance
(MED) as the primary joint metric alongside per-dimension RMSE, MAE, and Concordance Correlation Coef-
ficient. LSTM on OpenSMILE and on PAA achieves the strongest individual performance (MED = 0.241),
and hybrid Ridge stacking attains the best overall result (MED = 0.213, an 11.4% reduction), validated by
paired Wilcoxon tests. MERT remains the strongest model in absolute terms (MED = 0.201), but the proposed
framework outperforms the speech-pre-trained Transformers and the from-scratch Conformer. Meta-learner
weight analysis and per-feature permutation importance expose interpretable, dimension-specific contribution
patterns across descriptor families, learning paradigms, and individual features, providing a reproducible and
competitive non-Transformer baseline for continuous MER research.
Keywords Music emotion recognition · Valence–arousal regression · Ensemble learning · Audio
descriptors · Affective computing
1 Introduction
Music has long been recognized as one of the most powerful vehicles for emotional expression and communica-
tion [1]. Unlike language, which conveys meaning through explicit symbols, music operates on a more abstract
level, often evoking affective responses that are immediate, visceral, and deeply personal. A simple melodic
Neural Computing and Applications (2026) 38:664 https://doi.org/10.1007/s00521-026-12370-y

### Page 2

2664 Page 2 of 38 https://doi.org/10.1007/s00521-026-12370-y
progression, a sudden change in rhythm, or a shift in harmony can trigger emotional reactions that resonate
across individuals and cultures. This intimate connection between music and emotion has made the study of how
emotions are perceived, experienced, and classified in musical contexts a longstanding focus of research at the
intersection of psychology, musicology, neuroscience, and computer science.
In recent decades, the field of Music Emotion Recognition (MER) has emerged as a central area of computa-
tional music research [2]. The goal of MER is to develop methods capable of automatically identifying the emo-
tional content or impact of music, either as perceived by listeners or as intended by composers and performers.
This capability is not only of theoretical interest for understanding the cognitive and affective mechanisms behind
music perception, but also of practical significance for a wide range of applications. Systems that can recognize
or predict emotions in music have the potential to enhance music recommendation engines, support personalized
playlists, enable adaptive gaming and virtual reality experiences, and contribute to fields as diverse as affective
computing, music therapy, and human-computer interaction.
Approaches to MER typically follow two complementary paradigms. The categorical model classifies emo-
tions into discrete labels such as happiness, sadness, anger, or calmness, aligning with everyday language but
limiting the representation of gradual emotional transitions. The dimensional model, grounded in Russell’s cir-
cumplex theory of affect [3], represents emotions along continuous scales of valence (from positive to negative
affect) and arousal (from low to high activation), capturing subtle dynamics and complex affective blends. Both
paradigms have proven valuable, and contemporary research increasingly seeks to bridge them, acknowledging
that musical emotions can be both discretely labeled and continuously experienced.
Automatic emotion recognition in music is inherently challenging due to the multifaceted nature of musical
signals. Audio recordings encompass features at multiple levels, ranging from low-level acoustic descriptors
such as timbre, tempo and spectral shape, to mid-level constructs such as harmony, rhythm and melody, and to
higher-level cultural cues. At the same time, emotional perception is strongly modulated by listener-dependent
factors including personality, cultural background, and situational context. This variability complicates the design
of computational models that generalize across listeners and musical styles.
Machine learning advances have transformed MER from handcrafted features paired with traditional classi-
fiers to deep learning architectures capable of learning representations directly from audio. Recent approaches
encompass convolutional, recurrent, and transformer-based models that capture both local and long-range tem-
poral dependencies in emotional expression.
Despite these advances, fundamental challenges persist. The subjectivity of emotional perception, given that
the same music elicits different responses across listeners and contexts, complicates ground truth annotation and
model evaluation. Continuous valence–arousal annotations, while enabling fine-grained analysis, are often noisy
and inconsistent. Furthermore, MER systems frequently struggle to generalize across datasets and musical styles,
highlighting ongoing needs for robust modeling strategies and domain adaptation approaches.
The present work addresses these challenges through a comprehensive comparative framework for continuous
valence–arousal prediction. Rather than proposing novel architectures, we systematically investigate how differ-
ent families of audio descriptors, representing signal-processing, psychoacoustic, and music information retrieval
perspectives, compare in their ability to capture emotional trajectories, how their complementary strengths can
be leveraged through principled ensemble strategies, and how the resulting predictions can be interpreted at
the level of both descriptor families and individual features. The contributions of this work can be summarized
as follows. First, we provide a systematic comparison of three theoretically diverse audio descriptor families,
namely OpenSMILE (signal-processing), PAA (psychoacoustic, computed via Zwicker’s models), and Librosa
(MIR-standard), evaluated under a unified preprocessing and 5-fold file-wise cross-validation protocol. Second,
we assess six machine-learning paradigms (LSTM, MLP, Random Forest, TabNet, PLSR, XGBoost) in a multi-
output configuration that jointly predicts valence and arousal, yielding 18 descriptor–method combinations as
base learners. Third, we integrate the four most consistent paradigms (LSTM, MLP, Random Forest, XGBoost)
across the three descriptor families, for a total of 12 base models, through three late-fusion ensemble strategies:
1 3 Neural Computing and Applications (2026) 38:664

### Page 3

https://doi.org/10.1007/s00521-026-12370-y Page 3 of 38 6643
arithmetic averaging, Leave-One-Fold-Out (LOFO) weighted averaging, and Ridge meta-learning stacking.
Fourth, we extend the integration beyond decision-level fusion by adding an early-fusion stage on the concate-
nated 1085-dimensional feature space and a hybrid Ridge stacking meta-learner that combines the early- and late-
fusion predictions, allowing a direct comparison of the three canonical fusion levels on the same task and splits.
Fifth, we develop a two-level interpretability analysis of the framework: at the family level, a dimension-specific
weight analysis of the Ridge meta-learner exposes which descriptor families and modeling paradigms contribute
most to each emotional axis; at the feature level, a per-feature permutation-importance analysis is computed sepa-
rately for each descriptor family, identifying which specific descriptors within OpenSMILE, PAA, and Librosa
carry the predictive content and how concentrated or dispersed this content is across each pool. To the best of our
knowledge, this is the first work that combines descriptor-family weight analysis with per-feature permutation
importance in a continuous MER setting, providing interpretability at two complementary levels of granularity.
Sixth, we benchmark the proposed framework against four state-of-the-art audio architectures: three pre-trained
Transformers (MERT, HuBERT, wav2vec 2.0) under a unified multi-layer weighted-sum probing protocol and
a Conformer trained from scratch on the DEAM mel-spectrograms; the ensemble gains are validated through
paired Wilcoxon signed-rank significance tests. Together, these elements establish a reproducible, interpretable,
and transparent baseline for future research in continuous music emotion recognition.
At the structural level, the remainder of this article is organized as follows. Section 2 reviews the most relevant
literature on Music Emotion Recognition, with particular attention to continuous prediction approaches based on
the valence–arousal model. Section 3 describes the dataset and annotation scheme adopted in this study, while
Sect. 4 provides an overview of the general methodological framework and data preprocessing pipeline. Sec-
tion 5 focuses on the acoustic descriptors employed, outlining their characteristics and feature extraction proce-
dures. Section 6 presents the set of machine learning methods evaluated, spanning deep, ensemble-based, and
linear paradigms. Section 7 introduces the ensemble learning strategies designed to integrate the outputs of indi-
vidual models, including the late-fusion ensembles built on the base learners, the early-fusion stage operating on
concatenated descriptors, and the hybrid stacking meta-learner that combines early and late predictions. Section 8
details the experimental setup, including the training protocol, evaluation metrics, and implementation details.
Section 9 reports and discusses the experimental results: individual base models and ensemble configurations
are first analysed in terms of Mean Euclidean Distance and Concordance Correlation Coefficient, supported by
paired Wilcoxon signed-rank significance tests; a dedicated subsection then compares the proposed framework
against four state-of-the-art audio architectures, namely three pre-trained Transformers (MERT, HuBERT, wav-
2vec 2.0) and a Conformer trained from scratch on the DEAM mel-spectrograms; meta-learner weight analysis
closes the section, exposing which descriptor families and modeling paradigms contribute most to each emotional
axis, together with a per-feature permutation-importance analysis that identifies the most informative descriptors
within each family. Finally, Sect. 10 summarizes the main findings, discusses their broader implications, and
outlines directions for future research in continuous music emotion prediction.
2 State of the art
Research in Music Emotion Recognition (MER) has made remarkable progress in the last two decades, supported
by the creation of dedicated datasets and the rapid evolution of machine learning methods. A central role in this
development has been played by annotated corpora that provide systematic ground truth for model training and
evaluation. The DEAM dataset [4], for example, is one of the most widely used resources, offering dynamic
annotations of valence and arousal over 1,800 music excerpts and serving as the benchmark in multiple Medi-
aEval evaluation campaigns. Similarly, PMEmo [5] has enriched the MER landscape by combining continuous
valence–arousal annotations with electrodermal activity (EDA) recordings from listeners, thus enabling multi-
modal studies that integrate audio and physiological signals. MERP [6] contributes another valuable dimension by
collecting dynamic ratings together with rater profile information, paving the way for research on personalization
Neural Computing and Applications (2026) 38:664 1 3

### Page 4

4664 Page 4 of 38 https://doi.org/10.1007/s00521-026-12370-y
and bias in emotion perception. Other corpora address the subjectivity and variability of emotion annotation in
different ways: MUSAV [7] employs relative pairwise judgments of arousal and valence instead of absolute rat-
ings to mitigate inconsistencies, while TROMPA-MER [8] uses a citizen science platform to gather annotations
enriched with demographic, linguistic, and contextual metadata. Additional datasets such as MER1101 [9] and
those proposed in multilingual settings [10] further expand the experimental basis for MER research, providing
diversity both in music styles and in annotator populations.
Methodologically, early approaches relying on handcrafted features such as timbre descriptors, tempo, or
harmonic features have given way to deep learning pipelines capable of automatically extracting hierarchical
representations from raw signals. Convolutional neural networks (CNNs) applied to spectrograms or log-Mel
representations are among the most common approaches [9, 11], often augmented by multi-scale structures and
attention modules that capture emotional cues at different temporal and spectral levels. Recurrent neural networks
(RNNs) and their variants, such as GRUs and LSTMs, have been widely employed to model temporal dependen-
cies and dynamic changes in affect [12, 13], sometimes incorporating structured label spaces to reduce ambiguity
in emotional categories. More recent end-to-end architectures operate directly on raw audio waveforms, combin-
ing convolutional feature extractors with autoencoder-inspired reconstruction layers and bidirectional recurrent
networks, showing particular improvements in predicting valence trajectories [13]. Hybrid designs that integrate
efficient convolutional backbones with temporal modules have also been proposed, aiming to model both local
acoustic detail and long-range emotional flow [11, 14]. Beyond convolutional and recurrent topologies, graph-
based architectures have recently emerged as a promising alternative: Zhang et al. [15] proposed a multi-scale
controllable graph convolutional network that operates on spectro-temporal graphs derived from the audio signal,
achieving competitive performance on continuous valence–arousal prediction by explicitly modelling relational
structure across spectro-temporal regions. In parallel, ensemble learning strategies [16] have been explored to
enhance robustness by aggregating predictions across diverse models, while representation learning approaches
based on triplet neural networks [17] have been adapted to regression, allowing emotion-aware embeddings to be
learned and subsequently mapped to continuous valence–arousal targets.
The transformer paradigm has introduced another major shift in MER. Transformer-based models are par-
ticularly effective at capturing long-range dependencies and global context, enabling not only song-level clas-
sification but also the modeling of emotional trajectories across time. Several studies have demonstrated that
transformer encoders with self-attention pooling outperform traditional architectures in predicting valence and
arousal [18, 19], while others focus on transitions and turning points in the emotional trajectory, introducing
evaluation protocols such as windowed concordance correlation coefficients that emphasize temporal unfolding
rather than static accuracy [18]. These contributions highlight the increasing importance of temporal modeling
and sequence-level evaluation in MER. A related architectural development is the Conformer [20], originally pro-
posed for automatic speech recognition, which augments the Transformer with depthwise-separable convolutions
to combine the local-pattern bias of CNNs with the global self-attention mechanism. Although introduced for
speech, the Conformer’s hybrid local-global structure makes it applicable to continuous audio regression tasks
more broadly, including music emotion recognition.
A complementary line of research has emerged from the broader field of audio representation learning, where
self-supervised pre-training on large unlabelled corpora has produced general-purpose encoders that can be trans-
ferred to downstream tasks with minimal supervision. wav2vec 2.0 [21] introduced a contrastive masked-pre-
diction objective on raw waveforms, learning latent speech representations that subsequently transfer to a wide
range of speech-related tasks. HuBERT [22] refined this paradigm by replacing the contrastive objective with a
clustering-based discrete-target prediction that encourages the encoder to capture phonetic and acoustic regulari-
ties at multiple temporal scales. While both models are trained on speech, their hidden representations have been
shown to carry information relevant to non-speech audio classification, including affective tasks. Music-specific
pre-training has been pursued in MERT [23], which adapts the masked-prediction paradigm to a large music cor-
pus and incorporates auxiliary objectives based on acoustic and pitch-related targets, yielding representations that
capture both timbral and harmonic structure. The use of such pre-trained encoders as feature extractors for music
1 3 Neural Computing and Applications (2026) 38:664

### Page 5

https://doi.org/10.1007/s00521-026-12370-y Page 5 of 38 6645
emotion recognition is a natural extension of the deep-learning trajectory described above, and these models con-
stitute the SOTA baselines against which the framework proposed in this work is compared in Sect. 9.
In addition to purely audio-based methods, multimodal approaches have been shown to offer substantial advan-
tages. The integration of lyrics with acoustic signals through hierarchical or attention-based fusion consistently
improves classification performance [24]. Recent work by Talaghat et al. [25] further demonstrates the effective-
ness of multimodal integration, combining convolutional and recurrent layers with attention mechanisms to pro-
cess audio features from the chorus and lyrics embeddings, introducing a new dataset of over 9,000 tracks with
valence–arousal annotations. Real-time deployment scenarios have also received attention, with Hao et al. [26]
proposing a multimodal fusion architecture that combines audio and visual streams under latency constraints,
illustrating how the multimodal paradigm extends beyond accuracy improvements to address operational require-
ments relevant for interactive applications. Metadata such as language, demographics, or even self-reported mood
have also been incorporated to capture variability in emotion perception [8, 10]. On the generative side, models
that produce melodies under explicit emotional constraints [27] not only support applications in composition and
interactive systems but also provide insights into which musical properties causally contribute to the elicitation
of particular emotions.
A growing research frontier concerns personalization and explainability. Since emotional responses to music
are highly subjective, approaches that adapt predictions to the individual listener have gained attention [6, 28].
These efforts rely on datasets that provide annotator profiles or contextual data, and they aim to build systems
that are more accurate and user-centered. At the same time, explainable MER has emerged as an important theme,
with methods designed to trace predictions back to sound sources or to mid-level perceptual features such as
harmonic complexity, tonal stability, or rhythmic regularity [29, 30]. These studies not only improve the inter-
pretability of models but also enhance scientific understanding of the mechanisms linking musical structure to
emotional response.
Beyond recognition itself, several works explore how MER can be used in applications and interfaces. Some
contributions propose visual mappings of musical emotions into intuitive modalities such as color or graphical
displays [31, 32], while others integrate emotion recognition into adaptive music players that account for the
listener’s current state, for example by combining musical classification with facial expression recognition [33].
Such applications demonstrate the practical potential of MER in consumer technologies, music therapy, and
human-computer interaction.
Finally, unification efforts aim to bridge the gap between categorical and dimensional paradigms. Multi-task
frameworks that jointly learn discrete emotions and continuous valence–arousal values [34] show that both per-
spectives can be effectively integrated, benefiting from shared representations. Surveys and meta-analyses [2,
10, 35] underline that despite these advances, important challenges remain. Chief among them are the inherent
subjectivity and noise in annotations, evaluator variability, the limited generalization of models across datasets,
and the need for evaluation metrics that adequately capture the dynamic nature of music-induced emotions. These
open issues highlight the need for novel approaches capable of addressing both the technical and conceptual
limitations of current systems.
While the existing literature has made substantial progress in advancing Music Emotion Recognition through
architectural innovations, multimodal fusion, and increasingly sophisticated deep learning models, comparatively
less attention has been devoted to the systematic investigation of how different families of audio descriptors com-
pare in their ability to predict continuous emotional trajectories, and how their complementary strengths can be
leveraged through principled ensemble strategies. Many studies employ a single descriptor family or compare
models within a fixed feature space, leaving open the question of how the choice of audio representation interacts
with model architecture and learning paradigm. Similarly, while ensemble learning has been explored in discrete
emotion classification, its potential for combining heterogeneous descriptor-model combinations in continuous
valence-arousal prediction remains underexplored.
The present work addresses these gaps by providing a comprehensive and methodologically rigorous com-
parison of three theoretically diverse audio descriptor families, evaluating them in combination with six machine
Neural Computing and Applications (2026) 38:664 1 3

### Page 6

6664 Page 6 of 38 https://doi.org/10.1007/s00521-026-12370-y
learning paradigms and integrating their predictions through a multi-level ensemble framework that operates at
the decision, feature, and hybrid levels. The framework is benchmarked against pre-trained audio Transformers
and validated with paired statistical tests, with explicit attention to interpretability through meta-learner weight
analysis. The detailed components of this framework, including the descriptor families, the machine learning
paradigms, the ensemble strategies, and the experimental protocol, are presented in the following sections.
3 DEAM dataset
The Database for Emotional Analysis of Music (DEAM) [4] is one of the most widely adopted resources for the
study of continuous emotion recognition in music. It comprises 1,802 audio excerpts drawn from the Free Music
Archive and Jamendo, covering a broad spectrum of genres such as rock, pop, electronic, classical, and ambient
music. Each excerpt has a duration of 45 seconds, which offers sufficient temporal context for analyzing emo-
tional dynamics while maintaining manageable computational requirements.
Emotional annotations in DEAM are grounded in Russell’s circumplex model of affect [3], representing affec-
tive experience along two continuous dimensions: valence (from negative to positive affect) and arousal (from
calm to excited states) (see Fig. 1). The annotations were collected through a large-scale crowdsourcing cam-
paign, in which listeners continuously adjusted a joystick interface to indicate their perceived emotional state
while listening to each audio clip. This setup allowed the capture of the temporal evolution of emotions, rather
than static categorical judgments. Each musical excerpt was rated by multiple participants, with a median of nine
raters per song, and the final reference trajectories were obtained by averaging their annotations, thereby reducing
the influence of individual biases and idiosyncratic responses. Both valence and arousal values are normalized
to the range [ 1,+1], where −1 denotes negative or calm emotions and +1 corresponds to highly positive or
−
energetic states.
The dataset provides a relatively balanced coverage of the valence–arousal space, though certain biases are
evident and consistent with affective patterns found in publicly available music. The valence distribution shows
a mild positive skew (mean 0.15, σ 0.35), reflecting the general prevalence of pleasant or uplifting content.
≈ ≈
The arousal dimension spans a broader range (mean 0.05, σ 0.42), encompassing both calm and energetic
≈ ≈
excerpts. When discretized into the four quadrants of Russell’s model, approximately 28% of the excerpts fall
F ig. 1 Russell’s circumplex model of affect. Emotions are
organized in a two-dimensional space defined by valence
(positive–negative) and arousal (high–low)
1 3 Neural Computing and Applications (2026) 38:664

### Page 7

https://doi.org/10.1007/s00521-026-12370-y Page 7 of 38 6647
into the high-arousal/positive-valence quadrant, 30% into low-arousal/positive-valence, 22% into low-arousal/
negative-valence, and 20% into high-arousal/negative-valence. This distribution indicates good overall coverage
of emotional states, though slightly favoring positive valence.
Inter-rater reliability, as measured by Krippendorff’s alpha, averaged 0.21 for valence and 0.19 for arousal,
values that, though modest, are consistent with the high subjectivity of affective perception and with other data-
sets based on continuous emotion annotations. The aggregation of multiple raters mitigates this variability and
provides a more stable estimate of perceived emotion trajectories. DEAM’s annotation protocol also includes a
15-second silent “warm-up“ period preceding each musical excerpt, intended to allow participants to become
familiar with the joystick interface before the onset of the stimulus. Emotion annotations begin at the 15-second
mark, aligning data collection with the active listening phase, and they are sampled every 0.5 seconds.
From a broader perspective, DEAM’s design has several strengths that have established it as a benchmark
dataset in affective computing. Its use of continuous, time-aligned annotations allows for fine-grained modeling
of emotional variation across time, distinguishing it from corpora that rely solely on static or categorical labels.
The inclusion of diverse musical genres supports cross-style generalization, while its open-access availability has
made it a reference for reproducible experimentation and comparison across research groups.
Nevertheless, some limitations should be noted. The 45-second excerpts, while practical for annotation, may
not fully capture the long-term emotional evolution found in complete musical works. The dataset is composed
mainly of Western music, which may constrain cross-cultural generalization, and the subjective nature of emotion
perception implies that even averaged ratings reflect collective tendencies rather than objective truth. In addition,
a degree of genre imbalance is present, as popular or mainstream genres are more represented than niche or non-
Western forms.
Despite these caveats, DEAM remains the most comprehensive and widely used benchmark for dynamic
music emotion recognition. Its scale, annotation quality, and methodological rigor have established it as the
foundation for evaluating predictive models, studying temporal affective patterns, and advancing multimodal
approaches to the computational analysis of musical emotions. Table 1 summarizes the main characteristics of
the DEAM dataset.
4 Methodology
The methodology presented here is designed to address these gaps through a comprehensive and empirically
grounded investigation that systematically examines the interplay between audio descriptors, machine learning
methods, and ensemble strategies. The goal is not to propose a novel architecture, but rather to provide evidence-
based insights into best practices for building effective and interpretable MER systems using established and
reproducible techniques. Six central research questions guide the methodological framework:
1. How do different families of audio descriptors, capturing spectro-temporal, psychoacoustic, and timbral infor-
mation, compare in their ability to predict continuous valence and arousal?
Table 1 Summary of dataset Section Statistics summary
characteristics and annota-
Total excerpts 1,802 songs
tion statistics
Duration per excerpt 45 seconds
Frame duration 0.5 seconds
Total annotated frames 162,000
∼
Annotation dimensions Valence and Arousal (continuous, [ 1,+1])
−
Annotation method Continuous joystick-based ratings
Median raters per song 9
Inter-rater agreement (α) 0.21 (valence), 0.19 (arousal)
Neural Computing and Applications (2026) 38:664 1 3

### Page 8

8664 Page 8 of 38 https://doi.org/10.1007/s00521-026-12370-y
2. Among widely used machine learning approaches, which modeling paradigms best capture the complex non-
linear relationships between acoustic features and perceived emotion?
3. Can ensemble methods that integrate multiple descriptor–model combinations achieve meaningful improve-
ments over individual systems, and which ensemble strategies prove most effective?
4. How do the three canonical levels of information fusion, namely decision-level (late), feature-level (early),
and hybrid fusion, compare in this setting, and does combining them in a hybrid stacking meta-learner provide
additional gains over either level taken in isolation?
5. Which descriptor families, learning paradigms, and individual features carry the predictive content of the
framework, and how does this content distribute across the valence and arousal dimensions?
6. How does the proposed framework compare against state-of-the-art audio architectures, including both pre-
trained Transformers used as feature extractors and a Conformer trained from scratch, and what does this
comparison reveal about the trade-off between accuracy, interpretability, computational cost, and reliance on
external data?
The methodological workflow follows a hierarchical experimental design articulated across three stages (see
Fig. 2).
In the first stage, an exhaustive comparison is conducted across three distinct families of audio descriptors
combined with six complementary machine learning methods, representing diverse modeling paradigms. The
chosen descriptors represent fundamentally different philosophies of audio characterization: OpenSMILE, which
provides a comprehensive signal-processing-based representation; Psychoacoustic Annoyance (PAA) features,
which model auditory perception according to psychoacoustic principles; and Librosa descriptors, which include
the standard timbral and rhythmic features commonly adopted in music information retrieval. The six machine
learning methods, namely Long Short-Term Memory (LSTM) networks, Multi-Layer Perceptrons (MLP), Ran-
dom Forests (RF), TabNet, Partial Least Squares Regression (PLSR), and Extreme Gradient Boosting (XGBoost),
were selected to encompass diverse learning paradigms that capture temporal dynamics, non-linear mappings,
and ensemble-based relationships, respectively.
In the second stage, three canonical fusion levels are systematically evaluated to exploit complementarity
among base models. Decision-level (late) fusion combines the predictions of the base models through three strat-
egies of increasing sophistication: arithmetic mean averaging, providing an unweighted baseline; Leave-One-
Fold-Out (LOFO) weighted averaging, learning optimal linear weights through validation-based optimization;
F ig. 2 Overall workflow of
the proposed framework
1 3 Neural Computing and Applications (2026) 38:664

### Page 9

https://doi.org/10.1007/s00521-026-12370-y Page 9 of 38 6649
and stacking with Ridge regression meta-learning, enabling dimension-specific combination of predictions. Mul-
tiple late-fusion configurations are evaluated, ranging from same-method ensembles that combine identical para-
digms across descriptors to cross-method ensembles that mix diverse approaches across feature representations.
Feature-level (early) fusion concatenates the three descriptor families into a single representation on which one
base model per learning paradigm is trained. Hybrid fusion combines the predictions of the early-fusion and late-
fusion base models through a Ridge stacking meta-learner. The three fusion levels are evaluated under the same
cross-validation protocol, allowing a direct comparison of their relative effectiveness.
In the third stage, detailed analytical procedures are applied to extract insights from the ensemble results, to
position the framework against the state of the art, and to validate the observed gains. These analyses include
the interpretation of meta-learner weights to assess the relative contribution of each model and to expose dimen-
sion-specific contribution patterns; the comparison against four state-of-the-art audio architectures, namely three
pre-trained Transformers (MERT, HuBERT, wav2vec 2.0) evaluated under a unified multi-layer weighted-sum
probing protocol and a Conformer trained from scratch on the dataset’s mel-spectrograms; the application of
paired Wilcoxon signed-rank tests on the per-fold prediction errors to assess the statistical significance of the
gains achieved by the ensemble strategies over the best individual base models; and a per-feature permutation-
importance analysis of the three best XGBoost base models, one per descriptor family, to identify which specific
features within each descriptor pool carry the predictive content. The objective is not only to quantify improve-
ments in prediction accuracy but also to understand why particular combinations outperform others and to ground
the reported improvements in formal statistical evidence, providing guidance for future methodological design
in MER research.
The rationale underlying this methodological framework is grounded in four guiding principles.
First, diversity over novelty: rather than introducing architectural innovations, this work emphasizes the sys-
tematic exploration of diversity in descriptors, model types, and ensemble strategies. Theoretical and empirical
results in ensemble learning [36] demonstrate that combining diverse models often yields greater improvements
than refining a single homogeneous architecture.
Second, empirical rigor: all experimental components adhere to strict methodological controls to ensure fair
comparison and replicability. The file-wise cross-validation protocol, for instance, avoids data leakage by ensur-
ing that all frames from a given song appear exclusively in either the training or testing set, a crucial consideration
in sequential audio analysis. Reported gains are further validated through paired Wilcoxon signed-rank tests on
the per-fold prediction errors, providing formal statistical evidence that the observed improvements are not due
to fold-level variability.
Third, interpretability and transparency: the methods chosen are well-established and analytically tractable,
allowing insights into their internal mechanisms. The use of Ridge regression as a linear meta-learner makes it
possible to examine the contribution of each base model and the structure of learned combinations across emo-
tional dimensions.
Finally, practical applicability: by relying exclusively on publicly available libraries and standardized feature
extraction tools (OpenSMILE, Librosa, and psychoacoustic models), the methodology ensures full reproducibil-
ity and adaptability for other research groups or application contexts.
In addition, this framework embraces the principle that the effectiveness of a music emotion recognition system
depends not only on the sophistication of its modeling components but also on their complementarity and integra-
tion. Through rigorous evaluation and controlled ensemble design, the proposed methodology aims to provide
a clear, interpretable, and generalizable understanding of how diverse feature spaces and modeling approaches
jointly contribute to the prediction of emotional trajectories in music.
The following sections detail each methodological component in depth. The next section describes the extrac-
tion of audio descriptors and feature preprocessing procedures, followed by an overview of the machine learning
methods adopted and their configurations, and finally the ensemble learning strategies developed to integrate
model predictions into a unified, optimized framework.
Neural Computing and Applications (2026) 38:664 1 3

### Page 10

16064 Page 10 of 38 https://doi.org/10.1007/s00521-026-12370-y
5 Audio descriptors
The selection of appropriate audio descriptors is fundamental to the success of music emotion recognition sys-
tems, as these features represent the bridge between the raw acoustic signal and the higher-level emotional inter-
pretation. In this study, three distinct families of audio descriptors were investigated, each representing a different
theoretical and methodological approach to the characterization of musical audio. The chosen descriptor families,
namely OpenSMILE, Psychoacoustic Annoyance (PAA), and Librosa, were selected to maximize diversity in
feature representation while maintaining empirical and theoretical validity within music information retrieval and
affective audio analysis.
To ensure fair comparison across descriptor families and numerical stability during model training, all feature
sets undergo consistent preprocessing including standardization, outlier mitigation, and imputation of missing
values. The complete preprocessing protocol is detailed in Sect. 8 (Experimental Setup).
5.1 OpenSMILE: comprehensive spectro-temporal features
OpenSMILE (Open-Source Speech and Music Interpretation by Large-Space Extraction) [37, 38] is one of the
most widely adopted frameworks for the systematic extraction of acoustic features. Originally developed for
speech emotion recognition, OpenSMILE has been extensively validated across various audio domains, includ-
ing music analysis, and is considered a benchmark tool for standardized feature computation. It provides large,
well-documented feature sets that capture a wide spectrum of acoustic phenomena through hierarchical signal
processing.
For this study, we employed the Audeering implementation available at the GitHub repository [39]. The extrac-
tion was performed on non-overlapping 0.5-second frames, in line with the temporal resolution of the DEAM
annotations. For each frame, OpenSMILE extracts a comprehensive set of 988 acoustic features encompassing
spectral, prosodic, and voice quality descriptors. These features include spectral descriptors such as MFCCs
(Mel-Frequency Cepstral Coefficients), spectral centroid, rolloff, flux, and energy in multiple frequency bands;
prosodic features including fundamental frequency (F0), jitter, shimmer, and their statistical functionals; voice
quality measures such as Harmonics-to-Noise Ratio (HNR) and spectral harmonicity; and energy-related features
including RMS energy, loudness, and their derivatives.
The full 988-dimensional feature pool produced by the emobase_v2 configuration is passed to the downstream
models without further reduction. Since emobase_v2 is itself a curated affective-computing set, in which low-
level descriptors and statistical functionals are already selected for their relevance to emotional content, applying
an additional supervised feature selection would introduce a further dataset-specific filtering of an already filtered
representation. The complete vector is therefore retained, and the per-feature permutation-importance analysis
described in Sect. 9 identifies a posteriori which descriptors actually carry the predictive content.
OpenSMILE features embody a theory-driven and comprehensive approach to audio description. The frame-
work has been designed based on empirical evidence of feature relevance to affective communication and
validated across diverse emotion recognition contexts. Its inclusion in this work ensures a rich, multi-faceted
representation of the acoustic signal grounded in well-established acoustic correlates of emotion.
5.2 PAA: psychoacoustic annoyance features
The Psychoacoustic Annoyance (PAA) model [40, 41] represents a fundamentally different approach to audio
characterization. Rather than relying on purely signal-processing criteria, PAA features are grounded in percep-
tual psychology and auditory physiology, modeling how humans actually experience sound. Originally devel-
oped for the quantification of acoustic discomfort, the PAA framework has since been adapted for music analysis,
particularly in studies investigating the perceptual correlates of emotional arousal and valence.
1 3 Neural Computing and Applications (2026) 38:664

### Page 11

https://doi.org/10.1007/s00521-026-12370-y Page 11 of 38 66141
The PAA pipeline computes, for each 0.5-second frame, the five core perceptual quantities prescribed by the
Zwicker–Fastl framework [40], namely Loudness, Sharpness, Roughness, Fluctuation Strength, and Tonality.
The extraction is performed with MoSQITo [42], a Python implementation of the Zwicker–Fastl psychoacoustic
models. Loudness is computed in sones, accounting for frequency-dependent auditory sensitivity and temporal
integration. Sharpness, expressed in acum units, quantifies the perceived high-frequency energy and relates to the
brightness or shrillness of sound. Roughness, measured in asper units, captures rapid amplitude modulations in
the 15–300 Hz range that produce sensations of tension or harshness, often associated with high arousal. Fluc-
tuation strength, measured in vacil units, quantifies slower modulations (0.5–20 Hz) corresponding to rhythmic
pulsations and beats. Tonality represents the degree of harmonicity versus noisiness, reflecting the distinction
between tonal and atonal content.
In addition to these five descriptors, statistical functionals (mean, variance, and peak values) are computed to
summarize temporal evolution within each frame, yielding a total of 20 features per frame. These descriptors are
designed to reflect perceptual mechanisms such as critical band masking, frequency-dependent loudness percep-
tion, and temporal integration, which collectively define how sound energy is processed by the human auditory
system. The resulting features thus bridge the gap between physical sound properties and perceptual experience.
PAA’s inclusion in this study provides a perception-centered perspective that complements the more physically
grounded OpenSMILE features. The explicit modeling of auditory phenomena such as roughness and sharpness
is particularly relevant to emotion recognition, as previous psychological research [1] has linked these percep-
tual attributes to arousal and valence dimensions, respectively. By incorporating psychoacoustic modeling, PAA
captures aspects of musical affect that are otherwise invisible to traditional signal-based descriptors, offering a
valuable contribution to the diversity of feature representations explored.
5.3 Librosa: standard MIR timbral and rhythmic features
Librosa [43] is a well-established Python library for audio and music analysis that provides a standard set of fea-
tures commonly used in Music Information Retrieval (MIR) research. While less specialized than OpenSMILE
or PAA, Librosa offers an efficient and flexible implementation of the most frequently used timbral, spectral, and
rhythmic descriptors. Its inclusion serves as a baseline aligned with conventional MIR practice and allows for
direct comparison between standard descriptors and more specialized or perceptually motivated representations.
From each 0.5-second frame, a combination of spectral, timbral, rhythmic, and energy-related features is
extracted. Spectral features include the spectral centroid (representing the center of mass of the spectrum and
correlating with perceived brightness), spectral bandwidth (indicating spectral spread), spectral contrast (captur-
ing energy differences between peaks and valleys across sub-bands), spectral roll-off (the frequency below which
85% of spectral energy is contained), and spectral flatness (measuring the degree to which the spectrum is noise-
like). Timbral features are represented by 13 Mel-Frequency Cepstral Coefficients (MFCCs), which describe the
spectral envelope on a perceptually motivated mel scale and are widely used in both speech and music emotion
recognition. Additional harmonic information is captured by Chroma features, which represent the relative dis-
tribution of pitch classes across octaves. Rhythmic features include Tempo, estimated in beats per minute (BPM)
via autocorrelation of the onset strength envelope, and the Zero-Crossing Rate (ZCR), which reflects the rate of
signal polarity changes and correlates with percussiveness or noisiness. Finally, the Root Mean Square (RMS)
energy provides a measure of overall loudness.
Time-varying features such as spectral descriptors, MFCCs, and chroma vectors are statistically summarized
over the 0.5-second window through their mean, standard deviation, and range, resulting in a total of 77 features
per frame. All features are computed using a Short-Time Fourier Transform (STFT) with a 2048-sample window
and 512-sample hop size at 44.1 kHz sampling rate. Mel-scale computations use 128 mel bands spanning 0–8000
Hz, and chroma features are extracted using the Constant-Q Transform (CQT) to enhance pitch resolution.
Librosa features represent a pragmatic and domain-standard approach to MIR-based music analysis. Their
inclusion allows benchmarking against widely adopted descriptors and supports interpretability, as many of these
Neural Computing and Applications (2026) 38:664 1 3

### Page 12

16264 Page 12 of 38 https://doi.org/10.1007/s00521-026-12370-y
features have well-established perceptual and musical meanings (for example, chroma for harmonic structure and
tempo for rhythmic energy). The Librosa set thus provides a balanced complement to the theory-driven OpenS-
MILE and perception-oriented PAA descriptors.
5.4 Rationale for descriptor selection and diversity
The selection of the three descriptor families was guided by the objective of maximizing diversity across theoreti-
cal foundations, granularity, domain specificity, and computational philosophy. The feature sets differ markedly
in dimensionality, with OpenSMILE being high-dimensional (988 features, used in full), Librosa moderately
dimensional (77 features), and PAA low-dimensional (20 features). They also differ in domain orientation, with
OpenSMILE being general-purpose across speech and music, PAA focusing on auditory perception modeling,
and Librosa specifically tailored for music analysis. These variations yield distinct inductive biases for learning
algorithms and are the structural precondition that makes ensemble learning meaningful in this setting. If the
three families captured largely overlapping information, combining them would yield diminishing returns; if
they capture complementary information, their integration through ensemble strategies can compensate for weak-
nesses in individual feature spaces. The expectation is also dimension-specific: descriptors emphasizing loudness
and roughness (PAA) may correlate strongly with arousal, while harmonic and chromatic descriptors (Librosa)
may prove more predictive for valence. Whether and to what extent these theoretical expectations are reflected in
the actual contribution of each family to the trained models is one of the empirical questions addressed in Sect. 9.
6 Machine learning methods
The selection of suitable machine learning methods is central to effectively capturing the complex and non-linear
relationships that link acoustic features to perceived emotional dynamics. In this study, a diverse set of algorithms
was investigated, encompassing both traditional and modern paradigms of supervised regression. Each method
was implemented to predict continuous valence and arousal trajectories jointly within a unified multi-output
framework, ensuring consistency across modeling approaches and enabling direct comparability. This design
allows subsequent analysis to determine, empirically, which families of models provide the best balance between
predictive accuracy, interpretability, and computational efficiency.
The investigated algorithms include Long Short-Term Memory (LSTM) networks, Multi-Layer Perceptrons
(MLP), Random Forests (RF), TabNet, Partial Least Squares Regression (PLSR), and Extreme Gradient Boost-
ing (XGBoost). Together, these methods span a wide methodological spectrum, from deep neural architectures
capable of temporal modeling to classical linear and ensemble-based techniques optimized for tabular data. Each
contributes a distinct inductive bias, providing complementary perspectives on the mapping between acoustic
features and emotional dimensions.
6.1 Long Short-Term Memory networks (LSTM)
Long Short-Term Memory (LSTM) networks [44] constitute a specialized form of Recurrent Neural Network
(RNN) explicitly designed to capture long-range temporal dependencies in sequential data. Their internal gating
mechanisms allow selective retention and forgetting of information over time, mitigating the vanishing gradient
problem typical of conventional RNNs. This makes them particularly well suited for modeling emotional tra-
jectories in music, where affective states evolve continuously and are influenced by preceding acoustic context.
The LSTM models used in this study operate directly on temporal sequences of features extracted at 0.5-sec-
ond intervals, enabling the network to learn temporal patterns that correspond to gradual emotional transitions.
Two recurrent layers are stacked to capture both low and high level temporal dependencies, followed by a fully
connected output layer with two linear units representing valence and arousal. The model jointly minimizes the
1 3 Neural Computing and Applications (2026) 38:664

### Page 13

https://doi.org/10.1007/s00521-026-12370-y Page 13 of 38 66143
mean squared error across both dimensions, promoting the emergence of shared internal representations that
encode the acoustic correlates of musical affect. By design, the LSTM’s ability to maintain temporal memory
provides an explicit mechanism for tracking the evolving emotional content of music, making it a conceptually
appropriate choice for continuous affect prediction.
6.2 Multi-Layer Perceptron (MLP)
Multi-Layer Perceptrons (MLPs) [45] represent one of the most fundamental yet versatile forms of artificial neu-
ral networks, capable of learning non-linear mappings between high-dimensional input features and continuous
output variables. Although MLPs do not model temporal dependencies explicitly, they are particularly effective
when applied to frame-level descriptors that already incorporate statistical or contextual information, as is the
case for the features used in this work.
The MLP architecture consists of multiple fully connected layers with non-linear activations, culminating in a
two-unit linear output layer corresponding to valence and arousal. The network is trained using a Mean Squared
Error (MSE) objective computed jointly over both emotional dimensions. Despite their structural simplicity,
MLPs are powerful universal approximators and can efficiently capture complex interactions among acoustic
descriptors. Their computational efficiency and straightforward training dynamics make them a valuable baseline
for assessing the contribution of explicit temporal modeling in recurrent architectures.
6.3 Random Forest (RF)
Random Forests [46] are ensemble learning methods that construct a large number of decision trees, each trained
on a random subset of the data and feature dimensions. The final prediction is obtained as the mean output of all
trees, resulting in a model that is both robust and interpretable. In the context of continuous emotion prediction,
Random Forests provide a non-parametric alternative to neural networks, capable of modeling highly non-linear
relationships while remaining resistant to overfitting and insensitive to feature scaling.
In this study, Random Forest regressors were implemented in a multi-output configuration, predicting valence
and arousal jointly through a single ensemble structure. Each split within the trees was optimized to minimize the
joint squared error, consistent with the MSE objective, enabling the model to exploit shared dependencies and
covariances between the two emotional dimensions. This design allows the forest to capture inter-dimensional
relationships that are often ignored in independent regressors, while maintaining the interpretability typical of
tree-based models. Feature importance analyses can be derived directly from the trained ensemble, offering
insights into which acoustic parameters most strongly influence emotional perception.
6.4 TabNet
TabNet [47] represents a modern deep-learning approach specifically tailored to structured tabular data. Its
architecture combines sequential attention mechanisms with instance-wise feature selection masks, allowing the
model to focus dynamically on the most relevant features at each decision step. Unlike traditional feed-forward
networks that treat all input dimensions uniformly, TabNet performs conditional computation, selectively attend-
ing to different subsets of features depending on the input instance. This enables a balance between interpretabil-
ity and non-linear modeling capacity.
In the present framework, TabNet is applied to frame-level acoustic descriptors to learn complex mappings
between features and continuous emotion values. By leveraging attention-driven feature selection, it can iden-
tify which acoustic cues contribute most strongly to each emotional dimension in a context-dependent manner.
Although originally designed for general tabular data, TabNet’s interpretability and adaptive feature selection
make it a compelling candidate for music emotion recognition, where the relative importance of different descrip-
tors (for example, spectral versus rhythmic) may vary over time and across emotional states. The network is
Neural Computing and Applications (2026) 38:664 1 3

### Page 14

16464 Page 14 of 38 https://doi.org/10.1007/s00521-026-12370-y
configured in a multi-output regression mode to predict valence and arousal jointly, sharing internal representa-
tions across both emotional dimensions.
6.5 Partial Least Squares Regression (PLSR)
Partial Least Squares Regression (PLSR) [48] serves as a classical, interpretable baseline within this comparative
framework. PLSR projects high-dimensional input features onto a smaller set of latent components that maxi-
mize covariance with the target variables. In this work, PLSR operates in multi-target mode, predicting valence
and arousal simultaneously from a shared set of latent components. This dual projection simultaneously reduces
dimensionality and retains the directions of greatest predictive relevance, making PLSR particularly effective
when features are highly correlated or when the feature space exceeds the number of training samples.
Although inherently linear, PLSR provides valuable insight into the degree of linear separability between
acoustic features and emotional dimensions. By analyzing the weights and loadings of the latent components,
it is possible to interpret which feature groups align most strongly with valence or arousal. Its inclusion ensures
that the methodological framework spans the full continuum from simple, interpretable linear models to highly
expressive non-linear learners.
6.6 Extreme Gradient Boosting (XGBoost)
Extreme Gradient Boosting (XGBoost) [49] extends the family of tree-based ensemble methods through iterative
boosting, where successive trees are trained to correct the residual errors of previous ones. Each iteration focuses
learning capacity on the most difficult samples, gradually refining the prediction surface. XGBoost integrates
regularization mechanisms through both L1 and L2 penalties, ensuring stability and preventing overfitting even
in high-dimensional spaces.
Within this study, XGBoost was implemented in a multi-output configuration to jointly predict valence and
arousal. By optimizing a shared objective function across both targets, the model is able to capture joint depen-
dencies between emotional dimensions while benefiting from the high expressive power and efficiency of gra-
dient-boosted ensembles. Its combination of non-linear flexibility, robustness, and interpretability makes it a
natural extension of the Random Forest paradigm, capable of learning fine-grained relationships between acous-
tic cues and emotional responses.
6.7 Rationale for method selection and diversity
Each of the methods described above contributes a distinct perspective on the prediction of continuous emotional
trajectories. Neural architectures such as LSTMs and MLPs emphasize representation learning and hierarchical
abstraction, while tree-based and boosting methods focus on partitioning the feature space through interpretable
decision structures. TabNet bridges these paradigms by introducing attention-based feature selection in a tabular
context, and PLSR anchors the comparison within a well-understood linear framework. This methodological
diversity is fundamental to the ensemble stage that follows, in which model outputs will be integrated through
meta-learning to explore complementarity and redundancy among predictors. To keep the ensemble experimental
design tractable while preserving methodological diversity, the composition of the ensemble will be guided by
an empirical consistency criterion: only paradigms that perform competitively across all three descriptor families
will be retained as base learners in the ensemble stage. The corresponding selection is detailed in Sect. 9, after the
per-descriptor base-model results are presented.
1 3 Neural Computing and Applications (2026) 38:664

### Page 15

https://doi.org/10.1007/s00521-026-12370-y Page 15 of 38 66145
7 Ensemble learning strategies
Ensemble learning represents a powerful paradigm in predictive modeling, based on the premise that combining
multiple diverse models often yields superior generalization performance compared to any single constituent
model. This advantage arises from the reduction of both variance and bias through aggregation, as different mod-
els capture complementary aspects of the data and their individual errors tend to average out. In the context of
music emotion recognition, ensemble methods offer a particularly appealing solution to the inherent subjectivity
and complexity of the task, where no single model or descriptor family can fully capture the multifaceted rela-
tionship between musical structure and perceived emotion.
The multi-classifier literature [50] distinguishes three canonical levels at which information from heteroge-
neous sources can be combined: decision-level (or late) fusion, where the predictions of independently trained
base models are aggregated; feature-level (or early) fusion, where the input representations are merged before
training a single model on the joint representation; and hybrid fusion, where predictions of early- and late-fusion
models are combined through an additional meta-learning stage. We evaluate all three levels on the continuous
valence–arousal regression task, under a unified 5-fold file-wise cross-validation protocol that allows a direct
comparison of their relative effectiveness.
The ensemble framework developed in this study builds upon the foundations established by [36] and [51]. In
all three decision-level strategies, the first stage consists of the late-fusion base learners, namely the descriptor–
method combinations retained according to the consistency criterion introduced in Sect. 6.7 (the exact composi-
tion is reported in Sect. 9). Each base model is trained under the same 5-fold file-wise cross-validation protocol,
producing out-of-fold predictions that serve as the foundation for the three combination strategies considered
at the decision level: arithmetic mean averaging, Leave-One-Fold-Out (LOFO) weighted averaging, and Ridge
regression stacking, in order of increasing sophistication. Each strategy is described in turn below.
In the arithmetic mean approach, ensemble predictions are computed as the simple average of base model
predictions for each emotional dimension. Formally, for a set of N base models producing predictions yˆ , yˆ ,...,
1 2
yˆ , the ensemble prediction is given by yˆ = (1/N) Σ yˆ. This method requires no training or parameter
N ensemble i i
optimization and serves as a baseline to quantify the benefit of model diversity alone, independent of any learned
weighting scheme.
In the LOFO weighted averaging approach, optimal linear weights are learned for each base model through a
leave-one-fold-out optimization procedure. For each cross-validation fold k, weights w = [w ,w ,...,w ] are
1 2 N
optimized on the out-of-fold predictions from the remaining folds, minimizing the Mean Euclidean Distance
(MED) in the valence–arousal space, defined as the average per-frame Euclidean distance between predicted and
reference points. The learned weights are then applied to fold k to generate ensemble predictions. This process
is repeated for all folds, ensuring that weight optimization never sees the test data. The weights are shared across
both valence and arousal dimensions, providing a global weighting scheme that balances performance across
both emotional axes.
In the stacking approach, a Ridge Regression meta-learner is trained to combine base model predictions. The
meta-learner receives as input the predicted valence and arousal values from each of the base models and learns
to produce optimized final predictions. Ridge regression was chosen for its interpretability, simplicity, and robust-
ness against collinearity among predictors. It minimizes the mean squared error while imposing an L2 penalty on
the magnitude of the regression coefficients, thereby preventing overfitting and ensuring stable weight estimation
even when the base models are highly correlated. The regularization coefficient (α = 1.0) was selected empiri-
cally, testing different values, to balance bias and variance while maintaining interpretability of the resulting
weights. The Ridge regressor performs multivariate regression, jointly predicting both valence and arousal from
the concatenated base model predictions. This allows the meta-learner to capture any interdependencies between
the emotional dimensions while learning the optimal combination of base models.
Neural Computing and Applications (2026) 38:664 1 3

### Page 16

16664 Page 16 of 38 https://doi.org/10.1007/s00521-026-12370-y
A key methodological refinement in the stacking approach is the use of a Leave-One-Fold-Out training scheme,
designed to preserve complete independence between the base and meta-learning stages. The meta-learner is
trained exclusively on the out-of-fold predictions generated during cross-validation, ensuring that the meta-model
never sees predictions from base learners on the same data used for their training. This strategy effectively elimi-
nates information leakage and produces a truly generalizable ensemble model. Once trained, the meta-learner is
applied to the test predictions from each fold to obtain the final ensemble outputs for valence and arousal.
The three strategies just described all operate at the decision level, combining the outputs of independently
trained base models. The remainder of this section turns to the other two fusion levels introduced above, in which
integration occurs at the input space (early fusion) or across both levels (hybrid fusion).
In feature-level (early) fusion, the three descriptor families are concatenated frame by frame into a single
1085-dimensional joint representation (988 OpenSMILE + 77 Librosa + 20 PAA), and one base model per
retained learning paradigm is trained on the resulting feature space, ensuring a fair comparison with the late-
fusion ensemble under identical learning capacity. Cross-descriptor interactions, which decision-level fusion
can only recover indirectly through the meta-learner, are exposed directly to the early-fusion model, which is
free to allocate capacity across descriptor families as the learning objective dictates. While Bejani et al. [52]
include an ANOVA-based feature-ranking step on the joint representation, we pass the full concatenation to the
early-fusion models without dimensionality reduction, consistently with the no-selection policy adopted on the
OpenSMILE side. The resulting out-of-fold predictions are directly comparable, fold by fold, with their late-
fusion counterparts.
Hybrid fusion combines the predictions of the early- and late-fusion base models through a Ridge stacking
meta-learner identical in form and training scheme to the decision-level one, with the input pool enlarged to
include both fusion levels. This design lets the meta-learner re-weight the contributions of decision-level and
feature-level information in a dimension-specific manner, allocating different mixtures to valence and to arousal.
Since only the input pool grows, the hybrid stage adds negligible training cost once the base models are available.
The rationale for evaluating multiple combination mechanisms operates at two complementary levels. Within
the decision-level family, the three strategies span a simplicity–adaptability trade-off: arithmetic mean averag-
ing offers maximum simplicity and interpretability but may be suboptimal when base models have substantially
different levels of accuracy or when their errors are correlated; LOFO optimization addresses this limitation
by learning data-driven weights, but it remains constrained to a single set of global weights applied uniformly
across both emotional dimensions; stacking with meta-learning relaxes this constraint by allowing dimension-
specific weighting and the potential incorporation of nonlinear interactions. Across fusion levels, the comparison
addresses a different question, namely whether the locus of integration matters: decision-level fusion preserves
the inductive biases of the individual base learners and combines only their outputs; feature-level fusion lets a
single model exploit cross-descriptor interactions directly in the input space; hybrid fusion attempts to retain both
advantages by stacking the two paradigms. By comparing the three fusion levels and the three decision-level
strategies jointly, the study aims to quantify the performance gains associated with each layer of the integration
hierarchy in the context of continuous music emotion recognition.
A common feature of all combination strategies considered is that they remain analytically tractable. The
Ridge meta-learner, in particular, exposes a set of linear coefficients whose magnitude and sign can be directly
inspected, both across base models in the decision-level setting and across fusion levels in the hybrid setting.
Because the meta-learner is fitted separately on valence and on arousal, these coefficients are naturally dimension-
specific: a base model that contributes strongly to one emotional dimension is not forced to contribute equally
to the other, and the resulting weight profile can be read as a quantitative summary of which descriptor–method
combinations carry the predictive content for each dimension. This interpretability is a methodological advantage
over deep neural ensemble models that function as opaque combiners, and it is exploited in Section 9 to charac-
terize the relative contribution of descriptor families, learning paradigms, and fusion levels to the prediction of
valence and arousal.
1 3 Neural Computing and Applications (2026) 38:664

### Page 17

https://doi.org/10.1007/s00521-026-12370-y Page 17 of 38 66147
8 Experimental setup
The experimental evaluation was designed to ensure methodological rigor, reproducibility, and fair comparison
across all model–descriptor combinations. A uniform cross-validation protocol was applied to all base models,
with consistent preprocessing and evaluation metrics. Particular attention was devoted to preventing data leakage
and ensuring that all models were trained and evaluated under identical conditions.
8.1 Cross-validation protocol and preprocessing
To ensure robust and generalizable performance estimates, a 5-fold cross-validation strategy was adopted for all
experiments. Critically, the splitting was performed at the file level rather than the frame level, meaning that all
0.5-second frames extracted from a given musical excerpt were assigned exclusively to either the training set
or the test set within each fold, but never to both. This file-wise splitting is essential to prevent data leakage, as
frames from the same song are highly correlated and would otherwise allow models to exploit temporal depen-
dencies across the train-test boundary. The dataset’s 1,802 audio files were divided into five approximately equal
subsets, with each fold using four subsets for training (approximately 1,442 files) and one for testing (approxi-
mately 360 files). The same fold assignments were used consistently across all base models, ensuring that dif-
ferences in performance reflect genuine differences in modeling capacity rather than variations in training data
composition.
All audio files were segmented into non-overlapping 0.5-second frames, aligned with the temporal resolu-
tion of the DEAM emotion annotations. This uniform segmentation was applied consistently across all three
descriptor families (OpenSMILE, PAA, and Librosa), ensuring temporal synchronization and enabling direct
comparison and combination within ensemble configurations. The choice of frame-level prediction, rather than
song-level aggregation, is motivated by two considerations. First, DEAM provides continuous annotations at
0.5-second resolution, and operating at this granularity fully exploits the available temporal information. Second,
frame-level predictions preserve the ability to analyze emotional trajectories and temporal dynamics; song-level
or segment-level metrics can be readily derived through appropriate aggregation (for example, mean or median)
when required by specific applications, whereas the reverse, namely recovering fine-grained dynamics from
aggregated predictions, is not possible.
For each frame, audio descriptors were extracted using the respective toolkits, and the resulting feature matrices
were subjected to a uniform preprocessing pipeline applied consistently across all descriptor families. To ensure
numerical stability and fair comparison across feature spaces with different scales, all features were standard-
ized to zero mean and unit variance through z-score normalization, where the mean and standard deviation were
computed exclusively from the training set within each cross-validation fold. The same normalization parameters
were then applied to the corresponding test set, ensuring that no test-set statistics influenced the preprocessing.
To mitigate the influence of extreme outliers that may arise from atypical audio content or extraction artifacts,
feature values were clipped to the range [µ 5σ,µ+5σ] after standardization, where µ and σ refer to the train-
−
ing-set statistics. In cases where feature extraction yielded undefined or missing values (for example, missing
fundamental frequency in unvoiced segments, or undefined tempo estimates in near-silent passages), these values
were imputed using the mean value of the corresponding feature dimension, computed from the training set.
8.2 Hyperparameter configuration
Each machine-learning method was configured with a single fixed set of hyperparameter values, applied uni-
formly across all 5-fold cross-validation runs and across all descriptor families; the specific values used for each
model are detailed below. For Random Forest, XGBoost, TabNet, and PLSR, library defaults were used as the
starting point and lightly adapted to the data regime of the study; for LSTM and MLP, conventional configura-
tions for sequential and tabular regression were adopted. No formal hyperparameter search was conducted. This
Neural Computing and Applications (2026) 38:664 1 3

### Page 18

16864 Page 18 of 38 https://doi.org/10.1007/s00521-026-12370-y
is a deliberate methodological choice, consistent with the goal of the study, which is the systematic comparison
across descriptor families, learning paradigms, and fusion strategies rather than the pursuit of the best attainable
performance for any individual model. Because the same configuration is used for every fold, every descriptor
family, and every base learner of the same class, no model is given a tuning advantage over the others, and the
comparisons reported in Sect. 9 reflect differences in modeling capacity under matched experimental conditions.
The LSTM architecture consisted of two stacked recurrent layers with 64 hidden units each, followed by a
fully connected output layer with two units representing valence and arousal. Tanh activation was used for the
LSTM cells, with linear activation for the output layer. Dropout regularization with a rate of 0.2 was applied after
each LSTM layer to prevent overfitting. The network was trained using the Adam optimizer with a learning rate
of 0.001, minimizing mean squared error computed jointly over both emotional dimensions. Training proceeded
for up to 50 epochs with early stopping based on validation loss, using a patience of 10 epochs and a batch size
of 128 frames.
The MLP architecture comprised three fully connected hidden layers with 128, 64, and 32 units respectively,
followed by a two-unit output layer. ReLU activation was used for hidden layers, with linear activation for the
output. Dropout with a rate of 0.3 was applied after each hidden layer. The network was trained using Adam with
a learning rate of 0.001, a batch size of 256 frames, and up to 100 epochs with early stopping and a patience of
15 epochs.
The Random Forest regressor was configured with 300 trees, a maximum depth of 20, minimum samples per
split of 10, and minimum samples per leaf of 5. At each split, a random subset of features equal to the square
root of the total number of features was considered. The regressor operated in multi-output mode, with a single
ensemble structure predicting both valence and arousal jointly, allowing the model to exploit shared dependen-
cies between the two dimensions.
XGBoost was configured with 200 trees, a learning rate of 0.1, and a maximum depth of 6. Subsample and col-
umn subsample ratios were both set to 0.8 to introduce stochasticity and prevent overfitting, and L2 regularization
with lambda equal to 1.0 was applied to the tree weights. The model was implemented in multi-output mode via
a MultiOutputRegressor wrapper, optimizing a squared error objective for each dimension.
TabNet was configured with 5 decision steps, feature and output dimensions of 32 per step, and a relaxation
factor of 1.5 to control the sparsity of attention masks. The network was trained with a batch size of 256, a learn-
ing rate of 0.02, and the Adam optimizer, for up to 100 epochs with early stopping and a patience of 20 epochs.
A sparsity regularization term with lambda equal to 0.001 encouraged the model to focus on the most relevant
features at each step. The output layer consisted of two units predicting valence and arousal simultaneously.
Partial Least Squares Regression was implemented with 20 latent components. The NIPALS algorithm was
used for component extraction, and the model operated in multi-target mode, projecting the input features onto
latent components that maximize covariance with both valence and arousal targets simultaneously. All features
were pre-standardized as described above prior to PLSR training.
8.3 Evaluation metrics
Model performance was evaluated using a set of complementary metrics that capture different aspects of predic-
tion accuracy. The primary multi-output metric is the Mean Euclidean Distance (MED), defined as the average
over all frames of the Euclidean distance between predicted and ground-truth points in the two-dimensional
valence–arousal plane:
1
MED = (vˆ i v i )2+(aˆ i a i )2) (1)
N − −
∑ i √
where v and a denote the ground-truth valence and arousal values for frame i, and v and aˆ their predicted
i i i i
counterparts, with N the total number of frames. The metric provides a holistic measure of accuracy in the
1 3 Neural Computing and Applications (2026) 38:664

### Page 19

https://doi.org/10.1007/s00521-026-12370-y Page 19 of 38 66149
two-dimensional valence–arousal space, reflecting the perceptual distance between predicted and reference
emotional trajectories. Lower values indicate better performance and more accurate reconstruction of emotional
dynamics.
To complement the joint MED, two further error-based metrics are computed separately for valence and
arousal. The Root Mean Squared Error (RMSE) along each dimension penalises larger errors more strongly
through its quadratic dependence on the residuals:
1
RMSE y = (yˆ i y i )2) (2)
N −
√ i
∑
The Mean Absolute Error (MAE) along each dimension provides a robust estimate of the average deviation in
the same units as the target:
1
MAE y = yˆ i y i (3)
N | − |
i
∑
In both definitions y stands for either valence or arousal, with the corresponding metric reported as RMSE ,
V
RMSE , MAE , and MAE in the rest of the manuscript.
A V A
Beyond error-based measures, the Concordance Correlation Coefficient (CCC) is computed to assess the agree-
ment between predicted and ground-truth trajectories along each dimension:
CCC = (2ρσ yˆ σ y )/(σ y 2 ˆ +σ y 2+(µ yˆ − µ y )2) (4)
where ρ denotes Pearson’s correlation, σ the standard deviation, and µ the mean of predicted (yˆ) and ground-
truth (y) values. Unlike MED, RMSE, and MAE, which measure absolute error magnitude, CCC captures how
well predictions track the temporal variation of the emotional trajectory, penalising both poor correlation and
systematic bias. CCC is reported separately for valence (CCC ) and arousal (CCC ) and is the standard metric in
V A
continuous affective computing benchmarks such as MediaEval. The full evaluation table thus reports, for every
model and every ensemble configuration: the joint MED; the per-dimension RMSE , RMSE , MAE , MAE ;
V A V A
and the per-dimension CCC , CCC .
V A
All metrics are computed independently for each cross-validation fold, and final results are reported as mean
values across the five folds.
8.4 Ensemble configurations
All ensemble configurations are built upon out-of-fold predictions generated under the same 5-fold file-wise
cross-validation splits used for the base models, in order to preserve full independence between the base and
meta-learning stages (the rationale for this scheme is detailed in Sect. 7). For LOFO weighted averaging, the
weights are obtained by minimising the joint MED on the out-of-fold predictions of the training folds, then
applied to the held-out fold. For Ridge stacking, the regularisation parameter α was selected from 0.1, 0.5, 1.0,
5.0, 10.0 through grid search on the training folds, with α = 1.0 reported as the default configuration due to stable
performance across all ensemble types.
For the early-fusion (feature-level) experiments, the three descriptor families are concatenated frame by frame
into a single 1085-dimensional representation (988 OpenSMILE + 77 Librosa + 20 PAA features). The concat-
enation is performed after the per-family preprocessing described above. One base model per learning paradigm
retained for the ensemble (see Sect. 9 for the retained set) is trained on the joint representation, with hyperparam-
eter values identical to those used for the late-fusion base models of the same paradigm. The same 5-fold file-wise
splits used for the late-fusion ensembles are reused, so that the per-fold predictions of the early-fusion models are
directly comparable, fold by fold, with their late-fusion counterparts.
Neural Computing and Applications (2026) 38:664 1 3

### Page 20

26064 Page 20 of 38 https://doi.org/10.1007/s00521-026-12370-y
For the hybrid-fusion experiments, a Ridge regression meta-learner is trained on the concatenated pool of
out-of-fold predictions produced by the late-fusion and early-fusion base models. The meta-learner is configured
exactly as the one used in the decision-level Ridge stacking strategy (multi-output Ridge with α = 1.0, fitted with
non-negative coefficients and without intercept). The non-negativity constraint yields automatic sparsity in the
resulting weight vector, providing direct visibility on how the meta-learner allocates contributions across both
base models and fusion levels in a dimension-specific manner (analysis reported in Sect. 9).
8.5 SOTA architecture protocols
The four state-of-the-art audio architectures used as baselines, introduced in Sect. 2, are evaluated on the same
5-fold file-wise cross-validation splits as the proposed framework and with the same set of evaluation metrics,
ensuring a strictly comparable benchmark. Two distinct protocols are required because the four architectures fall
into two regimes: three are pre-trained encoders evaluated under a probing protocol, and the fourth is a Con-
former trained from scratch on the DEAM corpus.
The three pre-trained Transformers, namely MERT [23], HuBERT [22], and wav2vec 2.0 [21], are evaluated
in a frozen-encoder setting. For each model, the encoder weights are kept frozen and the hidden representations
from all Transformer layers are aggregated via a learnable multi-layer weighted sum, where the layer-mixing
weights are obtained as the softmax of a small set of trainable parameters. The aggregated representation is then
mapped to valence and arousal predictions through a compact MLP probe head, trained jointly with the layer-
mixing weights. Training uses the Adam optimizer with a learning rate of 1 10 3, dropout 0.25, batch size 64,
−
×
early stopping on a 10% file-wise held-out validation portion, and patience 15 epochs. The pre-trained encoder
weights are accessed through the public model checkpoints released by the original authors, with no further fine-
tuning of the encoder, so that the comparison reflects the quality of the pre-trained representations rather than that
of any task-specific adaptation.
The Conformer [20], in contrast, is trained end-to-end on log-mel spectrograms (16 kHz, 25 ms window, 10 ms
hop, 80 mel bands) extracted from the same annotated window. The architecture follows the canonical Conformer
design with capacity reduced to match the scale of DEAM (2 blocks, encoder dimension 96, 4 attention heads,
∼
700k parameters). Training uses AdamW with learning rate 1 10 3, weight decay 1 10 4, batch size 8, gradi-
− −
× ×
ent clipping 1.0, and early stopping with patience 5 on a 10% file-wise held-out validation portion of each training
fold; mel-spectrogram normalisation statistics are computed fold-internally to avoid leakage.
8.6 Per-feature importance analysis
Beyond the family-level comparison of base models, a per-feature importance analysis is run to identify which
specific descriptors within each family carry the predictive content. The analysis is conducted with the permu-
tation-importance procedure of Breiman [46] in the implementation pattern documented by scikit-learn. The
procedure is model-agnostic and operates entirely on a held-out fold without retraining. For each feature j in turn,
the values of that feature are randomly permuted across rows of the test set, leaving all other features untouched,
and the model is queried on the perturbed test set. The deterioration of the MED metric is recorded and averaged
over n = 20 independent permutations, yielding the importance score
repeats
I j = E MEDs j huffled − MED 0 (5)
[ ]
where MED is the baseline MED measured on the unperturbed test set. I is expressed in the same units as the
0 j
metric itself. It measures the absolute impact of feature j on the trained model: a large I indicates that the model
j
relies heavily on feature j, while I 0 indicates that the feature carries no predictive content. The score does
j
≈
not decompose the model’s prediction into per-feature contributions, because permutation effects are not additive
in the presence of correlated features and non-linear models. For ease of reading and to align with the standard
1 3 Neural Computing and Applications (2026) 38:664

### Page 21

https://doi.org/10.1007/s00521-026-12370-y Page 21 of 38 66241
presentation in the permutation-importance literature, the raw score is also reported as the share of feature j
within the family’s total positive importance,
I
j
share j = 100 (6)
× I
k k
∑
which is a 0–100 normalisation that sums to 100% across all features of the family and expresses how strongly a
feature stands out within its descriptor set.
The analysis is performed on the three XGBoost base models of the (descriptor method) grid, one per
×
descriptor family. Adopting a single model class as the importance estimator across the three families serves
three purposes. First, methodological consistency: it removes the model as a confounder in the cross-family
comparison of importance scores, so that differences in the resulting rankings reflect properties of the features
themselves rather than properties of different learning paradigms. Second, reproducibility: XGBoost training is
fully deterministic under a fixed random seed and a fixed feature ordering, which allows the analysis to be repro-
duced bit-exactly from the predictions stored in the cross-validation output. Third, empirical competitiveness
across families: as the base-model evaluation reported in Sect. 9.1 shows, XGBoost is the only learning paradigm
that ranks consistently among the top performers on each of the three descriptor families, with stable mid-range
MED values across OpenSMILE, PAA, and Librosa, whereas other paradigms either dominate on one family
and collapse on the others or never reach the top tier. The importance scores are therefore computed on models
whose predictive quality is empirically validated, and uniformly so, across the three feature spaces, rather than
on a model class that happens to be a strong fit only for one of them.
To avoid multiplying the computational cost without a corresponding gain in precision, the importance is not
computed fold-by-fold and then averaged. Instead, a single representative fold per family is selected as the fold
whose per-fold MED is closest to the across-fold mean, the XGBoost model is retrained on the remaining four
folds using the same hyperparameters and random seed as in Sect. 9.1, and the permutation loop is run on the
held-out representative fold. The fold-selection rule is pre-specified, deterministic, and independent of the impor-
tance results, ensuring that the analysis reflects a typical fold rather than a best- or worst-case one. As an internal
consistency check, the baseline MED computed by the retrained model on the representative fold is compared
against the MED stored in the original cross-validation predictions to confirm that the model whose importance
is being probed is the same model whose predictive performance is reported in Sect. 9.1. The number of per-
mutations per feature (n = 20) is chosen so that the standard error of the mean importance, which scales
repeats
as σ/√n
repeats
with σ the across-shuffle standard deviation, is small enough to separate signal from noise in a
z-score sense, even on the high-dimensional OpenSMILE feature set. The results of the analysis are reported in
Sect. 9.1.1.
8.7 Significance testing
To assess the statistical significance of the gains achieved by the ensemble strategies over the individual base
models, paired Wilcoxon signed-rank tests are applied on the per-fold MED values, following the methodological
recommendation of Demšar [53] for the non-parametric comparison of learning algorithms. Each test compares
the per-fold MED of one base model with the per-fold MED of one ensemble configuration on the same five
cross-validation folds, treating the two systems as matched pairs. The one-sided alternative “ensemble lower
error than base” is adopted, which directly tests the directional hypothesis of interest. With n = 5 paired observa-
tions, the minimum attainable one-sided p-value is 1/25 = 0.031 and the maximum attainable rank sum is W = 15;
the simultaneous occurrence of W = 15 and p = 0.031 represents the strongest possible statistical signal that this
experimental design can produce. The corresponding test outcomes are reported in Sect. 9.
Neural Computing and Applications (2026) 38:664 1 3

### Page 22

26264 Page 22 of 38 https://doi.org/10.1007/s00521-026-12370-y
8.8 Implementation
All experiments were implemented in Python 3.10 using standard libraries for machine learning and audio pro-
cessing. Scikit-learn version 1.3.0 was used for Random Forest, Ridge Regression, evaluation metrics, and pre-
processing utilities, while XGBoost version 2.0.0 provided the gradient boosting implementation. Deep learning
models were implemented in PyTorch version 2.1.0, with TabNet using the PyTorch TabNet library version 4.0.
Partial Least Squares Regression was implemented using scikit-learn’s PLSRegression module. Audio feature
extraction relied on OpenSMILE version 3.0 invoked via command-line interface, and Librosa version 0.10.0
for standard MIR descriptors. Psychoacoustic descriptors were extracted with MoSQITo [42]. Data manipulation
was performed using NumPy version 1.24.0 and Pandas version 2.0.0. To ensure full reproducibility, all random
number generators were seeded with a fixed value at the beginning of each experiment.
Throughout the experimental design, file-wise cross-validation, uniform preprocessing, fixed hyperparameter
configurations, and the use of out-of-fold predictions for ensemble construction jointly ensure that the reported
performance estimates are unbiased and comparable across all model–descriptor combinations and fusion
strategies.
9 Experimental results
This section presents the experimental results obtained from the systematic evaluation of individual base mod-
els, fusion strategies, weight analysis, statistical testing, and state-of-the-art audio architecture baselines. The
results are organised into four parts. Subsection 9.1 reports the performance of the eighteen descriptor–method
combinations evaluated as base models, including a per-feature permutation-importance analysis, and identifies
the four paradigms retained for the fusion stage according to the consistency criterion introduced in Sect.6.7.
Subsection 9.2 evaluates the integration of the retained base models at the three fusion levels (late, early, hybrid),
analyses the Ridge meta-learner weights, and validates the gains through paired Wilcoxon signed-rank tests.
Subsection 9.3 reports the comparison against four state-of-the-art audio architectures: three pre-trained Trans-
formers (MERT, HuBERT, wav2vec 2.0) and a Conformer trained from scratch. Subsection 9.4 closes the section
with a synthesis of the findings.
9.1 Individual model performance
The evaluation of individual base models reveals substantial variability in prediction accuracy across differ-
ent combinations of audio descriptors and machine learning methods. Table 2 reports the joint Mean Euclidean
Distance (MED), the per-dimension Root Mean Squared Errors (RMSE , RMSE ) and Mean Absolute Errors
V A
(MAE , MAE ), and the per-dimension Concordance Correlation Coefficients (CCC , CCC ) for all eighteen
V A V A
descriptor–method combinations tested in this study. The MED metric provides a holistic measure of prediction
quality in the two-dimensional valence–arousal space, while CCC captures agreement between predicted and
ground-truth trajectories.
Three combinations stand out at the top of the ranking and are essentially tied on the primary metric. OpenS-
MILE-LSTM and PAA-LSTM both achieve the lowest MED across the full table (0.241), narrowly followed by
Librosa-XGBoost (0.242); the three top performers lie within 0.001 MED of each other and can be considered
statistically indistinguishable on this metric at the precision considered. Their parity is confined to MED, how-
ever: on the remaining metrics OpenSMILE-LSTM separates from the other two, holding the best table-wide
values for RMSE , MAE , CCC , and CCC , as discussed below. The pattern is not driven by a single domi-
A A V A
nant combination but by a small cluster of competitive ones, distributed across all three descriptor families. The
bottom of the ranking is occupied by combinations involving TabNet and PLSR on PAA and Librosa, with MED
1 3 Neural Computing and Applications (2026) 38:664

### Page 23

https://doi.org/10.1007/s00521-026-12370-y Page 23 of 38 66243
Table 2 Performance of individual descriptor–method combinations
Descriptor Method MED RMSEV RMSEA MAEV MAEA CCCV CCCA
OpenSMILE LSTM 0.241 0.205 0.188 0.162 0.146 0.534 0.754
MLP 0.249 0.203 0.202 0.162 0.161 0.427 0.657
RF 0.248 0.200 0.201 0.160 0.162 0.412 0.650
TabNet 0.263 0.218 0.214 0.173 0.168 0.421 0.655
PLSR 0.253 0.205 0.207 0.164 0.165 0.409 0.649
XGBoost 0.244 0.200 0.195 0.160 0.155 0.451 0.696
Librosa LSTM 0.253 0.216 0.203 0.168 0.158 0.510 0.715
MLP 0.248 0.204 0.201 0.163 0.160 0.430 0.662
RF 0.243 0.199 0.196 0.159 0.156 0.440 0.681
TabNet 0.271 0.225 0.220 0.178 0.173 0.412 0.637
PLSR 0.250 0.205 0.202 0.164 0.161 0.400 0.669
XGBoost 0.242 0.199 0.194 0.159 0.154 0.467 0.701
PAA LSTM 0.241 0.204 0.193 0.161 0.151 0.460 0.724
MLP 0.254 0.205 0.209 0.164 0.167 0.382 0.629
RF 0.257 0.208 0.211 0.166 0.168 0.389 0.628
TabNet 0.258 0.208 0.211 0.167 0.169 0.370 0.622
PLSR 0.272 0.216 0.224 0.173 0.181 0.281 0.554
XGBoost 0.256 0.207 0.210 0.165 0.167 0.395 0.635
Lower is better for MED, RMSE, and MAE; higher is better for CCC. Bold values mark the best result across the whole table for each metric
(ties shown in bold for all tied entries)
values at or above 0.25, indicating that these paradigms are less effective at extracting predictive signal from the
lower-dimensional or perceptually structured representations.
Examining performance trends across methods, no single learning paradigm dominates uniformly across the
three descriptor families. LSTM achieves the lowest MED on OpenSMILE (0.241) and on PAA (0.241), while
XGBoost is the best paradigm on Librosa (0.242) and the second-best on OpenSMILE (0.244). The pattern is
better explained by what each paradigm exploits than by the size of the input space. LSTM is the only paradigm
that consumes the frames as an ordered sequence and can model the temporal evolution of the descriptors; this
gives it an advantage wherever the per-frame representation preserves a temporal structure worth tracking, which
is the case both for the perceptually grounded PAA stream and for the broad OpenSMILE pool, and explains
why it attains the lowest MED on these two families. On Librosa, by contrast, tree-based and boosting methods
take the lead: the moderately-dimensional spectral and timbral descriptors behave as largely self-contained per-
frame summaries that fit naturally with axis-aligned splits and additive boosting, so the sequential advantage of
the LSTM is reduced and XGBoost and Random Forest overtake it. MLP tracks the second tier across all three
families. PLSR and TabNet sit consistently in the bottom tier, with average ranks above five out of six.
When comparing descriptor families, the three produce competitive top performers and the gap between the
best models across families is small. OpenSMILE hosts the lowest-MED base model (LSTM, 0.241) and the
largest cluster of upper-table entries thanks to the breadth of its feature pool; Librosa contributes the strongest
non-LSTM combination (XGBoost, 0.242); PAA hosts the strongest LSTM-based result on a low-dimensional
representation (LSTM, 0.241). This convergence is consistent with the rationale of Sect. 5.4: the three families
capture complementary informational cues, and the best method for each depends on the inductive bias of the
learning paradigm rather than on a single family being uniformly superior.
Analysis of dimension-specific performance, examining MAE values separately for valence and arousal, con-
firms a pattern observed throughout the affective computing literature: arousal predictions exhibit lower error
rates compared to valence predictions, consistent with the fact that arousal correlates more directly with acoustic
energy, spectral dynamics, and rhythmic intensity, while valence depends on subtler harmonic, melodic, and
timbral cues. Across the three top combinations, OpenSMILE-LSTM achieves MAE = 0.146 and MAE =
A V
0.162; PAA-LSTM achieves MAE = 0.151 and MAE = 0.161; Librosa-XGBoost achieves MAE = 0.154
A V A
Neural Computing and Applications (2026) 38:664 1 3

### Page 24

26464 Page 24 of 38 https://doi.org/10.1007/s00521-026-12370-y
and MAE = 0.159. The CCC analysis amplifies this asymmetry: across the top combinations, CCC lies in the
V A
0.70–0.75 range while CCC remains in the 0.46–0.53 range, reflecting the inherent difficulty of tracking valence
V
trajectories from frame-level acoustic descriptors.
On the basis of this evidence, the consistency criterion introduced in Sect. 6.7 is applied by retaining the four
learning paradigms that perform competitively across all three descriptor families: LSTM, MLP, Random Forest,
and XGBoost. Paradigms are ordered by their average within-family rank, computed by ranking the six para-
digms from 1 to 6 on each of the seven metrics in Table 2, separately for each descriptor family, and averaging
across the resulting 21 observations per paradigm. XGBoost ranks first (1.98), narrowly ahead of LSTM (2.14),
followed by MLP and Random Forest (both 3.14), with PLSR (5.21) and TabNet (5.38) trailing well behind.
XGBoost ranks first by virtue of consistency rather than dominance: LSTM achieves the lowest MED on two
of the three descriptor families but ranks fifth on Librosa, whereas XGBoost remains in the top three on every
family. The two-position gap between the fourth and fifth paradigms provides a natural cutoff, and the twelve
base models retained for the ensemble stage correspond to the four-by-three grid (LSTM, MLP, RF, XGBoost)
×
(OpenSMILE, Librosa, PAA), excluding TabNet and PLSR.
9.1.1 Per-feature importance
The aggregate ranking presented above identifies which descriptor–method combinations perform best, but does
not address the complementary question of which specific features within each descriptor family carry the pre-
dictive content. To probe this, we report the per-feature permutation-importance analysis described in Sect. 8.6,
applied to the three XGBoost base models of Table 2 (one per descriptor family). For convenience, we recall that
the analysis assigns to each feature j a raw score I , defined as the average deterioration of MED caused by shuf-
j
fling that feature on the held-out fold, and a normalised share share , defined as the percentage of I within the
j j
sum of all per-feature importances of the family. The share is the standard normalisation used in the permutation-
importance literature and sums to 100% across all features of a family. The full definitions of the two quantities
and the procedural details (choice of XGBoost as a unified estimator, representative-fold selection, number of
permutations, sanity-check protocol) are given in Sect. 8.6; the results that follow build on that protocol without
restating it.
Tables 3, 4 and 5 list the ten most important features within each family. The Importance column reports the
raw score I defined above, while the % share column reports its normalised value within the family. The bottom
j
row of each table reports the cumulative figures for the top-10 subset, which give a compact indicator of how
concentrated the importance is within a small fraction of the pool. The same information is shown visually in
Fig. 3, which extends the cumulative curve to the full feature set of each family.
The three rankings expose a consistent finding across descriptor families: the predictive content is concentrated
on timbral and intensity-related features, while tonal and harmonic descriptors play a marginal role. In PAA, the
Table 3 Top-10 features by Rank Feature Importance % share
permutation importance for
1 sharp_mean +0.042 28.47
the PAA-Zwicker descriptor
2 loud_peak +0.014 9.75
family (out of 20)
3 loud_mean +0.012 8.20
4 sharp_peak +0.011 7.80
5 rough_mean +0.011 7.53
6 sharp_var +0.011 7.48
Importance is the raw defined 7 fs_peak +0.011 7.34
above; %share is its share within 8 rough_var +0.007 4.82
the family’s total positive impor-
9 loud_var +0.007 4.69
tance. Baseline MED: 0.255. The
10 fs_mean +0.005 3.75
bottom row reports the cumula-
tive figures for the top-10 subset Top-10 total +0.131 89.81
1 3 Neural Computing and Applications (2026) 38:664

### Page 25

https://doi.org/10.1007/s00521-026-12370-y Page 25 of 38 66245
Table 4 Top-10 features by Rank Feature Importance % share
permutation importance for
1 mfcc_1_mean +0.019 18.15
the Librosa descriptor fam-
2 spectral_flatness_mean +0.017 16.56
ily (out of 77)
3 mfcc_1_std +0.007 7.33
4 mfcc_2_mean +0.007 7.00
5 spectral_rolloff_mean +0.005 5.06
6 rms_mean +0.004 4.36
Importance is the raw defined 7 spectral_flatness_std +0.004 3.66
above; %share is its share within 8 tempo +0.004 3.57
the family’s total positive impor-
9 rms_std +0.003 3.25
tance. Baseline MED: 0.241. The
10 spectral_contrast_3_mean +0.002 2.26
bottom row reports the cumula-
tive figures for the top-10 subset Top-10 total +0.073 71.20
Table 5 Top-10 features by Rank Feature Importance % share
permutation importance for
1 mfcc_sma[1]_min +0.004 9.06
the OpenSMILE descriptor
2 lspFreq_sma[0]_quartile2 +0.002 3.47
family (out of 988)
3 lspFreq_sma[0]_quartile3 +0.002 3.43
4 mfcc_sma[1]_quartile1 +0.002 3.34
5 lspFreq_sma[0]_quartile1 +0.001 2.41
6 pcm_intensity_sma_amean +0.001 1.96
Importance is the raw defined 7 lspFreq_sma[7]_quartile1 +0.001 1.90
above; %share is its share within 8 mfcc_sma[1]_amean +0.001 1.90
the family’s total positive impor-
9 lspFreq_sma[0]_amean +0.001 1.69
tance. Baseline MED: 0.245. The
10 mfcc_sma[1]_quartile3 +0.001 1.57
bottom row reports the cumula-
tive figures for the top-10 subset Top-10 total +0.015 30.73
F ig. 3 Cumulative permutation-importance curves for
the three descriptor families. The horizontal axis reports
the number of features (logarithmic scale), ordered by
decreasing importance; the vertical axis reports the cumu-
lative share of total positive importance. Filled markers
indicate where each curve crosses the 80% threshold:
PAA at 8 features, Librosa at 15, OpenSMILE at 118. The
horizontal separation between the three crossing points
quantifies the different degrees of redundancy in each
feature pool
leading feature (sharp_mean) alone accounts for 28.5% of the family’s total positive importance (by far the larg-
est single contribution observed in the analysis), and the sharpness, loudness, and roughness descriptors together
account for more than 80% of the family total; tonality contributes less than 6%. In Librosa, the means of the first
two MFCC coefficients and the two spectral-flatness statistics (mean and standard deviation) together account
for 45% of the family total, while the twenty-four chroma features carry only about 7%. In OpenSMILE, the top-
ranked features are dominated by the first MFCC coefficient and by line-spectral-pair frequencies, both of which
encode the gross spectral envelope; F0 and pitch-related functionals contribute less than 1%. This convergence
across three independently designed feature pools indicates that the predictive signal driving the models is largely
Neural Computing and Applications (2026) 38:664 1 3

### Page 26

26664 Page 26 of 38 https://doi.org/10.1007/s00521-026-12370-y
a timbral one, a finding that aligns with the music emotion recognition literature, where spectral brightness and
noisiness are consistently identified as primary acoustic correlates of arousal.
The three families also differ markedly in how their predictive content is distributed across their feature pool,
as quantified by the cumulative-importance curves of Fig. 3. PAA is the most compact: with only 20 features
and a structured psychoacoustic design, the importance is spread relatively evenly, and eight features are already
sufficient to capture more than 80% of the family total. Librosa is intermediate: 15 of its 77 features cover the
80% threshold, beyond which the per-feature contributions decay quickly and become negligible. OpenSMILE
is the sparsest: reaching the 80% mark requires 118 of its 988 features, and the bulk of the pool contributes little
individually. This pattern quantifies the cost of dimensional richness: the broader the feature pool, the larger the
fraction of its features that the model treats as redundant or uninformative, which is consistent with the decision,
motivated in Sect. 5, to retain the curated emobase_v2 set in full rather than applying a supervised feature selec-
tion on top of it.
Two methodological caveats apply to the interpretation of these results. First, permutation importance mea-
sures how strongly the trained model relies on each feature, not how informative the feature is in absolute terms:
in the presence of correlated features the score of each is reduced because shuffling either one leaves a working
surrogate available to the model. The cumulative-importance curve is therefore a conservative estimate of how
much of the model’s behaviour is concentrated in the top-N features, and is particularly conservative for OpenS-
MILE, where many functionals of the same low-level descriptor encode overlapping information. Second, the
ranking is computed on the XGBoost model whose behaviour is being probed; a different learning paradigm fitted
on the same feature set could distribute its importance somewhat differently.
9.2 Ensemble strategies and fusion levels
This subsection evaluates the integration of the base models at the three fusion levels introduced in Sect. 7:
decision-level (late) fusion, feature-level (early) fusion, and hybrid fusion. Before turning to the fusion experi-
ments, we make explicit the selection of the base learners that feed them. The base-model evaluation of Sect. 9.1
showed that two of the six paradigms, PLSR and TabNet, fall well below the others and, more importantly, are
not competitive across all three descriptor families (their average within-family rank exceeds five out of six).
Following the consistency criterion anticipated in Sect. 6.7, only the four paradigms that perform competitively
on every descriptor family, namely LSTM, MLP, Random Forest, and XGBoost, are retained for the fusion stage.
This yields twelve base models (four paradigms three descriptor families), which constitute the pool from
×
which all fusion configurations are built.
9.2.1 Late fusion
Late fusion combines the predictions of the twelve retained base models through the three decision-level strategies
introduced in Sect. 7: arithmetic mean averaging, Leave-One-Fold-Out (LOFO) optimised weighted averaging,
and stacking with Ridge regression meta-learning. The strategies are applied to eight configurations, instantiated
by grouping the twelve base models according to complementary criteria. The configuration All 12 combines
all retained base models. Configurations All LSTM, All MLP, All RF, All XGBoost combine the same learning
paradigm across the three descriptor families (cross-descriptor ensembles). Configurations Within OpenSMILE,
Within Librosa, Within PAA combine all four learning paradigms within a single descriptor family (cross-method
ensembles).
Across configurations, a clear hierarchy emerges from Table 6 and is preserved across all three strategies: All
12 and All LSTM occupy the top of the ranking, followed by Within OpenSMILE and Within Librosa, then All
XGBoost and All MLP, and finally Within PAA and All RF. This ordering is essentially the same whatever the
combination mechanism, which indicates that the primary determinant of ensemble effectiveness is the diver-
sity and quality of the constituent set rather than the sophistication of the combination strategy. The two top
1 3 Neural Computing and Applications (2026) 38:664

### Page 27

https://doi.org/10.1007/s00521-026-12370-y Page 27 of 38 66247
Table 6 Ensemble performance across three decision-level strategies (arithmetic, LOFO, Ridge stacking) and eight configu-
rations
Configuration N MED RMSEV RMSEA MAEV MAEA CCCV CCCA
All 12 12
Arithmetic 0.228 0.189 0.181 0.151 0.144 0.485 0.724
LOFO 0.218 0.184 0.170 0.146 0.134 0.551 0.774
Ridge 0.217 0.184 0.170 0.146 0.133 0.549 0.778
All LSTM 3
Arithmetic 0.220 0.187 0.173 0.147 0.135 0.558 0.776
LOFO 0.220 0.186 0.172 0.147 0.135 0.557 0.777
Ridge 0.220 0.186 0.172 0.148 0.135 0.544 0.772
W. OpenSMILE 4
Arithmetic 0.230 0.191 0.182 0.152 0.145 0.491 0.725
LOFO 0.226 0.190 0.177 0.151 0.139 0.527 0.754
Ridge 0.225 0.189 0.176 0.150 0.139 0.518 0.760
W. Librosa 4
Arithmetic 0.230 0.191 0.184 0.152 0.145 0.501 0.725
LOFO 0.228 0.191 0.182 0.151 0.144 0.517 0.736
Ridge 0.228 0.191 0.182 0.152 0.143 0.510 0.740
All XGBoost 3
Arithmetic 0.237 0.195 0.190 0.156 0.151 0.456 0.700
LOFO 0.236 0.194 0.188 0.155 0.150 0.468 0.709
Ridge 0.235 0.195 0.188 0.155 0.149 0.473 0.715
All MLP 3
Arithmetic 0.239 0.196 0.192 0.157 0.154 0.434 0.676
LOFO 0.239 0.196 0.192 0.157 0.153 0.439 0.678
Ridge 0.237 0.196 0.191 0.156 0.150 0.446 0.701
W. PAA 4
Arithmetic 0.244 0.200 0.197 0.160 0.157 0.422 0.676
LOFO 0.238 0.199 0.189 0.158 0.149 0.453 0.717
Ridge 0.238 0.199 0.190 0.159 0.150 0.438 0.714
All RF 3
Arithmetic 0.243 0.198 0.196 0.159 0.157 0.425 0.668
LOFO 0.241 0.197 0.194 0.158 0.155 0.437 0.679
Ridge 0.240 0.197 0.194 0.157 0.154 0.448 0.692
Best base (OS-LSTM) 1 0.241 0.205 0.188 0.162 0.146 0.534 0.754
The reference row at the bottom reports the best individual base model for comparison (OpenSMILE-LSTM). Lower is better for MED, RMSE,
and MAE; higher is better for CCC. Bold marks the best result within each metric column
configurations both draw on all three descriptor families (All 12 across the four paradigms, All LSTM across the
three descriptors), while the configurations confined to a single descriptor family or to a single non-LSTM para-
digm trail behind, confirming that cross-descriptor diversity is the main source of ensemble gain.
The effect of the combination strategy, by contrast, is more nuanced than a simple “more sophisticated is bet-
ter” progression. The decisive step is from arithmetic averaging to data-driven weighting: on the All 12 configu-
ration the MED drops from 0.228 (arithmetic) to 0.218 (LOFO), a 4.5% reduction, as the weighting suppresses
the weaker base models that an unweighted average cannot discount. The further step from LOFO to Ridge
stacking, however, leaves the MED essentially unchanged (0.218 vs 0.217), and the two weighted strategies
are statistically indistinguishable on this metric (Sect. 9.2.4). On the homogeneous configurations (All LSTM,
Within Librosa), even the first step yields almost nothing, because the constituent models already produce highly
correlated predictions and weighting has little room to improve over the simple average. The value of Ridge
stacking therefore lies not in a further reduction of MED but in its dimension-specific weighting, which produces
a marginal improvement in concordance (CCC rises from 0.774 under LOFO to 0.778 under Ridge on All 12)
A
Neural Computing and Applications (2026) 38:664 1 3

### Page 28

26864 Page 28 of 38 https://doi.org/10.1007/s00521-026-12370-y
and, more importantly, makes the contribution of each base model directly interpretable per emotional dimension,
as analysed in Sect. 9.2.4.
Taken together, the best late-fusion result is obtained by the All 12 configuration, with LOFO and Ridge stack-
ing essentially tied (MED = 0.218 and 0.217). Relative to the best individual base model (OpenSMILE-LSTM,
MED = 0.241), the All 12 Ridge stacking reduces the MED by 9.8%, with simultaneous improvements in concor-
dance: CCC rises from 0.534 to 0.549 and CCC from 0.754 to 0.778. This is the configuration carried forward,
V A
as the late-fusion representative, to the comparison across fusion levels and to the weight analysis.
9.2.2 Early and hybrid fusion
Late fusion combines the base models only at the level of their predictions. The two remaining fusion levels inter-
vene earlier or at both stages. In feature-level (early) fusion, the three descriptor families are concatenated into a
1085-dimensional joint representation and one base model per retained learning paradigm is trained on it, so that
cross-descriptor interactions can be exploited directly in the input space. In hybrid fusion, a Ridge stacking meta-
learner combines the out-of-fold predictions of the early-fusion and late-fusion base models, integrating the two
levels. Table 7 reports the seven metrics for the four early-fusion base models and for the hybrid Ridge stacking,
with the best late-fusion ensemble and the best individual base model included as references.
The hybrid Ridge stacking achieves the best result of the proposed framework across all seven metrics: MED
= 0.213 (a 1.8% improvement over the best late-fusion ensemble and 11.4% over the best individual base model);
CCC = 0.575 (a 4.8% improvement over the best late-fusion ensemble and a 7.6% improvement over the best
V
individual base model); CCC = 0.798 (a 2.6% improvement over the best late-fusion ensemble and a 5.8%
A
improvement over the best individual base model). The pattern of metric improvements is consistent and reflects
a real gain in tracking quality, not just in mean error magnitude.
The early-fusion base models alone are weaker than the late-fusion ensemble: their MED values lie in the
0.233–0.242 range, all worse than the late-fusion Stacking All 12 (MED = 0.217). However, the four early-fusion
models follow the same paradigm ranking observed for the late-fusion base models (LSTM> XGBoost> RF >
MLP), and the early-fusion LSTM trained on the 1085-dimensional concatenated representation reaches MED
= 0.233, slightly better than any of the three late-fusion LSTMs trained on a single descriptor family. The early-
fusion stage thus contributes complementary, not substitutive, information: it allows the LSTM to exploit cross-
descriptor interactions directly in the input space, in a way that the late-fusion meta-learner can recover only
indirectly through the predictions.
9.2.3 Weight analysis
The Ridge meta-learner used for late and hybrid fusion exposes, through its learned coefficients, the contribution
of each base prediction to each emotional dimension. Because the meta-learner is fitted with non-negative coef-
ficients and no intercept, the weight vector is automatically sparse and directly interpretable. We analyse first the
Table 7 Performance of the early-fusion base models and of the hybrid Ridge stacking, with reference values for the best
late-fusion ensemble and the best individual base model
Experiment MED RMSEV RMSEA MAEV MAEA CCCV CCCA
Early MLP 0.242 0.201 0.195 0.160 0.154 0.461 0.692
Early RF 0.240 0.197 0.193 0.158 0.154 0.449 0.688
Early LSTM 0.233 0.199 0.180 0.158 0.141 0.554 0.773
Early XGBoost 0.235 0.195 0.188 0.156 0.149 0.492 0.724
Hybrid ridge 0.213 0.182 0.165 0.144 0.130 0.575 0.798
Stacking All 12 (best late) 0.217 0.184 0.170 0.146 0.133 0.549 0.778
OpenSMILE-LSTM (best base) 0.241 0.205 0.188 0.162 0.146 0.534 0.754
Lower is better for MED, RMSE, MAE; higher for CCC. Bold marks the best within the proposed framework
1 3 Neural Computing and Applications (2026) 38:664

### Page 29

https://doi.org/10.1007/s00521-026-12370-y Page 29 of 38 66249
Table 8 Ridge meta-learning weights for the All 12 configuration
Individual base models Aggregated weights
Base model Val Aro Aggregate Val Aro
OpenSMILE-LSTM 0.282 0.328 By learning paradigm
Librosa-LSTM 0.211 0.169 All LSTM (3) 0.619 0.718
PAA-LSTM 0.126 0.221 All XGBoost (3) 0.231 0.212
Librosa-XGBoost 0.169 0.126 All MLP (3) 0.122 0.057
OpenSMILE-XGBoost 0.057 0.086 All RF (3) 0.029 0.013
OpenSMILE-MLP 0.078 0.049 By descriptor family
Librosa-MLP 0.041 0.008 All OpenSMILE (4) 0.419 0.463
Librosa-RF 0.026 0.013 All Librosa (4) 0.447 0.316
PAA-XGBoost 0.005 0.000 All PAA (4) 0.135 0.221
PAA-MLP 0.003 0.000
OpenSMILE-RF 0.002 0.000
PAA-RF 0.001 0.000
Ridge regression (= 1.0, non-negative coefficients, no intercept) learns separate linear combinations for valence and arousal. Values are mean
across folds, normalised to 1.0 within each dimension. The left side reports the weights of the twelve individual base models. The right side
reports the same weights aggregated by learning paradigm (top) and by descriptor family (bottom): aggregate by paradigm sums the weights
of the three base models (one per descriptor family) sharing the same learning paradigm; aggregate by descriptor sums the weights of the four
base models (one per learning paradigm) sharing the same descriptor family
Table 9 Ridge meta-learning Individual base predictions Aggregated weights
weights for the hybrid stack- Base prediction Val Aro Aggregate Val Aro
ing. Sixteen base predictions
Early LSTM 0.242 0.322 By learning paradigm
(twelve late-fusion + four
Late OpenSMILE-LSTM 0.175 0.191 All LSTM (4) 0.665 0.744
early-fusion)
Early XGBoost 0.158 0.164 All XGBoost (4) 0.230 0.198
Late PAA-LSTM 0.104 0.156 All MLP (4) 0.096 0.058
Late Librosa-LSTM 0.144 0.075 All RF (4) 0.008 0.000
Values are mean across folds, Early MLP 0.071 0.057 By fusion level
normalised to 1.0 within each
Late Librosa-XGBoost 0.070 0.033 Early (4) 0.478 0.543
dimension. The left side reports
Late OpenSMILE-MLP 0.018 0.001 Late (12) 0.521 0.457
the weights of the sixteen
Early RF 0.007 0.000
individual base predictions.
The right side reports the same Late Librosa-MLP 0.004 0.000
weights aggregated by learn- Late PAA-MLP 0.003 0.000
ing paradigm (top, summing Late OpenSMILE-XGBoost 0.002 0.001
early- and late-fusion predictions Late Librosa-RF 0.001 0.000
sharing the same paradigm) and
Late OpenSMILE-RF 0.000 0.000
by fusion level (bottom, sum-
Late PAA-RF 0.000 0.000
ming all four early-fusion and all
twelve late-fusion predictions) Late PAA-XGBoost 0.000 0.000
late-fusion All 12 configuration (Table 8), then the hybrid configuration (Table 9); the two are visualised in panels
(a) and (b) of Fig. 4.
The weight table exposes a clear and interpretable structure. LSTM-based models receive the largest aggregate
share of the Ridge weights, accounting for 0.619 of the valence prediction and 0.718 of the arousal prediction in
the All 12 configuration. The contribution is distributed across all three descriptor families: OpenSMILE-LSTM
is the single largest contributor (0.282 valence, 0.328 arousal), followed by PAA-LSTM (0.126 valence, 0.221
arousal) for arousal and by Librosa-LSTM (0.211 valence, 0.169 arousal) for valence. The temporal modelling
capacity of LSTM thus dominates the ensemble irrespective of the input descriptor, a pattern that aligns with the
predictive importance of temporal dependencies in continuous emotion tracking.
XGBoost emerges as the second contributing paradigm, with an aggregate share of 0.231 for valence and 0.212
for arousal. The weight allocation is concentrated on the Librosa and OpenSMILE families (Librosa-XGBoost:
Neural Computing and Applications (2026) 38:664 1 3

### Page 30

36064 Page 30 of 38 https://doi.org/10.1007/s00521-026-12370-y
Fig. 4 Ridge meta-learner weights for (a) the late-fusion All 12 configuration (Table 8) and (b) the hybrid stacking configura-
tion (Table 9). For each base prediction the figure reports two bars, valence (blue) and arousal (orange); within each panel,
base predictions are ordered by the mean of their valence and arousal weights in descending order. Weights are mean across
folds and normalised to 1.0 within each dimension
0.169 valence, 0.126 arousal; OpenSMILE-XGBoost: 0.057 valence, 0.086 arousal), while the contribution from
PAA-XGBoost is essentially zero. The pattern reflects the inductive bias of gradient boosting: tree-based models
thrive on the higher-dimensional Librosa and OpenSMILE inputs but offer little additional signal on the perceptu-
ally structured PAA representation, where the LSTM already extracts most of the available information.
MLP and Random Forest contribute marginally (aggregate shares of 0.122 and 0.029 for valence, 0.057 and
0.013 for arousal). Half of their six base models receive weights at or below 0.01 on both dimensions: the non-
negative Ridge formulation performs an automatic selection, retaining only the predictions that add content
beyond what LSTM and XGBoost already provide and discarding the redundant ones.
Examining the dimension-specific patterns, the descriptor-aggregated weights in the right side of Table 8
expose a clean separation. The Librosa family contributes substantially more to valence than to arousal (0.447
vs 0.316), the largest dimension-asymmetry observed in the table. This is consistent with the harmonic and
chromatic content captured by Librosa descriptors (chroma features, spectral centroid, MFCCs), which carry
information relevant to harmonic mode and timbral character, the acoustic correlates traditionally associated
with valence. Symmetrically, the PAA family contributes more to arousal than to valence (0.221 vs 0.135), and
the OpenSMILE family also leans toward arousal (0.463 vs 0.419). This reflects the energy-, loudness-, and
roughness-based content that dominates these descriptor families, and that aligns with the acoustic correlates of
1 3 Neural Computing and Applications (2026) 38:664

### Page 31

https://doi.org/10.1007/s00521-026-12370-y Page 31 of 38 66341
arousal documented in the psychoacoustic literature. The dimension-specific weighting of the Ridge meta-learner
thus exposes a clean separation that is theoretically expected and empirically robust across folds.
This complementarity is the structural reason why the hybrid stacking outperforms both fusion levels in isola-
tion. Table 9 reports the Ridge weights learned by the hybrid meta-learner over the pool of sixteen base predic-
tions (twelve late-fusion + four early-fusion), separately for valence and arousal; the corresponding visualisation
is panel (b) of Fig. 4.
Three patterns dominate the hybrid weight structure. First, the early-fusion and late-fusion contributions are
nearly balanced, with early-fusion accounting for 0.478 of the valence prediction and 0.543 of the arousal predic-
tion, and late-fusion accounting for the remainder. The meta-learner thus does not select one fusion level over
the other but rather combines them in roughly equal proportions, confirming that the two carry complementary
information. Second, LSTM dominates the contribution as in the late-fusion All 12 ensemble: aggregating the
four LSTM models (one early plus three late) gives a share of 0.665 for valence and 0.744 for arousal. This is
consistent with the corresponding aggregate in the late-fusion Ridge weights (0.619/0.718 in Table 8) and with
the literature consensus that temporal modelling is essential for continuous emotion tracking. Third, eight out
of sixteen base predictions receive a weight at or below 0.01 in both dimensions and are effectively discarded
by the meta-learner: the four Random Forest variants (Early RF and the three Late RFs), the two PAA-MLP and
Librosa-MLP late predictions, and the two PAA-XGBoost and OpenSMILE-XGBoost late predictions. The non-
negative Ridge constraint thus performs an automatic selection on the input pool, retaining only the predictions
that add informational content.
9.2.4 Statistical significance
The gains achieved by the fusion strategies are assessed with paired Wilcoxon signed-rank tests on the per-fold
MED values, following the recommendation of Demšar [53] for the non-parametric comparison of learning algo-
rithms across matched folds. With n = 5 folds, the strongest attainable one-sided signal is W = 15 at p = 0.031
, obtained when one system has a lower per-fold error than the other on all five folds. The decisive step in the
late-fusion hierarchy passes this threshold: both the LOFO and the Ridge stacking All 12 ensembles achieve a
lower MED than the arithmetic All 12 ensemble on every one of the five folds (W = 15, p = 0.031). The further
step from LOFO to Ridge stacking, by contrast, does not reach significance (W = 11 on five folds, p 0.31):
≈
the two weighted strategies are statistically indistinguishable on MED, consistent with their near-identical mean
values. The hybrid Ridge stacking, in turn, improves on the best late-fusion ensemble on all five folds, recovering
the maximal W = 15, p = 0.031 signal. The same maximal signal separates the late-fusion ensemble from each
of the four early-fusion base models, which it outperforms on every fold (W = 15, p = 0.031 in all four com-
parisons), confirming that the hybrid gain comes from genuine complementarity rather than from the early-fusion
models being competitive on their own. The picture that emerges is therefore one of two statistically validated
steps, from unweighted to weighted late fusion and from late to hybrid fusion, separated by a plateau in which
the choice between LOFO and Ridge stacking is, for predictive accuracy, immaterial; the reason to prefer Ridge
stacking is its dimension-specific interpretability rather than a significant accuracy gain.
9.3 Comparison with state-of-the-art audio architectures
To position the proposed framework against the current state of the art in audio representation learning, four state-
of-the-art audio architectures are evaluated on the same five cross-validation folds. Three are pre-trained Trans-
formers used under the unified probing protocol described in Sect. 8: MERT [23], pre-trained on music; HuBERT
[22], pre-trained on speech with a masked discrete-target prediction objective; and wav2vec 2.0 [21], pre-trained
on speech with a contrastive masked-prediction objective. The fourth is a Conformer [20] trained from scratch on
the DEAM mel-spectrograms, included as an architectural baseline that does not rely on external data. Table 10
Neural Computing and Applications (2026) 38:664 1 3

### Page 32

36264 Page 32 of 38 https://doi.org/10.1007/s00521-026-12370-y
Table 10 Performance of the four state-of-the-art audio architectures and of the proposed framework
Model MED RMSEV RMSEA MAEV MAEA CCCV CCCA
MERT (music) 0.201 0.167 0.162 0.132 0.127 0.680 0.810
HuBERT (speech) 0.236 0.192 0.190 0.153 0.151 0.551 0.733
wav2vec 2.0 (speech) 0.239 0.197 0.192 0.156 0.152 0.519 0.718
Conformer (from scratch) 0.246 0.202 0.195 0.162 0.157 0.457 0.705
Hybrid Ridge (ours, best) 0.213 0.182 0.165 0.144 0.130 0.575 0.798
Stacking All 12 (ours, best late) 0.217 0.184 0.170 0.146 0.133 0.549 0.778
OpenSMILE-LSTM (ours, best base) 0.241 0.205 0.188 0.162 0.146 0.534 0.754
The first three are pre-trained Transformers; the fourth is a Conformer trained from scratch. The lower block reports the proposed framework,
with the hybrid Ridge stacking as its best configuration. Lower is better for MED, RMSE, and MAE; higher is better for CCC. Bold marks the
best result per metric
reports the resulting performance, alongside the three reference configurations of the proposed framework: the
hybrid Ridge stacking (its best configuration), the best late-fusion ensemble, and the best individual base model.
Four observations emerge. First, MERT achieves the lowest error of any model evaluated (MED = 0.201), with
CCC values of 0.680 for valence and 0.810 for arousal that exceed those of every other model in this study. The
result reflects the advantage of music-domain self-supervised pre-training: a 330M-parameter encoder trained
on a large unlabelled music corpus produces representations intrinsically adapted to the acoustic structure of the
task. The best configuration of the proposed framework, the hybrid Ridge stacking (MED = 0.213), is the closest
competitor to MERT, trailing it by 6.0% in MED, down from the 8.0% gap of the best late-fusion ensemble. The
hybrid framework thus narrows the distance to the music-pre-trained Transformer while relying on no external
data and a fraction of the parameters. Second, the speech-domain Transformers (HuBERT and wav2vec 2.0) trail
the proposed framework: HuBERT achieves MED = 0.236 and wav2vec 2.0 MED = 0.239, both above the hybrid
Ridge stacking (0.213) and the best late-fusion ensemble (0.217). The transfer of speech-pre-trained encoders
to music emotion recognition is therefore beneficial relative to most individual base models but not sufficient to
match the proposed ensemble of hand-crafted descriptors. Third, the gap between MERT and HuBERT (the same
family of architectures pre-trained on different corpora) is substantially larger than the gap between HuBERT and
wav2vec 2.0 (different architectures pre-trained on similar corpora), indicating that for this task the pre-training
domain matters more than the specific encoder design. Fourth, the Conformer trained from scratch reaches MED
= 0.246, below all other state-of-the-art baselines and the only one that also trails the best individual base model.
The proposed hybrid framework outperforms it by 13.4% in MED (0.213 vs 0.246), a directly apples-to-apples
comparison since neither model relies on external data. The architecture alone, without large-scale pre-training,
is not sufficient on a corpus of the size of DEAM, and the gap to the pre-trained Transformers quantifies the con-
tribution of pre-training in isolation from architectural design.
Beyond raw accuracy, two considerations qualify the comparison. First, MERT operates with two orders of
magnitude more parameters than the proposed framework and requires substantially more compute at inference
time (feature extraction on the order of hours of CPU time for the dataset, versus minutes for the hand-crafted
descriptors). The hybrid framework remains the practical choice for applications with latency or compute con-
straints, while closing most of the accuracy gap. Second, the meta-learner weights of the proposed framework
provide direct interpretability of the contributions of each descriptor family, learning paradigm, and fusion level
to each emotional dimension, an analysis that is unavailable for the Transformer baselines.
9.4 Remarks
Three broader observations emerge from the experiments presented in this section.
The first concerns where the predictive signal actually resides. Across base models, ensembles, and fusion
levels, the gains track the diversity of the information being combined far more closely than the sophistication
of the mechanism combining it. Weighting beats averaging, hybrid beats single-level fusion, and the All 12 and
1 3 Neural Computing and Applications (2026) 38:664

### Page 33

https://doi.org/10.1007/s00521-026-12370-y Page 33 of 38 66343
All LSTM configurations lead the ranking, but in every case the improvement materialises only when genuinely
different acoustic views are brought together, and saturates as soon as the combination becomes homogeneous.
The corollary is practical: for continuous MER, effort is better spent broadening the descriptor and fusion reper-
toire than refining a single combiner, since the meta-learner stage contributes a real but bounded increment once
diversity is in place.
The second concerns interpretability as a structural property rather than an add-on. Because every combina-
tion stage in the framework is a linear meta-learner, the same coefficients that produce the prediction also explain
it, and they do so in a way that recovers a theoretically expected structure without being told to: Librosa weight
concentrates on valence, OpenSMILE and PAA on arousal, and temporal models dominate both. This alignment
between learned weights and psychoacoustic expectation is the kind of evidence that a black-box encoder cannot
supply, and it is what distinguishes the contribution of this framework from a mere accuracy number.
The third concerns the position of hand-crafted-descriptor ensembles in the current landscape. The comparison
with pre-trained Transformers isolates pre-training domain, not architecture, as the decisive variable: a transpar-
ent ensemble of classical descriptors surpasses speech-pre-trained Transformers and a from-scratch Conformer,
and trails only the music-pre-trained MERT, which it approaches to within a narrow margin without any external
data. The practical implication is that, where compute, data, or interpretability are constraints, an interpretable
descriptor ensemble remains a competitive and fully transparent alternative, and a natural baseline against which
future music-pre-trained or hybrid systems can be measured.
10 Conclusions
This study presented a comprehensive comparative framework for predicting continuous emotional trajectories
in music using the valence–arousal model of affect. Through systematic evaluation of three theoretically diverse
audio descriptor families (OpenSMILE, PAA, Librosa) combined with six complementary machine learning
paradigms (LSTM, MLP, Random Forest, TabNet, PLSR, XGBoost), we investigated how descriptor diversity,
model architecture, and integration strategy jointly contribute to emotion prediction accuracy. The integration was
studied at the three canonical fusion levels: decision-level (late) through arithmetic averaging, LOFO-weighted
averaging, and Ridge stacking; feature-level (early) through descriptor concatenation; and hybrid stacking that
combines early- and late-fusion predictions. The proposed framework was further benchmarked against four
state-of-the-art audio architectures: three pre-trained Transformers (MERT, HuBERT, wav2vec 2.0) under a uni-
fied probing protocol, and a Conformer trained from scratch on the DEAM mel-spectrograms. The ensemble
gains were validated through paired Wilcoxon signed-rank tests, and the predictive content of each descriptor
family was further characterised through a per-feature permutation-importance analysis. The experimental design
prioritised methodological rigour through file-wise cross-validation to prevent data leakage, unified preprocess-
ing pipelines, and comprehensive evaluation using a primary multi-output metric (Mean Euclidean Distance,
MED) supported by dimension-specific RMSE, MAE, and Concordance Correlation Coefficient (CCC). Beyond
quantitative performance metrics, this work provides empirically validated insights into the relative strengths of
different feature representations and modelling approaches, establishing a transparent and reproducible baseline
for comparative MER research.
The six research questions posed in Sect. 4 receive direct empirical answers through the experimental results
of Sect. 9.
First, regarding descriptor families (Table 2 of Sect. 9): the three families OpenSMILE, Librosa, and PAA
produce competitive top performers and the gap between the best models across families is small. OpenSMILE-
LSTM and PAA-LSTM both achieve the lowest MED of any individual base model (0.241), narrowly ahead of
Librosa-XGBoost (0.242); the three top performers lie within 0.001 MED of each other. Each descriptor fam-
ily hosts one of these top three combinations, indicating that the families capture complementary informational
cues: OpenSMILE excels when paired with sequence learning on its broad affective-computing pool, PAA hosts
Neural Computing and Applications (2026) 38:664 1 3

### Page 34

36464 Page 34 of 38 https://doi.org/10.1007/s00521-026-12370-y
the strongest LSTM-based result on a low-dimensional perceptually structured representation, and Librosa con-
tributes the strongest non-LSTM combination through gradient boosting on its moderately-dimensional MIR
descriptors. The choice of the most effective descriptor depends on the inductive bias of the learning paradigm
with which it is paired, rather than on a single family being uniformly superior. The complementary per-feature
permutation-importance analysis reported in Sect. 9.1.1 sharpens this picture: across all three families the predic-
tive content is concentrated on timbral and intensity-related descriptors (sharpness and loudness in PAA, the first
MFCC coefficients and spectral flatness in Librosa, the first MFCC coefficient and line-spectral-pair frequencies
in OpenSMILE), while tonal and harmonic descriptors play a marginal role in each family. The three families
differ, however, in how concentrated their predictive content is: the top-10 features cover 89.8% of the total
positive importance in PAA, 71.2% in Librosa, and only 30.7% in OpenSMILE, quantifying the redundancy that
characterises broader feature pools.
Second, regarding modelling paradigms (Table 2 of Sect. 9): two paradigms, LSTM and XGBoost, stand out
as the strongest, but neither is best on every descriptor family. LSTM achieves the lowest MED on OpenSMILE
(0.241) and on PAA (0.241), while XGBoost is the strongest paradigm on Librosa (0.242) and the second-best on
OpenSMILE (0.244). The discriminating factor is what each paradigm exploits rather than the size of the input
space: LSTM is the only paradigm that consumes the frames as an ordered sequence, and it leads wherever the
per-frame representation preserves a temporal structure worth tracking, as in the PAA and OpenSMILE streams;
on Librosa, whose descriptors behave as largely self-contained per-frame summaries, axis-aligned splits and
additive boosting take the lead instead. The average within-family rank, computed across the seven metrics
of Table 2 (21 observations per paradigm), identifies a clear cutoff after the fourth paradigm: XGBoost (1.98),
LSTM (2.14), MLP and Random Forest (both 3.14) form a top tier, while PLSR (5.21) and TabNet (5.38) trail
by over two rank positions. The four top paradigms are thus retained as the base learners for the ensemble stage,
while PLSR and TabNet are excluded by the consistency criterion introduced in Sect. 6.7.
Third, regarding decision-level ensemble strategies (Table 6 of Sect. 9): combining the twelve retained base
models through Ridge meta-learning achieves the best late-fusion performance, with the All 12 configuration
reaching MED = 0.217, CCC = 0.549, and CCC = 0.777. This corresponds to a 9.8% MED improvement over
V A
the best individual base model (OpenSMILE-LSTM, MED = 0.241), a 2.7% improvement in CCC (0.534 to
V
0.549), and a 3.2% improvement in CCC (0.754 to 0.777). Progressive improvements in MED are observed
A
from arithmetic averaging (0.228) to LOFO-weighted averaging (0.218) to Ridge stacking (0.217), with the larg-
est single jump occurring in the move from arithmetic to LOFO weighting; the further refinement from LOFO
to Ridge stacking is marginal in MED but produces measurable gains in CCC. The paired Wilcoxon signed-rank
tests reported in Sect. 9.2 validate the two substantive steps of the hierarchy, from unweighted to weighted late
fusion and from late to hybrid fusion, at the maximum attainable significance level (W = 15, p = 0.031 on five
folds), while the refinement from LOFO to Ridge stacking is not statistically significant on MED.
Fourth, regarding fusion levels (Table 7 of Sect. 9): the hybrid Ridge stacking, combining the predictions of
the late-fusion base models and the early-fusion base models, achieves the best result of the proposed framework
(MED = 0.213, CCC = 0.575, CCC = 0.798). The hybrid result improves on the best late-fusion ensemble by
V A
1.8% in MED, 4.8% in CCC , and 2.6% in CCC , and improves on the best individual base model by 11.4% in
V A
MED, 7.6% in CCC , and 5.8% in CCC . The early-fusion base models alone are weaker than the late-fusion
V A
ensemble (MED in the 0.233–0.242 range), but the hybrid meta-learner extracts complementary signal from both
fusion levels, with weights distributed in roughly equal proportions (47.8% early, 52.2% late for valence; 54.3%
early, 45.7% late for arousal; Table 9 of Sect. 9). The result confirms that the locus of integration matters and that
decision-level and feature-level fusion carry partially non-overlapping information.
Fifth, regarding interpretability (Tables 8 and 9, and the per-feature analysis of Sect. 9.1.1): the framework
exposes its predictive content at two complementary levels of granularity. At the family and paradigm level, the
Ridge meta-learner weights show that LSTM-based models receive the largest aggregate share (61.9% of the
valence prediction and 71.8% of the arousal prediction in the late-fusion All 12 configuration, 66.5%/74.4% in
the hybrid stacking), with XGBoost second at roughly 23% in both fusion levels. The weights also expose a clean
1 3 Neural Computing and Applications (2026) 38:664

### Page 35

https://doi.org/10.1007/s00521-026-12370-y Page 35 of 38 66345
dimension-specific separation: the Librosa family contributes more to valence than to arousal, while OpenSMILE
and PAA contribute proportionally more to arousal, an asymmetry that aligns with the psychoacoustic correlates
of the two emotional dimensions. At the individual-feature level, the permutation-importance analysis concen-
trates the predictive content on timbral and intensity-related descriptors across all three families, with mark-
edly different concentration (the top-10 features cover 89.8% of the total positive importance in PAA, 71.2% in
Librosa, and 30.7% in OpenSMILE). This two-level interpretability, unavailable for the Transformer baselines, is
the distinctive methodological contribution of the framework.
Sixth, regarding the comparison against state-of-the-art audio architectures (Table 10 of Sect. 9): under a uni-
fied probing protocol with frozen encoder, multi-layer weighted-sum aggregation, and an MLP probe head, the
music-domain pre-trained MERT achieves the lowest error of any model evaluated (MED = 0.201, CCC =
V
0.680, CCC = 0.810). The proposed hybrid Ridge stacking remains its closest competitor, within 6.0% in MED
A
while relying on no external data and a fraction of the parameters. The two speech-domain pre-trained Transform-
ers trail the proposed framework (HuBERT at MED = 0.236 and wav2vec 2.0 at MED = 0.239, both above the
hybrid Ridge stacking at 0.213 and the late-fusion ensemble at 0.217), and the Conformer trained from scratch
trails further (MED = 0.246), indicating that transfer from speech and architecture alone are beneficial relative to
most individual base models but not sufficient to match an interpretable hand-crafted-descriptor ensemble. The
pre-training domain is the dominant factor explaining the gap, with the encoder architecture playing a second-
ary role: the gap between MERT and HuBERT (same family of architectures, different domains) is substantially
larger than the gap between HuBERT and wav2vec 2.0 (different architectures, similar domains).
Beyond the empirical findings, this work establishes a methodological reference for affective computing
research. The framework’s modularity (separate stages for feature extraction, base-model training, and ensemble
combination at three fusion levels), its reliance on publicly available libraries and standardised feature extraction
tools, and its validation through paired Wilcoxon signed-rank tests jointly ensure full reproducibility and provide
a consistent baseline for future investigations. A distinctive feature is the interpretability of the meta-learner
weights, which exposes how individual descriptors and paradigms contribute to each emotional dimension and
supports applications where transparent predictions are required, such as music therapy or recommendation
systems.
Several limitations warrant acknowledgement. The DEAM dataset, while widely adopted, comprises primarily
Western music and 45-second excerpts, which may limit generalisation to complete musical works, non-Western
styles, and longer-term emotional arcs. The relatively modest inter-rater reliability (Krippendorff’s alpha around
0.20) reflects the inherent subjectivity of emotion perception, meaning that aggregated annotations represent
collective tendencies rather than ground truth. Finally, the deliberate focus on established methods rather than
state-of-the-art deep architectures prioritises interpretability and reproducibility over absolute performance, leav-
ing room for further accuracy gains through more complex models or domain-adaptive transfer from large pre-
trained audio encoders.
Future research will extend this framework in three main directions. Cross-dataset generalisation is a natural
first step: evaluating the framework on a second continuous valence–arousal corpus such as PMEmo would test
whether the observed contribution patterns and fusion-level hierarchy transfer to different annotation protocols
and musical populations. Domain-adaptive transfer from music-pre-trained encoders such as MERT, possibly
combined with the proposed hybrid framework, may close the residual gap to MERT while preserving interpret-
ability. Finally, multimodal integration of lyrics, metadata, and physiological signals (EDA, EEG, heart rate)
would enable a more complete account of musical affective experience.
In conclusion, this work demonstrates that systematic comparison, methodological rigour, and transparent
evaluation are as valuable as architectural innovation in advancing Music Emotion Recognition research, and
provides an empirically validated baseline that balances accuracy, interpretability, and reproducibility for future
studies.
Acknowledgements See funding section.
Neural Computing and Applications (2026) 38:664 1 3

### Page 36

36664 Page 36 of 38 https://doi.org/10.1007/s00521-026-12370-y
Author contributions Giuseppe Mazzola: Conception, design, implementation, testing, article writing, and review. Cor-
responding author. Valeria Seidita: Conception, design, manuscript review. Marco La Cascia: manuscript review.
Funding Open access funding provided by Università degli Studi di Palermo within the CRUI-CARE Agreement. This
work has been funded by the PNRR Project “MUSIC4D: Music, entrepreneUrshIp, Creativity, For the Digital revolution”,
PRJ-1493.
Data availability The work uses already publicly available datasets and materials. References are appropriately cited in the
paper.
Declarations
Competing interests No competing interests for this work.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The
images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your
intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
1. Juslin PN, Västfjäll D (2008) Emotional responses to music: the need to consider underlying mechanisms. Behav Brain
Sci 31(5):559–575
2. Kang J, Herremans D (2025) Are we there yet? A brief survey of music emotion prediction datasets, models and
outstanding challenges. IEEE Trans Affect Comput. https://doi.org/10.1109/TAFFC.2025.3583505
3. Russell JA (1980) A circumplex model of affect. J Pers Soc Psychol 39(6):1161
4. Aljanaki A, Yang Y-H, Soleymani M (2017) Developing a benchmark for emotional analysis of music. PLoS One
12(3):0173392
5. Zhang K, Zhang H, Li S, Yang C, Sun L (2018) The pmemo dataset for music emotion recognition. In: Proceedings of
the 2018 Acm on international conference on multimedia retrieval, pp. 135–142
6. Koh EY, Cheuk KW, Heung KY, Agres KR, Herremans D (2022) Merp: A music dataset with emotion ratings and raters’
profile information. Sensors 23(1):382
7. Bogdanov D, Lizarraga Seijas X, Alonso-Jiménez P, Serra X (2022) Musav: a dataset of relative arousal-valence
annotations for validation of audio models
8. Gómez-Cañón JS, Gutiérrez-Páez N, Porcaro L, Porter A, Cano E, Herrera-Boyer P, Gkiokas A, Santos P, Hernández-
Leo D, Karreman C et al (2023) Trompa-mer: an open dataset for personalized music emotion recognition. Journal of
Intelligent Information Systems 60(2):549–570
9. Zhang L, Yang X, Zhang Y, Luo J (2023) Dual attention-based multi-scale feature fusion approach for dynamic music
emotion recognition. In: ISMIR, pp. 207–214
10. Hu Q, Murad MAA, Li Q (2025) Advancing music emotion recognition: large-scale dataset construction and evaluator
impact analysis. Multimedia Syst 31(2):1–16
11. Shang Y, Peng Q, Wu Z, Liu Y (2024) Music-induced emotion flow modeling by enmi network. PLoS One 19(10):0297712
12. Liu H, Fang Y, Huang Q (2019) Music emotion recognition using a variant of recurrent neural network. In: 2018
International Conference on Mathematics, Modeling, Simulation and Statistics Application (MMSSA 2018). Atlantis
Press, pp 15–18
13. Orjesek R, Jarina R, Chmulik M (2022) End-to-end music emotion variation detection using iteratively reconstructed
deep features. Multimedia Tools and Applications 81(4):5017–5031
14. Zhang M, Zhu Y, Zhang W, Zhu Y, Feng T (2023) Modularized composite attention network for continuous music
emotion recognition. Multimedia Tools and Applications 82(5):7319–7341
15. Zhang T, Li Q, Yang X, Chen CLP (2025) MCGC-Net: Multi-scale controllable graph convolutional network on music
emotion recognition. IEEE Trans Affect Comput 1–14 (Early access)
16. Juma-Ang CS, Torre NA, Bandalan C (2024) Music emotion recognition using ensemble learning. In: 2024 IEEE
International Conference on Communication, Networks and Satellite (COMNETSAT). IEEE, pp 289–295
1 3 Neural Computing and Applications (2026) 38:664

### Page 37

https://doi.org/10.1007/s00521-026-12370-y Page 37 of 38 66347
17. Cheuk KW, Luo Y-J, Balamurali B, Roig G, Herremans D (2020) Regression-based music emotion prediction using
triplet neural networks. In: 2020 International Joint Conference on Neural Networks (IJCNN). IEEE, pp 1–7
18. Stoller PA, Araya M (2025) A transformer approach for predicting transitions in emotional trajectory directly from music
audio. Neural Comput Appl 1–18
19. Chen Y, Ma Z, Wang M, Liu M (2024) Advancing music emotion recognition: A transformer encoder-based approach.
In: Proceedings of the 6th ACM International Conference on Multimedia in Asia. pp 1–5
20. Gulati A, Qin J, Chiu C-C, Parmar N, Zhang Y, Yu J, Han W, Wang S, Zhang Z, Wu Y, Pang R (2020) Conformer:
Convolution-augmented Transformer for speech recognition. In: Proc. Interspeech 2020, pp. 5036–5040 . h t t p s : / / d o i . o r g
/ 1 0 . 2 1 4 3 7 / I n t e r s p e e c h . 2 0 2 0 - 3 0 1 5
21. Baevski A, Zhou Y, Mohamed A, Auli M (2020) wav2vec 2.0: A framework for self-supervised learning of speech
representations. Adv Neural Inf Process Syst 33:12449–12460
22. Hsu W-N, Bolte B, Tsai Y-HH, Lakhotia K, Salakhutdinov R, Mohamed A (2021) HuBERT: Self-supervised speech
representation learning by masked prediction of hidden units. IEEE/ACM Transactions on Audio Speech and Language
Processing 29:3451–3460. https://doi.org/10.1109/TASLP.2021.3122291
23. Li Y, Yuan R, Zhang G, Ma Y, Chen X, Yin H, Xiao C, Lin C, Ragni A, Benetos E, Gyenge N, Dannenberg R, Liu R, Chen
W, Xia G, Shi Y, Huang W, Wang Z, Guo Y, Fu J (2024) MERT: acoustic music understanding model with large-scale
self-supervised training. In: Proceedings of the international conference on learning representations (ICLR)
24. Sujeesha A, Mala J et al (2024) Automatic music mood classification using multi-modal attention framework. Eng Appl
Artif Intell 128:107355
25. Talaghat MA, Parvinnia E, Mehrabi M, Boostani R (2025) A multimodal deep network for music emotion recognition
using audio chorus and lyrics. IEEE Access. https://doi.org/10.1109/ACCESS.2025.3614020
26. Hao X, Li H, Wen Y (2025) Real-time music emotion recognition based on multimodal fusion. Alex Eng J 116:586–600.
https://doi.org/10.1016/j.aej.2024.12.060
27. Huang R, Li Y, Kang D, Chen Y, Yu C, Wang X (2021) Melody generation with emotion constraint. In: Proceedings of
the 2021 5th international conference on electronic information technology and computer engineering. pp 1598–1603
28. Zhang D, You W, Liu Z, Sun L, Chen P (2025) Personalized dynamic music emotion recognition with dual-scale attention-
based meta-learning. In: Proceedings of the AAAI conference on artificial intelligence, vol 39. pp 1629–1637
29. Aljanaki A, Soleymani M (2018) A data-driven approach to mid-level perceptual musical feature modeling. arXiv
preprint arXiv:1806.04903
30. Chowdhury S, Praher V, Widmer G (2021) Tracing back music emotion predictions to sound sources and intuitive
perceptual qualities. arXiv preprint arXiv:2106.07787
31. Wang H, Sourin A (2023) Deep learning-based visualization of music mood. In: 2023 international conference on
cyberworlds (CW). IEEE, pp 32–39
32. Dharmapriya J, Dayarathne L, Diasena T, Arunathilake S, Kodikara N, Wijesekera P (2021) Music emotion visualization
through colour. In: 2021 International conference on electronics, information, and communication (ICEIC). IEEE, pp
1–6
33. Arora A, Kaul A, Mittal V (2019) In: Mood based music player. 2019 International conference on signal processing and
communication (ICSC). IEEE, pp 333–337
34. Kang J, Herremans D (2025) Towards unified music emotion recognition across dimensional and categorical models.
arXiv preprint arXiv:2502.03979
35. Wang Y, Zhao X, Deng C, Xiao Y, Ruan H, Jin P, Cai X (2025) A survey on music emotion recognition using learning
models. Multimedia Syst 31(4):278. https://doi.org/10.1007/s00530-025-01871-w
36. Dietterich TG (2000) Ensemble methods in machine learning. In: international workshop on multiple classifier systems.
Springer, pp 1–15
37. Eyben F, Wöllmer M, Schuller B (2010) Opensmile: the munich versatile and fast open-source audio feature extractor.
In: Proceedings of the 18th ACM international conference on multimedia, pp 1459–1462
38. Eyben F, Weninger F, Gross F, Schuller B (2013) Recent developments in opensmile, the munich open-source multimedia
feature extractor. In: Proceedings of the 21st ACM international conference on multimedia. pp 835–838
39. GmbH (2025) openSMILE: The munich open-source large-scale multimedia feature extractor. h t t p s : / / g i t h u b . c o m / a u d e e
r i n g / o p e n s m i l e . GitHub repository, version 3.0.0, accessed November 2025
40. Zwicker E, Fastl H (2013) Psychoacoustics: Facts and Models, vol vol 22. Springer, Berlin
41. Di G-Q, Chen X-W, Song K, Zhou B, Pei C-M (2016) Improvement of zwicker’s psychoacoustic annoyance model
aiming at tonal noises. Appl Acoust 105:164–170
42. Green Forge Coop (2024) MOSQITO: a unified and modular framework for sound quality metrics. Zenodo. h t t p s : / / d o i .
o r g / 1 0 . 5 2 8 1 / z e n o d o . 1 1 0 2 6 7 9 6
43. McFee B, Raffel C, Liang D, Ellis DP, McVicar M, Battenberg E, Nieto O (2015) librosa: Audio and music signal
analysis in python. SciPy 2015:18–24
44. Hochreiter S, Schmidhuber J (1997) Long short-term memory. Neural Comput 9(8):1735–1780
Neural Computing and Applications (2026) 38:664 1 3

### Page 38

36864 Page 38 of 38 https://doi.org/10.1007/s00521-026-12370-y
45. Kruse R, Mostaghim S, Borgelt C, Braune C, Steinbrecher M (2022) Multi-layer perceptrons. Computational Intelligence:
a Methodological Introduction. Springer, Cham, p pp 53-124
46. Breiman L (2001) Random forests. Machine learning 45(1):5–32
47. Arik SÖ, Pfister T (2021) Tabnet: attentive interpretable tabular learning. In: Proceedings of the AAAI conference on
artificial intelligence, vol. 35, pp. 6679–6687
48. Wold S, Sjöström M, Eriksson L (2001) Pls-regression: a basic tool of chemometrics. Chemom Intell Lab Syst 58(2):109–
130
49. Chen T, He T, Benesty M, Khotilovich V, Tang Y, Cho H, Chen K, Mitchell R, Cano I, Zhou T et al (2015) Xgboost
extreme gradient boosting. R package version 0.4-2 1(4):1–4
50. Atrey PK, Hossain MA, El Saddik A, Kankanhalli MS (2010) Multimodal fusion for multimedia analysis: a survey.
Multimedia Syst 16(6):345–379. https://doi.org/10.1007/s00530-010-0182-0
51. Zhou Z-H (2025) Ensemble Methods: Foundations and Algorithms. CRC Press, Boca Raton
52. Bejani M, Gharavian D, Charkari NM (2014) Audiovisual emotion recognition using ANOVA feature selection method
and multi-classifier neural networks. Neural Comput Appl 24(2):399–412. https://doi.org/10.1007/s00521-012-1228-3
53. Demšar J (2006) Statistical comparisons of classifiers over multiple data sets. J Mach Learn Res 7:1–30
Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
affiliations.
Authors and Affiliations
Giuseppe Mazzola1 · Valeria Seidita1 · Marco La Cascia1
Giuseppe Mazzola
giuseppe.mazzola@unipa.it
Valeria Seidita
valeria.seidita@unipa.it
Marco La Cascia
marco.lacascia@unipa.it
1 Dipartimento di Ingegneria, Università degli Studi di Palermo, Viale delle Scienze bd. 6, 90128 Palermo, Italy
1 3 Neural Computing and Applications (2026) 38:664
