---
来源文件 / Source PDF: `emotion2vec-2023-arxiv-2312.15185.pdf`
提取日期 / Extracted: 2026-10-30
提取方式 / Method: pdfplumber 文本层直接提取（非 OCR）
PDF 页数 / Pages: 12
总字符数 / Characters: 44562
---
## 引用信息 / Citation (APA 7th)

> Ma, Z., Zheng, Z., Ye, J., Li, J., Gao, Z., Zhang, S., & Chen, X. (2023). emotion2vec: Self-supervised pre-training for speech emotion representation. *arXiv preprint* arXiv:2312.15185. https://arxiv.org/abs/2312.15185

注：本文后续正式发表于 INTERSPEECH 2024；本 PDF 为 arXiv 预印本版。


## 正文（按页提取 / Extracted page by page）

### Page 1

emotion2vec: Self-Supervised Pre-Training
for Speech Emotion Representation
ZiyangMa1,ZhishengZheng1,JiaxinYe2,JinchaoLi3,
ZhifuGao4,ShiliangZhang4,XieChen1†
1 ShanghaiJiaoTongUniversity,2 FudanUniversity,
3 TheChineseUniversityofHongKong,4 Alibaba
Abstract et al. (2021) explore no fine-tuning, partial fine-
tuning,andentirefine-tuningwithsomeSSLmod-
Weproposeemotion2vec, auniversalspeech
elsforSERontheIEMOCAPdataset(Bussoetal.,
emotion representation model. emotion2vec
2008),andgivesomeempiricalconclusions. While
ispre-trainedonopen-sourceunlabeledemo-
tiondatathroughself-supervisedonlinedistilla- this is an ad-hoc solution, on the one hand, fine-
tion,combiningutterance-levellossandframe- tuningSSLmodelsrequiresalargecomputational
levellossduringpre-training. emotion2vecout- cost, on the other hand, these conclusions may
performsstate-of-the-artpre-traineduniversal be data-specific or model-constrained. Recently,
modelsandemotionspecialistmodelsbyonly
Chenetal.(2023a)proposedanSERmodelnamed
training linear layers for the speech emotion
Vesper, which is obtained by model distillation
recognitiontaskonthemainstreamIEMOCAP
fromWavLM-large(Chenetal.,2022)withemo-
dataset. Inaddition,emotion2vecshowscon-
tiondata. VesperisdesignedtoperformtheSER sistentimprovementsamong10differentlan-
guagesofspeechemotionrecognitiondatasets. task,whoseuniversalrepresentationcapabilitystill
emotion2vec also shows excellent results on needstobedemonstrated. Accordingly,auniver-
other emotion tasks, such as song emotion salspeech-basedemotionrepresentationmodelis
recognition, emotion prediction in conversa- urgentlyneededinthefield.
tion,andsentimentanalysis. Comparisonex-
Hereweproposeemotion2vec,auniversalemo-
periments,ablationexperiments,andvisualiza-
tion representation model that can be used to ex-
tioncomprehensivelydemonstratetheuniver-
tract speech features for diverse emotion tasks.
salcapabilityoftheproposedemotion2vec. To
thebestofourknowledge,emotion2vecisthe Self-supervisedpre-trainingisperformedon262
firstuniversalrepresentationmodelinvarious hoursofopen-sourceemotiondatawithanonline
emotion-relatedtasks,fillingagapinthefield.1 distillationparadigmtoobtainemotion2vec. Con-
sideringthatbothwhole-playinformationandlocal
1 Introduction
detailsconveyemotion,weproposeapre-training
Extractingemotionalrepresentationfromspeechis strategycombiningutterance-levellossandframe-
anessentialstepofvariousemotionaltaskssuchas levelloss. OnthemainstreamIEMOCAPdataset,
speechemotionrecognition(SER)andsentiment thedownstreamlinearmodeltrainedwithfeatures
analysis. TraditionalmethodsemployFilterBanks extracted from emotion2vec outperforms all the
(FBanks)orMelFrequencyCepstrumCoefficients mainstream SSL models and the latest specialist
(MFCCs)asspeechfeatures. Thesefeaturesarenot models. emotion2vec is tested on 13 datasets in-
rich in semantic information, resulting in limited cluding 10 languages, and the results show that
performance on emotional tasks. Popular meth- emotion2vecexhibitslanguagegeneralizationabil-
ods utilize features extracted from speech-based ity. Moreover,inadditiontotheSERtask,wealso
self-supervisedlearning(SSL)pre-trainedmodels, experimentedwithemotion2vecfeaturesonsong
leadingtoasignificantperformanceimprovement. emotionrecognition,emotionpredictioninconver-
Onepotentialchallengeblockingfurtherperfor- sation,andsentimentanalysis. Theresultsindicate
manceimprovementisthattheseSSLmodelsare thatemotion2vechasexcellenttaskgeneralization
not entirely suitable for emotional tasks. Wang ability. Extensive ablation experiments and visu-
alizationanalysisdemonstratetheeffectivenessof
†Correspondingauthor
ourpre-trainingmethodsandtheversatilityofthe
1Code,checkpoints,andextractedfeaturesareavailableat
https://github.com/ddlBoJack/emotion2vec proposedemotion2vecmodel.
3202
ceD
32
]LC.sc[
1v58151.2132:viXra

### Page 2

2 RelatedWork For speech emotion representation in other emo-
tiontasks,suchasmultimodalemotionrecognition,
2.1 Speech-basedSSL
popularpractice(Lietal.,2023a)issimilartowhat
Self-supervisedlearninghasachievedremarkable ismentionedabove.
success in the field of representation learning,
3 Methods
showcasing its efficacy across natural language
processing (Devlin et al., 2019; Liu et al., 2019; Herewemainlyintroducetheself-supervisedpre-
Radford et al., 2019; Brown et al., 2020), com- trainingmethodoftheproposedemotion2vec,for
putervision(Grilletal.,2020;Heetal.,2020;Bao whichthecoreistotrainthemodelwithUtterance-
et al., 2021; He et al., 2022), as well as speech level Loss and Frame-level Loss using Online
processing(Baevskietal.,2020;Hsuetal.,2021; Distillationparadigm.
Chenetal.,2022;Baevskietal.,2022). Forspeech
representation learning, all SSL models can be 3.1 ModelPipeline
classifiedintotwocategoriesaccordingtotheself- AsshowninFigure1,emotion2veccontainstwo
supervisedtargetsutilizedduringpre-training(Ma networksinthepre-trainingphase,whicharethe
etal.,2023b): 1)Offlinetargets. 2)Onlinetargets. teachernetworkT andthestudentnetworkS. Both
Models employing offline targets often require a modelssharethesamemodelarchitecture,includ-
well-trainedteachermodelbeforethepre-training ingafeatureextractorF composedofmulti-layer
stage, to extract self-supervised targets. Repre- convolutionalneuralnetworksandabackbonenet-
sentative models of this type are HuBERT (Hsu work B composed of multi-layer Transformers.
et al., 2021), WavLM (Chen et al., 2022) using Thesemodulescanbeconfiguredwithdifferentar-
K-meanstargets,andPBERT(Wangetal.,2022), chitectures,whichwillbedescribedinSection4.1.
MonoBERT&PolyBERT(Maetal.,2023c)using Given a raw audio utterance X = [x ,···,x ],
1 Nx
phoneme-based targets. Models using online tar- theTeacherT andtheStudentS respectivelyuti-
gets do not need a pre-trained teacher model in lize feature extractors FT and FS to obtain the
advance, whiletheteachermodelsareconstantly downsampled features Z = [z ,···,z ], which
1 Nz
updatedduringthepre-trainingphase,withanon- canbewrittenas:
linedistillationparadigm. Representativemodels
ZT = FT(X), (1)
of this type are data2vec (Baevski et al., 2022),
data2vec 2.0 (Baevski et al., 2023) using frame- ZS = FS(X). (2)
levelmasklanguagemodel(MLM)loss,andCA- FortheteachernetworkT,thedownsampledfea-
DINO (Han et al., 2023) using utterance-level turesZT aredirectlyfedintothebackbonenetwork
cross-entropyloss. emotion2vecispre-trainedcom- BT. ForthestudentnetworkS,thedownsampled
bining both utterance-level loss and frame-level featuresZS aremaskedlconsecutiveframeswith
loss,leadingtoasuperiorspeechemotionrepresen- probability p for each frame as the start. Then
tationmodel. learnableutteranceembeddingU = [u ,···,u ]
1 Nu
isplacedinthefrontbeforebeingfedintotheback-
2.2 SpeechEmotionRepresentation
bonenetworkBS. Theformulacanbewrittenas
Wepresentthefirstuniversalspeechemotionrep- follows:
k
resentation model, whereas most of the previous 1 (cid:88)
YT = BT(ZT), (3)
works directly employ speech pre-training mod- k i
i=1
els (Pepino et al., 2021; Li et al., 2022), or fine-
US;YS = BS(U;Mask(ZS)), (4)
tunethepre-trainingmodelsontheirspecificemo-
tional data with specific emotional tasks (mostly where YT is the average of the output embed-
SER) (Morais et al., 2022; Chen and Rudnicky, ding of the top k layer Transformer Block BT.
i
2023),toextractspeechemotionrepresentation. A Utterance-leveloutputembeddingUS andframe-
seriesofworksinvestigatetheSERperformanceof leveloutputembeddingYS aretheoutputsofthe
wav2vec2.0(Wangetal.,2021),HuBERT(Wang studentbackbonenetworkBS. Mask istheapply-
etal.,2021),aswellasWavLM(Ioannidesetal., ingmaskoperation. YT,YS andUS arethesame
2023),eitherfine-tuningornot. Arecentwork(Ma inthehiddenlayerdimensions,whereYT andYS
et al., 2023a) found that data2vec features also havethesameN temporaldimensions,whileUS
z
haveagoodrepresentationabilityintheSERtask. hasN temporaldimensions,respectively.
u

### Page 3

Utterance-level
Loss
Frame-level 😶 😄 😭 😡 😮 😱 😆
Loss
… … 🔥
//
Teacher Student Student
Utterance Embedding ❄
Backbone EMA Backbone Backbone
Unmasked Embedding
Network Network Network
Masked Embedding
… …
🔥 Trainable
❄ Frozen Feature Copy Feature Feature
// Stop Gradient Extractor Extractor Extractor
Figure1: Theoverallframeworkofemotion2vec. Duringthepre-trainingphase,emotion2vecconductsonlinedis-
tillationwithateachernetworkandastudentnetwork. Whenaspecificdownstreamtaskisperformed,emotion2vec
isfrozenandalightweightdownstreammodelistrained.
3.2 Utterance-levelLoss Global Embedding In the case of utilizing
globalembedding,noadditionalutterancetokens
Utterance-levellossconstructsanutterance-level
areadded. Weusetemporalpoolingofframe-level
pretext task to learn the global emotion. We use
output embedding YS instead of US to compute
mean squared error (MSE) to calculate the loss,
theloss.
whichcanbewrittenas:
L Utt = (Y¯T −U¯S)2, (5) Utterance-level
Loss (Token)
where
1 (cid:88)
Nz
Y¯T = YT, (6)
N i
z
i=1 Utterance-level
1 (cid:88)
Nu Loss (Chunk)
U¯S = US, (7)
N i
u …
i=1
whichmeansthatutterance-levellossL iscom-
Utt
putedbytemporalpoolingresultsofYT andUS. Utterance-level
Loss (Global)
Hereweproposethreewaystocomputeutterance-
levelloss,whichwecalltokenembedding,chunk
embedding,andglobalembedding,asshownin
Figure2:Differentwaystocomputeutterance-levelloss
Figure2.
inemotion2vecpre-training.
TokenEmbedding Tokenembeddingemploys
a single token to represent global emotion infor-
mation encoded by the student network S. More 3.3 Frame-levelLoss
explicitly,wesetN to1inthelearnableutterance
u
Frame-level loss constructs a frame-wise pretext
embeddingU = [u ,···,u ].
1 Nu
task to learn the context emotion. We only com-
ChunkEmbedding Chunkembeddingemploys putethelossonthemaskedpart,whichisthecom-
multipletokenstorepresentglobalemotioninfor- monpracticeforamasklanguagemodeling(MLM)
mation. Inthiscase,moreglobalinformationcan pretext task. The frame-level loss L can be
Frm
beaggregatedwithinthechunk. expressedas:

### Page 4

Hzwithdimension512. Thenalinearprojection
1 (cid:88)
L = (YT −YS)2, (8) for dimension transformation from 512 to 768 is
Frm M i i
i∈M applied, followed by the mask operation to con-
whereMdenotestheindexsequenceofframe-level structtheinputforthebackbonenetworkB. Here
webrieflyintroducedifferentbackbonenetworks
output embedding YS being masked, and M de-
indata2vecanddata2vec2.0.
notesthetotalnumberoftokensbeingmasked.
data2vec The backbone network B contains a
3.4 OnlineDistillation
5-layer learnable convolutional positional encod-
Online distillation is a self-supervised learning ing followed by a 12-layer standard Transformer.
strategy for teacher-student learning, where the EachTransformerblockissetto768modeldimen-
student network updates parameters by back- sion,3072bottleneckdimension,and12attention
propagation and the teacher network updates pa- heads. Finally,alinearprojectionfrom768to768
rameters with an exponentially moving average is equipped on the student outputs, the results of
(EMA)(Grilletal.,2020). Forthestudentnetwork which are employed to calculate MLM loss with
S,thetotallossLforbackpropagationisacombi- teacheroutputs.
nationofframe-levellossL andutterance-level
Frm
data2vec2.0 Thedata2vec2.0modelsharesthe
lossL ,donatedas:
Utt
sameTransformerarchitecturewithdata2vec,ex-
L = L +αL , (9) ceptforonemoreCNNdecoder. TheTransformer
Frm Utt
encoder only encodes the non-masked parts of
withatunableweightα. Fortheteachernetwork downsampled features Z, and then the masked
T, The parameters θT are initialized as the same parts are complemented with random Gaussian
0
parameters of the student network θS, and then noise before being passed to the CNN decoder,
0
areupdatedwithEMAwithineachmini-batch,do- inaMAE-stylefashion,toimproveefficiency. The
natedas: CNNdecoderisa4-layer1-Dconvolutionalneural
networkwithallkernelsizessetto7,stridessetto
θT = τθT +(1−τ)θS . (10)
t+1 t t+1 1,andchannelssetto384,withoutdownsampling.
Alinearprojectionfrom384to768isequippedto
whereτ isaparameterthatincreaseslinearlydur-
computeMLMloss,whichworksthesamewayas
ing pre-training. In practice, within each mini-
data2vec.
batch the parameters of teacher feature extractor
FT arecopieddirectlyfromFS,whiletheparam- 4.2 TrainingDetails
etersofteacherbackbonenetworkBT areupdated
Self-supervisedPre-training Inthepre-training
withEMAfromBT andBS.
phase, we train emotion2vec with 262 hours of
unlabeled emotion data shown in Figure 1 with
4 ExperimentsSetup
differentinitialmodels. Forthetrainingoverhead,
4.1 InitialModel Thepre-trainingisconductedon4NVIDIAA10
TensorCoreGPUs,andwesimulate16GPUsby
Differentinitialmodelsleadtodifferentarchitec-
setting the update frequency to 4. We train emo-
turesoffeatureextractorsF, backbonenetworks
tion2vecfor100epochs,eachofwhichtakesabout
B,andinitializationparametersθ . Hereweadopt
0
twomodels,data2vec2 anddata2vec2.03,bothof 37 minutes. We use a dynamic batchsize, where
themaximumnumberoftokensis1×106. Forthe
which have the same feature extractor design but
optimizingstrategy,weuseAdamwithalearning
different backbone network designs. The feature
rateof7.5×10−5 andaweightdecayof1×10−2.
extractorF isa7-layer1-Dconvolutionalneural
Wetrainemotion2vecusingacosinelearningrate
network with kernel sizes (5,2,2,2,2,2,2) and
scheduler,with5%proportionoflinearwarm-up.
strides(10,3,3,3,3,2,2),resultingin320xdown-
For the student model, each time step of the in-
sampling. GiventherawaudioinputX ata16000
put has a probability of p = 0.5 to be the start
Hzsamplerate,theoutputrepresentationsZ are50
index, and the subsequent l = 5 time steps are
2https://dl.fbaipublicfiles.com/fairseq/
masked. The hyperparameter α that controls the
data2vec/audio_base_ls.pt
lossweightissetto1. Fortheteachermodel,we
3https://dl.fbaipublicfiles.com/fairseq/
data2vec2/base_libri.pt use the average of the top k = 8 blocks of the

### Page 5

transformerlayeroutputsforprovidingthetraining Differentdatasetsareusedtotestdifferentdown-
targets. Weapplyalinearlyincreasingstrategyfor streamtaskswithvariouslanguages. Formainre-
τ fromτ = 0.999toτ = 0.99999fortheteacher sultsinSection5.2,wereportcross-validation(CV)
s e
parametersexponentiallymovingaverage. resultsontheIEMOCAPdataset. Theoriginalla-
belscoverfiveclasses,tobeconsistentandcompa-
SupervisedFine-tuning Allmodelarchitectures
rablewithpreviousmethods(Yeetal.,2023;Chen
of diverse downstream tasks are designed to be
etal.,2023b),wemerge‘excited’with‘happy’to
as simple as possible, to demonstrate the repre-
better balance the size of each emotion class, re-
sentationability ofthe pretrainedmodel. For the
sultinginfourclasses. Weconductbothleave-one-
non-sequential task, following the common prac-
session-out5-foldCVandleave-one-speaker-out
tice of SUPERB (Yang et al., 2021), we use two
10-foldCV.Moreover,wereportresultsonMELD
linearlayerswithaReLUactivationfunctionsand-
underitsoriginalsplitsetup,andRAVDESS(Liv-
wichedbetweenthem. Forthesequentialtask,we
ingstoneandRusso,2018),SAVEE(Jacksonand
use two layers of gated recurrent units (GRU) to
Haq,2014)datasetsunderarandomleave-one-out
makepredictions.
10-fold CV setup, which implies at each fold, all
sampleswithinthedatasetarerandomlysplitinto
4.3 Datasets
80%, 10%, and 10% samples in training, valida-
Asummaryofthedatasetsemployedinourexper- tion, and testing sets. Among them, speech in
imentsispresentedinTable1. Thereare18emo- RAVDESSandSAVEEdatasetsisnotseeninthe
tionaldatasetsincluding10differentlanguages: 9 pre-trainingstage,whichdemonstratesthegener-
inEnglish,and1inMandarin,Bangla,French,Ger- alizationoftheproposedmodelonout-of-domain
man, Greek, Italian, Persian, Russian, and Urdu. corpora.
Foreachdataset,itcanbecategorizedintermsof ForlanguagegeneralizationtaskinSection5.3,
Pretrain(i.e.,whetherusedduringthepre-training wereportCVresultsfor9out-of-domaindatasets,
phase), Downstream (i.e., whether tested in the including 1 in Mandarin (M3ED (Zhao et al.,
downstreamtask),Source(i.e.,wheresamplescol- 2022)), Bangla (SUBESCO (Sultana et al.,
lected),Emo(i.e.,numberofemotioncategories), 2021)), French (CaFE (Gournay et al., 2018)),
Spk (i.e., number of speakers), Lang, (i.e., Lan- German (EmoDB (Burkhardt et al., 2005)),
guage), #Utts (i.e., number of utterances), and Greek (AESDD (Vryzas et al., 2018)), Ital-
#Hours (i.e., total duration of samples). Speech ian (EMOVO (Costantini et al., 2014)), Persian
dataisextractedfromthesedatasetsanduniformly (ShEMO(MohamadNezamietal.,2019)),Russain
processedintoasinglechannelof16kHz. (RESD(Lubenetsetal.)),andUrdu(URDU(Latif
In the pretraining phase, we utilize five etal.,2018)). Ifnotspecified,languagegeneraliza-
large-scale English datasets, including IEMO- tion results are obtained using the random leave-
CAP (Busso et al., 2008), MELD (Poria one-out10-foldCVaswementionedaboveunless
et al., 2019), MEAD (Wang et al., 2020), the dataset provides a set partition. Such as the
CMU-MOSEI (Zadeh et al., 2018), and MSP- RESD dataset, we follow its original split setup
Podcast (Martinez-Lucas et al., 2020), resulting with 280 testing samples and 1116 training sam-
inatotalof262hours. TheIEMOCAPcorpuscon- ples. Additionally,weallocate10%fromthetrain-
tainsatotalof5sessionsand10differentspeakers, ingsamplesforvalidationandothersfortraining.
witheachsessionbeingaconversationoftwoex- FortaskgeneralizationtaskinSection5.4. We
clusivespeakers. MELDisamulti-partyconversa- testedotherspeechemotiontasks,includingsong
tionaldatasetcontainingabout13,847utterances emotion recognition, emotion prediction in con-
from1,433dialoguescollectedfromtheTVseries versation, andsentimentanalysis, onRAVDESS-
‘Friends’. MEAD is a talking-face video corpus Song(LivingstoneandRusso,2018),IEMOCAP
featuring 60 actors and actresses talking with 8 and CMU-MOSI (Zadeh et al., 2016) & CMU-
differentemotionsatthreedifferentintensitylev- MOSEI (Zadeh et al., 2018). For song emotion
els. CMU-MOSEI is a multimodal dataset from recognitionandemotionpredictioninconversation,
YouTube for sentiment and emotion analysis in wereportCVresults. Forsentimentanalysis,we
videos. MSP-Podcast is collected from podcast report results with its original split setup. To be
recordingsthatdiscussavarietyoftopicslikepoli- comparablewithpreviouswork,theexperimental
tics,sports,andmovies. setupvariesaccordingtothespecifictask.

### Page 6

Table1: Thedatasetsataglanceforemotion2vecpre-traininganddownstreamtasks.
Dataset Pretrain Downstream Source Emo Spk Lang #Utts #Hours
IEMOCAP(Bussoetal.,2008) ✓ ✓ Act 5 10 English 5531 7.0
MELD(Poriaetal.,2019) ✓ ✓ FriendsTV 7 407 English 13847 12.2
CMU-MOSEI(Zadehetal.,2018) ✓ ✓ YouTube 7 1000 English 44977 91.9
MEAD(Wangetal.,2020) ✓ ✗ Act 8 60 English 31792 37.3
MSP-Podcast(V1.8)(Martinez-Lucasetal.,2020) ✓ ✗ Podcast 8 10000+ English 72969 113.5
Total ✓ – – – – English 169053 262.0
CMU-MOSI(Zadehetal.,2016) ✗ ✓ YouTube 7 89 English 2199 2.6
RAVDESS-Speech(LivingstoneandRusso,2018) ✗ ✓ Act 8 24 English 1440 1.5
RAVDESS-Song(LivingstoneandRusso,2018) ✗ ✓ Act 8 23 English 1012 1.3
SAVEE(JacksonandHaq,2014) ✗ ✓ Act 7 4 English 480 0.5
M3ED(Zhaoetal.,2022) ✗ ✓ TVs 7 626 Mandarin 24449 9.8
EmoDB(Burkhardtetal.,2005) ✗ ✓ Act 7 10 German 535 0.4
EMOVO(Costantinietal.,2014) ✗ ✓ Act 7 10 Italian 588 0.5
CaFE(Gournayetal.,2018) ✗ ✓ Act 7 12 French 936 1.2
SUBESCO(Sultanaetal.,2021) ✗ ✓ Act 7 20 Bangla 7000 7.8
ShEMO(MohamadNezamietal.,2019) ✗ ✓ Act 6 87 Persian 3000 3.4
URDU(Latifetal.,2018) ✗ ✓ Talkshows 4 38 Urdu 400 0.3
AESDD(Vryzasetal.,2018) ✗ ✓ Act 5 5 Greek 604 0.7
RESD(Lubenetsetal.) ✗ ✓ Act 7 200 Russian 1396 2.3
5 Results forms on par with these models with only linear
layers,whiletheirdownstreamnetworkshave2x,
5.1 EvaluationMetrics
135x,and114xmoreparametersthanemotion2vec,
We apply commonly used evaluation metrics, respectively. Weprovidetheresultsofleave-one-
weighted accuracy (WA), unweighted accuracy session-out five-fold cross-validation and leave-
(UA), and weighted average F1 (WF1), to eval- one-speaker-outten-foldcross-validationforrefer-
uatetheperformanceofspeechemotiontasks. WA ence.
correspondstotheoverallaccuracyandUAcorre- We also conduct experiments on other main-
sponds to the average class-wise accuracy. WF1 stream English datasets to prove the generaliza-
is a comprehensive evaluation, especially for the tionofemotion2vecinTable3. MELDisanoisy
situationofsampleimbalance. dataset used to test the SER performance of the
modelincomplexenvironments. RAVDESSand
5.2 MainResults SAVEE are out-of-domain datasets with respec-
tiverecordingenvironments. Experimentalresults
The results are shown in Table 2, where we
showthatemotion2vecexhibitsstate-of-the-artper-
comparedifferentSSLpre-trainedmodelsonthe
formanceondifferentdatasetsindifferentenviron-
IEMOCAP dataset, as well as larger-scale pre-
ments.
trained models, and the latest specialist models
designed for SER tasks. We follow the evalua-
5.3 Languagegeneralization
tionofSUPERB(Yangetal.,2021),freezingthe
pre-trainedmodelandtrainingdownstreamlinear Giventhevariouslanguages,theSERdatasetsex-
layerswiththehiddendimensionalsetto256. As hibit notable domain shifts. The generalization
can be seen from the table, emotion2vec outper- of the model to unseen language is critically im-
formsallexistingSSLpre-trainedmodels,across portant for SER. We validate the generalization
allbasemodelswithsimilarparametersandlarge ofemotion2vecandotherbaselinesontheout-of-
models with greater parameters. Compared with domainlanguageSERdatasets. Wefollowtheeval-
Versper-12, an SER model obtained by distilla- uationofSUPERB(Yangetal.,2021),freezingthe
tionfromWavLM-large,emotion2vecworksbet- pre-trained models and training downstream lin-
ter with fewer parameters. TIM-NET (Ye et al., earlayerswiththehiddendimensionalsetto256,
2023), MSTR (Li et al., 2023b), and DST (Chen wheretheWavLM-base,WavLM-base+,data2vec,
et al., 2023b) are the latest SER specialist mod- dat2vec 2.0, and emotion2vec are our implemen-
els,respectively,whichusedifferentscalesofup- tationsfollowingthepracticeabove. Asshownin
stream features and downstream networks. The Table4,emotion2vecoutperformsalltheSSLbase-
proposedemotion2vecmodeloutperformsorper- linemethodsonthe9differentlingualdatasetsin

### Page 7

Table 2: SER task performance of different SSL pre-trained models on the IEMOCAP dataset. The setting of
thedownstreammodelsfollowsSUPERB(Yangetal.,2021)touselinearlayerstotesttherepresentationability
ofdifferentupstreammodels. “LS-960"meansLibriSpeech960hours,“LL-60k"meansLibriLight60khours,
and “Mix-94k" means 94k hours of data including LibriLight, VoxPopuli, and GigaSpeech. For emotion data,
“LSED-206"meansLSED206hours,and“Emo-262"referstothe262hoursofpre-trainingdatainTable1. Models
aretestedusingleave-one-session-outfive-foldcross-validationwith20%fromthetrainingsetusedasthevalidation
setforeachsession. Modelswithunderlineareleave-one-speaker-outten-foldcross-validationwith8speakers
fortraining,1speakerforvalidation,and1speakerfortestingwithineachfold. Modelswith*implythesame
foldforbothvalidationandtesting,forafaircomparisonassomeworkusesthisprinciple. Wealsocomparewith
larger-scalepre-trainedmodelsandthelatestspecialistmodelsdesignedforSERtasks.
Model Pre-trainingCorpus Upstream #UpstreamParams Downstream #DownstreamParams WA(%)↑
Self-supervisedModel
smallsize
wav2vec(Schneideretal.,2019) 32.54M 0.13M 59.79
LS-960 Proposed Linear
vq-wav2vec(Baevskietal.,2019) 34.15M 0.20M 58.24
basesize
wav2vec2.0(Baevskietal.,2020) LS-960 95.04M 0.20M 63.43
HuBERT(Hsuetal.,2021) LS-960 94.68M 0.20M 64.92
WavLM(Chenetal.,2022) LS-960 94.70M 0.20M 65.94
WavLM+(Chenetal.,2022) Mix-94k 94.70M 0.20M 67.98
data2vec(Baevskietal.,2022) LS-960 93.75M 0.20M 67.38
data2vec2.0(Baevskietal.,2023) LS-960 93.78M 0.20M 68.58
Proposed Linear
Vesper-4(Chenetal.,2023a) Mix-94k+LSED-206 63.52M 0.26M 68.40
Vesper-12(Chenetal.,2023a) Mix-94k+LSED-206 164.29M 0.26M 70.70
emotion2vec LS-960+Emo-262 93.79M 0.20M 71.79
emotion2vec* LS-960+Emo-262 93.79M 0.20M 74.48
emotion2vec LS-960+Emo-262 93.79M 0.20M 72.94
emotion2vec* LS-960+Emo-262 93.79M 0.20M 77.64
largesize
wav2vec2.0(Baevskietal.,2020) LL-60k 317.38M 65.64
HuBERT(Hsuetal.,2021) LL-60k Proposed 316.61M Linear 0.26M 67.62
WavLM(Chenetal.,2022) Mix-94k 316.62M 70.03
SupervisedModel
TIM-Net(Yeetal.,2023) MFCC - CNN(TIM-Net) 0.40M 68.29
MSTR(Lietal.,2023b) - HuBERT-large 316.61M Transformer(MSTR) 27.00M 70.03
DST(Chenetal.,2023b) WavLM-large 316.62M Transformer(DST) 22.78M 71.80
Table3: emotion2vecperformanceonmainstreamEnglishdatasets.
WA(%)↑ UA(%)↑ WF1(%)↑ WA(%)↑ UA(%)↑ WF1(%)↑ WA(%)↑ UA(%)↑ WF1(%)↑
Model
MELD RAVDESS SAVEE
WavLM-base 46.95 16.34 35.16 37.01 37.11 36.08 42.08 38.46 38.93
WavLM-base+ 43.78 16.75 34.60 38.89 38.40 37.75 43.54 39.27 42.19
data2vec 45.75 24.98 43.59 69.58 69.70 69.25 82.50 82.26 82.37
data2vec2.0 48.92 26.10 45.80 81.04 80.80 80.97 83.13 82.94 83.03
emotion2vec 51.88 28.03 48.70 82.43 82.86 82.39 84.38 82.30 84.45
Table4: emotion2vecperformanceondatasetsofotherlanguages.
WA(%)↑ UA(%)↑ WF1(%)↑ WA(%)↑ UA(%)↑ WF1(%)↑ WF1(%)↑ UA(%)↑ WF1(%)↑
Model
AESD(Gr) CAFE(Fr) RESD(Ru)
WavLM-base 55.33 55.50 54.86 31.61 32.02 30.88 56.17 56.17 55.69
WavLM-base+ 53.83 54.41 52.48 31.40 33.39 30.40 55.00 55.19 55.08
data2vec 56.67 57.26 56.57 57.10 57.68 57.36 49.42 49.77 48.97
data2vec2.0 71.33 70.20 70.93 71.51 72.98 71.50 64.08 64.33 64.17
emotion2vec 72.33 72.27 71.57 74.52 75.26 74.53 64.75 65.04 64.53
Model EmoDB(De) EMOVO(It) M3ED(Zh)
WavLM-base 59.06 55.32 58.96 40.17 40.34 37.36 44.03 18.90 34.50
WavLM-base+ 65.66 64.60 64.83 40.34 41.98 40.11 45.09 20.18 36.49
data2vec 67.17 64.81 66.52 51.21 51.97 49.82 44.44 21.10 37.77
data2vec2.0 83.77 83.07 83.93 60.69 61.27 60.79 47.50 24.12 41.74
emotion2vec 84.34 84.85 84.32 61.21 62.97 60.89 49.15 26.98 44.38
Model SUBESCO(Bn) ShEMO(Fa) URDU(Ur)
WavLM-base 54.50 54.77 53.96 67.27 46.60 65.63 71.00 70.25 70.82
WavLM-base+ 54.73 54.69 54.59 66.73 44.29 65.12 67.25 68.68 67.47
data2vec 78.29 78.25 78.21 70.80 53.96 69.84 71.75 72.67 71.83
data2vec2.0 87.91 87.95 87.90 77.90 62.03 76.96 77.50 78.42 77.12
emotion2vec 90.91 90.96 90.91 79.97 66.04 79.56 81.50 81.87 81.60

### Page 8

Table5: emotion2vecperformanceofthesongemotionrecognitiontaskontheRAVDESS-Songdataset.
Model Upstream Downstream WA(%)↑ UA(%)↑ WF1(%)↑
Self-supervisedModel
WavLM-base Freeze 52.3 52.4 52.1
WavLM-base+ Freeze 54.9 53.9 54.2
data2vec Freeze 63.8 64.1 63.4
data2vec2.0 Freeze 73.0 74.6 72.7
L3-Net(KohandDubnov,2021) Freeze Linear 71.0 - -
SpecMAE(Sadoketal.,2023) Finetune 54.5 - 53.9
VQ-MAE-S(Patch-tf)(Sadoketal.,2023) Finetune 84.0 - 84.0
VQ-MAE-S(Frame)(Sadoketal.,2023) Finetune 84.2 - 84.3
emotion2vec Freeze 85.0 85.2 84.8
SpecialistModel
VQ-MAE-S(Patch-tf)(Sadoketal.,2023) 83.7 - 83.4
Finetune Query2Emo
VQ-MAE-S(Frame)(Sadoketal.,2023) 85.8 - 85.7
termsofWA,UA,andWF1. Theseresultsdemon- dimensions,hyperparameters,andtrainingstrate-
stratethatemotion2veccapturestheemotionpat- giesarekeptthesameasthereferenceimplemen-
ternsacrosslanguagesandshowsstate-of-the-art tation with leave-one-speaker-out 10-fold cross-
performance. validation. For the speech modality, the input is
768-dimensionalemotion2vecfeatures. Forthetext
5.4 Taskgeneralization modality,theinputis378-dimensionalBERT(De-
vlin et al., 2019) features. For the speech + text
Inordertoverifythegeneralizationofthemodel,in
multimodal, the input is a concatenation of emo-
additiontospeechemotionrecognition,wetested
tion2vecfeaturesandBERTfeatures, whichalso
other speech emotion tasks, including song emo-
remainsthesameasthereferenceimplementation.
tion recognition, emotion prediction in conversa-
AsshowninTable6,withspeechfeaturesreplaced
tion,andsentimentanalysis.
with emotion2vec in the EPC task, there are per-
SongEmotionRecognition Songemotionrecog- formancegainsinbothspeechsinglemodalityand
nitionisasub-taskofmusicemotionrecognition speech-textmulti-modality.
(MER), which aims to identify the emotion ex-
pressed in a singing voice. Following common Table6: emotion2vecperformanceofemotionpredic-
practice,weperformfive-foldcross-validationwith tioninconversationontheIEMOCAPdataset.
randomlyshuffleddata,andremainonefoldunseen
Modality Model UAR(%)↑ MacroF1(%)↑
duringeachtraining,todemonstratethegeneraliza- Noroozietal.’s(2017) 56.78 55.11
Shietal.’s(2020) 61.98 60.21
tionofthefeatures. WavLM-base,WavLM-base+, Speech
Shietal.’s(2023) 65.01 65.91
data2vec,dat2vec2.0,andemotion2vecareourim- emotion2vec 77.19 76.71
Noroozietal.’s(2017) 71.19 70.65
plementations,followingthepracticeabove. The Text(forreference) Shietal.’s(2020) 74.94 74.54
results for L3-NET, SpecMAE, and VQ-MAE-S Shietal.’s(2023) 77.30 76.67
Noroozietal.’s(2017) 74.61 73.62
aretakenfromtheirpapers. AsshowninTable5, Shietal.’s(2020) 76.31 75.50
Speech+Text
Shietal.’s(2023) 80.18 80.01
emotion2vecoutperformsallknownSSLmodels emotion2vec 81.68 80.75
evenwithoutfinetuningthemodelinthesongemo-
tionrecognitiontask.
Sentiment Analysis Sentiment analysis is the
EmotionPredictioninConversation Emotion task of analyzing text or speech to determine
predictioninconversation(EPC)referstopredict- whether the affective state conveyed is positive,
ingthefutureemotionalstateofaspecificspeaker negative, or neutral. Following Lian et al.’s
basedonhistoricalconversationinformation. We (2023) practice, we eliminate the neutral senti-
reproduce Shi et al.’s (2023) method except that ment and perform the binary classification task
thespeechfeaturesareobtainedfromourproposed on the standard training/validation/test set of
emotion2vec. Briefly,themodelemploysseveral CMU-MOSI (Zadeh et al., 2016) and CMU-
GRUs with a hierarchical structure for emotion MOSEI (Zadeh et al., 2018), respectively. Also
prediction. Each prediction takes the previous 6 inlinewithLianetal.’s(2023)practice,weutilize
turns of the dialogue, in which one speaker can themeanofthelastfourlayers’featuresofthepre-
saymultipleutterancesineachturn. Thenetwork trainedmodel,totrainthedownstreamlinearlayers.

### Page 9

AsshowninTable7,emotion2vecoutperformspre- Table9: Ablationstudywithdifferentloss.
traineddata2vecandWavLMwithself-supervised
FrmLoss UttLoss Downstream WA(%)↑ UA(%)↑ WF1(%)↑
learningandpretrainedWhisperEncoder(Radford ✗ ✓ Utt 28.96 25.0 13.13
✓ ✗ Frm 70.85 71.61 70.71
etal.,2023)withsupervisedlearningutilizingASR
✓ ✓ Utt 62.77 63.53 62.43
task. ✓ ✓ Frm 71.79 72.69 71.80
✓ ✓ Utt⊕Frm 71.37 72.69 71.29
Table7:emotion2vecperformanceofsentimentanalysis
onCMU-MOSIandCMU-MOSEIdatasets.
Utterance-level Loss Method In this experi-
ment,wecomparetheimpactofdifferenttypesof
WF1(%)↑
Model
CMU-MOSI CMU-MOSEI utterance-levellossproposedinSection3.2onper-
BaseSize
formance. AsshowninTable10,chunkembedding
data2vec 65.06 72.79
WavLM 62.36 73.47 chosen to compute utterance-level loss performs
WhisperEncoder 65.41 74.75 thebest.
emotion2vec 69.16 76.56
LargeSize Table10:Ablationstudywiththemethodsforutterance-
WavLM 68.27 77.66
levelloss.
WhisperEncoder 64.93 76.46
UttLossMethod WA(%)↑ UA(%)↑ WF1(%)↑
Token 70.46 71.07 70.33
5.5 AblationStudy
Chunk 71.79 72.69 71.80
Global 70.30 71.52 70.18
Ifnotspecified,resultsareobtainedusingthestan-
dardleave-one-session-out5-foldcross-validation
ontheIEMOCAPdataset. Utterance-levelLossWeight Inthisexperiment,
we compare the impact of utterance-level loss
InitializationMethod Inthisexperiment,weex-
weight on performance. As shown in Table 11,
plore the impact of initialization methods on per-
weightingutterance-levellossandframe-levelloss
formance. data2vecanddata2vec2.0aretworep-
witharatioof1:1worksbest.
resentativemodelstrainedwithonlinedistillation,
bothofwhicharepre-trainedonLibrispeech960 Table11: Ablationstudywiththeweightforutterance-
hours. AsshowninTable8,initializingwithapre- levelloss.
trained model would be better than the cold start
UttLossα WA(%)↑ UA(%)↑ WF1(%)↑
method. Modelinitializingwithdata2vec2.0per-
0 70.85 71.61 70.71
formsbetterthantheoneinitializingwithdata2vec.
0.1 71.06 72.16 71.08
1 72.14 72.84 72.13
Table8: Ablationstudywithinitializationmethods.
10 70.58 71.37 70.61
Initialization WA(%)↑ UA(%)↑ WF1(%)↑
ColdStart 61.34 62.71 61.19
data2vec 70.2 70.93 70.11 5.6 Visualization
data2vec2.0 71.79 72.69 71.80
Toinvestigatetheintuitiveeffectofemotion2vec
andotherSSLbaselinesonemotionrepresentation
TrainingLoss Inthisexperiment,weexplorethe learning,wevisualizetherepresentationslearned
impactonperformanceofdifferentcombinations by WavLM, data2vec, and emotion2vec through
of loss when pre-training, and different features the UMAP technique (McInnes et al., 2018) in
when training downstream models. As shown in Figure3andFigure4. Weconducttheleave-one-
Table9,ifonlyutterance-levellossisadopteddur- session-outevaluationstrategyonIEMOCAP,and
ingpre-training,themodelalmostdoesnotwork. If the8:2hold-outevaluationonSUBESCO,bothof
pre-trainedwithframe-levelloss,themodelobtains whichwerandomlyselect10%samplesfromthe
reasonableresultswhetherutterance-levellossex- trainingsetasthevalidationset. Specifically,fora
istsornot. Whenpre-trainedwithbothutterance- faircomparison,therepresentationsfromthefirst
levellossandframe-levelloss,themodelachieves linearlayerarevisualizedafteranidenticaltraining
goodresults. Wealsotrytoconcatenateutterance phasefordifferentSSLmodels.
embeddingsandframeembeddingswhentraining Figure3visualizesdifferentSSLmodelstorep-
downstream models, where we obtain similar re- resent arousal. In a sense, arousal refers to emo-
sultsasframeembeddingsonly. tionalintensity. Figure3(a)andFigure3(b)show

### Page 10

(a) WavLM (b) data2vec (c) emotion2vec
Figure3: UMAPvisualizationsoflearnedfeaturesondownstreamSERtaskfromWavLM,data2vec,andemo-
tion2vecontheIEMOCAPdataset. RedandBluetonesmeanlowandhigharousalemotionalclasses,respectively.
(a) WavLM (b) data2vec (c) emotion2vec
Figure4: UMAPvisualizationsoflearnedfeaturesondownstreamSERtaskfromWavLM,data2vec,andemo-
tion2vecontheSUBESCOdataset.
heavyoverlappingbetweenhighandlowarousal tasks,languages,andscenarios. Inthefuture,we
emotion classes. In contrast, Figure 3 (c) shows willexplorethescalinglawofemotionrepresenta-
that the high arousal and low arousal representa- tionmodels,namelyhowtoprovideabetterrepre-
tionsareclusteredreceptively,andthefeaturedis- sentationwithmoredataandlargerparameters.
tribution exhibits a trend transitioning from high
arousal tolow arousal, which is more reasonable
References
compared to other methods. Figure 4 shows the
ability of different SSL models to represent dis- Alexei Baevski, Arun Babu, Wei-Ning Hsu, and
MichaelAuli.2023. Efficientself-supervisedlearn-
creteemotionclasses. AsFigure4(a)andFigure4
ingwithcontextualizedtargetrepresentationsforvi-
(b)show,WavLManddata2vecsufferfromclass
sion,speechandlanguage. InProc.IMCL.
confusionproblems. Onthecontrary,thefeatures
Alexei Baevski, Wei-Ning Hsu, Qiantong Xu, Arun
learnedbyemotion2vecdemonstrateahigherintra-
Babu,JiataoGu,andMichaelAuli.2022. data2vec:
class compactness and a much larger inter-class
Ageneralframeworkforself-supervisedlearningin
margin. Theresultsindicatethatemotion2vecpro- speech,visionandlanguage. InProc.ICML.
videsmoreclass-discriminativeandemotion-aware
AlexeiBaevski, SteffenSchneider, andMichaelAuli.
representationstosupportitssuperiorperformance.
2019. vq-wav2vec: Self-supervisedlearningofdis-
cretespeechrepresentations. InProc.ICLR.
6 Conclusion
AlexeiBaevski,YuhaoZhou,AbdelrahmanMohamed,
In this paper, we propose emotion2vec, a univer- andMichaelAuli.2020. wav2vec2.0: Aframework
forself-supervisedlearningofspeechrepresentations.
salemotionrepresentationmodel. emotion2vecis
InProc.NeurIPS.
pre-trainedon262hoursofunlabeledemotiondata
throughself-supervisedonlinedistillation,leading Hangbo Bao, Li Dong, Songhao Piao, and Furu Wei.
2021. BEiT:BERTpre-trainingofimageTransform-
to universal emotion representation ability. We
ers. InProc.ICLR.
prove that our strategy of combining utterance-
levellossandframe-levellossduringemotionpre- Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah,JaredDKaplan,PrafullaDhariwal,Arvind
trainingiseffective. Extensiveexperimentsdemon-
Neelakantan,PranavShyam,GirishSastry,Amanda
stratethattheproposedemotion2vechastheability
Askell,etal.2020. Languagemodelsarefew-shot
toextractemotionrepresentationacrossdifferent learners. InProc.NeurIPS.

### Page 11

FelixBurkhardt,AstridPaeschke,MiriamRolfes,Wal- Wei-NingHsu,BenjaminBolte,Yao-HungHubertTsai,
ter F Sendlmeier, Benjamin Weiss, et al. 2005. A KushalLakhotia,RuslanSalakhutdinov,andAbdel-
databaseofGermanemotionalspeech. InProc.In- rahmanMohamed.2021. HuBERT:Self-supervised
terspeech. speechrepresentationlearningbymaskedprediction
ofhiddenunits. InProc.TASLP.
Carlos Busso, Murtaza Bulut, Chi-Chun Lee, Abe
Kazemzadeh, Emily Mower, Samuel Kim, Jean- George Ioannides, Michael Owen, Andrew Fletcher,
nette N Chang, Sungbok Lee, and Shrikanth S Viktor Rozgic, and Chao Wang. 2023. Towards
Narayanan.2008. IEMOCAP:Interactiveemotional paralinguistic-only speech representations for end-
dyadicmotioncapturedatabase. InProc.LREC. to-endspeechemotionrecognition. InProc.Inter-
speech.
Li-WeiChenandAlexanderRudnicky.2023. Exploring
wav2vec2.0finetuningforimprovedspeechemotion PhilipJacksonandSJUoSGHaq.2014. Surreyaudio-
recognition. InProc.ICASSP. visualexpressedemotion(SAVEE)database. Univer-
sityofSurrey.
Sanyuan Chen, Chengyi Wang, Zhengyang Chen,
YuWu,ShujieLiu,ZhuoChen,JinyuLi,Naoyuki EunjeongKohandShlomoDubnov.2021. Comparison
Kanda, Takuya Yoshioka, Xiong Xiao, et al. 2022. and analysis of deep audio embeddings for music
WavLM:Large-scaleself-supervisedpre-trainingfor emotionrecognition. InProc.CEURWorkshop.
fullstackspeechprocessing. InProc.JSTSP.
Siddique Latif, Adnan Qayyum, Muhammad Usman,
WeidongChen,XiaofenXing,PeihaoChen,andXiang- andJunaidQadir.2018. Crosslingualspeechemo-
min Xu. 2023a. Vesper: A compact and effective tion recognition: Urdu vs. western languages. In
pretrainedmodelforspeechemotionrecognition. In Proc.FIT.
arXivpreprint.
JinchaoLi,ShuaiWang,YangChao,XunyingLiu,and
WeidongChen,XiaofenXing,XiangminXu,Jianxin HelenMeng.2023a. Context-awaremultimodalfu-
Pang, and Lan Du. 2023b. DST: Deformable sionforemotionrecognition. InProc.Interspeech.
speechTransformerforemotionrecognition. InProc.
ICASSP. Yuanchao Li, Yumnah Mohamied, Peter Bell, and
CatherineLai.2022. Explorationofaself-supervised
GiovanniCostantini,IacopoIaderola,AndreaPaoloni, speech model: A study on emotional corpora. In
andMassimilianoTodisco.2014. EMOVOcorpus: Proc.SLT.
anItalianemotionalspeechdatabase. InProc.LREC.
ZhipengLi,XiaofenXing,YuanboFang,WeibinZhang,
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and and Hengsheng Fan. 2023b. Multi-scale temporal
Kristina Toutanova. 2019. BERT: Pre-training of transformerforspeechemotionrecognition. InProc.
deepbidirectionaltransformersforlanguageunder- Interspeech.
standing. InProc.NAACL.
Zheng Lian, Haiyang Sun, Licai Sun, Kang Chen,
PhilippeGournay,OlivierLahaie,andRochLefebvre. Mngyu Xu, Kexin Wang, Ke Xu, Yu He, Ying Li,
2018. ACanadianFrenchemotionalspeechdataset. JinmingZhao,etal.2023. MER2023: Multi-label
InProc.ACMMultimedia. learning,modalityrobustness,andsemi-supervised
learning. InProc.ACMMultimedia.
Jean-Bastien Grill, Florian Strub, Florent Altché,
Corentin Tallec, Pierre Richemond, Elena YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Man-
Buchatskaya, Carl Doersch, Bernardo Avila Pires, dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Zhaohan Guo, Mohammad Gheshlaghi Azar, et al. Luke Zettlemoyer, and Veselin Stoyanov. 2019.
2020. Bootstrapyourownlatent: anewapproachto RoBERTa: ArobustlyoptimizedBERTpretraining
self-supervisedlearning. InProc.NeurIPS. approach. InarXivpreprint.
BingHan,ZhengyangChen,andYanminQian.2023. StevenRLivingstoneandFrankARusso.2018. The
Self-supervised learning with cluster-aware-DINO Ryersonaudio-visualdatabaseofemotionalspeech
forhigh-performancerobustspeakerverification. In andsong(RAVDESS):Adynamic,multimodalset
arXivpreprint. offacialandvocalexpressionsinNorth American
English. InProc.PloSOne.
KaimingHe,XinleiChen,SainingXie,YanghaoLi,Pi-
otrDollár,andRossGirshick.2022. Maskedautoen- IlyaLubenets,NikitaDavidchuk,andArtemAmentes.
codersarescalablevisionlearners. InProc.CVPR. Aniemore.
KaimingHe,HaoqiFan,YuxinWu,SainingXie,and ZiyangMa,WenWu,ZhishengZheng,YiweiGuo,Qian
Ross Girshick. 2020. Momentum contrast for un- Chen,ShiliangZhang,andXieChen.2023a. Lever-
supervised visual representation learning. In Proc. aging speech PTM, text LLM, and emotional TTS
CVPR. forspeechemotionrecognition. InProc.ICASSP.

### Page 12

ZiyangMa,ZhishengZheng,ChangliTang,YujinWang, Sadia Sultana, M Shahidur Rahman, M Reza Selim,
and Xie Chen. 2023b. MT4SSL: Boosting self- andMZafarIqbal.2021. SUSTBanglaemotional
supervised speech representation learning by inte- speech corpus (SUBESCO): An audio-only emo-
gratingmultipletargets. InProc.Interspeech. tionalspeechcorpusforBangla. InProc.PloSOne.
ZiyangMa,ZhishengZheng,GuanrouYang,YuWang, Nikolaos Vryzas, Rigas Kotsakis, Aikaterini Liatsou,
Chao Zhang, and Xie Chen. 2023c. Pushing the CharalamposADimoulas,andGeorgeKalliris.2018.
limitsofunsupervisedunitdiscoveryforSSLspeech Speechemotionrecognitionforperformanceinterac-
representation. InProc.Interspeech. tion. InProc.AES.
LuzMartinez-Lucas,MohammedAbdelwahab,andCar- Chengyi Wang, Yiming Wang, Yu Wu, Sanyuan
losBusso.2020. TheMSP-conversationcorpus. In Chen, Jinyu Li, Shujie Liu, and Furu Wei. 2022.
Proc.Interspeech. Supervision-guided codebooks for masked predic-
tioninspeechpre-training. InProc.InterSpeech.
LelandMcInnes,JohnHealy,andJamesMelville.2018.
UMAP:Uniformmanifoldapproximationandpro-
KaisiyuanWang,QianyiWu,LinsenSong,Zhuoqian
jectionfordimensionreduction. InarXivpreprint.
Yang, Wayne Wu, Chen Qian, Ran He, Yu Qiao,
andChenChangeLoy.2020. MEAD:Alarge-scale
OmidMohamadNezami,PariaJamshidLou,andMan-
audio-visualdatasetforemotionaltalking-facegen-
soureh Karami. 2019. ShEMO: a large-scale vali-
eration. InProc.ECCV.
dateddatabaseforPersianspeechemotiondetection.
InProc.LREC.
YingzhiWang, AbdelmoumeneBoumadane, andAb-
delwahabHeba.2021. Afine-tunedwav2vec2.0/Hu-
EdmilsonMorais,RonHoory,WeizhongZhu,ItaiGat,
BERT benchmark for speech emotion recognition,
Matheus Damasceno, and Hagai Aronowitz. 2022.
speakerverificationandspokenlanguageunderstand-
Speech emotion recognition using self-supervised
ing. InarXivpreprint.
features. InProc.ICASSP.
FatemehNoroozi,NedaAkrami,andGholamrezaAn- Shu-Wen Yang, Po-Han Chi, Yung-Sung Chuang,
barjafari.2017. Speech-basedemotionrecognition Cheng-I Jeff Lai, Kushal Lakhotia, Yist Y Lin,
andnextreactionprediction. InProc.SIU. AndyTLiu,JiatongShi,XuankaiChang,Guan-Ting
Lin,etal.2021. SUPERB:Speechprocessinguniver-
LeonardoPepino,PabloRiera,andLucianaFerrer.2021. salperformancebenchmark. InProc.Interspeech.
Emotionrecognitionfromspeechusingwav2vec2.0
embeddings. InProc.Interspeech. JiaxinYe,Xin-ChengWen,YujieWei,YongXu,Kun-
hong Liu, and Hongming Shan. 2023. Temporal
Soujanya Poria, Devamanyu Hazarika, Navonil Ma- modelingmatters: Anoveltemporalemotionalmod-
jumder,GautamNaik,ErikCambria,andRadaMi- elingapproachforspeechemotionrecognition. In
halcea. 2019. MELD: A multimodal multi-party Proc.ICASSP.
datasetforemotionrecognitioninconversations. In
Proc.ACL. Amir Zadeh, Rowan Zellers, Eli Pincus, and Louis-
PhilippeMorency.2016. MOSI:Multimodalcorpus
AlecRadford,JongWookKim,TaoXu,GregBrock- of sentiment intensity and subjectivity analysis in
man,ChristineMcLeavey,andIlyaSutskever.2023. onlineopinionvideos. InarXivpreprint.
Robustspeechrecognitionvialarge-scaleweaksu-
pervision. InProc.ICML. AmirAliBagherZadeh,PaulPuLiang,SoujanyaPoria,
Erik Cambria, and Louis-Philippe Morency. 2018.
AlecRadford,JeffreyWu,RewonChild,DavidLuan,
Multimodal language analysis in the wild: CMU-
DarioAmodei,IlyaSutskever,etal.2019. Language
MOSEI dataset and interpretable dynamic fusion
modelsareunsupervisedmultitasklearners. InOpe-
graph. InProc.ACL.
nAIblog.
Jinming Zhao, Tenggan Zhang, Jingwen Hu, Yuchen
Samir Sadok, Simon Leglaive, and Renaud Séguier.
Liu,QinJin,XinchaoWang,andHaizhouLi.2022.
2023. Avectorquantizedmaskedautoencoderfor
M3ED: Multi-modal multi-scene multi-label emo-
speechemotionrecognition. InarXivpreprint.
tionaldialoguedatabase. InProc.ACL.
Steffen Schneider, Alexei Baevski, Ronan Collobert,
andMichaelAuli.2019. wav2vec:Unsupervisedpre-
trainingforspeechrecognition. InProc.Interspeech.
Xiaohan Shi, Sixia Li, and Jianwu Dang. 2020. Di-
mensional emotion prediction based on interactive
contextinconversation. InProc.Interspeech.
Xiaohan Shi, Xingfeng Li, and Tomoki Toda. 2023.
Emotion awareness in multi-utterance turn for im-
provingemotionpredictioninmulti-speakerconver-
sation. InProc.Interspeech.
