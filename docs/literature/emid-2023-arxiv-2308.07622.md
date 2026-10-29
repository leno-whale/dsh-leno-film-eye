---
来源文件 / Source PDF: `emid-2023-arxiv-2308.07622.pdf`
提取日期 / Extracted: 2026-10-30
提取方式 / Method: pdfplumber 文本层直接提取（非 OCR）
PDF 页数 / Pages: 8
总字符数 / Characters: 38974
DOI: 10.1145/3607541.3616821
PDF 元数据标题 / Metadata title: EMID: An Emotional Aligned Dataset in Audio-Visual Modality
---
## 引用信息 / Citation (APA 7th)

> Zou, J., Mei, J., Ye, G., Huai, T., Shen, Q., & Dong, D. (2023). EMID: An emotional aligned dataset in audio-visual modality. In *Proceedings of the 1st International Workshop on Multimedia Content Generation and Evaluation: New Methods and Practice (McGE '23)*. ACM. https://doi.org/10.1145/3607541.3616821

注：文件名含 arXiv 编号 2308.07622；本 PDF 为 ACM 正式出版的 McGE '23 会议版（2023-10-29，加拿大渥太华）。


## 正文（按页提取 / Extracted page by page）

### Page 1

EMID: An Emotional Aligned Dataset in Audio-Visual Modality
JialingZou∗ GuangzeYe TianyuHuai
JiahaoMei∗ EastChinaNormalUniversity EastChinaNormalUniversity
51255901103@stu.ecnu.edu.cn Shanghai,China Shanghai,China
10215102440@stu.ecnu.edu.cn 5226591017@stu.ecnu.edu.cn tyhuai@stu.ecnu.edu.cn
EastChinaNormalUniversity
Shanghai,China
QiweiShen DaoguoDong†
EastChinaNormalUniversity EastChinaNormalUniversity
Shanghai,China Shanghai,China
10215101495@stu.ecnu.edu.cn dgdong@cs.ecnu.edu.cn
ABSTRACT ACMReferenceFormat:
Inthispaper,weproposeEmotionallypairedMusicandImage JialingZou,JiahaoMei,GuangzeYe,TianyuHuai,QiweiShen,andDaoguo
Dong.2023.EMID:AnEmotionalAlignedDatasetinAudio-VisualModality.
Dataset(EMID),anoveldatasetdesignedfortheemotionalmatch-
InProceedingsofthe1stInternationalWorkshoponMultimediaContent
ingofmusicandimages,tofacilitateauditory-visualcross-modal
GenerationandEvaluation:NewMethodsandPractice(McGE’23),October
taskssuchasgenerationandretrieval.Unlikeexistingapproaches 29,2023,Ottawa,ON,Canada.ACM,NewYork,NY,USA,8pages.https:
thatprimarilyfocusonsemanticcorrelationsorroughlydivided
//doi.org/10.1145/3607541.3616821
emotional relations, EMID emphasizes the significance of emo-
tionalconsistencybetweenmusicandimagesusinganadvanced
13-dimensionemotionalmodel.Byincorporatingemotionalalign- 1 INTRODUCTION
mentintothedataset,itaimstoestablishpairsthatcloselyalign
GuidedImageryandMusic(GIM)isdefinedasacomprehensive
with human perceptual understanding, thereby raising the per-
therapy integrating professional knowledge of psychology, bio-
formance of auditory-visual cross-modal tasks. We also design
medicine,andaesthetics[3,4].Throughassociationsandmetaphors
asupplementalmodulenamedEMI-Adaptertooptimizeexisting
betweenmusicandimages,patientscangaindeeperinsightinto
cross-modalalignmentmethods.Tovalidatetheeffectivenessofthe
and explore their inner world, which helps to foster emotional
EMID,weconductapsychologicalexperiment,whichhasdemon-
expressionandimprovetherapeuticresults[2,37].However,the
stratedthatconsideringtheemotionalrelationshipbetweenthe
currentGIMschemeexhibitscertainlimitations,includingimpre-
twomodalitieseffectivelyimprovestheaccuracyofmatchingin
cisetargetingthatlacksofpathologicalspecificity,prolongedand
abstractperspective.Thisresearchlaysthefoundationforfuture
labor-intensiveproceduresthatresultinhighannotationcosts,and
cross-modalresearchindomainssuchaspsychotherapyandcon-
soon.
tributestoadvancingtheunderstandingandutilizationofemo-
Recently,theemergenceofArtificialIntelligenceGeneratedCon-
tionsincross-modalalignment.TheEMIDdatasetisavailableat
tent(AIGC)hasinstigateddisruptivetransformationsinvarious
https://github.com/ecnu-aigc/EMID.
cross-modalinteractionscenarios.AIGCreferstoarisingtechnol-
ogythatutilizesadvancedalgorithmsanddeeplearningmethods
CCSCONCEPTS
tomatchorcreateawiderangeoftextual,visual,auditory,and
•Appliedcomputing→Mediaarts;•Informationsystems multi-mediacontenttailoredtohumandemands[5].Fromanin-
→Multimediastreaming. tuitive standpoint, AIGC offers a viable avenue to mitigate the
costsassociatedwithmusicandimagecollectionandannotation
KEYWORDS
inGIM.Furthermore,ithasthepotentialtoprovidepatientswith
Music-ImageDataset,EmotionalMatching,Cross-modalAlignment aseamlessandcaptivatingaudio-visualexperience,ultimatelyen-
hancingtheeffectivenessofthetreatment.Nevertheless,tothebest
∗Bothauthorscontributedequallytothisresearch. ofourknowledge,littleexistingresearchorimplementationhas
†Correspondingauthor. beenfoundthatappliesAIGCtechnologyspecificallytothefield
ofpsychotherapy.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
Actually,theaforementionedphenomenoncanbeattributedto
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation thecurrentcross-modalalignmentapproachesreliedonbyAIGC,
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe whichprimarilyfocusonsemanticrelation,ignoringemotionaland
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
artisticlevelmatching,asshowninFigure1.Animageofalaughing
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. girlcaneasilycorrespondtoanaudioofgiggling,butaphotoof
McGE’23,October29,2023,Ottawa,ON,Canada. landscapewithoutanysoundcluemaybechallengingtoaccessa
©2023Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
suitablematchatthesemanticlevel.Meanwhile,itischallengingto
ACMISBN979-8-4007-0278-5/23/10...$15.00
https://doi.org/10.1145/3607541.3616821 findappropriatemusicthatmatchesaccordantartisticconception
4202
guA
9
]MM.sc[
2v22670.8032:viXra

### Page 2

McGE’23,October29,2023,Ottawa,ON,Canada. JialingZouetal.
ofboththemwithoutanyexplicitlabelsorguidance.Therefore,
thisarticleaimstoproposeamusic-imagedatasetthatincorporates
emotionalinformation,inordertofulfillthefollowingobjectives:
(1)updatetheoriginalcross-modalalignmentpatterntoproject
emotionalfeaturesintothesharedlatentspace.Thisadjustmentis
helpfultoaddresschallengesrelatedtodatacollectionandannota-
tionrelianceaswell,(2)providedatasupportfortrainingexisting
cross-modal generation and retrieval models. This dataset goes
beyondsimplisticandsuperficialsemanticbindingandtakesinto
accounttheemotionalassociationsbetweenvisualandauditory
modalities,enhancingtheapplicabilityoftheproposeddatasetin
thefieldofpsychotherapy.
Tobemorespecific,ourworkmakesthefollowingkeycontribu-
tions:
• We introduce a high-quality Emotionally paired Music and
Figure 1: Defect of current cross-modal alignment ap-
ImageDataset(EMID),comprisingmorethan30kdatapairs
proaches,ignoringtheemotionalrelationsofmusicandim-
accompaniedbyabundantemotionalannotations.
ages.
• Wepioneertheattempttoaligntwodistinctmodalitiesbased
onemotions.Ourapproachinvolvesextractingsemanticsfrom
Furthermore,inscenarioswhereaudioissubstitutedwithstruc-
sourcedatatoformrawimage-musicpairs,subsequentlyde-
turedandcreativemusic,theoriginalsemanticalignmentscheme
terminingtheoptimalmatchesbyprojectingeachcandidate
[40]becomesobsolete.Nonetheless,varioussolutionshavebeen
ontotheemotionalcoordinatespace,therebymodifyingembed-
proposedtoaddressthisissue.Forexample,MusicCaps[1]man-
dedrepresentationsfromoriginalcross-modaljointembedding
uallyannotatedmusicsegmentsof5,521piecesofAudioSet[11],
space.
eachwithanEnglishtextdescriptionwrittenbytenprofessional
• Ameticulouslydesignedprofessionalpsychologicalexperiment musicians;Huangetal.[18]proposesadatasetcalledMuLaMCap,
isconductedtoassessthedataset’squalityandaffirmthepivotal whichleveragesapre-trainedjointmusic-textmodelMULAN[17]
roleofemotionsinmodalalignment. toannotatemusicsegmentsinAudioSet[11]basedonmusicde-
scriptionsgeneratedbyLLMand200kmusicdescriptivesentences
Overall,theEMIDwillserveasasolidfoundationforAIGC’s andlabelsfromMusicCaps[1],retainingover400kmusic-textpairs.
applicationinpsychotherapy-relatedwork.Itsavailabilitypaves Theapproachofemotionalalignment,however,betterconforms
thewayfornoveladvancementsinmusicandimageconditional tohumancognition[24,41].Nevertheless,therehavebeenrarere-
generationandretrieval,takingaclosersteptohumancognition searchontheemotionalalignmentbetweenimagesandmusic,with
andunlockingnewpossibilitiesandopportunities. oneofthesolelyknownmusic-imagepaireddatasetbasedonartis-
ticconception,theBOPdataset[8],whichartificiallyannotates3k+
imagesand1.5k+pianopiecesbasedoncreationbackgroundand
2 RELATEDWORK
emotionsconveyed.Nonetheless,themanualannotationscheme
2.1 Cross-modalDataset obstructsdataexpansion,andtherichnessofsourcedataisex-
pectedtobeimproved.Therefore,thereisanurgentdemandfora
Thelatestadvancementsincross-modaldatasetdevelopmentlabor
music-imagematchingdataset.
primarilyfocusonobtainingimages,audio,orvideosbasedon
textualinputs(text-to-image[7,26,30,34,35];text-toaudio/videos
2.2 Cross-modalTask
[9,11,19])consistingoflabels,descriptiveinformation,evaluation
content,etc.,whichareavailablethroughouttheinternetandcan Cross-modaltasksinvolvinggeneration,retrieval,andeditingare
becollectedbyautomatedtoolswithease.Themajorityoftextsec- predominantlyaddressedusingstate-of-the-artframeworkssuch
tionsfromexistingcross-modaldatasetsarecomposedoflimited asGAN[13],VQ-VAE[31,42],andDiffusionmodels[16,32].The
tagsormonotonoussentences[29],hinderingtheestablishmentof recentrapiddevelopmentofAIGChasgarneredsubstantialatten-
strongsensoryimpactsthroughtheircollocationwithimagesor tionfrombothacademiaandindustry.Researchefforts[22,23,25]
audio.Toovercomethislimitation,effortsarebeingmadetocollect havebeendirectedtowardsvisualeditingguidedbysoundandvice
moreimpressiveaudio-visualcombinations.Initially,videosand versa,takingadvantageofconditionalguidancetofacilitatetasks
audioareoftenpairednaturally,suchasthehugedatasetAudioSet likestyletransfer,localfine-tuning,inpaintingandsuper-resolution
[11],whichischaracterizedasanobject-orientedvideodataset whilepreservingtheintegrityoftheoriginalcontent.
organizedbyaudioevents,usingameticulouslyconstructedhier- Regardinggenerativework,thereisstillampleroomforadvance-
archicalontologyof632distinctaudioclasses,includingatleast ment.Earlygenerativeworksfocusonrestoringsoundofsilent
100instancesof485audioeventclasses.However,plainmatching instrument-playingvideosbasedontheperformer’sbodymove-
approachmayleadtoissuessuchasmisalignmentbetweenvideo mentsorgestures[10,38].Subsequentjobsattempttogenerate
framesandaudio,highdatanoiseandclassificationerrors[9]. correspondingaudiobasedonimagesorvideosofanimals,water

### Page 3

EMID:AnEmotionalAlignedDatasetinAudio-VisualModality McGE’23,October29,2023,Ottawa,ON,Canada.
Arousal
EMI-Adapter
Music
I1 I2 I3 Ij IN YT NCF …
(1) IM
E
A
n
G
c
E
o
B
de
IN
r
D M1 M1·I1 M1·I2M1·I3 ··· M1·IN (2) (3) (4) BMF
M2 M2·I1 M2·I2M2·I3 ··· M2·IN Valence EMID Dataset SVDpp Im … age
M3 M3·I1 M3·I2M3·I3 ··· M3·IN
Mi ··· ··· ··· ··· ···
C
Th
a
e
n d
it
i
h
d
m
at
u
e
s
i
i
m
c
age
New
embeddings
MN MN·I1MN·I2MN·I3··· MN·IN Selected image for pairing
Cosine distance of image and music
X Similarity score S
Figure2:TheconstructionprocessofEMIDincludesthefollowingsteps.(1)UseImageBindtogetthesemanticembeddingfor
imagesandmusicasmatrix𝑋 and𝑌.Thenwegetthesimilarityscorematrixthrough𝑆 =𝑆𝑜𝑓𝑡𝑚𝑎𝑥(𝑋 ·𝑌𝑇),(2)select𝐾 images
withthehighestscores(inredcolor)from𝑖 𝑡ℎ rowof𝑆asthecandidateimage-setforthe𝑖 𝑡ℎ music,thencalculatethecosine
distanceofeachmusicclipanditsimage-candidatesinemotionalvalence-arousalspace,(3)generateEMIDthroughweighted
summationofsemanticscoresandemotionalscores,remaining𝑚best-matchingpairs,(4)designalightweightcomponent,
EMI-Adapter,whichcanmergeemotionalfeaturesintothejointembeddingspaceaftertrainingbasedontheEMID.
flow,knockingactionsandmore[33,36,45].However,thistypeof emotion.Forexample,thecombinationofadagiotempo,deeptones,
audiooftenamountstoasemanticrepetitionoftheimage,lacking subduedharmonies,andgentlerhythmscanevokeapoignantsense
imaginativeandartisticaudio-visualelements.Toovercomethis ofsadness(e.g.thesecondmovementofDvorak’sNewWorldsym-
constraint,recentworkshaveexplorednovelmannerstointroduce phony).Ontheotherhand,fastrhythms,strongpercussion,and
moreimaginativeandartisticideasintothegenerationprocess. livelymelodiescanconveyfeelingsofhappinessandjoy(e.g.the
Fanetal.[8]designsamulti-modalarchitecturenamedConchShell firstmovementofBach’sBrandenburgConcerto).
based on GAN networks [13], which can generate piano music Toacquireadiverserangeofemotionaldata,werefertothework
clipsofaround8secondsconditionedoninputlandscapeimages. conductedbyCowenetal.[6],fromwhosevisualizationwebpage1
Surísetal.[39]proposeanewmethodforrecommendingmusic wecrawl1,841musicclips,eachaccompaniedbyrichemotionalan-
tracksthatalignwithagivenvideo(orviceversa),withoutextra notations.Thesemusicclipsencompassvariousgenres,including
relianceonmanualannotation,establishingaconnectionbetween rock,folk,jazz,classical,wind,andheavymetal,coveringabroad
theaudio-visualpairsatarhythmicandartisticlevel. spectrumofemotionaldimensions,suchasamusing,annoying,anx-
Trainingmulti-modaldatarepresentationsthatcanbealignedin ious/tense,beautiful,calm/relaxing,dreamy,energizing/pump-up,
latentspaceshasbeenprovedtoofferrobustsupportforconditional erotic/desirous,indignant/defiant,joyful/cheerful,sad/depressing,
generationtasks[12,27,40].However,thereisstillagiantresearch scary/fearfulandtriumphant/heroicthatcontains13emotionsin
gapinthedomainofdirectemotionalalignmentspecificallyfocused total,whicharerepresentedbyletters𝐴to𝑀inFigure5,Figure6
onmusicandimages.Therefore,theEMIDproposedinthisarticle andTable2.
aimstolaythefoundationforthisspecificaspectofresearchand Toestablishastandardizedrepresentationofemotions,weadopt
development. theValence-ArousalspacetheoryproposedbyHanjalic[14].In
thistheory,valenceisusedtomeasurethepositiveornegative
3 THEPROPOSEDDATASET:EMID aspects of music emotions, while arousal describes the level of
emotionalstimulation.Forimages,weutilizethe8-dimensional
WeconstructtheEMID,ahigh-qualitycollectionofmusic-image
emotionclassificationimagedataproposedbyYouetal.[44].This
pairstakingaccountofaffectiveaspects.TheEMIDensuresase-
classificationsystemcompriseseightcategories:happiness,awe,
manticclosenessbetweenmusicandimageswhileevokingsimilar
contentment,surprise,anger,disgust,fear,andsadness.Toestablish
affectiveexperiencesandestablishingaunifiedspaceofimagina-
anemotionalconnectionbetweenmusicandimages,weexertthe
tion.Inthefollowingsections,wewillprovideacomprehensive
NRC-VAD-Lexicon[28]dictionarytoselectthreesemanticallysim-
anddetaileddescriptionoftheemotionalalignmentprocess.
ilarwordsforeachimageclassification,whichserveasemotional
descriptionsforthatparticularcategory.Subsequently,wequery
3.1 EmotionalAlignmentProcess
thedictionarytoobtainthe<V,A>coordinatescorrespondingto
TheautomatedconstructionprocessoftheEMIDinvolvesthree theseeightclassifications(showninFigure3a)andcalculatetheir
distinctphases:(1)acquisitionofemotionalfeatures,(2)formation averages as the approximate <V, A> coordinates for the images
ofcandidatepairs,and(3)injectionofemotionalinformation.The withineachcategory(showninFigure3b).
overallpipelineisillustratedinFigure2. It is worth noting that individual images are not specifically
assignedwithindependentcoordinates,asthepresenceofclassifi-
3.1.1 AcquisitionofEmotionalFeatures. Bothimagesandmusic
cationlabelsalreadyconstrainanestimatedrangeofeachsample
havetheabilitytoconveyintricateemotions,althoughtheirmeth-
withintheValence-Arousalspace.Byemployingtheclassification
odsofevokingfeelingsandintensitiesdiffer.Asafirststep,we
aimtoextractcomparableemotionalinformationfromindividual
samplesofmusicandimages.Eachmusicclipconveysadistinctive 1https://www.ocf.berkeley.edu/~acowen/music.html

### Page 4

McGE’23,October29,2023,Ottawa,ON,Canada. JialingZouetal.
(a)Foreachoftheeightemotionalcategories,weselectthree (b)ToobtaintheapproximateValence-Arousalcoordinatesfor
semanticallysimilarwordsfromtheNRC-VAD-Lexicondictio- everyimagecategory,wecalculatethemeanvaluesoftheemo-
naryasemotionaldescriptions,whicharemarkedwiththesame tionaldescriptioncoordinatesinFigure3aforthemandmap
colorinthefigure.NotethattherangeofValence-Arousalvalues thesevaluesto(−1,1).
is(0,1).
Figure3:Valence-ArousalcoordinatesofeightemotionalcategoriesfromtheNRC-VAD-Lexicon[28]dictionaryandthefinal
calculatedvalues
coordinatestoindicatethelocationofsamplepoints,wedramati- Table1:PerformanceofdifferentEMI-Adapters.Thebest
callyreducethecomputationalexpensesassociatedwithmeasuring resultsareviewedinbold.
emotionaldistancesinsubsequentanalysis,whilealsominimizing
anyunfavorableinfluenceontheultimatematchingefficacy.
HR@10 NDGC@10
3.1.2 FormationofCandidatePairs. Basedonpreviouswork,we NCF 0.580 0.404
initiallypickseveralmatchedimagesforeachmusicsamplebased BMF 0.580 0.410
onsemanticsimilaritiestocreateaninitialdataset.Specifically,we SVD 0.602 0.427
employthecross-modalretrievalmodelImageBind[12]tocalculate
thesemanticmatricesforbothmusicandimagedatasets,recording
as𝑋 ∈ 𝑅𝑁𝑀∗𝑑,𝑌 ∈ 𝑅𝑁𝐼∗𝑑 respectively, Where 𝑁 𝑀 ,𝑁 𝐼 refer to
the number of music and image samples, and𝑑 represents the 𝑇 forpairingasfollows:
dimensionoflatentspacethatpertainstoImageBind.Byperforming
matrixmultiplication,weattainasimilarityscorebetweeneach 𝑇 =𝛼·𝑆+(1−𝛼)·𝐸 (2)
musicsampleandimagesample,resultinginasemanticsimilarity
matrixS.Thespecificcalculationprocessisasfollow:
Thismatrixdeterminesthecompatibilitybetweenmusicandimage
samples.Toproduceasetof𝑁
𝑀
∗𝑚musicimagepairs,wechoose
𝑆 =𝑆𝑜𝑓𝑡𝑚𝑎𝑥(𝑋 ·𝑌𝑇 ) (1) 𝑚imagesforeachmusicsamplebasedonthescorerankingfrom
highesttolowest.
bet
E
w
a
e
c
e
h
n
e
t
l
h
em
e𝑖
e
𝑡
n
ℎ
t
m
𝑆 𝑖
u
𝑗
si
=
cse
∥
g
𝑀
m
𝑀 𝑖∥ 𝑖
e
· ·𝐼
n
∥ 𝑗 𝐼
t
𝑗∥
an
r
d
efl
th
e
e
cts
𝑗 𝑡ℎ
th
i
e
m
s
a
e
g
m
e.
a
U
nt
t
i
i
c
liz
d
i
i
n
s
g
ta
t
n
h
c
i
e
s ble
T
i
o
n
e
t
n
h
s
e
u
e
r
m
et
b
h
e
a
d
t
d
t
i
h
n
e
g
n
s
e
p
w
ac
ly
e,
m
a
a
t
t
i
c
n
h
y
ed
em
sa
o
m
ti
p
o
l
n
e
a
s
l
a
f
r
u
e
s
a
io
s
n
cl
p
o
l
s
u
e
g
a
in
s
,
p
E
o
M
ss
I
i
-
-
matrix,weselect𝐾 (setting𝐾 = 100intheEMID)imageswith Adapter,isdesignedtoregulatetheencodingofImageBindand
the highest semantic relevance for each music sample, thereby incorporateemotionalinformationintothesharedlatentspace.We
settingupcandidatemusic-imagepairs.Notethatthisrawdataset simultaneouslytrainseverallightweightnetworkmodules,compris-
solelyreliesonsimplesemanticassociations,whichmayresultin ingofNCF[15],BMF[21],andSVDpp[20],asadapterstopromote
suboptimalmatchingperformance.Tofurthertacklethisissue,we cross-modalalignmentbasedonexistingmusic-imagepairs.Re-
considertheintegrationofemotionalinformation. sultspresentinTable1andFigure4illustratetheperformanceof
thedifferentEMI-Adapterplugins.
3.1.3 InjectionofEmotionalInformation. Finally,weadoptasim- Moreover,theEMI-Adapterhasthecapabilitytocapturemore
ilarmethodasabovetocalculatethe<V,A>coordinatesofeach comprehensiveemotionalinformationfromtheinputmodeslever-
musicsampleandthecosinedistancefromimagesinitscandi- agingthefoundationofImageBind,eliminatingtherelianceon
datesetinValence-Arousalspacesoastoacquiretheemotional additionalemotionalannotationsprovidedbythesourcesamples.
similaritymatrix𝐸betweenmusicandalternativeimages.Then Thissignificantadvancementwillgreatlyfacilitatethefutureex-
weaddsemanticandemotionalsimilaritymatricesbyadjusting pansionoftheEMID,enablingittoencompassabroaderrangeof
appropriateweightparameters𝛼 togeneratethefinalscorematrix emotionalcontent.

### Page 5

EMID:AnEmotionalAlignedDatasetinAudio-VisualModality McGE’23,October29,2023,Ottawa,ON,Canada.
(a)Curveoftrainingloss (b)CurveofHRscores (c)CurveofNDCGscores
Figure4:Theabovecurvesdisplaythevariationoftraininglossandevaluationresultsin50iterationsforthreetypesof
networks,with@10indicatingthattop-10imageswillberecommended.Atthispoint,theEMIDversionusedfortrainingis
takenas𝑚=3and𝛼 =0.6.
Table2:Thequantitiesofmusicdatasetbefore/afterexpandingandtheaverageofmanuallysetthresholdson13emotions.
Emotion A B C D E F G H I J K L M Total
Beforeexpanding 45 80 54 131 306 174 367 86 36 124 129 105 199 1836
Averagethreshold 0.611 0.606 0.559 0.620 0.707 0.632 0.751 0.661 0.610 0.669 0.603 0.570 0.628 -
Afterexpanding 255 545 320 771 1531 889 1832 1036 323 1014 799 484 939 10738
3.2 FilteringandExpansionofMaterials secondsandastepsizeof1second.Basedontheideaofdynamic
3.2.1 Data Filtering. To keep data balance, we exclude several programming,weobtainthesimilarityscore(rangedfrom0to
musicsampleswithadurationoflessthan3.7secondsfromthe 1)fromthecross-similaritymatrix.Subsequently,wedetermine
originallycrawledmusicpieces,leavingbehindafinaldatasetof the selection of new music clips by setting a manually defined
1,836musicsampleswithassociatedtags,amongwhich98%ofthe thresholdtothesimilarityscoreofeachmusic,primarilyaiming
musicclipsheldadurationof4.8sto5.2s,asthelongestis9.4sand todifferfromtheoriginalonesintermsofauditorycontentwhile
theshortestis3.7s.Regardingtheimagedataset,forthepurposeof reservingsimilaraffectivity.Thesenewclipsareassignedthesame
psychotherapy,wedecidetoexcludethedisgustingcategory,which labelsasthecorrespondingsourcesamples.Thequantitiesofthe
containselementsofthreat,violence,andblood.Inaddition,to musicdatasetbeforeandafterexpansionarepresentedinTable2,
avoidthenegativeimpactofimagequalityonpairing,wemanually andtheultimatelyexpandedmusicdatasetinvolves10,738music
definethresholdsforthemeanandvarianceofimagebrightness. clips.
Imagesfallingbelowthesethresholdsareconsideredinvalidorof
lowqualityandthenfilteredout.Furthermore,weemploytheGIT 3.3 DatasetStatistics
model[43]togeneratetextdescriptionsforallimages.Basedon
Theultimatedatasetcomprises32,214pairsofimagesandmusic
thesecaptions,weremoveimagesthatareprimarilycharacterized
(setting𝑚=3).TheEMIDisaccompaniedwithrichannotationsas
bytextualinformationratherthanvisualcontent,aswellasphotos
themusicsamplesareequippedwiththreetypesoflabels:genre,
of bands or singers performing on stage as far as possible, for
emotion,andsentiment,amongwhichthegenrelabelsclassifythe
thesakeofescapingfromtheimpedimentofstrongsemanticsto
musicinto13emotionaldimensions,whilethesentimentlabels
emotionalconnection.Afterthesefilteringsteps,thefinalretained
provide a detailed breakdown of the percentage distribution of
imagedatasetconsistsof19,901pieces.
eachmusicsampleacrossdifferentemotionaldimensions,andthe
3.2.2 DataExpansion. Togathermoreavailabledata,weexpand emotionlabelsembodyanother11sensorydimensionvaluesthat
themusicsamplesbyleveragingtheAPIofthemusiclisteningand quantifythesubjectiveexperienceevokedbythemusic.Onthe
recognitionplatform2.Thisallowsustoobtain1,361integralmusic otherhand,theimagesamplesaremarkedwithcategorylabels
trackscorrespondingtofragmentsinouroriginaldataset.Next, andbriefcontentdescriptions.Thisinformationassistsinfurther
usingthelibrosalibrary3,wecomputethecross-similaritymatrix understandingtheintricateconnectionsbetweenthetwomodali-
betweenthemusicclipsintheexistingdatasetandoriginalmusic ties.ThelocationofpairsfromtheEMIDinthecross-emotional
tracksbyemployingaslidingwindowapproachwithalengthof5 spaceofmusicandimagesbeforeandafterconsideringemotional
alignmentisshowninthefollowingFigure5.Itcanbeobserved
2https://audd.io/ thatthedistributionofdataismorebalancedondifferentemotional
3https://github.com/librosa/librosa dimensionsafterfusingeffectiveinformation.

### Page 6

McGE’23,October29,2023,Ottawa,ON,Canada. JialingZouetal.
(a) (b)
Figure5:Distributionofmusic-imagepairsintheEMIDwithout(𝛼 =1)andwith(𝛼 =0.6)emotionalalignment.
Table3:AccuracyofMusic-ImageMatchingStudy.Thebest
resultsareviewedinbold.
Max Min Mean Variance
RandomMatch
Music-to-Image 0.363 0.176 0.252 0.002
Image-to-Music 0.341 0.132 0.247 0.002
Overall 0.330 0.176 0.250 0.001
BeforeEmotionalAligned
Music-to-Image 0.604 0.429 0.516 0.005
Image-to-Music 0.725 0.462 0.575 0.012
Figure6:PairaccuracyofImage-to-MusicVerificationand
Overall 0.621 0.445 0.546 0.005
Music-to-ImageVerificationonthe13emotions,letterAto
AfterEmotionalAligned(Ours) Mstandsfordifferentemotions.
Music-to-Image 0.648 0.407 0.556 0.003
Image-to-Music 0.692 0.352 0.563 0.011
theirpersonalfeelingofmusicexpressionafterlisteningtothemu-
Overall 0.659 0.462 0.560 0.005
sicclip.Onlyoneoftheoptionsisthecorrectanswerdetermined
bytheEMID(i.e.thebestmatchestimatedfromthescorematrix
insection3.1.3),andtheremainingthreeimagesareconsidered
4 ASSESSMENTEXPERIMENT as interference items. All options belong to different emotional
categories.
4.1 ExperimentalProtocol
Image-to-MusicVerification.Eachsubjectissupposedtocom-
Preview.ToassesstheefficacyoftheEMID,weconducttwotypes plete91(7×13)trialsas7setsofmatchedimagesfrom13emotional
ofpsychologicalexperiments:music-to-imagevalidationandimage-
categoriesareselectedrespectivelyasstimulusmaterials.Ineach
to-musicvalidation.Inordertoexplorewhetherintensifyingemo-
trialcorrespondingtooneimageset,subjectswillbepresentedwith
tionalconnectionscaneffectivelysupportcross-modalalignment threeimagesusedfordescribingthesamemusicclip(i.e.𝑚images
research,subjectsareinstructedtodetermineoneoptimalmatch
thatultimatelypairwiththemusicclipinsection3.1.3,setting
withtheassignedexamplefromtheothermodalityaccordingto 𝑚 = 3).Afterobservingthreeimages,subjectsareinformedto
theirsubjectiveintuition,
choosethemostsuitablemusicclipfromthefouroptionsbasedon
theirpersonalfeelingofimageexpression.Thesettingsforcorrect
4.1.1 Subjects. Thestudyinvolves50subjectsfromEastChina
answersandinterferenceitemsarethesameasabove.
NormalUniversity,comprising29malesand21females.Theaver-
AblationExperiment.Tofurtherprobetheeffectofemotions
ageageofthesubjectsisapproximately21yearsold.Allsubjects
onalignmentwork,wealsodesignanadditionalsmall-scaleab-
areright-handed,withnormalnakedorcorrectedvision.
lationexperimentforcomparison.Tobemorespecific,webuild
4.1.2 Design. Music-to-Image Verification. Each subject is sup- avariantoftheEMIDbysettingthe𝛼 =1informula2,thuswe
posedtocomplete91(7×13)trialsas7musicclipsfrom13emo- attainadatasetmerelyconsideringImageBindsemanticmatching.
tionalcategoriesareselectedrespectivelyasstimulusmaterials.In Byadoptingthesamepartitioningschemeutilizedintheprevious
eachtrialcorrespondingtoonemusicclip,subjectsareinformed experiment,wecancomparetheimpactofimagepairingbefore
tochoosethemostsuitableimagefromthefouroptionsbasedon andafteremotionalalignmentonfinalaccuracywhilemaintaining

### Page 7

EMID:AnEmotionalAlignedDatasetinAudio-VisualModality McGE’23,October29,2023,Ottawa,ON,Canada.
consistentmusiccoverage.Atotalof15subjectsparticipatedin similaremotionsmayalsoaffecttheaccuracyofclassification.To
thisexperiment. gainbroaderinsightsintotheseissues,ourfutureresearchwill
Additionally,inordertoverifythatsemanticalignmentalsoplays furtherexplorethereasonsbehindtheseaccuracydifferencesand
acrucialroleasthefirststepofourwork,wesimulaterandom addressingthesechallenges.
matchingscenariosfortwotypesofvalidations(actuallyachieved
byrandomlygeneratinguserresponses).Theinterferenceterm 5 CONCLUSION
settings in the ablation experiment remain consistent with the
Inthispaper,weproposedanemotionalalignedmusic-imagepaired
previousexperiment.
dataset named EMID, which considers the sentimental connec-
4.1.3 Evaluation. Basedontheresponsedataofdifferentsubjects, tionsofdifferentmodalitiesinadditiontosemanticrelations.More-
wecalculatetheseparateaccuracyandoverallaccuracyofmusic-to- over,weenhancedtheexistingcross-modalalignmentapproaches
imageandimage-to-musicexperiments.Additionally,weconduct throughasimplemodulecalledEMI-adapter,whichcontributesto
ananalysistoinvestigatethedistributionofaccuracyacrossdiffer- effectivelycapturingandintegratingemotionalinformationfrom
entmusicemotionalcategories.Notethataccuracyreferstothe theindicatedsamplesandprojectingitintothejointembedding
ratioofthenumberofconsistentsituationsbetweenthesubjects’ space.Intheend,thepsychologicalexperimentdemonstratedthat
answersandpairsintheEMIDtothetotalnumberofvalidation the matching pattern in the EMID is more in line with human
questions. cognitioncomparedtotraditionalschemes,andalsomoresuitable
forcross-modaltasksinthefieldofpsychotherapy.Currently,our
4.2 PerformanceAnalysis datasetstillsuffersissueslikeinsufficientscale,weakmusicstruc-
ture,andlimiteddatacoverage.Thesechallengeswillbefurther
Thestatisticalinformationofthesubjectdatacollectedispresented
discussedandaddressedinourfutureresearch.
inTable3.Theresultsshowthatthemusic-imagematchingwith
emotionalalignmentoutperformsotherschemesinoverallvalida-
REFERENCES
tion.Tobemorespecific,simulatedrandommatchingconformsto
[1] AndreaAgostinelli,TimoIDenk,ZalánBorsos,JesseEngel,MauroVerzetti,An-
ourconjecture,withanoverallmeanaccuracyof0.25.Semantic
toineCaillon,QingqingHuang,ArenJansen,AdamRoberts,MarcoTagliasacchi,
matchingbasedonImageBindperformssignificantlybetterthan etal.2023.Musiclm:Generatingmusicfromtext.arXivpreprintarXiv:2301.11325
randompairing,withavarianceof0.005,themaximumaccuracy (2023).
[2] KatRAgres,RebeccaSSchaefer,AnjaVolk,SusanvanHooren,AndreHolzapfel,
is0.621,theminimumis0.445,andthemeanis0.546.Afteremo-
SimoneDallaBella,MeinardMüller,MartinaDeWitte,DorienHerremans,Rafael
tionalalignment,thematchingaccuracyimprovesfurtherinboth RamirezMelendez,etal.2021. Music,computing,andhealth:aroadmapfor
music-to-imagevalidationandoverallexperiment,asthegeneral thecurrentandfuturerolesofmusictechnologyforhealthcareandwell-being.
Music&Science4(2021),2059204321997709.
assessmenthasavarianceof0.005,withamaximumaccuracyof [3] HelenLindquistBonny.1989.Soundassymbol:Guidedimageryandmusicin
0.659,aminimumof0.462,andameanof0.560.However,inimage- clinicalpractice.MusicTherapyPerspectives6,1(1989),7–10.
[4] HelenLBonny.2010.Musicpsychotherapy:Guidedimageryandmusic.InVoices:
to-musicverification,theeffectafteremotionalalignmentisslightly AWorldForumforMusicTherapy,Vol.10.
inferiortobeforealignment.Thismaybeduetothestrongseman- [5] YihanCao,SiyuLi,YixinLiu,ZhilingYan,YutongDai,PhilipSYu,andLichao
tics presented in the three images selected through ImageBind, Sun.2023.Acomprehensivesurveyofai-generatedcontent(aigc):Ahistoryof
generativeaifromgantochatgpt.arXivpreprintarXiv:2303.04226(2023).
whichcandefinitelycorrespondtospecificbackgroundsoundsor
[6] AlanSCowen,XiaFang,DisaSauter,andDacherKeltner.2020. Whatmusic
instrumentsinthemusic.Butinmusic-to-imagevalidationwhich makesusfeel:Atleast13dimensionsorganizesubjectiveexperiencesassociated
picksonesuitableimagebasedonamoreabstractformofmusic, withmusicacrossdifferentcultures. ProceedingsoftheNationalAcademyof
Sciences117,4(2020),1924–1934.
bothsemanticandemotionalfactorswillbetakenintoaccountas [7] JiaDeng,WeiDong,RichardSocher,Li-JiaLi,KaiLi,andLiFei-Fei.2009.Imagenet:
imagesandmusicusedinpsychotherapyaresupposedtoevoke Alarge-scalehierarchicalimagedatabase.In2009IEEEconferenceoncomputer
visionandpatternrecognition.Ieee,248–255.
strongemotionsratherthanhavingexplicitsemantics.
[8] WanpengFan,YuanzhiSu,andYuxinHuang.2022.ConchShell:AGenerative
Figure6presentsthattheaccuracydistributionofmusic-image AdversarialNetworksthatTurnsPicturesintoPianoMusic. arXivpreprint
matchingintheEMIDtendstoaverageasawholeindifferentmusic
arXiv:2210.05076(2022).
[9] EduardoFonseca,XavierFavory,JordiPons,FredericFont,andXavierSerra.
emotioncategories.Insomecategories,therearenotabledifferences 2022.FSD50K:AnOpenDatasetofHuman-LabeledSoundEvents.IEEE/ACM
inaccuracybetweendifferentvalidationdirections,particularlyin TransactionsonAudio,Speech,andLanguageProcessing30(2022),829–852. https:
categories𝐶(anxious/tense)and𝐽 (joyful/cheerful).Inthecaseof //doi.org/10.1109/TASLP.2021.3133208
[10] ChuangGan,DengHuang,PeihaoChen,JoshuaBTenenbaum,andAntonio
theformercategory,theaccuracyofmusic-to-imageverificationis Torralba.2020.Foleymusic:Learningtogeneratemusicfromvideos.InComputer
significantlyhighercomparedtotheotherdirection.Thisdifference Vision–ECCV2020:16thEuropeanConference,Glasgow,UK,August23–28,2020,
maybeattributedtotheremovalofthedisgustingclassificationin Proceedings,PartXI16.Springer,758–775.
[11] JortFGemmeke,DanielPWEllis,DylanFreedman,ArenJansen,WadeLawrence,
thesourceimagedatasetthatisclosesttocategory𝐶atthesensory
RChanningMoore,ManojPlakal,andMarvinRitter.2017.Audioset:Anontology
level.Ontheotherhand,thelatterisexactlytheopposite,possibly
andhuman-labeleddatasetforaudioevents.In2017IEEEinternationalconference
duetothelargescaleofamusement classificationinthesource
onacoustics,speechandsignalprocessing(ICASSP).IEEE,776–780.
[12] RohitGirdhar,AlaaeldinEl-Nouby,ZhuangLiu,MannatSingh,KalyanVasudev
imagedataset,whichpossessessimilarfeelingstocategory𝐽. Alwala,ArmandJoulin,andIshanMisra.2023.Imagebind:Oneembeddingspace
Furthermore,wenoticethatthevalidationaccuracyofcategory𝐼 tobindthemall.InProceedingsoftheIEEE/CVFConferenceonComputerVision
andPatternRecognition.15180–15190.
(indignant/defiant)isrelativelyhigher,whilecategory𝐵(annoying)
[13] IanGoodfellow,JeanPouget-Abadie,MehdiMirza,BingXu,DavidWarde-Farley,
andcategory𝐻 (erotic/desirous)tendtohaveloweraccuracy.This SherjilOzair,AaronCourville,andYoshuaBengio.2020.Generativeadversarial
networks.Commun.ACM63,11(2020),139–144.
patternmaybeinfluencedbytheincompleteequilibriumdistribu-
[14] AlanHanjalicandLi-QunXu.2005.Affectivevideocontentrepresentationand
tionofthesourcedataset.Additionally,theinterferencebetween modeling.IEEEtransactionsonmultimedia7,1(2005),143–154.

### Page 8

McGE’23,October29,2023,Ottawa,ON,Canada. JialingZouetal.
[15] XiangnanHe,LiziLiao,HanwangZhang,LiqiangNie,XiaHu,andTat-Seng etal.2021.Learningtransferablevisualmodelsfromnaturallanguagesupervision.
Chua.2017.Neuralcollaborativefiltering.InProceedingsofthe26thinternational InInternationalconferenceonmachinelearning.PMLR,8748–8763.
conferenceonworldwideweb.173–182. [31] AliRazavi,AaronVandenOord,andOriolVinyals.2019.Generatingdiverse
[16] JonathanHo,AjayJain,andPieterAbbeel.2020.Denoisingdiffusionprobabilistic high-fidelityimageswithvq-vae-2.Advancesinneuralinformationprocessing
models.AdvancesinNeuralInformationProcessingSystems33(2020),6840–6851. systems32(2019).
[17] QingqingHuang,ArenJansen,JoonseokLee,RaviGanti,JudithYueLi,and [32] RobinRombach,AndreasBlattmann,DominikLorenz,PatrickEsser,andBjörn
DanielPWEllis.2022.MuLan:AJointEmbeddingofMusicAudioandNatural Ommer.2022.High-resolutionimagesynthesiswithlatentdiffusionmodels.In
Language.InIsmir2022HybridConference. ProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition.
[18] QingqingHuang,DanielSPark,TaoWang,TimoIDenk,AndyLy,Nanxin 10684–10695.
Chen,ZhengdongZhang,ZhishuaiZhang,JiahuiYu,ChristianFrank,etal.2023. [33] Ludan Ruan, Yiyang Ma, Huan Yang, Huiguo He, Bei Liu, Jianlong Fu,
Noise2music:Text-conditionedmusicgenerationwithdiffusionmodels.arXiv NicholasJingYuan,QinJin,andBainingGuo.2023. Mm-diffusion:Learning
preprintarXiv:2302.03917(2023). multi-modaldiffusionmodelsforjointaudioandvideogeneration.InProceed-
[19] ChrisDongjooKim,ByeongchangKim,HyunminLee,andGunheeKim.2019. ingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition.
AudioCaps:GeneratingCaptionsforAudiosinTheWild.InProceedingsofthe2019 10219–10228.
ConferenceoftheNorthAmericanChapteroftheAssociationforComputational [34] ChristophSchuhmann,RomainBeaumont,RichardVencu,CadeGordon,Ross
Linguistics:HumanLanguageTechnologies,Volume1(LongandShortPapers). Wightman,MehdiCherti,TheoCoombes,AarushKatta,ClaytonMullis,Mitchell
AssociationforComputationalLinguistics,Minneapolis,Minnesota,119–132. Wortsman,etal.2022.Laion-5b:Anopenlarge-scaledatasetfortrainingnext
https://doi.org/10.18653/v1/N19-1011 generationimage-textmodels.AdvancesinNeuralInformationProcessingSystems
[20] YehudaKoren.2008. Factorizationmeetstheneighborhood:amultifaceted 35(2022),25278–25294.
collaborativefilteringmodel.InProceedingsofthe14thACMSIGKDDinternational [35] ChristophSchuhmann,RobertKaczmarczyk,AranKomatsuzaki,AarushKatta,
conferenceonKnowledgediscoveryanddatamining.426–434. RichardVencu,RomainBeaumont,JeniaJitsev,TheoCoombes,andClayton
[21] YehudaKoren,RobertBell,andChrisVolinsky.2009.Matrixfactorizationtech- Mullis.2021.LAION-400M:OpenDatasetofCLIP-Filtered400MillionImage-
niquesforrecommendersystems.Computer42,8(2009),30–37. TextPairs.InNeurIPSWorkshopDatacentricAI.JülichSupercomputingCenter.
[22] SeungHyunLee,SieunKim,InnfarnYoo,FengYang,DonghyeonCho,Youngseo [36] RoyShefferandYossiAdi.2023. Ihearyourtruecolors:Imageguidedaudio
Kim,HuiwenChang,JinkyuKim,andSangpilKim.2023.Soundini:Sound-Guided
generation.InICASSP2023-2023IEEEInternationalConferenceonAcoustics,Speech
DiffusionforNaturalVideoEditing.arXivpreprintarXiv:2304.06818(2023). andSignalProcessing(ICASSP).IEEE,1–5.
[23] SeungHyunLee,WonseokRoh,WonminByeon,SangHoYoon,Chanyoung [37] MariaEleniSmyrnioti,ChrysaArvaniti,GeorgiaKostopanagiotou,andChrysan-
Kim,JinkyuKim,andSangpilKim.2022.Sound-guidedsemanticimagemanipu- thiBatistaki.2023.GuidedImageryandMusicinPatientsWithChronicDaily
lation.InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPattern Headache:APilotStudy.MusicTherapyPerspectives41,1(2023),e13–e20.
Recognition.3377–3386. [38] KunSu,XiulongLiu,andEliShlizerman.2020.Audeo:Audiogenerationfora
[24] BochenLiandAparnaKumar.2019. QuerybyVideo:Cross-modalMusicRe-
silentperformancevideo.AdvancesinNeuralInformationProcessingSystems33
trieval..InISMIR.604–611. (2020),3325–3337.
[25] TingleLi,YichenLiu,AndrewOwens,andHangZhao.2022. Learningvisual [39] DídacSurís,CarlVondrick,BryanRussell,andJustinSalamon.2022.It’sTime
stylesfromaudio-visualassociations.InComputerVision–ECCV2022:17thEuro- forArtisticCorrespondenceinMusicandVideo.InProceedingsoftheIEEE/CVF
peanConference,TelAviv,Israel,October23–27,2022,Proceedings,PartXXXVII. ConferenceonComputerVisionandPatternRecognition.10564–10574.
Springer,235–252. [40] ZinengTang,ZiyiYang,ChenguangZhu,MichaelZeng,andMohitBansal.
[26] Tsung-YiLin,MichaelMaire,SergeBelongie,JamesHays,PietroPerona,Deva 2023. Any-to-Any Generation via Composable Diffusion. arXiv preprint
Ramanan,PiotrDollár,andCLawrenceZitnick.2014.Microsoftcoco:Common
arXiv:2305.11846(2023).
objectsincontext.InComputerVision–ECCV2014:13thEuropeanConference, [41] HaThiPhuongThao,GemmaRoig,andDorienHerremans.2023. EmoMV:
Zurich,Switzerland,September6-12,2014,Proceedings,PartV13.Springer,740– Affectivemusic-videocorrespondencelearningdatasetsforclassificationand
755.
retrieval.InformationFusion91(2023),64–79.
[27] AlexLiu,SouYoungJin,Cheng-ILai,AndrewRouditchenko,AudeOliva,and [42] AaronVanDenOord,OriolVinyals,etal.2017.Neuraldiscreterepresentation
JamesGlass.2022.Cross-ModalDiscreteRepresentationLearning.InProceedings learning.Advancesinneuralinformationprocessingsystems30(2017).
ofthe60thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume [43] JianfengWang,ZhengyuanYang,XiaoweiHu,LinjieLi,KevinLin,ZheGan,
1:LongPapers).3013–3035. ZichengLiu,CeLiu,andLijuanWang.2022.GIT:AGenerativeImage-to-text
[28] SaifMohammad.2018.Obtainingreliablehumanratingsofvalence,arousal,and
TransformerforVisionandLanguage.TransactionsonMachineLearningResearch
dominancefor20,000Englishwords.InProceedingsofthe56thannualmeetingof (2022).
theassociationforcomputationallinguistics(volume1:Longpapers).174–184. [44] QuanzengYou,JieboLuo,HailinJin,andJianchaoYang.2016.Buildingalarge
[29] ArshaNagrani,PaulHongsuckSeo,BryanSeybold,AnjaHauth,SantiagoManen, scaledatasetforimageemotionrecognition:Thefineprintandthebenchmark.
ChenSun,andCordeliaSchmid.2022. Learningaudio-videomodalitiesfrom
InProceedingsoftheAAAIconferenceonartificialintelligence,Vol.30.
imagecaptions.InComputerVision–ECCV2022:17thEuropeanConference,Tel [45] YipinZhou,ZhaowenWang,ChenFang,TrungBui,andTamaraLBerg.2018.
Aviv,Israel,October23–27,2022,Proceedings,PartXIV.Springer,407–426. Visualtosound:Generatingnaturalsoundforvideosinthewild.InProceedings
[30] AlecRadford,JongWookKim,ChrisHallacy,AdityaRamesh,GabrielGoh,
oftheIEEEconferenceoncomputervisionandpatternrecognition.3550–3558.
SandhiniAgarwal,GirishSastry,AmandaAskell,PamelaMishkin,JackClark,
