---
来源文件 / Source PDF: `deam-2017-plosone-e0173392.pdf`
提取日期 / Extracted: 2026-10-30
提取方式 / Method: pdfplumber 文本层直接提取（非 OCR）
PDF 页数 / Pages: 22
总字符数 / Characters: 59599
DOI: 10.1371/journal.pone.0173392
PDF 元数据标题 / Metadata title: Developing a benchmark for emotional analysis of music
PDF 元数据作者 / Metadata author: Anna Aljanaki, Yi-Hsuan Yang, Mohammad Soleymani
---
## 引用信息 / Citation (APA 7th)

> Aljanaki, A., Yang, Y.-H., & Soleymani, M. (2017). Developing a benchmark for emotional analysis of music. *PLOS ONE, 12*(3), e0173392. https://doi.org/10.1371/journal.pone.0173392

注：该文提出的基准数据集即 DEAM（Database for Emotion Analysis in Music）。


## 正文（按页提取 / Extracted page by page）

### Page 1

RESEARCHARTICLE
Developing a benchmark for emotional
analysis of music
AnnaAljanaki1¤*,Yi-HsuanYang3,MohammadSoleymani2
1UtrechtUniversity,Utrecht,theNetherlands,2SwissCenterforAffectiveSciences,UniversityofGeneva,
Geneva,Switzerland,3AcademiaSinica,Taipei,Taiwan
¤ Currentaddress:SwissCenterforAffectiveSciences,UniversityofGeneva,Geneva,Switzerland
*aljanaki@gmail.com
Abstract
a1111111111
a1111111111
Musicemotionrecognition(MER)fieldrapidlyexpandedinthelastdecade.Manynewmeth-
a1111111111
odsandnewaudiofeaturesaredevelopedtoimprovetheperformanceofMERalgorithms.
a1111111111
a1111111111 However,itisverydifficulttocomparetheperformanceofthenewmethodsbecauseofthe
datarepresentationdiversityandscarcityofpubliclyavailabledata.Inthispaper,we
addresstheseproblemsbycreatingadatasetandabenchmarkforMER.Thedatasetthat
werelease,aMediaEvalDatabaseforEmotionalAnalysisinMusic(DEAM),isthelargest
availabledatasetofdynamicannotations(valenceandarousalannotationsfor1,802songs
OPENACCESS
andsongexcerptslicensedunderCreativeCommonswith2Hztimeresolution).Using
Citation:AljanakiA,YangY-H,SoleymaniM
DEAM,weorganizedthe‘EmotioninMusic’taskatMediaEvalMultimediaEvaluationCam-
(2017)Developingabenchmarkforemotional
analysisofmusic.PLoSONE12(3):e0173392. paignfrom2013to2015.Thebenchmarkattracted,intotal,21activeteamstoparticipatein
doi:10.1371/journal.pone.0173392 thechallenge.Weanalyzetheresultsofthebenchmark:thewinningalgorithmsandfea-
Editor:ChristosPapadelis,BostonChildren’s ture-sets.Wealsodescribethedesignofthebenchmark,theevaluationproceduresandthe
Hospital/HarvardMedicalSchool,UNITED datacleaningandtransformationsthatwesuggest.Theresultsfromthebenchmarksug-
STATES
gestthattherecurrentneuralnetworkbasedapproachescombinedwithlargefeature-sets
Received:July26,2016 workbestfordynamicMER.
Accepted:February20,2017
Published:March10,2017
Copyright:©2017Aljanakietal.Thisisanopen
accessarticledistributedunderthetermsofthe
CreativeCommonsAttributionLicense,which Introduction
permitsunrestricteduse,distribution,and
Musicemotionrecognition(MER)isayoung,butfastexpandingfield,stimulatedbytheinter-
reproductioninanymedium,providedtheoriginal
authorandsourcearecredited. estfrommusicindustrytoimproveautomaticmusiccategorizationmethodsforlarge-scale
onlinemusiccollections.In[1],ananalysisofwrittenmusicqueriesfromcreativeprofession-
DataAvailabilityStatement:Allrelevantdataand
alsshowedthat80%ofthequeriesforproductionmusiccontainemotionalterms,making
materialsareavailableathttp://cvml.unige.ch/
databases/DEAM/. themoneofthemostsalientandimportantcomponentsofexploratorymusicsearch.Inthe
lastdecade,manynewMERmethodshavebeenproposed(see[2,3]forreviews).However,
Funding:AA’sworkwassupportedbyCOMMIT/
methodologicaldifferencesindatarepresentationresultinachoiceofdifferentevaluation
project(commit-nl.nl).MSwassupportedby
AmbizioneprogramoftheSwissNationalScience metrics,whichmakestheaccuracyofthealgorithmsimpossibletocompare.Fig1shows14
Foundation(GrantnumberPZ00P2_154981). differentdataannotationandrepresentationchoicesinaformofalabyrinth.Inadditionto
Competinginterests:Theauthorshavedeclared
thesechoices,awidevarietyofcategoricalanddimensionalemotionalmodelsareused,suchas
thatnocompetinginterestsexist. basicemotions[4],valenceandarousalmodel[5–8],GenevaEmotionalMusicScales(GEMS)
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 1/22

### Page 2

Developingabenchmarkforemotionalanalysisofmusic
[9,10],orcustommoodclusters[11–13].Despitedifferencesindatarepresentation,mostof
themethodsareessentiallysolvingthesameproblemofmappingacousticfeatures(orlyrics
andmeta-databasedfeatures)totheemotionalannotations.Aspecificlearningalgorithmcan
notalwaysbeadaptedtootherrepresentations(thoughmanyalgorithms,suchasSVMordif-
ferenttypesofneuralnetworks,areversatile),butaudiofeaturesaremoreoftentransferable.A
benchmarkcanthereforeenableacomparisonofdifferentmethodsandfeaturesets.
AnotherproblemofMERisthatduetoaudiocopyrightrestrictions,thedatasetsusedin
variousstudiesareseldommadepublicandreusedinotherstudies.Annotationsareoften
obtainedbycrawlingthetagsfromsocialmusicwebsites,suchaslast.fmorallmusic.com.In
thiscase,theaudioisusuallycopyrightedandcannotberedistributedbytheresearchers.The
musicthatisdistributedforfreeunderalicensesuchasCreativeCommons,usuallyisless
well-knownandhaslesstags,andthereforeneedstobeannotated.Annotatingwithemotional
labelsisburdensome,becausewithsuchasubjectivetaskmanyannotationsareneededfor
everyitem.
Afundamentalpropertyofmusicisthatitunfoldsovertime.Anemotionexpressedinthe
songmayalsochangeovertime,thoughitisalwayspossibletoreducethisvarietytoasingle
averagevalue.Theonlinemusicwebsites,suchasmoodfuse.com,musicovery.com,allmusic.
com,usuallyrepresentsongsinamoodspacebyasinglelabel,whichisalwaysanapproxima-
tionoftheemotionalcontentofthesong.Indesignofthebenchmark,werecognizedthetime-
dependentnatureofmusicbysettingouttopredicttheemotionofthemusicdynamically(per-
second),i.e.,themainpurposeofthebenchmarkistocomparedynamicMERalgorithms,also
knownasmusicemotionvariationdetection(MEVD)algorithmsintheliterature[2].
Inthispaper,wedescribethedesign,evaluationmetricsanddatathatweusedtobench-
markdynamicMERalgorithms.MediaEvalDatabaseforEmotionalAnalysisinMusic
(DEAM)isthecombinationofthedatasetsdevelopedinthreeyears(withdatatransformation
andcleaningproceduresappliedtothem),inadditiontothemanualannotationswereceived
onAmazonMechanicalTurk(MTurk).DEAMcontains1,802songs(58full-lengthsongsand
1,744excerptsof45seconds)fromavarietyofWesternpopularmusicgenres(rock,pop,elec-
tronic,country,Jazzetc).PartofthedatawasannotatedinthelabandpartusingMTurkplat-
form(http://www.mturk.com).Sincethebenchmarkstartedin2013,wehaveoptedfor
characterizingtheemotionofmusicasnumericalvaluesintwodimensions—valence(positive
ornegativeemotionsexpressedinmusic)andarousal(energyofthemusic)(VA)[14,15],to
makeiteasiertodepictthetemporaldynamicsofemotionvariation.Wereleasethefulldataset
includingtheaveragedandtherawannotationsforthebenefitofthecommunity(available
onlineathttp://cvml.unige.ch/databases/DEAM).Overthreeyearsofactivity21teamspartici-
patedinthetask.Wewillalsosystematicallyevaluatethefeature-setsandthealgorithmsin
thispaper.
Background
MERisayoungfieldwhichhasbeendevelopinginthelastdecade.Inthissection,wewill
reviewavailablebenchmarksforMERalgorithms.
MIREXbenchmarkandstaticMER. TheonlyotherbenchmarkthatexistsforMER
methodsistheaudiomoodclassification(AMC)task,organizedbyannualMusicInformation
RetrievalEvaluationeXchange(http://www.music-ir.org/mirex/wiki/)(MIREX)[11].Inthis
task,600audiofilesareprovidedtotheparticipantsofthetask,whohaveagreednottodistrib-
utethefilesforcommercialpurposes.Since2013,anothersetof1,438segmentsof30seconds
clippedfromKoreanpopsongshasbeenaddedtoMIREX.Thebenchmarkusesfivediscrete
emotionclusters,derivedfromclusteranalysisofonlinetags,insteadofmorewidelyaccepted
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 2/22

### Page 3

Developingabenchmarkforemotionalanalysisofmusic
dimensionalorcategoricalmodelsofemotion.EmotionalmodelusedinAMChasbeenthe
topicofdebatesinceitisnotbasedonpsychologicalresearch.Thereisalsosemanticoracous-
ticoverlapbetweenclusters[16].Furthermore,thedatasetonlyappliesasingularstaticrating
peraudioclip(i.e.itdealswiththestaticMERproblem),whichdoesnottakeintoaccountthe
temporallydynamicnatureofmusic.
DynamicMERmethods. Sincethelate1980s,time-varyingresponsestomusicweremea-
suredusingContinuousResponseDigitalInterface[17].Usually,onlyonedimension(suchas
tension,musicalintensityoremotionality)wasmeasured.Schubertproposedtousetwo-
dimensionalinterface(valence–arousalplane)toannotatemusicwithemotioncontinuously
[18].ThisapproachwasadoptedbyMERresearchersaswell.
Thefirststudythatmodelsmusicalemotionunfoldingovertimewithmusicalfeatures
(loudness,tempo,melodiccontour,texture,andspectralcentroid)wasconductedbySchubert
in2004[19].Themodel,usingalinearregression,couldexplainfrom33%to73%ofvariation
inemotion.In2006,Korhonenetal.[20]suggestedamethodtomodelmusicalemotionasa
functionofmusicalfeaturesusingsystemidentificationtechniques.Korhonenetal.usedthe
low-levelspectralfeaturesextractedusingMarsyassoftware(http://marsyas.info),andpercep-
tualfeaturesextractedwithPsySoundsoftware[21].Thesystemreachedaperformanceof0.22
forvalenceand0.78forarousalintermsofthecoefficientofdetermination(R2).In2010,
Schmidtetal.[22]usedKalmanfilteringtopredictper-secondchangesinthedistributionof
emotionovertimeon15secondmusicexcerpts.In2011,SchmidtandKimsuggestedusinga
newmethod—ConditionalRandomFields—tomodelcontinuousemotionwitharesolution
of11×11invalence–arousalspace[23].Averysmallfeature-setwasused—MFCCs,spectral
contrastandtimbre—andthesystemreachedperformanceof0.173intermsofEarthMover’s
Distance(betweenthetrue11×112Dhistogramofvalence–arousalvaluesandpredicted
one).Pandaetal.[24]usedSupportVectorMachinesandfeaturesextractedwithMarsyasand
MIRToolboxtotrackmusicoverquadrantsofvalence–arousalspace.Imbrasaiteetal.[25]
combinedContinuousConditionalRandomFieldswitharelativerepresentationoffeatures.
Later,Imbrasaiteetal.[26]showedthatusingContinuousConditionalNeuralFieldsoffers
improvementoverthepreviousapproach.Wangetal.[27]representedtheambiguityofemo-
tionthroughaGaussiandistributionandtrackedtheemotionvariationovertimeusingamap-
pingbetweenmusicemotionspaceandlow-levelacousticfeaturespacethroughasetoflatent
featureclasses.Markovetal.[28]usedGaussianProcessesfordynamicMER.Thebidirec-
tionalLongShort-TermMemoryRecurrentNeuralNetworkswerefirstappliedtocontinuous
emotionrecognitionnotinthedomainofmusic,butinthedomainofmultimodalhuman
emotiondetectionfromspeech,facialexpressionandshouldergesture[29].
Mostofthealgorithmsmentionedinthissectionwereemployedinthebenchmark:Sup-
portVectorRegression,linearregression,Kalmanfiltering,GaussianProcesses,Conditional
RandomFields,ContinuousConditionalNeuralFieldsandLongShort-TermMemoryRecur-
rentNeuralNetworks,givingusanopportunitytoqualitativelycomparetheirperformancein
thebenchmark.
DatasetsfordynamicMER. Mostofthestudiesreviewedabovedidnotreleasepublic
data.TheonlyexceptionistheMoodSwingsdataset[30],developedbySchmidtetal.,which
comprises240segmentsofUSpopsongs(each15-secondlong)withper-secondVAannota-
tions,collectedthroughMTurk.Afteranautomaticverificationstepthatremovedunreliable
annotations,eachclipinthisdatasetwasannotatedby7to23subjects.
Asimilartaskfromadifferentdomainiscontinuousemotionrecognitionfromhuman
behavior.Audiovisualemotionchallenge(AVEC)[31–35]isachallengethathasbeenrunning
since2011andisaddressingtheproblemofcontinuousemotionrecognition.Since2011,they
usedSEMAINE[36]andRECOLA[37]databaseswhichincludehumanbehaviorwith
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 3/22

### Page 4

Developingabenchmarkforemotionalanalysisofmusic
continuousemotionlabels.Therearealsopublicdatasetswithstaticpersongmusicemotion
annotations.TheDEAPdataset[38]hastheratingsonvalence,arousalanddominancefor
120clipsofone-minutemusicvideoclipsofWesternpopmusic.Eachclipwasannotatedby
14–16listeners(50%female),whowereaskedtoratethefeltvalence,arousalanddominance
ona9-pointscaleforeachclip.TheAMG1608dataset[39]containstheVAratingsfor1,608
Westernmusicindifferentgenres,alsoannotatedthroughMTurk.
Musicdatabase
Ourdatasetconsistsofroyalty-free(CreativeCommonslicenseenablesustoredistributethe
content)musicfromseveralsources:freemusicarchive.org(FMA),jamendo.com,
andthemedleyDBdataset[40].Thereare1,744clipsof45secondsfromFMAand58full
lengthsongs,halfofwhichcomefrommedleyDBandanotherhalffromJamendo.
ThemusicfromtheFMAwasinrock,pop,soul,blues,electronic,classical,hip-hop,interna-
tional,experimental,folk,jazz,countryandpopgenres.ThemusicfromtheMedleyDBdataset
inadditionhadmusicinworldandrapgenres,andthemusicfromJamendoalsohadreggae
music.For2014and2015dataset,wemanuallycheckedthemusicandexcludedthefileswith
badrecordingqualityorthosecontainingspeechornoiseinsteadofmusic.Foreachartist,we
selectednomorethan5songstobeincludedinthedataset.FormedleyDBandJamendofull-
Fig1.AlabyrinthofdatarepresentationchoicesforaMERalgorithm.Thechoicesthatwemadeforthebenchmarkarehighlightedin
red.
doi:10.1371/journal.pone.0173392.g001
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 4/22

### Page 5

Developingabenchmarkforemotionalanalysisofmusic
lengthsongs,weselectedsongswhichhademotionalvariationinthem,usinganexisting
dynamicMERalgorithmforfilteringandmanualfinalselection[41].
Annotations
Gettinghighqualitydataisacrucialstepforahighlysubjectivetask.Tocollectannotations,
wehaveturnedtocrowdsourcingusingMTurk,whichwassuccessfullyusedbyotherstolabel
largelibraries[30,39].Wedevelopedaproceduretofilteroutpoorqualityworkers,following
currentstate-of-the-artcrowdsourcingapproaches[42].Theworkerspassedatesttodemon-
strateathoroughunderstandingofthetask,andanabilitytoproducegoodqualitywork.The
testcontainedseveralautomaticallyscoredmultiplechoicequestions,andseveralfree-form
questionsandassignments,whichwereevaluatedmanuallyiftheautomaticallyscoredpart
waspassedcorrectly.Inyears2013and2014,eachexcerptwasannotatedbyaminimumof10
workers.In2015,eachsongwasannotatedbyfiveworkers,threeofwhichwererecruited
amongthemostsuccessfulworkersfrompreviousyears,andtwowereworkinginthelab.To
ensureahigh-qualityoutcome,wefirstdiscussedandsetafaircompensationforsucha
demandingtask(about$8perhour)onaMTurkworkers’forum(http://www.mturkgrind.
com/).Wethendouble-checkedtheagreementbetweentheannotatorsineachbatchbefore
assigninganincreasingqualificationscorewhichpermittedworkerstoworkonthenext
batches.Thedynamicannotationswerecollectedusingaweb-interfaceonascalefrom−10to
10,wheretheMechanicalTurkworkerscoulddynamicallyannotatethesongsonvalenceand
arousaldimensionsseparatelywhilethesongwasbeingplayed.Thestaticannotationswere
madeonnine-pointscaleonvalenceandarousalforthewhole45secondsexcerptsafterthe
dynamicannotations.Fig2showstheinterfaceusedforannotation.
AssummarizedinTable1,inadditiontotheaudiofeatures,wealsoprovidemeta-datacov-
eringthegenrelabelsobtainedfromFMA,medleyDBandJamendo,folksonomytagscrawled
fromlast.fm,andmeta-dataabouttheannotators.
Annotationconsistency
Wewillevaluateannotationconsistencyusingtwomeasures:Cronbach’sαonthesequences
ofannotationsforeachofthesongs,andcoefficientofdeterminationofaGeneralizedAddi-
tiveModelthatgeneralizessong’sannotationsacrossannotators.
Weresampletheannotationsto2Hz,andnormalizetheannotationsforeachsongby
a ¼a þðA (cid:0) AÞ; ð1Þ
j;i j;i j
wherea isanannotationbyannotatorjattimestampi,A (cid:22) isthemeanoftheannotationsby
j,i j
annotatorj,andA (cid:22) isameanofallannotationsforthissongbyallannotators(globalmean).
Cronbach’sαisusedtoestimatethedegreetowhichasetofitemsmeasuresasingleunidi-
mensionallatentconstruct.Thismeasureshouldtheoreticallyrangebetween0and1,butin
practicecanbenegativewheninter-itemcorrelationsarenegative.Thereisnolowerbound
onnegativevaluesofthismeasure.Onlypositivevaluesareinformativeandaccuratelyreport
degreeofagreement.Therefore,weclipthenegativetailbyassigningthevalueof0.Table2
showstheaveragedCronbach’sαforeachyear’sannotations.Totestwhetherannotationcon-
sistencyimprovedwithachangeofexperimentaldesign,wewillcomparethethreegroups.
Groups’samplesizesandvariancesaredifferent,thereforewewilluseanon-parametrictest
basedonranks.Kruskal-Wallistest(onewayANOVAonranks)showsthattherearesignifi-
cantdifferencesbetweengroupsforarousal(χ2(2)=81.24,p-value=2.2×10−16)andDun-
nett-Tukey-Kramertestshowsthatthedifferencesaresignificantbetweenallthreeyearsona
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 5/22

### Page 6

Developingabenchmarkforemotionalanalysisofmusic
Fig2.Annotationinterfaceforbothcontinuous(upper-leftcorner)andstaticpersong(middle;usingtheself-assessmentmanikins[43])ratings
ofarousal.
doi:10.1371/journal.pone.0173392.g002
Table1.ThedataoverviewofDEAM.
Year Numberof Source Meta-dataabout Meta-dataaboutannotators
songs music
2013 1000(744 MTurk Genre Timeoftheday,mood
unique)
2014 1000 MTurk Genre Confidenceinrating,familiarityofmusic,likingofmusic,freeemotionlabel,BigFive
personality,preferredgenre
2015 58 MTurk/ Genre Liking,freeemotionlabel
Lab
doi:10.1371/journal.pone.0173392.t001
1%significancelevel.Forvalence,thedifferencesexist(χ2(2)=57.91,p-value=2.6×10−13),
butonlyannotationsfrom2015aresignificantlydifferentfromothergroups.
Cronbach’sαtesthassomedeficiencies,suchasbeingsensitivetothenumberofitemson
thetest(greaternumberofitemsinthetestcanartificiallyinflatethevalueofalpha).There-
fore,weconductanadditionalconsistencytestwithgeneralizedadditivemixedmodels
(GAMs)[44].AGAMisageneralized(i.e.,allowingnon-normalerrordistributionsofthe
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 6/22

### Page 7

Developingabenchmarkforemotionalanalysisofmusic
Table2.Annotationconsistency.Cronbach’sαandgeneralizedadditivemixedmodels(GAM)’scoefficientofdetermination(meanandstandarddeviation)
peryear.
Year 2013 2014 2015
Totallength 9h18min 12h30min 3h46min
Cronbach’sαforarousal .28±0.28 .31±0.30 .66±0.26
GAM’sR2forarousal .13±0.10 .14±0.11 .44±0.19
Cronbach’sαforvalence .28±0.29 .20±0.24 .51±0.35
GAM’sR2forvalence .13±0.10 .10±0.08 .37±0.21
doi:10.1371/journal.pone.0173392.t002
responsevariable)linearmodelwithalinearpredictorinvolvingasumofsmoothfunctionsof
covariates.Themodelisdefinedasfollows:
gðmÞ¼b þf ðx Þþf ðx Þþ:::þf ðx Þ; ð2Þ
0 1 1 2 2 n n
wheregisalinkfunction(afunctiondefiningarelationshipbetweenthelinearpredictorand
themeanofthedependentvariable);μ=E(Y),whereYisadependentvariable;andf(x)are
i i
non-parametricsmoothfunctions,estimated,e.g.viascatterplotsmoothingtechniques,orcan
alsobeparametricfunctionsorfactors.
GAMsaresuitableformodelingcontinuousannotationsofemotion,becausetheseannota-
tionsareusuallynon-linearinnatureanddonothaveabruptchanges,makingitpossibleto
modelthemusingsmoothfunctions.KcKeownandSneddon[44]describedhowGAMsand
theirmixedmodelextensioncanbeusedtomodelcontinuousemotionannotationsandmake
inferencesconcerninglineardifferencesbetweengroups.Inthispaper,weonlyuseGAMsto
assesstheeffectsizeofsharedperceivedemotion.Thisisdonebybuildingamodelforeach
songandcalculatingtheR2ofthemodel.
Thereisonlyonesmoothcomponentinthemodel—time.Weusepenalizedcubicregres-
sionsplineswithbasisdimensionof20andidentitylinkfunction.Theresultsareshownin
Table2.Fig3showsscatter-plotsofthemanualannotationsandthefittedGAMSfor2songs
pickedfrom2015dataset.
TherearesignificantdifferencesbetweengroupsforarousalaccordingtoKruskal-Wallis
test(χ2(2)=121.03,p-value=2.2×10−16)andDunnett-Tukey-Kramertestshowsthatthedif-
ferencesaresignificantbetween2015andothergroupsona1%significancelevel.Forvalence,
theoutcomeisthesame:differencesexist(χ2(2)=134.37,p-value=2.2×10−16),andonly
year’s2015annotationsaresignificantlydifferentfromothergroups.
Accordingtobothconsistencymeasures,in2015wecouldachievebetterconsistency,
whichcanbeattributedtoemployinglabworkers,choosingcompletesongsoverexcerptsand
introducingpreliminarylistening.
Influenceofmusicfamiliarity,likingandotherfactorsonannotations. TheCreative
Commonsmusicthatweselectedwaslargelyunfamiliartoparticipants(onlyin1%ofthelis-
teningsessionstheparticipantreportedhavingheardthepiecebefore).Hence,therewasnot
enoughdatatoderiveanypatternsregardingthefamiliarityofthemusic.
Wefoundthatlikinginfluencedselfevaluationofconfidenceinrating.Fig4showsthe2D
histogramforself-reportedconfidenceinratingandlikingthemusic.Theconfidenceinrating
isonaverageveryhigh(theworkersneverreportedbeingveryuncertain),whichis,probably,
causedbythefactthatthedatawascollectedfrompaidworkerswhodidnotwanttobesus-
pectedofincompetence.Likingthemusicinfluencedperceivedself-reportedconfidence.A
similareffectwasfoundin[45],whentherewasapositivedependencybetweenlikingthe
musicandannotationconsistency.Wecouldnotfindanyeffectofaveragedmusiclikingon
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 7/22

### Page 8

Developingabenchmarkforemotionalanalysisofmusic
Fig3.FittedGAMsforthearousalandvalenceannotationsoftwosongs.
doi:10.1371/journal.pone.0173392.g003
actualratingconsistencyasmeasuredbycorrelationofaratingwithotherworkers,orCron-
bach’sαofasong.
Convergenceofannotations. Itisaknownissuethattheannotatorsneedsomeinitial
orientationtime(IOT),beforetheircontinuousannotationsbecomemeaningfulandreliable.
In[46],medianIOTwasfoundtobe8secondsforvalenceand12secondsforarousal.Also,
aftergloweffects—largeoutliersinspreadofscoresjustaftertheendofapiece—wereidenti-
fied.In[47],participantsrequiredonaverage8.31secondstoinitiategivingemotionaljudge-
mentsonmusiconatwo-dimensionalplane.Thelengthofdelaywasinfluencedby
familiarity,genreandtempoofmusic.
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 8/22

### Page 9

Developingabenchmarkforemotionalanalysisofmusic
Fig4. Likingofthemusicandconfidenceinratingfora)valence,Spearman’sρ=0.37,p-value=2.2×10−16b)arousal,Spearman’sρ=0.29,p-
value=2.2×10−16.
doi:10.1371/journal.pone.0173392.g004
TomeasuretheIOToftheannotatorsinthebeginningofthesong,wecalculatetheaverage
Krippendorff’sαforeverysampleofthecorrespondingsecondforthewholedatasetof2015.
Thesongsinthedatasethaddifferentlength.Fig5showsthattheannotationsstarttoconverge
aroundthe13thsecond.Asimilarresultwasobtainedin2013thannotations[48].So,despite
preliminarylisteningstage,thereactiontimedidnotdiminish.
Weremovethefirst15secondsoftheannotationfromthebenchmarkdata.
Benchmarkhistoryanddesign
Thebenchmarkformusicemotionrecognitionalgorithms,describedinthisarticle,wasorga-
nizedinyears2013-2015insidetheMediaEvalBenchmarkingInitiativeforMultimediaEvalu-
ation(http://www.multimediaeval.org).MediaEvalisacommunity-drivenbenchmark
dedicatedtoevaluatingalgorithmsformultimediaaccessandretrieval,thatisorganizedannu-
allysinceyear2008(asVideoCLEF,inyears2008and2009).Thelistoftasksofferedatthe
benchmarkisrenewedeveryyearbasedoninterestandfeedbackfromthemultimedia
retrievalcommunity.AlongsideEmotioninMusictask,10-11othertasksrelatedtospeech,
music,imageandvideoprocessingwereheldatMediaEvalinyears2013-2015.Wefollowed
MediaEvalbenchmarkingtradition,bydevelopingaseparatedevelopmentandevaluation-set
foreachyear.
Taskdefinition2013
Inyear2013,thetaskwasfirstproposedandorganizedinsideMediaEvalframeworkby
MohammadSoleymani,Yi-HsuanYangandErikSchmidt[49].Thetaskconsistedoftwosub-
tasks:dynamicandstaticemotioncharacterization.Indynamicemotioncharacterization,the
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 9/22

### Page 10

Developingabenchmarkforemotionalanalysisofmusic
Fig5.Krippendorff’sαofdynamicannotationsin2015,averagedoveralldynamicsamples.
doi:10.1371/journal.pone.0173392.g005
participatingalgorithmspredictedemotion(valenceandarousal)ofthemusicdynamically
per-second.Inthestatictask,thevalenceandarousalofthecompletemusicclip(45seconds)
werepredicted.Thetrainingdatasetconsistedof700excerptsof45seconds,whichwere
labelledbothwithdynamicannotation(1Hz)andstaticannotation,wherestaticwasnot
derivedfromdynamic,butwasgivenseparately.300clipswereleftoutfortheevaluation-set.
ThemusiccamefromFreeMusicArchive.Later,duplicates(excerptssampledfromthesame
song)werediscoveredandremovedfromthisdata,leaving744clipsoutof1000.
Taskdefinition2014
In2014,thestaticemotioncharacterizationtaskwasremovedandanewsubtask—feature
design—wasaddedinstead[50].Inthefeaturedesigntask,newfeatures,whichhavenotbeen
developedbefore,wereproposedandappliedtovalenceandarousalpredictiontask.Thefea-
turedesigntaskwasnotpopularandonlyoneteamsubmittedtothattask[51].Thetraining
setconsistedof744clipsfrompreviousyearand1000newclips,allfromFreeMusicArchive,
servedastheevaluation-set.Thetimeresolutionforthedynamictaskwaschangedto2Hz.
Taskdefinition2015
In2015,thefeaturedesignsubtaskwasremoved,leavingonlydynamicemotioncharacteriza-
tiontask.Thetrainingsetconsistedof431clips,whichwereselectedoutof1,744clipsfrom
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 10/22

### Page 11

Developingabenchmarkforemotionalanalysisofmusic
previousyearsbasedonconsistencymetrics.Thedatacleaningprocedureisdescribedin[41].
Theevaluation-setconsistedof58fulllengthsongs,onehalffromthemedleyDBdataset[40]
ofroyalty-freemultitrackrecordingsandanotherhalffromthejamendo.commusicweb-
site,whichprovidesmusicunderCreativeCommonslicense.Thesongswere(cid:25)4minutes
(234±107s)longonaverage.Thetimeresolutionfortheannotationswas2Hz.Thepartici-
pantshadtosubmit:
• Featuresthattheparticipantsusedintheirapproach.Thefeatureswereusedtotrainabase-
lineregressionmethod(linearregression)toestimatedynamicaffect.Anyfeaturesautomati-
callyextractedfromtheaudioorthemeta-dataprovidedbytheorganizerswereallowed.
• Predictionsusingbaselinefeatures.
• Predictionsusinganycombinationofthefeaturesandmachinelearningmethodsoftheir
choice.
Evaluationmetrics
Weusedtwoevaluationmetricstocomparetheperformanceofdifferentmethods:Pearson’s
correlationcoefficientbetweenthegroundtruthandpredictedvaluesforeachsong,averaged
acrosssongs,androotmeansquareerror(RMSE),averagedthesameway.Inyears2013and
2014,weusedcorrelationcoefficientasthemainmetricandRMSEasanauxiliarymetricto
breaktheties.Thetieisasituation,whenthedifferencebetweentwomethodsadjacentinthe
rankingisnotsignificantbasedontheonesidedWilcoxontest(p<0.05).In2015,weused
RMSEasourprimarymetric.RMSEmetricmeasureshowfaristhepredictionoftheemotion
fromthetrueemotionofthesong,andcorrelationmeasureswhetherthedirectionofchange
isguessedcorrectly.However,incaseofdynamicemotions,thetrendshapeofthetracesare
alsoimportant.Inthispaper,wewillalsoreportconcordancecorrelationcoefficient(CCC)ρ
c
asanevaluationmetric.ThismetricwassuggestedbyLin[52]in1989andisdefinedasfol-
lows:
2s
r ¼ xy ; ð3Þ
c s2þs2þðx(cid:22)þy(cid:22)Þ
x y
wherexandyarethevectorsofnumberstocompare,s2isthevarianceofx,s isthecovari-
x xy
anceofxandy,andx(cid:22)isthemeanofvectorx.CCChasrecentlybeenpromotedasthemetric
ofchoiceforcontinuousemotionrecognition[35].
Baselinefeatures
Ineveryyear,baselinefeaturesextractedfromtheaudiowereofferedtotheparticipantsalong
withtheaudiofiles.Inthemajorityofcases,thesefeatureswereusedbytheparticipantsin
theirsubmissions.Inyear2013,thefeatureswereMFCCs,octave-basedspectralcontrast,
spectralfeatures(centroid,flux,rolloff,flatness),chromagram,andtimbre,pitch,andloudness
featuresfromtheEchonest7API.Inyear2014,wereleasedthefeaturesextractedwithopen-
SMILEtoolbox[53]asdescribedin[54].Inyear2015,weextractedasmallersetoffeatures
withopenSMILE.Weobtained260low-levelfeatures(meanandstandarddeviationof65low-
levelacousticdescriptors,andtheirfirst-orderderivatives)fromnon-overlappingsegmentsof
500ms,withtheframesizeof60mswitha10msstep.
Nofeatureselectionwasappliedwhenbuildingbaselinelinearregressionmodelsfrom
baselinefeatures.Inyear2014,asanexception,differentfeatureswereusedtobuildabaseline
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 11/22

### Page 12

Developingabenchmarkforemotionalanalysisofmusic
Table3.Performanceofthealgorithmsforarousalandvalenceinyear2013.BLSTM-RNN—Bi-directionalLong-ShortTermMemoryRecurrentNeural
Networks.GPR—GaussianProcessesRegression.SVR—SupportVectorRegression.
Method Arousal Valence
RMSE ρ RMSE ρ
BLSTM-RNN[54] .08±.05 .31±.37 .08±.04 .19±.43
GPR[28] .10±.05 .11±.36 .09±.05 .06±.28
SVR[57] .10±.06 .14±.28 .12±.07 −.01±.27
Baseline .25±.11 .16±.36 .23±.10 .06±.30
doi:10.1371/journal.pone.0173392.t003
model(spectralflux,harmonicchangedetectionfunction,loudness,roughnessandzerocross-
ingrate).
Analysisofproposedmethods
Inthissection,wewillanalyzethebestsystemssuggestedoverthethreeyearsofbenchmark.
Inthelasteditionofthebenchmark(2015),weaskedtheparticipantstoprovidetheirfeature-
sets,andtoruntheiralgorithmsonthebaselinefeature-set.Inthisway,wecanconductasys-
tematicevaluationofthealgorithmsandfeature-setsseparately.
Taskparticipation
Threeteamsparticipatedinthetaskinyear2014andtheresultswereanalyzedin[48].In
2014,thereweresixteamsandin2015,twelveteams.Everyteamwroteaworkingnotespaper
whichisavailableintheproceedingsonthecorrespondingyearMediaEvalworkshop.Thelast
editionofthebenchmarkhadmostparticipatingteams,andmostofthealgorithmsfromthe
previousyearsfeaturedinthelastedition.Inthispaper,wewillmostlyanalyzetheresultsof
thebenchmarkheldin2015.
Performanceinachallengeoveryears
Tables3–5showtheresultsofthebenchmarkinyear2013,2014and2015.Theresultsare
sortedbyRMSEofarousalascending(bestsolutionsontop).Column“Method”showsthe
abbreviationofthemachinelearningalgorithmusedbyaparticularteam,andaworkingnotes
Table4.Performanceofthealgorithmsforarousalandvalenceinyear2014.KF—KalmanFilter.LSTM
—Long-ShortTermMemoryRecurrentNeuralNetwork.CCRF—ContinuousConditionalRandomFields.
CCNF—ContinuousConditionalNeuralFields.MR—Multi-levelregression.PLSR—PartialLeastSquares
Regression.
Method Arousal Valence
RMSE ρ RMSE ρ
KF[56] .08±.05 .21±.57 .14±.07 .17±.5
LSTM[55] .10±.05 .35±.45 .08±.05 .20±.49
CCRF[58] .12±.05 .23±.56 .09±.05 .12±.55
CCNF[26] .12±.07 .18±.60 .10±.06 .07±.29
MR[59] .12±.05 .17±.41 .09±.05 .10±.37
PLSR[51] .13±.07 .28±.50 .10±.06 .15±.5
Baseline .14±.06 .18±.36 .10±.06 .11±.34
doi:10.1371/journal.pone.0173392.t004
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 12/22

### Page 13

Developingabenchmarkforemotionalanalysisofmusic
Table5.Performanceofthealgorithmsforarousalandvalencein2015.BLSTM-ELM—BLSTM-basedmulti-scaleregressionfusionwithExtremeLearn-
ingMachine.AE-HE-BLSTM—BLSTM+featurescreatedthroughdeeplearning.LS—Linearregression+Smoothing.LSB—LeastSquaresBoosting
+Smoothing.SVR+CCRF—SVR+ContinuousConditionalRandomFields.
Method Arousal Valence
RMSE ρ RMSE ρ
BLSTM-RNN[60] .12±0.06 .66±0.25 .17±0.09 .12±0.54
BLSTM-ELM[60] .12±0.05 .63±0.27 .15±0.08 .15±0.47
LSTM-RNN[61] .12±0.06 .61±0.28 .19±0.10 .03±0.50
LSTM-RNN[61] .12±0.06 .60±0.29 .19±0.10 .02±0.49
LS[62] .12±0.05 .65±0.22 .17±0.09 .01±0.50
LSB[62] .12±0.05 .59±0.23 .17±0.09 .05±0.43
SVR[63] .12±0.05 .56±0.27 .19±0.10 −0.02±0.45
SVR+CCRF[64] .12±0.05 .54±0.27 .17±0.09 .02±0.43
AE-HE-BLSTM[60] .12±0.06 .52±0.37 .17±0.09 .02±0.51
LSTM-RNN[61] .12±0.06 .61±0.25 .19±0.10 .00±0.50
Baseline .14±0.06 .37±0.26 .18±0.09 −0.01±0.38
doi:10.1371/journal.pone.0173392.t005
paperthatwaspublishedintheproceedings,wherethedetailsoftheapproachareexplained.
Allthemethodsbeatthebaseline,shownonthebottomrow.Thebaselinemethodisamulti-
linearregressionwithopenSMILEfeatures.
Inyear2013and2015,LSTM-RNNbasedsolutionswerethebestbothforarousaland
valence,inyear2014LSTM-basedsolutionwassecondbestforarousal,butbestforvalence.
Inyear2013,alltheteamsuseddifferentfeature-sets.Theresultsareanalyzedindetail
in[48].
Inyear2014,solutions[26]and[55]usedopenSMILEfeature-sets.Therestoftheteams
usedotherfeatures.Thecombinationthatproducedthebestresultforarousal(butworsethan
baselineresultforvalence)[56],wasacombinationofaKalmanfilterandlow-levelfeatures:
MFCCs,zero-crossingrate,spectralflux,centroid,rolloff,andspectralcrestfactor.
Table5showsonly10bestsolutionsfor2015.Eachofthe12teamssubmitted3runs,which
createsmorethan30differentsolutions,someofwhichwereonparwiththebaseline.Allof
thesolutionslistedusethebaselineopenSMILEfeature-set,butitisusuallytransformed,or
newfeaturesareadded.
Evaluationofthemachinelearningalgorithms
Inthissection,wedescribeanevaluationofthealgorithmsonthesamefeature-set(thebase-
linefeaturesofyear2015).
Table6showstheevaluationofthealgorithmsparticipatingin2015challengeonthisfea-
ture-set.10bestapproachesarereported.TheperformanceintermsofRMSEforarousalisthe
sameforallthesolutions(thoughcorrelationcoefficientisdifferent),indicatingthatthealgo-
rithmsmighthavereachedsomesortofceilinginperformancewiththiscombinationofanno-
tationsandfeatures.
ThealgorithmsaresortedbytheirperformanceaccordingtoRMSEonarousalascending
(RMSEincreasesandperformancedecreases).Thealgorithmsshowverygoodperformance
onarousalandcompletelyunsatisfactoryperformanceonvalence.Itisaknownissue,that
valenceismuchmoredifficulttomodelthanarousal,butnottotheextentthatweobserve.
In2013and2014,valenceandarousalannotationswerehighlycorrelatedwhereasin2015,
theywerenot.Wehypothesizethatduetothehighcorrelationthealgorithmsdidnottrainto
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 13/22

### Page 14

Developingabenchmarkforemotionalanalysisofmusic
Table6.Performanceofthedifferentalgorithmsforarousalandvalence,usingthebaselinefeature-set.Combo—AnunweightedcombinationofLS,
LSBandBoostedensembleofsinglefeaturefilters.
Method Arousal Valence
RMSE ρ ρ RMSE ρ ρ
c c
BLSTM-RNN[60] .12±.06 .66±.25 .30±.24 .15±.08 .15±.47 .06±.17
BLSTM-ELM[60] .12±.05 .63±.27 .25±.22 .15±.08 .15±.47 .06±.17
LR+S[62] .12±.05 .65±.22 .32±.23 .17±.09 .01±.50 .01±.19
LSB[62] .12±.05 .59±.23 .30±.24 .17±.09 .05±.43 .01±.18
LSTM-RNN[61] .12±.06 .61±.25 .31±.26 .19±.10 .00±.50 .01±.20
Combo[62] .12±.05 .64±.23 .28±.22 .17±.09 .00±.48 .01±.19
SVR[63] .12±.05 .56±.27 .31±.25 .19±.10 −0.02±.45 .00±.18
SVR+CCRF[64] .12±.05 .52±.30 .22±.22 .17±.10 .00±.43 .00±.13
LSTM-RNN[65] .12±.06 .59±.24 .30±.23 .18±.09 .03±.48 .00±.20
SVR[60] .12±.07 .56±.24 .08±.08 .15±.09 .01±.40 .00±.04
Baseline-FNN .12±.08 .45±.22 .25±.20 .14±.13 .00±.41 .04±.16
doi:10.1371/journal.pone.0173392.t006
recognizevalence-specificcuesandcouldnotperformwellontheevaluation-set.Fig6shows
thescatterplotsoftheannotationsalongwithregressionlines.
AlmostallthesolutionslistedinTable6areeitherbasedonLSTM-RNNnetworksorSVR.
ExceptionaresolutionssuggestedbyteamSAILUSC[62],whicharebasedonlinearregression
withsmoothing,orleastsquaresboosting.LSTM-RNNnetworksarecapableofincorporating
localcontextintheirpredictions.Asmoothingstepalsoincorporatesthecontext,thoughit
cannotlearnthedependenciesintime-series.WealsoprovideabaselineFeed-ForwardNeu-
ralNetword(FNN)—dropout-regularizedneuralnetwiththreehiddenlayers.Withoutany
smoothingstep,thefeed-forwardneuralnetdemonstratesworseperformanceintermsof
Fig6. Distributionofthelabelsonarousal-valenceplanefora)development-setb)evaluation-set.
doi:10.1371/journal.pone.0173392.g006
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 14/22

### Page 15

Developingabenchmarkforemotionalanalysisofmusic
Pearson’scorrelationcoefficient.Withmedian-filtersmoothingappliedtoresults,thecorrela-
tioncoefficientforarousalissimilartotherestoftheapproaches(0.57±0.24).
Evaluationofthefeature-sets
Inthissection,wewillanalyzethefeaturesproposedbytheteamsin2015throughbuildinga
systemusingthesamemachinelearningalgorithm,butdifferentfeature-sets.Wechosethe
bestperformingalgorithmofpreviousyears—LSTM-RNN.
Weconstructedanetworkwiththreehiddenlayerswith250,150and50nodes,similarto
thearchitectureusedbyICLteam.Weusedthenumberofmemoryblocksineachhidden
layer,thelearningrate(LR),andthestandarddeviationoftheGaussiannoiseappliedtothe
inputactivations,whichwereoptimizedforourdatabytheICLteam[61].Everylayerwas
pretrained(inasupervisedway)beforethenextlayerwasaddedandthenetworkwastrained
again.Weused20-foldcross-validationforevaluatingresults.
Proposedfeatures. Avarietyofsoftwareforaudiosignalprocessingandfeatureextrac-
tionwasusedbyparticipants:Marsyas,MIRToolboxforMatlab,PsySound,openSMILE,
Essentia,jAudio.Mostly,participantsusedthefeaturesthatareknowntobeimportantfor
emotionrecognition,suchasMFCCs,tempo,loudness,lowlevelspectralfeaturesrelatedto
timbre.Fewnovelfeatureswereproposed.Kumaretal.[51]proposedthreenewtypesoffea-
tures:compressibilityfeatures,whichdescribehowmuchtheaudiocanbecompressed,
medianspectralbandenergy,whichdescribesthespectralbandwidthoftheaudio.Thecom-
pressibilityofaudiowasstronglypositivelycorrelatedwithstaticarousalratings(Pearson’s
r=0.656).Caietal.[66]proposededgeorientationhistogramsonmel-frequency
spectrogram.
Resultsondevelopmentandevaluation-setcross-validation. Table7showstheevalua-
tionofthefeature-setsonvalence,orderedbyConcordanceCorrelationCoefficientofthe
resultsonevaluation-set,descending.Thebestperformingfeature-setforvalence(byJUNLP
team)isabaselinefeature-setwithfeatureselectionappliedtoittofindthefeaturesoptimized
forvalencerecognition.Thesecondbestfeature-set,suggestedbyPKUAIPLteam,consisted
ofthebaselinefeature-setwithanadditionofthreetypesoffeatures:MFCCsandΔMFCCs,
edge-orientationhistogramsandstandardlow-levelspectralfeatures.Inaddition,team
PKUAIPLappliedauto-regressiveandmovingaveragefilterstothefeaturestoaccountforthe
temporalchangesinmusic,andaddedtheoutputasnewfeaturestothefeaturevector.Team
Table7.Performanceofthedifferentfeature-setsonvalence,developmentandevaluation-setsof2015,20foldcross-validation.
Method Development-set Evaluation-set
RMSE ρ ρ RMSE ρ ρ
c c
JUNLP(2)[67] .26±.15 .22±.51 .09±.24 .27±.13 .19±.35 .08±.15
PKUAIPL[64] .22±.13 .33±.50 .16±.27 .27±.14 .16±.35 .07±.20
HKPOLYU[63] .21±.13 .41±.53 .20±.28 .28±.14 .19±.36 .06±.17
JUNLP(3)[67] .26±.15 .23±.53 .09±.24 .28±.13 .17±.33 .06±.14
UNIZA(1)[68] .22±.14 .32±.50 .16±.27 .29±.14 .14±.37 .06±.14
ICL[61] .22±.13 .30±.50 .15±.27 .30±.14 .12±.40 .06±.16
JUNLP(1)[67] .22±.14 .32±.50 .15±.27 .28±.13 .12±.39 .05±.15
UNIZA(2)[68] .23±.14 .31±.49 .15±.26 .29±.16 .09±.40 .05±.17
IRIT-SAMOVA[65] .23±.14 .33±.50 .16±.27 .29±.15 .08±.41 .05±.16
MIRUtrecht[69] .24±.15 .30±.49 .13±.23 .29±.14 .11±.43 .04±.15
doi:10.1371/journal.pone.0173392.t007
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 15/22

### Page 16

Developingabenchmarkforemotionalanalysisofmusic
Table8.Performanceofthedifferentfeature-setsonarousal,developmentandevaluation-setsof2015,20foldcross-validation.
Method Development-set Evaluation-set
RMSE ρ ρ RMSE ρ ρ
c c
HKPOLYU[63] .20±.12 .48±.47 .23±.28 .22±.12 .39±.41 .24±.26
THU-HCSIL[60] .21±.13 .46±.42 .22±.26 .27±.12 .33±.40 .16±.22
IRIT-SAMOVA(3)[65] .21±.13 .49±.43 .21±.27 .24±.13 .52±.37 .25±.25
IRIT-SAMOVA[65] .21±.12 .45±.44 .21±.27 .24±.12 .43±.30 .22±.22
JUNLP(1)[67] .21±.12 .45±.43 .19±.26 .24±.12 .52±.31 .26±.24
UNIZA(2)[68] .22±.12 .41±.44 .19±.25 .24±.12 .48±.32 .26±.24
PKU-AIPL[64] .21±.12 .40±.44 .19±.26 .23±.10 .52±.30 .32±.27
UNIZA(1)[68] .22±.12 .40±.44 .19±.25 .25±.13 .49±.30 .27±.23
JKU-Tinnitus(2)[70] .22±.13 .39±.45 .19±.26 .30±.14 .06±.38 .04±.17
JKU-Tinnitus(1)[70] .22±.12 .38±.43 .19±.26 .29±.14 .09±.39 .05±.15
doi:10.1371/journal.pone.0173392.t008
HKPOLYUsuggestedasupervisedtransformationonthebaselinefeature-set(valence–arousal
similaritypreservingembedding).Thistransformationmapshigh-dimensionalfeaturevectors
toalower-dimensionalspacesothatforsimilarsongs(intermsofvalenceorarousal)thefea-
turevectorsarealsocloserinthislow-dimensionalspace.
Table8showstheevaluationofthefeature-setsonarousal,orderedbyConcordanceCorre-
lationCoefficientoftheresultsofdevelopment-set,descending.TeamsHKPOLYU,THU-HC-
SILandIRIT-SAMOVAsuggestedthebestfeaturesforarousal.Thefeaturesbytheteam
HKPOLYUwerealreadydescribedabove.TeamTHU-HCSILappliedDeepBeliefNetworks
toasetoffeaturesextractedwithopenSMILEandMIRToolbox,inordertolearnthehigher
representationforeachgroupfeaturesindependently,whichwerethenfusedbyaspecialauto-
encoderwithamodifiedcostfunctionconsideringsparseandheterogeneousentropy,topro-
ducethefinalfeaturesatarateof2Hzforthesucceedingregression.TeamIRIT-SAMOVA
couldachieveaverygoodperformancewithaverysimplefeature-setconsistingof6measure-
mentsonbandsofaBarkscaleforspectralvalley,andspectralflatnessonERBandBarkscale,
foratotalofonly8features.Spectralflatnessprovidesawaytoquantifyhownoise-likea
soundis.Spectralvalleyisafeaturederivedfromtheso-calledspectralcontrastfeature,which
representstherelativespectraldistribution.
Discussionsandperspectives
Duringthethreeyearsoforganizingthe‘EmotioninMusic’taskatMediaEval,changeswere
introducedtothedatacollectionroutine,whichledtotheimprovementofthequalityofthe
annotations.Inthefirsttwoyearsofthebenchmark,thesizeofthesegmentwaschosenin
suchawaythatbothstaticanddynamicratingswerepossible.Thisresultedinacompromise,
whichledtoselectingthewindowof45seconds,whichappearstobetooshorttocapturealot
ofemotionalvariation,andtoolongtomakeestimatingthestaticemotionunambiguous.In
2015,weoptedforfull-lengthsongs.Incombinationwithpreliminarylisteningandmore
carefulselectionofworkers,thequalityoftheannotationswasimproved.However,full-length
songsmightalsonotbetheoptimalsolutionbecausetheannotationprocedureisvery
demandingandrequiresalotofconcentration,andthereisadangerthatfull-lengthsong
annotationstretchesthelimitsofwhathumanannotatorsarecapableof.Thisquestion
requiresmoreinvestigation.Also,in2015weemployedadynamicMERmethodandmanual
filteringtoselectsongswithmoreemotionalvariety,inparticularsongsintheupperleftand
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 16/22

### Page 17

Developingabenchmarkforemotionalanalysisofmusic
lowerrightquadrantsoftheVAspace.Thisledtoadifferentdistributionoflabels,which
allowedtoidentifyproblemswithvalencerecognition.
Estimatingtheabsolutevalueofanemotioninrealtimecouldbedifficultfortheannota-
tors,andoftenthedirectionofchangeisindicatedcorrectlywhereasthemagnitudeisnot.We
proposedtoalleviatethisproblembyoffsettingtheannotationsintothesamebiasusingthe
overallemotionofthesong(asannotatedseparately).
Thevalence–arousalmodelconsideredinthebenchmarkhasbeenwidelyadoptedin
researchonaffectivecomputing[2,38,71–73].However,themodelisnotfreeofcriticisms
andsomeotheralternativesmaybeconsideredinthefuture.Forexample,theVAmodelhas
beencriticizedforbeingtooreductionistandthatotherdimensionssuchasdominanceshould
beadded[74].Moreover,theterms‘valence’and‘arousal’maybesometimestooabstractfor
peopletohaveacommonunderstandingofitsmeaning.SuchdrawbacksoftheVAmodelcan
furtherharmtheinter-annotatoragreementoftheannotationsforanannotationtaskwhichis
alreadyinherentlyfairlysubjective.
Inthebenchmark,weresampledtheannotationstoeither1Hzor2Hz.Thisledtobench-
markparticipantsusing1or0.5secondwindowsasthemainunitofemotionprediction.As
farasmusicalemotionisusuallycreatedonbiggertimescales,thebestalgorithmsfordynamic
MERwerethosethatcouldincorporatethebiggercontext,througheitheralgorithmdesign
(LSTM-RNN)orsmoothingstepappliedatalaterstage.Anotherwayofperformingdynamic
MERistofirstsegmenttheemotionalsegmentsorusedifferentunits,suchasscores,foremo-
tionrecognition[75].
Thebestfeature-setsthatweresuggestedforthetasktreatedpredictingvalenceandarousal
separately,andsuggestedseparatefeatureselectionordimensionalityreductionstepsforeach
emotionaldimension.Again,itwasshownthatthougharousalcanbesuccessfullymodeled
justwithsimpletimbralfeatures(spectralvalleyandspectralflatness),modelingvalenceis
muchmorecomplex,andsatisfactoryperformancewasnotachievedbyanyofthealgorithms.
Itisknownthatemotionperceptionishighlysubjective,especiallyforvalence[2].There-
fore,insteadoftakingtheaveragevaluesoftheemotionalannotationsasthegroundtruthand
trainingageneralizedmodelforpredictingthem,wemightwanttohavealookattheraw
annotationsandinvestigatethedifferenceacrosstheannotators.Forexample,itispossible
thattwosongswithsimilaraverageratingswouldhavedifferentvariancesintherawannota-
tion,andthatitisbettertoexplicitlymodelthevariancecomputationally[27,72].Itisalso
possibletobuildpersonalizationtechniquesforcustomizedMERpredictions[76,77],though
toourbestknowledgelittlehasbeendonetopersonalizeadynamicMERmodel.
AsshowninTable1,theDEAMdatasetcontainsrichextrameta-dataaboutthesongsand
theannotators,suchasthegenrelabelsofthesongs,thefamiliarityandlikingofeachofthe
annotatedsongsforeachannotators,andeventhepersonalitytraitsoftheannotators(in
2014).Suchinformationcanbestudiedandexploitedinfuturework.
AlthoughthebenchmarkismainlydesignedfordynamicMER,theannotations,afterbeing
summarizedovertime,canalsobeusefulforstaticMER.Wealsoexpectthedatasetcanfacili-
tatetheapplicationanddevelopmentofothermid-tohigh-levelaudioandnon-audiofeatures
(e.g.[78,79]),andothermachinelearningalgorithms(e.g.thatbetteraccountfortemporal
dynamicsorpersonaldifferences)inthecontextofMER.
Emotionrecognitionfromaudiovisualsignalsisataskthatisrelatedtorecognizingthe
spontaneousemotionalexpressions.Coutinhoetal.[80]demonstratedthatemotionrecogni-
tionmodelscanbetransferredfromspeechtomusicandviceversa.Asaresult,therearepar-
allelsbetweenthewinningmodelsinAVECchallengesthatareaddressingemotion
recognitionfromhumanbehaviorandtheonesaddressingEmotioninMusictask.Inboth
cases,fine-tunedLSTMrecurrentneuralnetworksarethebestperformingmodels[60,81].
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 17/22

### Page 18

Developingabenchmarkforemotionalanalysisofmusic
Conclusions
Inthispaper,weanalyzedandsummarizedourfindingsindevelopinganewbenchmarkfor
emotionalanalysisinmusic.Analyzingthreeyearsofannotationsondynamicemotionrecog-
nition,wefoundthemtobedemandinginneedofveryconscientiousandwelltrainedannota-
tors.Weonlysucceededinacquiringhighqualitylabelsonacrowdsourcingplatformafter
directlyengagingwithworkersandprovidingfeedbackinadditiontoafairandmutually
agreedcompensation.Wefoundthattheresultsarelesssensitivetothetypeofacousticfea-
tures,ifwetakeenoughofthemintoaccount.Recurrentneuralnetworksandparticularly
LSTMisveryeffectiveincapturingthedynamicchangesinemotioninmusicfromacoustic
features.
WereleasethedataunderNonCommercialCreativeCommons(BY-NC)andwehope
thatthisbenchmarkincludingitsdatasetandevaluationmetricshelpsacceleratingresearchin
MER.
Acknowledgments
WewouldliketothankErikM.Schmidt,MikeN.Caro,Cheng-YaSha,AlexanderLansky,
Sung-YenLiuandEduardoCountinhofortheircontributionsinthedevelopmentofthistask.
WealsothankthetaskparticipantsandtheanonymousTurkers,withoutwhomthebench-
markwouldnothappen.
AuthorContributions
Conceptualization:MSAAYY.
Datacuration:AAMSYY.
Formalanalysis:AAMSYY.
Fundingacquisition:MS.
Investigation:AAMSYY.
Methodology:MSAAYY.
Resources:MSYYAA.
Software:AAMS.
Visualization:AA.
Writing–originaldraft:AAMS.
Writing–review&editing:AAMSYY.
References
1. InskipC,MacfarlaneA,RaffertyP.Towardsthedisintermediationofcreativemusicsearch:analysing
queriestodetermineimportantfacets.InternationalJournalonDigitalLibraries.2012;12(2):137–147.
doi:10.1007/s00799-012-0084-1
2. YangYH,ChenHH.Machinerecognitionofmusicemotion:Areview.ACMTransactionsonIntelligent
SystemsandTechnology.2012;3(3).doi:10.1145/2168752.2168754
3. KimYE,SchmidtEM,MignecoR,MortonBG,RichardsonP,ScottJ,etal.Musicemotionrecognition:
Astateoftheartreview.In:ProceedingsofInternationalSocietyforMusicInformationRetrievalConfer-
ence;2010.p.255–266.
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 18/22

### Page 19

Developingabenchmarkforemotionalanalysisofmusic
4. LaurierC,LartillotO,EerolaT,ToiviainenP.Exploringrelationshipsbetweenaudiofeaturesandemo-
tioninmusic.In:ProceedingsofTriennalConferenceofEuropeanSocietyforCognitiveSciencesof
Music;2009.p.260–264.
5. YangYH,LinYC,SuYF,ChenHH.Aregressionapproachtomusicemotionrecognition.IEEETrans-
actionsonAudio,Speech,andLanguageProcessing.2008;16(2):448–457.doi:10.1109/TASL.2007.
911513
6. EerolaT.Modellingemotionsinmusic:Advancesinconceptual,contextualandvalidityissues.In:Pro-
ceedingsofAESInternationalConfernece;2014.
7. BarthetM,FazekasG,SandlerM.Multidisciplinaryperspectivesonmusicemotionrecognition:Implica-
tionsforcontentandcontext-basedmodels.In:ProceedingsofInternationalSymposiumonComputer
MusicModelling&Retrieval;2012.p.492–507.
8. HuX,YangYH.Cross-datasetandcross-culturalmusicmoodprediction:AcaseonWesternandChi-
nesePopsongs.IEEETransactionsonAffectiveComputing.2016;PP(99):1.doi:10.1109/TAFFC.
2016.2523503
9. VuoskoskiJK,EerolaT.Measuringmusic-inducedemotion:Acomparisonofemotionmodels,person-
alitybiases,andintensityofexperiences.MusicaeScientiae.2011;15(2):159–173.doi:10.1177/
1029864911403367
10. AljanakiA,WieringF,VeltkampRC.ComputationalmodelingofinducedemotionusingGEMS.In:Pro-
ceedingsofInternationalSocietyforMusicInformationRetrievalConference;2014.p.373–378.
11. HuX,DownieJS,LaurierC,BayM,EhmannAF.The2007MIREXAudioMoodClassificationTask:
Lessonslearned.In:ProceedingsofInternationalSocietyforMusicInformationRetrievalConference;
2008.p.462–467.
12. SchubertE.UpdateoftheHevneradjectivechecklist.PerceptualMotorSkills.2003;96:1117–1122.
doi:10.2466/pms.2003.96.3c.1117PMID:12929763
13. LaurierC,SordoM,SerràJ,HerreraP.Musicmoodrepresentationsfromsocialtags.In:Proceedings
ofInternationalSocietyforMusicInformationRetrievalConference;2009.p.381–386.
14. RussellJ.Acircumplexmodelofaffect.JournalofPersonalityandSocialPsychology.1980;39:1161–
1178.doi:10.1037/h0077714
15. ThayerRE.TheBiopsychologyofMoodandArousal. NewYork: OxfordUniversityPress;1989.
16. LaurierC,HerreraP.AudioMusicMoodClassificationusingsupportvectormachine.In:MIREXtask
onAudioMoodClassification;2007.
17. GeringerJM,MadsenCK,GregoryD.Afifteen-yearhistoryoftheContinuousResponseDigitalInter-
face:Issuesrelatingtovalidityandreliability.BulletinoftheCouncilforResearchinMusicEducation.
2004;160:1–15.
18. SchubertE.Continuousresponsetomusicusingatwodimensionalemotionspace.In:Proceedingsof
InternationalConferenceofMusicPerceptionandCognition;1996.p.263–268.
19. SchubertE.Modelingperceivedemotionwithcontinuousmusicalfeatures.MusicPerception:AnInter-
disciplinaryJournal.2004;21(4):561–585.doi:10.1525/mp.2004.21.4.561
20. KorhonenMD,ClausiDA,JerniganME.Modelingemotionalcontentofmusicusingsystemidentifica-
tion.IEEETransactionsonSystems,Man,andCybernetics.2006;36(3):588–599.doi:10.1109/
TSMCB.2005.862491PMID:16761812
21. CabreraD.PsySound:Acomputerprogramforpsychoacousticalanalysis.ProceedingsofAustralian
AcousticalSocietyConference.1999;p.47–54.
22. SchmidtEM,KimYE.Predictionoftime-varyingmusicalmooddistributionsusingKalmanfiltering.In:
ProceedingsofIEEEInternationalConferenceonMachineLearningandApplications;2010.p.655–
660.
23. SchmidtEM,KimYE.Modelingmusicalemotiondynamicswithconditionalrandomfields.In:Proceed-
ingsofInternationalSocietyforMusicInformationRetrievalConference;2011.
24. PandaR,PaivaRP.Usingsupportvectormachinesforautomaticmoodtrackinginaudiomusic.In:Pro-
ceedingsof130thAudioEngineeringSocietyConvention;2011.
25. ImbrasaiteV,BaltrusˇaitisT,RobinsonP.Emotiontrackinginmusicusingcontinuousconditionalran-
domfieldsandrelativefeaturerepresentation.In:ProceedingsofIEEEInternationalConferenceon
MultimediaandExpoWorkshops;2013.p.1–6.
26. ImbrasaiteV,BaltrusˇaitisT,RobinsonP.CCNFforcontinuousemotiontrackinginmusic:Comparison
withCCRFandrelativefeaturerepresentation.In:ProceedingsofIEEEInternationalConferenceon
MultimediaandExpo.;2014.
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 19/22

### Page 20

Developingabenchmarkforemotionalanalysisofmusic
27. WangJC,YangYH,WangHM,JengSK.TheAcousticEmotionGaussiansmodelforemotion-based
musicannotationandretrieval.In:ProceedingsofACMInternationalConferenceonMultimedia;2012.
p.89–98.
28. MarkovK,IwataM,MatsuiT.MusicemotionrecognitionusingGaussianprocesses.In:WorkingNotes
ProceedingsoftheMediaEval2013Workshop;2013.
29. NicolaouMA,GunesH,PanticM.Continuouspredictionofspontaneousaffectfrommultiplecuesand
modalitiesinvalence-arousalspace.IEEETransactionsonAffectiveComputing.2011;2(2):92–105.
doi:10.1109/T-AFFC.2011.9
30. SpeckJA,SchmidtEM,MortonBG,KimYE.Acomparativestudyofcollaborativevs.traditionalmusical
moodannotation.In:ProceedingsofInternationalSocietyforMusicInformationRetrievalConference;
2011.
31. SchullerB,ValstarM,EybenF,McKeownG,CowieR,PanticM.Avec2011–thefirstinternational
audio/visualemotionchallenge.In:InternationalConferenceonAffectiveComputingandIntelligent
Interaction.Springer;2011.p.415–424.
32. SchullerB,ValsterM,EybenF,CowieR,PanticM.AVEC2012:thecontinuousaudio/visualemotion
challenge.In:Proceedingsofthe14thACMinternationalconferenceonMultimodalinteraction.ACM;
2012.p.449–456.
33. ValstarM,SchullerB,SmithK,EybenF,JiangB,BilakhiaS,etal.AVEC2013:thecontinuousaudio/
visualemotionanddepressionrecognitionchallenge.In:Proceedingsofthe3rdACMinternational
workshoponAudio/visualemotionchallenge.ACM;2013.p.3–10.
34. ValstarM,SchullerB,SmithK,AlmaevT,EybenF,KrajewskiJ,etal.Avec2014:3ddimensionalaffect
anddepressionrecognitionchallenge.In:Proceedingsofthe4thInternationalWorkshoponAudio/
VisualEmotionChallenge.ACM;2014.p.3–10.
35. RingevalF,SchullerB,ValstarM,CowieR,PanticM.AVEC2015:The5thInternationalAudio/Visual
EmotionChallengeandWorkshop.In:ProceedingsofACMInternationalConferenceonMultimedia;
2015.p.1335–1336.
36. McKeownG,ValstarM,CowieR,PanticM,SchroderM.TheSEMAINEDatabase:AnnotatedMulti-
modalRecordsofEmotionallyColoredConversationsbetweenaPersonandaLimitedAgent.IEEE
TransactionsonAffectiveComputing.2012Jan;3(1):5–17.doi:10.1109/T-AFFC.2011.20
37. RingevalF,SondereggerA,SauerJ,LalanneD.IntroducingtheRECOLAmultimodalcorpusofremote
collaborativeandaffectiveinteractions.In:AutomaticFaceandGestureRecognition(FG),201310th
IEEEInternationalConferenceandWorkshopson;2013.p.1–8.
38. KoelstraS,Mu¨hlC,SoleymaniM,LeeJS,YazdaniA,EbrahimiT,etal.DEAP:Adatabaseforemotion
analysisusingphysiologicalsignals.IEEETransactionsonAffectiveComputing.2012;3(1):18–31.doi:
10.1109/T-AFFC.2011.15
39. ChenYA,WangJC,YangYH,ChenHH.TheAMG1608datasetformusicemotionrecognition.In:Pro-
ceedingsofIEEEInternationalConferenceonAcoustics,SpeechandSignalProcessing;2015.p.693–
697.
40. BittnerR,SalamonJ,TierneyM,MauchM,CannamC,BelloJP.MedleyDB:Amultitrackdatasetfor
annotation-intensiveMIRresearch.In:ProceedingsoftheInternationalSocietyforMusicInformation
RetrievalConference;2014.
41. AljanakiA,YangYH,SoleymaniM.EmotioninMusictaskatMediaEval2015.In:WorkingNotesPro-
ceedingsoftheMediaEval2015Workshop;2015.
42. SoleymaniM,LarsonM.Crowdsourcingforaffectiveannotationofvideo:Developmentofaviewer-
reportedboredomcorpus.In:WorkshoponCrowdsourcingforSearchEvaluation;2010.
43. MorrisJD.SAM:TheSelf-AssessmentManikinanefficientcross-culturalmeasurementofemotional
response.JAdvertisingResearch.1995;35(8):63–68.
44. McKeownGJ,SneddonI.Modelingcontinuousself-reportmeasuresofperceivedemotionusinggener-
alizedadditivemixedmodels.PsychologicalMethods.2014;19(1):155–174.doi:10.1037/a0034282
PMID:24219542
45. AljanakiA,WieringF,VeltkampRC.Studyingemotioninducedbymusicthroughacrowdsourcing
game.InformationProcessingandManagement.2016;52(1):115–128.doi:10.1016/j.ipm.2015.03.004
46. SchubertE.Reliabilityissuesregardingthebeginning,middleandendofcontinuousemotionratingsto
music.PsychologyofMusic.2013;41(3):350–371.doi:10.1177/0305735611430079
47. BachorikJP,BangertM,LouiP,LarkeK,BergerJ,RoweR,etal.Emotioninmotion:Investigatingthe
time-courseofemotionaljudgmentsofmusicalstimuli.MusicPerception.2009;26(4):355–364.doi:10.
1525/mp.2009.26.4.355
48. SoleymaniM,AljanakiA,YangYH.EmotionalAnalysisofMusic:Acomparisonofmethods.In:Pro-
ceedingsofACMInternationalConferenceonMultimedia;2014.
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 20/22

### Page 21

Developingabenchmarkforemotionalanalysisofmusic
49. SoleymaniM,CaroMN,SchmidtEM,YangYH.TheMediaEval2013BraveNewTask:Emotionin
Music.In:WorkingNotesProceedingsoftheMediaEval2013Workshop;2013.
50. AljanakiA,YangYH,SoleymaniM.EmotioninMusictaskatMediaEval2014.In:WorkingNotesPro-
ceedingsoftheMediaEval2014Workshop;2014.
51. KumarN,GuptaR,GuhaT,VazC,vanSegbroeckM,KimJ,etal.Affectivefeaturedesignandpredict-
ingcontinuousaffectivedimensionsfrommusic.In:WorkingNotesProceedingsoftheMediaEval2014
Workshop;2014.
52. LinLIK.Aconcordancecorrelationcoefficienttoevaluatereproducibility.Biometrics(InternationalBio-
metricSociety).1989;45(1):255–268.PMID:2720055
53. EybenF,WeningerF,GrossF,SchullerB.RecentdevelopmentsinopenSMILE,theMunichOpen-
sourceMultimediaFeatureExtractor.In:ProceedingsofACMInternationalConferenceonMultimedia;
2013.p.835–838.
54. WeningerF,EybenF,SchullerB.TheTUMApproachtotheMediaEvalMusicEmotionTaskUsing
GenericAffectiveAudioFeatures.In:WorkingNotesProceedingsoftheMediaEval2013Workshop;
2013.
55. CoutinhoE,WeningerF,SchullerB,SchererKR.TheMunichLSTM-RNNapproachtotheMediaEval
2014EmotioninMusicTask.In:WorkingNotesProceedingsoftheMediaEval2014Workshop;2014.
56. MarkovK,MatsuiT.Dynamicmusicemotionrecognitionusingstate-spacemodels.In:WorkingNotes
ProceedingsoftheMediaEval2014Workshop;2014.
57. AljanakiA,WieringF,VeltkampRC.MIRUtrechtparticipationinMediaEval2013:EmotioninMusic
Task.In:WorkingNotesProceedingsoftheMediaEval2013Workshop;2013.
58. YangW,CaiK,WuB,WangY,ChenX,YangD,etal.BeatsenssolutionforMediaEval2014Emotion
inMusicTask.In:WorkingNotesProceedingsoftheMediaEval2014Workshop;2014.
59. FanY,XuM.MediaEval2014:THU-HCSILapproachtoemotioninmusictaskusingmulti-levelregres-
sion.In:WorkingNotesProceedingsoftheMediaEval2014Workshop;2014.
60. XuM,LiX,XianyuH,TianJ,MengF,ChenW.Multi-scaleapproachestotheMediaEval2015“Emotion
inMusic”Task.In:WorkingNotesProceedingsoftheMediaEval2015Workshop;2015.
61. CoutinhoE,TrigeorgisG,ZafeiriouS,SchullerB.Automaticallyestimatingemotioninmusicwithdeep
long-shorttermmemoryrecurrentneuralnetworks.In:WorkingNotesProceedingsoftheMediaEval
2015Workshop;2015.
62. GuptaR,NarayananS.Predictingaffectinmusicusingregressionmethodsonlowlevelfeatures.In:
WorkingNotesProceedingsoftheMediaEval2015Workshop;2015.
63. LiuY,LiuY,GuZ.Affectivefeatureextractionformusicemotionprediction.In:WorkingNotesProceed-
ingsoftheMediaEval2015Workshop;2015.
64. CaiK,YangW,ChengY,YangD,ChenX.PKU-AIPLsolutionforMediaEval2015EmotioninMusic
Task.In:WorkingNotesProceedingsoftheMediaEval2015Workshop;2015.
65. PellegriniT,BarriereV.Time-continuousestimationofemotioninmusicwithrecurrentneuralnetworks.
In:WorkingNotesProceedingsoftheMediaEval2015Workshop;2015.
66. CaiK,YangW,ChengY,YangD,ChenX.PKU-AIPL’SolutionforMediaEval2015EmotioninMusic
Task.In:WorkingNotesProceedingsoftheMediaEval2015Workshop;2015.
67. PatraBG,MaitraP,DasD,BandyopadhyayS.MediaEval2015:MusicEmotionRecognitionbasedon
feed-forwardneuralnetwork.In:WorkingNotesProceedingsoftheMediaEval2015Workshop;2015.
68. ChmulikM,GuothI,MalikM,JarinaR.UNIZAsystemforthe“EmotioninMusic”taskatMediaEval
2015.In:WorkingNotesProceedingsoftheMediaEval2015Workshop;2015.
69. AljanakiA,WieringF,VeltkampR.MediaEval2015:Asegmentation-basedapproachtocontinuous
emotiontracking.In:WorkingNotesProceedingsoftheMediaEval2015Workshop;2015.
70. WeberM,KrismayerT,Wo¨ßJ,Aigmu¨llerL,BirnzainP.MediaEval2015:JKU-Tinnitusapproachto
EmotioninMusicTask.In:WorkingNotesProceedingsoftheMediaEval2015Workshop;2015.
71. HuqA,BelloJP,RoweR.Automatedmusicemotionrecognition:Asystematicevaluation.Journalof
NewMusicResearch.2010;39(3):227–244.doi:10.1080/09298215.2010.513733
72. WangJC,YangYH,WangHM,JengSK.ModelingtheaffectivecontentofmusicwithaGaussianmix-
turemodel.IEEETransactionsonAffectiveComputing.2015;6(1):56–68.doi:10.1109/TAFFC.2015.
2397457
73. SoleymaniM,LarsonM,PunT,HanjalicA.Corpusdevelopmentforaffectivevideoindexing.IEEE
TransactionsonMultimedia.2014;16(4):1075–1089.doi:10.1109/TMM.2014.2305573
74. CollierG.Beyondvalenceandactivityintheemotionalconnotationsofmusic.PsychologyofMusic.
2007;35(1):110–131.doi:10.1177/0305735607068890
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 21/22

### Page 22

Developingabenchmarkforemotionalanalysisofmusic
75. AljanakiA,WieringF,VeltkampRC.Emotionbasedsegmentationofmusicalaudio.In:Proceedingsof
InternationalSocietyforMusicInformationRetrievalConference;2015.
76. SuD,FungP.Personalizedmusicemotionclassificationviaactivelearning.In:ProceedingsofACM
InternationalWorkshoponMusicInformationRetrievalwithUser-CenteredandMultimodalStrategies;
2012.p.51–62.
77. ChenYA,WangJC,YangYH,ChenHH.Linearregression-basedadaptationofmusicemotionrecogni-
tionmodelsforpersonalization.In:ProceedingsofIEEEInternationalConferenceAcoustics,Speech&
SignalProcessing;2014.p.2149–2153.
78. SchmidtEM,KimYE.Learningrhythmandmelodyfeatureswithdeepbeliefnetworks.In:Proceedings
ofInternationalSocietyforMusicInformationRetrievalConference;2013.
79. PandaR,RochaB,PaivaR.Dimensionalmusicemotionrecognition:Combiningstandardandmelodic
audiofeatures.In:ProceedingsofInternationalSymposiumonComputerMusicModelling&Retrieval;
2013.
80. CoutinhoE,DengJ,SchullerB.Transferlearningemotionmanifestationacrossmusicandspeech.In:
2014InternationalJointConferenceonNeuralNetworks(IJCNN);2014.p.3592–3598.
81. HeL,JiangD,YangL,PeiE,WuP,SahliH.MultimodalAffectiveDimensionPredictionUsingDeep
BidirectionalLongShort-TermMemoryRecurrentNeuralNetworks.In:Proceedingsofthe5thInterna-
tionalWorkshoponAudio/VisualEmotionChallenge.AVEC’15.NewYork,NY,USA:ACM;2015.
p.73–80.
PLOSONE|DOI:10.1371/journal.pone.0173392 March10,2017 22/22
