---
来源文件 / Source PDF: `emosical-2024-findings-emnlp.pdf`
提取日期 / Extracted: 2026-10-30
提取方式 / Method: pdfplumber 文本层直接提取（非 OCR）
PDF 页数 / Pages: 12
总字符数 / Characters: 44237
---
## 引用信息 / Citation (APA 7th)

> Kim, H., Choi, A., Lee, S., Jung, H., & Lee, K. (2024). Emosical: An emotion-annotated musical theatre dataset. In *Findings of the Association for Computational Linguistics: EMNLP 2024* (pp. 4169–4180). Association for Computational Linguistics.


## 正文（按页提取 / Extracted page by page）

### Page 1

Emosical: An Emotion-Annotated Musical Theatre Dataset
HayoonKim1 AhyeonChoi1 SunghoLee1 HyunjinJung1 KyoguLee1,2,3
1MusicandAudioResearchGroup,SeoulNationalUniversity
2InterdisciplinaryPrograminArtificialIntelligence,SeoulNationalUniversity
3ArtificialIntelligenceInstitute,SeoulNationalUniversity
{hyway, chah0623, sh-lee, 3388jung, kglee}@snu.ac.kr
Abstract While those techniques have advanced the un-
derstanding of human emotions in different do-
This paper presents Emosical, a multi-
mains, emotion recognition still remains a chal-
modal open-source dataset of musical films.
lenge. First,itishardtocaptureground-truthemo-
Emosicalcomprisesvideo, vocalaudio, text,
tion,whichisexpressedthroughbothlinguisticand
andcharacteridentitypairedsampleswithan-
notatedemotiontags. Emosicalprovidesrich non-linguisticelements. Thiscomplexityrequires
emotionannotationsforeachsamplebyinfer- multi-modal data to capture the emotional con-
ringthebackgroundstoryofthecharacters. To textfully,butintegratingandsynchronizingsuch
achieve this, we leverage the musical theatre diverseinputspresentstechnicaldifficulties(Bal-
script,whichcontainsthecharacters’complete trušaitisetal.,2018). Althoughsomemodelsare
backgroundstoriesandnarrativecontexts. The
trainedusingrecordedmulti-modaldatasets(Busso
annotationpipelineincludesfeedingthespeak-
et al., 2008), creating these datasets is resource-
ingcharacter,text,globalpersona,andcontext
intensive and lacks the scalability and diversity
ofthedialogueandsongtrackintoalargelan-
guagemodel. Toverifytheeffectivenessofour needed to fully capture the complexity of human
taggingscheme,weperformanablationstudy emotions.
by bypassing each step of the pipeline. The Additionally,humanemotionsarecomplexand
ablation results show the usefulness of each subtle, with the inherent ambiguity of expressed
componentingeneratingaccurateemotiontags.
emotional cues and variations in cultural expres-
Asubjectivetestisconductedtocomparethe
sions(Russell,2003). Thus,existingmodelsstrug-
generatedtagsofeachablationresult. Wealso
gletorecognizeemotionsfromexpressedfeatures
perform a statistical analysis to find out the
atafine-grainedlevel,mostlyclusteringemotions
globalcharacteristicsofthecollectedemotion
tags. Emosicalwouldenableexpressivesyn- intocoarsecategories(VerveridisandKotropoulos,
thesis and tagging of the speech and singing 2006). Wesuspectthatknowledgeoftheunderly-
voiceinthemusicaltheatredomaininfuture ingpersonalityorsituationmakesiteasiertoinfer
research. Emosical is publicly available at one’semotionmoreaccuratelyandfinely,whichis
https://github.com/gillosae/emosical.
acapabilitymissinginmostdatasets.
Weproposethattheatreisaparticularlyeffective
1 Introduction
mediumforaddressingthesechallenges. Theatre
Asafundamentalaspectofhumanexperience,rec- naturallyencompassesmulti-modalemotionalex-
ognizingemotionrequiresadepthofunderstanding pressions since actors and directors use various
in the multi-domains. With the advances in deep techniquessuchasdialogue,music,lighting,and
learningtechniques,variousapproachesdelveinto stagedesigntocommunicateawiderangeofemo-
detectingemotionthroughexpressedemotionfrom tionstotheaudience(Artaud,1938). Theseemo-
different modalities (Poria et al., 2017). Studies tionsaretypicallyexpressedwithanemphasisfor
aimtodetectemotionthroughthedomainoftext greaterimpact(Stanislavski,1948),makingiteas-
(Pang et al., 2008; Socher et al., 2013), speech iertocaptureandanalyzethemeffectively. Also,
(Satt et al., 2017; Akçay and Og˘uz, 2020), and thetheatrehastheuniquepropertyofcontaininga
facial expressions (Zafeiriou et al., 2015; Li and ‘script’fortheplay,whichenablestheinferenceof
Deng,2020). Furthermore,approachestointegrate eachcharacter’sstorylineandpersonality. Inthis
multiplemodalities(Zadehetal.,2017;Lianetal., view,theatrecontainsadiverserangeofexpressed
2023)havebeenintroduced. emotions conveyed through multiple modalities
4169
FindingsoftheAssociationforComputationalLinguistics:EMNLP2024,pages4169–4180
November12-16,2024©2024AssociationforComputationalLinguistics

### Page 2

Figure1: Emotioninferringprocessof‘HealingIncantation’in‘Tangled.’
thataredeeplyrootedineachcharacter’snarrative our tagging pipeline tags corresponding singing
context,makingitasuitablemediumforemotion emotionswellbyinferringemotionsfromthecon-
research. textandcharacter’spersona. Throughourpipeline,
In response, we build Emosical, an emotion- even though the song consists of the same lyrics,
annotated theatre dataset. Specifically, we select theresultingtagsaredifferentduetodifferentscene
musical theatre for our dataset in order to con- contextsfedtoobtainthetags.
tain singing samples. There is no theatre dataset This pipeline has another advantage that it ap-
specificallycuratedformachinelearningpurposes. plies to building some types of emotion-paired
It might be due to theatre’s inherent complexity, datasets,whicharehardtodevelop. Forinstance,
which combines spoken natural language, audio, thereisnopublicsingingdataannotatedwithemo-
andvisualelements,makingithardtocreatecom- tionsasidefromLivingstoneandRusso(2018). Un-
plex recordings manually. Therefore, we design likespeech,singingdemandsattentiontonuances
anannotationpipelinethatinfersemotionfromthe likepitch,tone,andemotionaldelivery(Sundberg,
narrativebyleveragingthescriptfromeachtheatre. 1987). Eventhoughsingingisapowerfulmedium
Ourannotationpipelineaimstoanalyzeandan- that conveys expressive emotional expression, it
notatethenarrative’semotionsasautomaticallyas ishardtorecordasingingvoicesamplewithspe-
possible. Thus,wecrawlmusicaltheatrefilmsand cific emotions manually. However, our approach
apply them as pipeline input. We require theatre enables emotional inference on any kind of data,
filmvideowiththetimestampandspeakeridentity including singing - under the condition that the
alignedSRTfileastheinputs. Inthepipeline, we identity’sbackgroundcontextisgiven.
feed the character, text, global persona, and con- Through text, video, and vocal-aligned sam-
textofthedialogueandsongtrackintoanLLMto ples with rich emotion annotations, we aim for
obtainthecorrespondingemotiontagpersample. Emosical to be primarily used to understand the
Ourannotationpipelinecapturesemotioneffec- relationship between theatre’s multi-modal char-
tively by capturing the narrative context through acteristics and emotions. Additionally, we hope
fed inputs. In musical theatre, some prominent the dataset could also be used for tasks such as
songs tend to be reprised and presented multiple emotiontaggingandemotionalsynthesisforeach
timesthroughouttheact,conveyingdifferentemo- modality; a baseline system for the former is de-
tional nuances. Figure 1 shows an example; the velopedandevaluatedasanexample. Tothisend,
number ‘Healing Incantation’ of ‘Tangled’ is the Emosicalprovidesdetailedandfine-grainedemo-
case, which emerges once at an introductory mo- tion annotation for every short segment. Unlike
ment, once at a highly-elated scene, and lastly at emotion-annotateddatasets(McKeownetal.,2012;
theendingpartofthemovie. Inthefigure,thethree Nojavanasgharietal.,2016),whichtendtoanno-
reprisedsongshavedistinctlydifferentemotions, tateemotionsinbroadgroupsoverlongsegments,
clearly indicating diverse emotional expressions. our dataset with dense emotion tags annotated to
‘HealingIncantation’isreprisedtripletimesinthe short data samples allows for more precise and
movie. Eventhoughtheyallhavethesamelyrics temporalstudiesofemotionalchanges.
4170

### Page 3

Modality Annotation DatasetSize
Dataset Text Speech Singing Video Identity Emotion #Movies #Samples #Speakers #Tags
ESD(Zhouetal.,2022) ✓ ✓ ✓ - 350 20 5
EmoDB(Burkhardtetal.,2005b) ✓ ✓ ✓ ✓ - 535 10 7
RAVDESS(LivingstoneandRusso,2018) ✓ ✓ ✓ ✓ ✓ ✓ - 2452 24 8
IEMOCAP(Bussoetal.,2008) ✓ ✓ ✓ ✓ - 10039 10 9
CMU-MOSEI(Zadehetal.,2018) ✓ ✓ ✓ ✓ ✓ - 23453 1000
MELD(Poriaetal.,2019) ✓ ✓ ✓ ✓ ✓ - 13000 260 7
SEMAINE(McKeownetal.,2012) ✓ ✓ ✓ ✓ ✓ 80 4 5
OMG-Emotion(Barrosetal.,2018) ✓ ✓ ✓ ✓ ✓ 7371 7
EmotiW(Dhalletal.,2023) ✓ ✓ ✓ ✓ 1809 7
VocalSet(Wilkinsetal.,2018) ✓ ✓ - 3560 20 -
OpenSinger(Huangetal.,2021) ✓ ✓ - 43075 93 -
M4Singer(Zhangetal.,2022) ✓ ✓ - 20942 20 -
MPII-MD(Rohrbachetal.,2015a) ✓ ✓ 94 68337 - -
MovieQA(Tapaswietal.,2016) ✓ ✓ 140 6771 - -
V2C-Animation(Chenetal.,2022) ✓ ✓ ✓ ✓ ✓ 26 10217 153 8
Cognimuse(Zlatintsietal.,2017) ✓ ✓ ✓ ✓ ✓ 13 11109 -
Emosical(ours) ✓ ✓ ✓ ✓ ✓ ✓ 20 27294 261 128
Table1: Comparisonofvariousopen-sourcedatasetswithEmosical.
Wesummarizeourcontributionsasfollows: fromtheTVseriesannotatedwithemotionlabels,
including synchronized video, audio, and textual
• We present Emosical, the first open-source data, appropriate for emotion recognition in con-
musicalfilmdatasetwithemotionannotations. versationalcontexts.
• Ourdatasetcontainssingingvoicesampleswith
TheSEMAINEdatabase(McKeownetal.,2012)
identity and emotion annotation, which most
containsaudiovisualrecordingsofinteractionsbe-
existingsingingvoicedatasetlacks.
tweenhumansandanavatardesignedtoelicitemo-
• Webuildanautomaticemotiontaggingpipeline tionalresponses,includinghigh-qualityaudioand
thatutilizesthemusicalfilmscripttoinfer the video data with continuous annotations for emo-
backgroundstoryofthesinger. tiondimensionssuchasarousalandvalence. The
RÉCitalCorpusforMultimodalEmotionAnalysis
• Weprovideabaselinetaggingmodeltrainedon
(RECOLA)dataset(Ringevaletal.,2013)includes
ourdataset,whichpredictsemotionlabelsfrom
audio,video,andphysiologicaldatarecordedfrom
thespeechandsingingvoicesignals.
participantsduringteamworkingtasks,annotated
for continuous emotion dimensions, making it a
2 RelatedWorks
comprehensiveresourceforstudyingdynamicemo-
Table1summarizesseveralkeycharacteristicsof tional expressions. The OMG-Emotion dataset
therelateddatasetsandcomparesthemwithours. (Barrosetal.,2018)containsvideorecordingsof
people reacting to predefined stimuli, with anno-
MultimodalEmotionRecognitionDatasets. A
tations for continuous emotion dimensions, pro-
multitudeofdatasetshavebeendevelopedformul-
viding continuous perspectives on emotional re-
timodalemotionrecognitionbyintegratingvarious
sponses.
modalities such as video, audio, and text. The
IEMOCAP(InteractiveEmotionalDyadicMotion TheAudio-VisualEmotionChallenge(AVEC)
Capture)dataset(Bussoetal.,2008)includesaudio- (Ringeval et al., 2019) provides datasets, includ-
visualdatafromactorsperformingscriptedandim- ingsynchronizedvideoandaudiorecordingsanno-
provisedscenariosdesignedtoelicitspecificemo- tatedwithemotionalstates. TheEmotionRecogni-
tions. Similarly, the CMU Multimodal Opinion tionintheWild(EmotiW)challenge(Dhalletal.,
SentimentandEmotionIntensity(CMU-MOSEI) 2023)similarlyfeaturesdatasetscapturingsponta-
dataset(BagherZadehetal.,2018)offersemotion- neousexpressionsofemotionsinreal-worldenvi-
annotated video segments from YouTube videos. ronments,includingvideo,audio,andtextualdata,
The Multimodal EmotionLines Dataset (MELD) suitable for developing emotion recognition sys-
(Poriaetal.,2019)consistsofdialoguesequences temsthatworkinnaturalisticsettings.
4171

### Page 4

Speech Emotion Recognition Datasets. The Statistics Count
EmotionalSpeechDatabase(EmoDB)(Burkhardt
Total#offilms 20
et al., 2005a) includes recordings of professional
Total#ofvideo/audiosegments 27294
actors who simulated seven different emotions. Theaveragelengthofsegments 2.66s
TheRyersonAudio-VisualDatabaseofEmotional Total#ofdistinctspeakers 479
Speech and Song (RAVDESS) (Livingstone and Total#ofspeechsamples 21040
Total#ofsingingsamples 6254
Russo,2018)containsactorsvocalizingtwolexi-
cally matched statements. Each expression is la- Total#ofwordsinscripts 162277
Total#ofuniquewordsinscripts 15610
beled for one of eight emotional states, offering
Total#ofemotiontags 128
a rich dataset for both speech and song emotion
recognition. The Speech Emotion Recognition Table2: SummaryofEmosicaldatasetstatistics.
(ESD)dataset(Zhouetal.,2022)isamultilingual
.
dataset containing emotional speech data, which
data/
providesadiversesetofemotionalspeechsamples
raw/
forcross-lingualemotionrecognitionstudies. theatre/
frozen.mov
...
Film Datasets. Film-specific datasets offer ex-
srt/
tensiveresourcesforanalyzingthecomplexinter- frozen.srt
play of visual, auditory, and narrative elements ...
audio/
in movies. The V2C-Animation dataset (Chen
frozen/
et al., 2021) focuses on animated videos and in- 1.wav
cludes video clips with corresponding textual de- ...
...
scriptions. The MPII Movie Description Dataset
video/
(Rohrbach et al., 2015b) is a large-scale collec- text/
tionofmovieclipsannotatedwithnaturallanguage metadata/
number_info.csv
descriptions. MovieQA (Tapaswi et al., 2016) is
global_persona/
a dataset designed to test story comprehension frozen.yaml
...
throughquestion-answeringtasksbasedonmovie
scene_summarization/
plots,integratingvisual,textual,andauditoryinfor-
frozen.yaml
mation to evaluate narrative understanding. Cog- ...
nimuse(Zlatintsietal.,2017)isacomprehensive
Figure2: StructureofEmosical.
datasetthatincludesmultimodalannotations(au-
dio,visual,andtextual)ofHollywoodmovies,with
detailedannotationsforsceneboundaries,charac- Weprovidesubtitlefiles(inSRTextension;through-
terinteractions,andemotion. outthepaper,wewilldenotethemasSRTfiles)that
contain characters and text aligned to the movie.
3 Dataset
TheseSRTfilesaredifferentfromthepubliclyavail-
ableonesandhavemoreprecisetimestamps. We
Overview. Table2showstheoverallstatisticsof
Emosical. It comprises 27294 samples, totaling alsoprovidemetadatathatcontainsemotionandvo-
caltypepersample,aswellasnoisyaudiorecord-
20hours,from20distinctmusicalfilms,including
ings,whichwillbecleanedwithanenhancement
animation musicals, musical movies, and theatre
model. To use the dataset, users will first place
recordings. Each sample is a tuple of {vocal au-
movievideofilesinthedata/raw/theatredirec-
dio,video,text,character}accompaniedbyanno-
toryandplacethemalongwithcorrespondingsub-
tated emotion tags. Vocal audio samples include
title files in the data/raw/srt directory. Then,
21040speechand6254singingsamples. Theover-
userscanruntheprovidedcode,whichtransforms
all structure of the dataset is shown in Figure 2.
thedatasetintothecompiledformwithadditional
Thedatasetcollectionandtheannotationprocess
directories,includingdata/audio/,data/video,
areshowninFigure3.
and data/text. We also provide metadata that
DatasetStructure. Giventhatthemoviesarenot shows which clip corresponds to which scene so
freelyavailable,weofferautomatedscriptstopro- userscanaccessindividualvideo/audioclipsfrom
cessthedataandlinksfordownloadingeachfilm. specificscenesofeachmovie.
4172

### Page 5

Figure3: DatasetcollectionpipelineofEmosical.
3.1 DatasetCreation theffmpegtoolkit(Tomar,2006).
Weaimtodevelopadatasetsuitableformultimodal VocalIsolationandEnhancement. Considering
emotionanalysisofmusicaltheatre. Additionally, thepotentialaudioapplicationssuchasvoicesyn-
weaimforourdatasettobeapplicableformultiple thesisandtaggingtasks,itisdesirabletohaveclean
purposes, including voice synthesis and tagging voicesignalswithoutanybackgroundnoise. There-
tasksutilizingouraudiodataset. Tosuitthesepur- fore,beforesegmentingtheaudio,weseparateall
poses,weconstructadatagenerationpipelinethat thevoicesignalsfromtheremainingusingtheopen-
is especially focused on audio processing. The sourceDemucsmodel(Rouardetal.,2023). After
pipelinecanbeautomaticallyrunwhenrawvideo thesegmentation,weperformthefollowingtwoex-
files,preparedSRTfiles,andmetadataaregiven. trasteps. First,wemanuallycheckfornoisyaudio
files. Fornoisyaudio,wefurtherremovetheback-
Timestamp Correction. Our dataset leverages
groundnoisebyemployingthebackgroundnoise
thepubliclyavailableoriginalSRTfiles. SRTfiles
reduction model, SGMSE (Richter et al., 2023).
containthesequentialnumberofcurrentutterances,
Second, we filter out audio clips that do not sat-
startingandendingpointsinthevideotimeline,and
isfythefollowingrequirements: (i)nooverlapping
correspondingtext. However,astheyareforsub-
speech and singing voices, (ii) no residual noise,
titles,theirtimestampsarenotsufficientlyprecise
and(iii)negligibleprocessingartifacts. Wemanu-
forourpurposes,e.g.,splittingthevideoandaudio
allyexcludethesesegmentssinceweaimtocurate
withtimestamps. Therefore,weneedtoprecisely
anautomaticallyprocessabledataset.
tunethetimestampandtextofeachSRTsegment
to contain the starting and ending point of each Speaker Identification. After collecting video
utteranceproperly. Toachievethis,wefirstutilized clips,audiosegments,andtheircorrespondingtext,
a transcription alignment tool Gentle (Hawkins eachisannotatedwiththecorrespondingspeaker’s
etal.,2024)tocreatetheroughtimestamps. Then, identity and matched against the SRT file. This
wemanuallypost-processedthosetoensureaccu- is useful not only as an additional feature of the
racyandtoseteachsample’slengthtobewithin10 datasetbutalsofortheemotionannotationpipeline;
seconds. TheprovidedSRTfilesarepost-processed ithelpslargelanguagemodels(LLMs)effectively
ones. distinguisheachcharacterandrecognizetheemo-
tionalnuancesconveyedthroughthestoryline;re-
Video/AudioSegmentation. Foreachvideo,we fertoSection3.2forthedetails. Toidentifyspeak-
utilizetheMoviePylibrary(Zulkoetal.,2024)to ers,wefirstselectrepresentativeaudiosamplesfor
parsesamplesaccordingtothestartingandending each main character. Then, we use a pre-trained
timestampsinitscorrespondingSRTfile. Wealso speakerdiarizationmodelandassignaspeakerwith
extract the corresponding audio data and convert the highest similarity to each speech/singing seg-
thestereoaudiointomonobysummingtheleftand ment. Note that our audio samples include both
right channels. These processings are done with speechandsingingfromthesamespeakers. This
4173

### Page 6

is called a cross-genre setup, which is known to
bechallenging,especiallywhensingingvoicesare
involved (Li et al., 2022). We used WeSpeaker
(Wangetal.,2023),theonlypubliclyavailablepre-
trainedcross-genremodel. However,itshouldbe
notedthatthemodelwastrainedonadatasetinthe
Chineselanguage(Lietal.,2022),potentiallylead-
ingtoinaccurateestimationsfortheEnglishfilms.
Therefore, to ensure the accuracy of the speaker
annotation,wemanuallycheckedeachannotation
andfixeditifnecessary. Throughthisdatacollec-
tionpipeline,wefinallygatheratripletof{vocal,
text,speaker}foraudiodata. Inthemetadata,each
voice segment is annotated with binary data that
distinguishessingingvoicesegmentsfromspeech.
3.2 EmotionAnnotation
Figure4: 128emotionwheelswith7primary,40sec-
Aswecollectedthe{video,audio(vocal),charac-
ondary,and81tertiaryemotions.
ter,text}datathroughtheaforementionedpipeline,
we now aim to annotate the emotion for each
sample. Toachievethis,wefocusonthestoryline As a result, it aids LLM in successfully guessing
of the theatre to further infer the emotion of the thecharacter’semotionalstatewhensayingspecific
character line by line. Note that this approach is textorsingingspecificlyrics.
similartoBhattacharyaetal.(2023),whichgener-
TheEmotionWheel. Mostemotion-annotated
atedstorydescriptionstohandledownstreamtasks.
datasets categorize emotions into 4 to 8 groups
We leverage full text from the SRT file and feed
(Zhou et al., 2022; Burkhardt et al., 2005a; Liv-
it to a LLM. Specifically, the annotation process
ingstone and Russo, 2018). However, it is desir-
integratesfourkeycomponentsforeachcharacter:
abletouseamoresophisticatedtaxonomyofemo-
(i) global persona, (ii) scene summarization, (iii)
tion labels to capture the nuanced emotions con-
visualdescription,and(iv)thetextofeachsample.
veyed in the musical film. This motivates us to
GlobalPersona. Foreachcharacter,wedefinea leverage the emotion wheel. The Plutchik emo-
globalpersonathatencapsulatestheiroverarching tion wheel (Plutchik and Kellerman, 2013) is de-
traits and narrative role. We obtain the global veloped to categorize human emotions based on
personabyfeedingthewholescriptintothelarge theideathatdistinctemotionscanbemixedtocre-
language model and prompting it to summarize ateotheremotions. Weusetheexpandedversion
the character’s overall storyline and personality. of Plutchik’s original emotion wheel. The “128
As the latter ablation study shows, this is crucial EmotionWheel”isgraduallystructuredwithpri-
for understanding the emotional context of their mary,secondary,andtertiaryemotionstoprovidea
actionsandexpressionsthroughoutthemovie. moregranularunderstandingofhumanemotional
experiences(Roberts,2024). These128emotions
SceneSeparationandSummarization. Wesep-
aresub-classesoftheprimary7emotions(‘angry,’
arate the entire text into multiple scenes to effec-
‘disgusted,’ ‘sad,’ ‘happy,’ ‘surprised,’ ‘bad,’ and
tively summarize the context of each section of
‘fearful’), making each label suitable for primary
the film. Then, we feed the aggregated text of
emotionclustering,enablingeasycomparisonwith
thesceneintoLLMtoobtainasummarizedstory.
other datasets. Also, diverse tags can enrich the
Summarizingthescenehelpsinferthecharacters’
inputlanguagewhentrainingthemodelforprompt-
emotional state when they commence certain ut-
ingpurposes.
terances, thereby guiding the LLM in generating
accurateemotiontagsafterward. Overall,feeding LLMPromptingwithDSPy. Withthecharac-
global persona and context summarization helps ter’sglobalpersona,scenesummarization,sample
LLMfollowthestorylineandunderstandthechar- description, and text with the character ready at
acter’spersonalitythroughoutthemusicaltheatre. hand, we feed them with prompts into the LLM
4174

### Page 7

(Chat-GPT3.5Turbo(Brownetal.,2020))togener- AUC Precision Recall F-score
ateemotionannotationsforeachlineofthedataset. Ours 0.690 0.739 0.690 0.710
Speech-based 0.173 0.355 0.173 0.184
WeutilizeDSPy(Khattabetal.,2023),aframe-
Text-based 0.286 0.635 0.286 0.338
worktooptimizeLLMpromptsandweightswith
smalltrainingdata. IntheDSPyframework,wede- Table3: Emotion-taggingpipelinevs. othermodels.
finetheSignature,whichoutlineswhatinformation
weprovidetotheLLM.OurSignatureisdefinedas
Base Fine-tuned
{character, text, visualdescription, scenecontext,
Train Test Train Test
global persona} to include all necessary details
BootstrapFewShot 43.86 58.82 31.58 82.35
on a full picture of the scene and characters. We
+RandomSearch(ours) 43.86 58.82 45.61 85.29
manuallycreated50trainingsamplesconsistingof
Signatureelementsandtheground-truthemotion Table4: BaselineLLMvs. Fine-tunedLLM.
tagwithitsrationale.
Then, we proceed to fine-tune our LLM. The
fine-tuningprocessinvolvesthechain-of-thought 4 EvaluationandAnalysis
(CoT)(Weietal.,2022)method. Specifically,our
4.1 EmotionTaggingPipeline
CoTuses3DSPymodules. Thefirstmoduleasks
We evaluate the effectiveness of our emotion-
LLMtogeneratearationaleaboutthesituationthat
taggingpipelineversusotherbaselinemodels. For
thespeakerencounteredbasedontheinputSigna-
comparisonwithotheremotion-taggingbaselines,
ture. ThisguidestheLLMinfollowingaconcrete
wechangeourpipelinetoclassifyeachsampleinto
reasoningprocess. Next,thesecondmodulemakes
seven emotions (anger, disgust, fear, joy, neutral,
LLMclassifytheemotionbasedontheformerout-
sadness,surprise). Theevaluationisperformedon
put rationale, which leads to more accurate and
ahuman-annotateddatasetwecreatedfromashort
contextuallyrelevanttags.
musicaltheatrefilm. Weperformevaluationonthe
However,ourLLMsometimespredictsanemo-
handcrafteddatasetbecauseourpipelinerequires
tiontagoutsidethe128emotionwheelduetothe
global persona and context input, which is only
unconstrainednatureoftheLLM.Tomitigatethis,
availablefromthefulltheatrescript. Wecompare
we apply DSPy Assertion (Singhvi et al., 2024),
ourpipelinewithpubliclyavailablespeech-based
which poses constraints to guide the LLM’s out-
(Hartmann,2022)andtext-based(R-F,2022)pre-
put. Iftheemotiontagdoesn’tmeettheassertions,
trainedmodelsinTable3.
DSPy.Suggest triggers the backtracking process.
ThisLLMre-evaluatestheinputcontexttogener- 4.2 LLMFinetuning
ate a new emotion tag. However, when the back-
Intheemotion-taggingpipeline,wefine-tuneLLM
trackingexceedsthepre-definedmaximumnumber,
(GPT-turbo 3.5), leveraging DSPy with human-
thethirdmoduleisintroduced,promptingtheLLM
annotated training data consisting of 50 training
to classify the emotion into seven primary emo-
and200testsamples. Thefinalpipelineleverages
tions. Lastly, we prompt the LLM to classify the
chain-of-thoughtandBootstrapFewshotWithRan-
emotionfromthesub-emotionsoftheprimaryemo-
domSearch as a teleprompter. Fine-tuned LLM
tion. This fine-tuned LLM significantly exceeds
leveraging our pipeline significantly exceeds the
theaccuracyoftheuntrainedbaselineLLM.
baselineLLM,asshowninTable4.
4.3 AblationStudy
3.3 DataSplit
Tovalidatetheusefulnessofeachcomponentfed
Weprovideadditionalmetadataforthedatasetsplit to an LLM in the pipeline, we conduct an abla-
fordevelopmentandtestpurposes. Wesplitthe20 tionstudybybypassingeachcomponent. Ourpro-
filmsinto16and4;thelatterisusedonlyfortests. posed model feeds global persona, previous con-
The16moviesarefurthersplit,whererandom80% text, singer, and lyrics to LLM to bring out the
ofeachmovieisusedforthedevelopmentwhilethe final emotion tag. We bypass each step to com-
remainingareusedforthetest. Thissplitallowsus paretheusefulness. Ablationsareoffourgroups:
toevaluatethemodelsbothinseen(in-distribution) Ablation1(Text),Ablation2(Text+Character),Ab-
andunseen(possiblyout-of-distribution)film. lation3(Text+Character+SceneSummarization),
4175

### Page 8

Lyrics Ablation1 Ablation2 Ablation3 Proposed
Anna: For the first time in forever hopeful hopeful excited hopeful
Anna: I could be noticed by someone vulnerable fearful hopeful hopeful
Anna: And I know it is totally crazy excited nervous excited playful
Anna: To dream I’d find romance hopeful optimistic excited excited
Anna: But for the first time in forever fearful fearful optimistic hopeful
Anna: At least I’ve got a chance pressured pressured hopeful optimistic
Elsa: Don’t let them in, don’t let them see fearful anxious fearful anxious
Elsa: Be the good girl you always have to be overwhelmed frustrated pressured pressured
Elsa: Conceal, don’t feel, put on a show numb anxious fearful pressured
Elsa: Make one wrong move, and everyone will know anxious anxious anxious fearful
Ablation1:Textonly. Ablation2:Text+Character. Ablation3:Text+Character+SceneSummarization.
Proposed:Text+Character+SceneSummarization+GlobalPersona.
Table5: AblationresultsofmusicalfilmFrozen.
Ablation1 Ablation2 Ablation3 Proposed
2.72 0.07 3.01 0.08 3.33 0.08 3.60 0.07
± ± ± ±
Figure5: Thedistributionofprimaryemotionlabels.
Table6: Meanopinionscores(MOS)oftagsfromthe
taggingmodelswith95%confidenceintervals.
andProposed(Text+Character+SceneSumma-
rization+GlobalPersona).
Table5showstheablationresultsofthemusical
film‘Frozen.’ Fromaqualitativeanalysisperspec-
tive, in Ablation 1, when only text is fed to the
LLM, the model judges emotion solely based on
lyrics. InAblation2,thespeakerisalsofedwith Figure6: WordcloudofemotiontagsinEmosical.
text. Hence, LLM can distinguish two different
singers,distinguishingthecontrastedemotionsof
the two singers. In Ablation 3 and the proposed is‘sleepy,’Figure6showsthewordcloudof128
method, in which both previous contexts are fed, emotiontags.
LLMunderstandsthecontextofthesinging, one
character singing in joy while another faces the 4.5 TaggingModel
pressuredsituation.
We conduct vocal emotion tagging experiments
We conduct subjective tests to evaluate the fit- using the Emosical dataset. We designed a sim-
ness of generated tags per each ablation and pro-
plebaselinemodelforclassifyingbothspeechand
posedtaggingpipeline. Werandomlyselectedsam-
singingvoicesinto7primaryemotions. Themodel
ples from the dataset and tested 50 data samples
isaconvolutionalneuralnetwork(CNN)architec-
withtext,character,andgeneratedemotiontags,25
ture, starting with a convolutional layer with 32
sampleseachforspeechandsinging. Thetestwas
filters,followedbybatchnormalizationandReLU
conductedon27subjects. Theresultsofthefour
activation. It includes three sequential residual
groupsareshowninTable6. AsshowninTable6,
blocks, each doubling the number of filters (64,
theproposedtaggingpipelineshowsbettertagging
128,and256)andincorporatingbatchnormaliza-
resultsthanbypassedpipelinesinablations.
tion and shortcut connections. Adaptive average
pooling reduces the feature map to a fixed size,
4.4 DatasetAnalysis
followedbydropoutforregularization. Thefully
Figure5showsthedistributionsofthefrequency connectedlayersreducethefeaturesto128dimen-
ofthetags. Inclusteredtagsofprimaryemotions, sionsandfinallytothe7emotionclasses,withthe
the top tag with the highest frequency is ‘hope- outputusinglogsoftmaxactivation. Themodelis
ful,’followedby‘curious,’whichisasubsetofthe trainedwiththecross-entropylossfunctionandop-
primary emotion ‘happy.’. The least frequent tag timizedusingtheAdamWoptimizer(Loshchilov,
4176

### Page 9

AUC F-score Precision Recall • DiversityofSourceMaterial. Thedatasetis
Singing 0.598 0.219 0.146 0.178 currentlylimitedto20distinctmusicalfilms,
Speech 0.573 0.153 0.225 0.221 which may not fully capture the wide range
Both 0.611 0.129 0.120 0.167
of emotional expressions and styles present
across different musical theatre productions.
Table 7: Voice emotion tagging results with different
So,weplantoexpandthedatasettoinclude
datasetconfigurations.
morefilms,aswellasmusicalrecordingsfrom
livetheatreperformancestoenhancethegen-
eralizabilityofmodelstrainedonthisdata.
2017)withaOneCycleLRlearningratescheduler
(SmithandTopin,2019). Theperformanceofthe • ManualInterventionDuringDataProcessing.
baselinetaggingmodelisreportedinTable7. Whileweautomatedmuchofthedataprocess-
ingpipeline, certainsteps, suchasverifying
5 Conclusion SRTtimestampaccuracyandcheckingspeaker
diarization results, still require human inter-
We presented a novel dataset, Emosical, the first
vention. Furtherrefinementandautomationof
open-source multimodal dataset specifically cu-
theseprocesseswouldimprovetheefficiency
rated for musical films with comprehensive emo-
andscalabilityofdatasetcreation.
tionannotations. Byintegratingvideo,audio,text,
• EmotionTaggingGranularity. Althoughwe
and character identity with emotion tags derived
employanextensivesetof128emotiontags
from a detailed narrative context, Emosical pro-
based on the emotion wheel, this granular-
vides a rich resource for advancing research in
ity can lead to challenges in ensuring con-
emotionrecognition,synthesis,andtagginginthe
sistent and accurate tagging across samples.
musicaltheatredomain.
Insomecases,thesubtletiesbetweenclosely
Our dataset leveraged a novel annotation
related emotions might be difficult to distin-
pipeline,incorporatingglobalpersona,scenecon-
guish,leadingtopotentialambiguities.
text, visual description, and dialogue or lyrics to
generate nuanced emotion tags using a large lan- • DependencytoLLMs. Ouremotiontagging
guagemodel(LLM).Throughstatisticalanalysis relies on LLMs’ capabilities. While these
andaseriesofablationstudies,wedemonstrated models offer sophisticated natural language
theeffectivenessofourtaggingscheme. Oursub- understanding,theyarenotinfallibleandcan
jectiveevaluationsfurthervalidatedtheprecision sometimesgenerateinaccurateorinconsistent
andreliabilityofourannotations. tags, especially when faced with highly nu-
Additionally, we proposed a baseline tagging ancedemotionalexpressions.
model for emotion recognition in singing voices, • Bias and Representation. The selected mu-
settingafoundationforfutureresearchinthisarea. sicalfilmsmayreflectcertainculturalbiases
Emosicalopensupnewavenuesforexploringthe
andpredominantlyrepresentWesternmusical
interplaybetweenvariousmodalitiesinconveying theatretraditions. Thislimitstheapplicability
emotionsandcanserveasavaluableresourcefor ofthedatasetforstudyingemotionsinamore
developingmoreemotionallyresonantsystems. globalandculturallydiversecontext. Future
Futureworkmayincludeexpandingthedataset effortsshouldincludeamorediverserangeof
toencompassmorediversegenresandlanguages, filmsfromvariousculturesandlanguages.
refiningtheemotiontaggingpipeline,andexplor-
• TemporalContextandDynamics. Whilethe
ing its applications in various multimodal emo-
dataset includes scene summarization and
tion recognition and synthesis tasks. We believe
globalpersonainformation,capturingthefull
Emosicalcancontributetofurtherresearchinmul-
temporaldynamicsandevolutionofemotions
timodal understanding of emotion expressions in
overlongerperiodswithinthefilmsremains
musicaltheatre.
achallenge. Futureworkcouldfocusonbet-
terintegratingtemporalcontexttounderstand
6 Limitations
howemotionsdevelopandchangeovertime.
Severallimitationsshouldbenotedforfuturework • QualityofVocalIsolation. Weobservedthat
andimprovementsinEmosical. thequalityofisolatedvocalsvaries, particu-
4177

### Page 10

larlywhenbackgroundmusicornoiseiscom- PabloV.A.Barros,NikhilChuramani,EgorLakomkin,
plex. Improvingvocalisolationmethodsorex- HenriqueSiqueira,AlexanderSutherland,andStefan
Wermter.2018. Theomg-emotionbehaviordataset.
ploringalternativeapproachescouldenhance
2018InternationalJointConferenceonNeuralNet-
theclarityandusabilityoftheaudiosamples.
works(IJCNN),pages1–7.
• Evaluation Metrics and Human Subjectivity.
AanishaBhattacharya,YamanKSingla,BalajiKrish-
Emotions’subjectivenatureindicatesthathu-
namurthy, Rajiv Ratn Shah, and Changyou Chen.
manevaluationscanvary,impactingthecon-
2023. A video is worth 4096 tokens: Verbalize
sistencyofourMOStestsandotherevaluation videos to understand them in zero shot. Preprint,
metrics. Developingmoreobjectiveandstan- arXiv:2305.09758.
dardizedevaluationmethodswouldbebenefi-
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
cialforassessingthequalityofannotations.
Subbiah,JaredDKaplan,PrafullaDhariwal,Arvind
Addressingtheselimitationsinfutureiterationsof Neelakantan,PranavShyam,GirishSastry,Amanda
Askell,etal.2020. Languagemodelsarefew-shot
Emosicalwillhelpcreateamorerobustandcom-
learners. Advancesinneuralinformationprocessing
prehensive dataset, ultimately contributing to the
systems,33:1877–1901.
advancement of multimodal emotion recognition
and synthesis research in the domain of musical Felix Burkhardt, Astrid Paeschke, M. Rolfes, Walter
Sendlmeier,andBenjaminWeiss.2005a. Adatabase
theatre.
ofgermanemotionalspeech. volume5,pages1517–
1520.
Acknowledgments
ThisworkwaspartlysupportedbyInstituteofIn- FelixBurkhardt,AstridPaeschke,MiriamRolfes,Wal-
terFSendlmeier,BenjaminWeiss,etal.2005b. A
formation&communicationsTechnologyPlanning
databaseofgermanemotionalspeech. InInterspeech,
&Evaluation(IITP)grantfundedbytheKoreagov-
volume5,pages1517–1520.
ernment(MSIT)[NO.RS-2021-II211343,Artificial
IntelligenceGraduateSchoolProgram(SeoulNa- Carlos Busso, Murtaza Bulut, Chi-Chun Lee, Abe
tionalUniversity)]andpartlybyInstituteofInfor- Kazemzadeh, Emily Mower Provost, Samuel Kim,
Jeannette Chang, Sungbok Lee, and Shrikanth
mation communications Technology Planning &
Narayanan. 2008. Iemocap: Interactive emotional
Evaluation(IITP)grantfundedbytheKoreangov-
dyadic motion capture database. Language Re-
ernment(MSIT)[No. RS-2022-II220320,2022-0- sourcesandEvaluation,42:335–359.
00320,Artificialintelligenceresearchaboutcross-
Qi Chen, Yuanqing Li, Yuankai Qi, Jiaqiu Zhou,
modal dialogue modeling for one-on-one multi-
MingkuiTan,andQiWu.2021. V2c: Visualvoice
modalinteractions].
cloning. Preprint,arXiv:2111.12890.
QiChen,MingkuiTan,YuankaiQi,JiaqiuZhou,Yuan-
References
qingLi,andQiWu.2022. V2c: visualvoicecloning.
InProceedingsoftheIEEE/CVFConferenceonCom-
Mehmet Berkehan Akçay and Kaya Og˘uz. 2020.
puterVisionandPatternRecognition,pages21242–
Speech emotion recognition: Emotional models,
21251.
databases,features,preprocessingmethods,support-
ingmodalities,andclassifiers. SpeechCommunica-
tion,116:56–76. AbhinavDhall,MonishaSingh,RolandGoecke,Tom
Gedeon,DonghuoZeng,YananWang,andKazushi
Antonin Artaud. 1938. The Theater and Its Double. Ikeda. 2023. Emotiw 2023: Emotion recognition
GrovePress,NewYork. in the wild challenge. In Proceedings of the 25th
InternationalConferenceonMultimodalInteraction,
AmirAliBagherZadeh,PaulPuLiang,SoujanyaPoria,
pages746–749.
Erik Cambria, and Louis-Philippe Morency. 2018.
Multimodal language analysis in the wild: CMU-
JochenHartmann.2022. Emotionenglishdistilroberta-
MOSEI dataset and interpretable dynamic fusion
base. https://huggingface.co/j-hartmann/
graph. InProceedingsofthe56thAnnualMeetingof
emotion-english-distilroberta-base/.
theAssociationforComputationalLinguistics(Vol-
ume1: LongPapers),pages2236–2246,Melbourne,
Hawkinsetal.2024. Gentle. Accessed: 2024-06-14.
Australia.AssociationforComputationalLinguistics.
TadasBaltrušaitis,ChaitanyaAhuja,andLouis-Philippe Rongjie Huang, Feiyang Chen, Yi Ren, Jinglin Liu,
Morency. 2018. Multimodal machine learning: A Chenye Cui, and Zhou Zhao. 2021. Multi-Singer:
surveyandtaxonomy. IEEEtransactionsonpattern Fastmulti-singersingingvoicevocoderwithalarge-
analysisandmachineintelligence,41(2):423–443. scalecorpus. Preprint,arXiv:2112.10358.
4178

### Page 11

Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, R-F. 2022. Wav2vec english speech emotion
Zhiyuan Zhang, Keshav Santhanam, Sri Vard- recognition. https://huggingface.co/r-f/
hamanan,SaifulHaq,AshutoshSharma,ThomasT. wav2vec-english-speech-emotion-recognition.
Joshi, Hanna Moazam, Heather Miller, Matei Za- Accessed: 2024-06-14.
haria,andChristopherPotts.2023. Dspy: Compiling
declarativelanguagemodelcallsintoself-improving Julius Richter, Simon Welker, Jean-Marie Lemercier,
pipelines. Preprint,arXiv:2310.03714. BunlongLay,andTimoGerkmann.2023. Speechen-
hancementanddereverberationwithdiffusion-based
generativemodels. Preprint,arXiv:2208.05830.
Lantian Li, Ruiqi Liu, Jiawen Kang, Yue Fan, Hao
Cui,YunqiCai,RavichanderVipperla,ThomasFang
Fabien Ringeval, Björn Schuller, Michel Valstar,
Zheng, and Dong Wang. 2022. Cn-celeb: multi-
NicholasCummins,RoddyCowie,andMajaPantic.
genrespeakerrecognition. SpeechCommunication,
2019. Avec’19: Audio/visualemotionchallengeand
137:77–91.
workshop. InProceedingsofthe27thACMInterna-
tionalConferenceonMultimedia,pages2718–2719.
ShanLiandWeihongDeng.2020. Deepfacialexpres-
sion recognition: A survey. IEEE transactions on FabienRingeval,AndreasSonderegger,JürgenSauer,
affectivecomputing,13(3):1195–1215. andDenisLalanne.2013. Introducingtherecolamul-
timodalcorpusofremotecollaborativeandaffective
Zheng Lian, Licai Sun, Mingyu Xu, Haiyang Sun, interactions. pages1–8.
KeXu,ZhuofanWen,ShunChen,BinLiu,andJian-
hua Tao. 2023. Explainable multimodal emotion Geoffrey Roberts. 2024. Feelings wheel. Accessed:
reasoning. arXivpreprintarXiv:2306.15401. 2024-06-14.
AnnaRohrbach,MarcusRohrbach,NiketTandon,and
StevenR.LivingstoneandFrankA.Russo.2018. The
BerntSchiele.2015a. Adatasetformoviedescrip-
ryersonaudio-visualdatabaseofemotionalspeech
tion. InProceedingsoftheIEEEconferenceoncom-
andsong(RAVDESS):Adynamic,multimodalset
puter vision and pattern recognition, pages 3202–
of facial and vocal expressions in north american
3212.
english. PLOSONE,13(5):1–35.
AnnaRohrbach,MarcusRohrbach,NiketTandon,and
ILoshchilov.2017. Decoupledweightdecayregulariza- BerntSchiele.2015b. Adatasetformoviedescrip-
tion. arXivpreprintarXiv:1711.05101. tion. In Proceedings of the IEEE Conference on
ComputerVisionandPatternRecognition(CVPR).
GaryMcKeown,MichelValstar,RoddyCowie,Maja
Simon Rouard, Francisco Massa, and Alexandre Dé-
Pantic, and Marc Schroder. 2012. The semaine
fossez.2023. Hybridtransformersformusicsource
database: Annotatedmultimodalrecordsofemotion-
separation. InICASSP23.
ally colored conversations between a person and a
limitedagent. IEEETransactionsonAffectiveCom-
JamesARussell.2003. Coreaffectandthepsycholog-
puting,3(1):5–17.
icalconstructionofemotion. Psychologicalreview,
110(1):145.
BehnazNojavanasghari,TadasBaltrušaitis,CharlesE
Hughes,andLouis-PhilippeMorency.2016. Emore- AharonSatt,ShaiRozenberg,RonHoory,etal.2017.
act: amultimodalapproachanddatasetforrecogniz- Efficientemotionrecognitionfromspeechusingdeep
ingemotionalresponsesinchildren. InProceedings learning on spectrograms. In Interspeech, pages
of the 18th acm international conference on multi- 1089–1093.
modalinteraction,pages137–144.
ArnavSinghvi,ManishShetty,ShangyinTan,Christo-
Bo Pang, Lillian Lee, et al. 2008. Opinion mining pherPotts,KoushikSen,MateiZaharia,andOmar
andsentimentanalysis. FoundationsandTrends®in Khattab.2024. Dspyassertions: Computationalcon-
informationretrieval,2(1–2):1–135. straints for self-refining language model pipelines.
Preprint,arXiv:2312.13382.
RobertPlutchikandHenryKellerman.2013. Theories
Leslie N Smith and Nicholay Topin. 2019. Super-
ofemotion,volume1. Academicpress.
convergence: Veryfasttrainingofneuralnetworks
usinglargelearningrates. InArtificialintelligence
SoujanyaPoria,ErikCambria,RajivBajpai,andAmir
andmachinelearningformulti-domainoperations
Hussain. 2017. A review of affective computing:
applications,volume11006,pages369–386.SPIE.
Fromunimodalanalysistomultimodalfusion. Infor-
mationfusion,37:98–125. Richard Socher, Alex Perelygin, Jean Wu, Jason
Chuang,ChristopherDManning,AndrewYNg,and
Soujanya Poria, Devamanyu Hazarika, Navonil Ma- ChristopherPotts.2013. Recursivedeepmodelsfor
jumder,GautamNaik,ErikCambria,andRadaMi- semanticcompositionalityoverasentimenttreebank.
halcea. 2019. Meld: A multimodal multi-party In Proceedings of the 2013 conference on empiri-
dataset for emotion recognition in conversations. calmethodsinnaturallanguageprocessing,pages
Preprint,arXiv:1810.02508. 1631–1642.
4179

### Page 12

ConstantinStanislavski.1948. BuildingaCharacter. Kun Zhou, Berrak Sisman, Rui Liu, and Haizhou
TheatreArtsBooks,NewYork. Li. 2022. Emotional voice conversion: Theory,
databasesandesd. Preprint,arXiv:2105.14762.
J. Sundberg. 1987. The Science of the Singing Voice.
NorthernIllinoisUniversityPress. Athanasia Zlatintsi, Petros Koutras, Georgios Evan-
gelopoulos,NikosMalandrakis,NikiEfthymiou,Ka-
Makarand Tapaswi, Yukun Zhu, Rainer Stiefelha- terina Pastra, Alexandros Potamianos, and Petros
gen, Antonio Torralba, Raquel Urtasun, and Sanja Maragos. 2017. Cognimuse: a multimodal video
Fidler. 2016. Movieqa: Understanding stories database annotated with saliency, events, seman-
in movies through question-answering. Preprint, ticsandemotionwithapplicationtosummarization.
arXiv:1512.02902. EURASIPJournalonImageandVideoProcessing,
2017.
SuramyaTomar.2006. Convertingvideoformatswith
Zulkoetal.2024. Moviepy. Accessed: 2024-06-14.
ffmpeg. LinuxJournal,2006(146):10.
Dimitrios Ververidis and Constantine Kotropoulos.
2006. Emotional speech recognition: Resources,
features, and methods. Speech communication,
48(9):1162–1181.
Hongji Wang, Chengdong Liang, Shuai Wang,
Zhengyang Chen, Binbin Zhang, Xu Xiang, Yan-
lei Deng, and Yanmin Qian. 2023. Wespeaker: A
researchandproductionorientedspeakerembedding
learningtoolkit. InICASSP2023-2023IEEEInter-
nationalConferenceonAcoustics,SpeechandSignal
Processing(ICASSP),pages1–5.IEEE.
JasonWei,XuezhiWang,DaleSchuurmans,Maarten
Bosma,FeiXia,EdChi,QuocVLe,DennyZhou,
etal.2022. Chain-of-thoughtpromptingelicitsrea-
soninginlargelanguagemodels. Advancesinneural
informationprocessingsystems,35:24824–24837.
Julia Wilkins, Prem Seetharaman, Alison Wahl, and
Bryan Pardo. 2018. VocalSet: A singing voice
dataset. In International Society for Music Infor-
mationRetrievalConference.
AmirZadeh,MinghaiChen,SoujanyaPoria,ErikCam-
bria, and Louis-Philippe Morency. 2017. Tensor
fusion network for multimodal sentiment analysis.
arXivpreprintarXiv:1707.07250.
AmirAli Zadeh, Paul Pu Liang, Soujanya Poria, Erik
Cambria,andLouis-PhilippeMorency.2018. Multi-
modallanguageanalysisinthewild: CMU-MOSEI
datasetandinterpretabledynamicfusiongraph. In
Proceedings of the56th Annual Meeting of the As-
sociationforComputationalLinguistics(Volume1:
Long Papers), pages 2236–2246, Melbourne, Aus-
tralia.AssociationforComputationalLinguistics.
StefanosZafeiriou,ChaZhang,andZhengyouZhang.
2015. Asurveyonfacedetectioninthewild: past,
presentandfuture. ComputerVisionandImageUn-
derstanding,138:1–24.
LichaoZhang,RuiqiLi,ShoutongWang,LiqunDeng,
Jinglin Liu, Yi Ren, Jinzheng He, Rongjie Huang,
JiemingZhu,XiaoChen,etal.2022. M4singer: A
multi-style,multi-singerandmusicalscoreprovided
mandarinsingingcorpus. AdvancesinNeuralInfor-
mationProcessingSystems,35:6914–6926.
4180
