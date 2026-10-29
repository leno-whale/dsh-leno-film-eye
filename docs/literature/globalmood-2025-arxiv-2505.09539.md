---
来源文件 / Source PDF: `globalmood-2025-arxiv-2505.09539.pdf`
提取日期 / Extracted: 2026-10-30
提取方式 / Method: pdfplumber 文本层直接提取（非 OCR）
PDF 页数 / Pages: 9
总字符数 / Characters: 41545
PDF 元数据标题 / Metadata title: GlobalMood: A cross-cultural benchmark for music emotion recognition
PDF 元数据作者 / Metadata author: Harin Lee; Elif Çelen; Peter Harrison; Manuel Anglada-Tort; Pol van Rijn; Minsu Park; Marc Schönwiesner; Nori Jacoby
---
## 引用信息 / Citation (APA 7th)

> Lee, H., Çelen, E., Harrison, P., Anglada-Tort, M., van Rijn, P., Park, M., Schönwiesner, M., & Jacoby, N. (2025). GlobalMood: A cross-cultural benchmark for music emotion recognition. *arXiv preprint* arXiv:2505.09539. https://arxiv.org/abs/2505.09539


## 正文（按页提取 / Extracted page by page）

### Page 1

GLOBALMOOD: A CROSS-CULTURAL BENCHMARK FOR MUSIC
EMOTION RECOGNITION
HarinLee1,2,3 ElifÇelen1 PeterHarrison4 ManuelAnglada-Tort5
PolvanRijn1 MinsuPark6 MarcSchönwiesner3 NoriJacoby1,7
1MPIEmpiricalAesthetics 2MPIforHumanCognitiveandBrainSciences
3LeipzigUniversity 4UniversityofCambridge 5Goldsmiths,UniversityofLondon
6NewYorkUniversityAbuDhabi 7CornellUniversity
ABSTRACT context[3–5],andforgeneratingmusicthatresonateswith
individual preferences [6]. More broadly, understanding
Humanannotationsofmoodinmusicareessentialformu-
how music conveys emotion is a core question in the sci-
sic generation and recommender systems. However, ex-
ence of music [7–9]. To date, however, most algorithms
istingdatasetspredominantlyfocusonWesternsongswith
havebeentrainedondatasetsderivedfromWesternlisten-
termsderivedfromEnglish,whichmaylimitgeneralizabil-
ersandWesternmusic, usingtaxonomiesprimarilybased
ityacrossdiverselinguisticandculturalbackgrounds. We
onEnglishlanguage(e.g.,MIREX[10]).
introduce‘GlobalMood’,anovelcross-culturalbenchmark
A significant challenge is creating cross-cultural mod-
datasetcomprising1,180songssampledfrom59countries,
els capable of handling non-Western music and emotion
withlarge-scaleannotationscollectedfrom2,519individ-
vocabularies beyond English. Addressing this challenge
uals across five culturally and linguistically distinct loca-
isessentialtodevelopingalgorithmsthataccuratelyreflect
tions: U.S.,France,Mexico,S.Korea,andEgypt. Rather
global users’ preferences, including those whose musical
than imposing predefined emotion and mood categories,
tastes extend beyond the limited range of styles currently
weimplementabottom-up,participant-drivenapproachto
represented in training datasets. Moreover, without cap-
organicallyelicitculturallyspecificmusic-relatedemotion
turing culturally specific nuances of emotion, especially
terms. Wethenrecruitanotherpoolofhumanparticipants
those difficult to translate, key aspects of musical mean-
to collect 988,925 ratings for these culture-specific de-
ingmaybemissedentirely. Directdictionarytranslations
scriptors. Ouranalysisconfirmsthepresenceofavalence-
of English terms may be insufficient, as terms describing
arousal structure shared across cultures, yet also reveals
emotions are deeply cultural and may lack exact equiva-
significant divergences in how certain emotion terms (de-
lents[11–14].
spite being dictionary equivalents) are perceived cross-
Toaddresstheseissues,weintroduce‘GlobalMood’,1
culturally. State-of-the-artmultimodalmodelsbenefitsub-
anewbenchmarkdatasetdesignedtosupportculturallyin-
stantiallyfromfine-tuningonourcross-culturallybalanced
clusiveandlinguisticallydiverseemotionandmoodrecog-
dataset,particularlyinnon-Englishcontexts. Broadly,our
nition in music. Our contribution innovates along three
findingsinformtheongoingdebateontheuniversalityver-
keydimensions: (i)thediversityofmusicalstimuli,drawn
sus cultural specificity of emotional descriptors, and our
from 59 countries; (ii) the diversity of annotators, span-
methodologycancontributetoothermultimodalandcross-
ning five distinct regions (with plans to extens to over 20
lingualresearch.
languages and locations in future); (iii) a data-driven ap-
proachforcollectingdescriptors,generatedorganicallyby
1. INTRODUCTION
participants in their own language during the annotation
Music evokes diverse emotional responses in listeners, process.
spanning a wide spectrum beyond basic emotional cate- Datawerecollectedthroughtwostagesinvolvingato-
gories [1,2]. A central challenge in Music Information tal of 2,519 participants and 1,180 songs balanced evenly
Retrieval(MIR)isdesigningalgorithmsthatcanreplicate across 59 countries: In the first stage (Section 4.1; Fig-
thisemotionalsensitivity. Thisiscrucialforbuildingrec- ure1), usingasmallersubsetof200songs, weemployed
ommendationsystemsthatalignwithlisteners’moodand our recently developed iterative task that combines open-
ended elicitation with collective refinement [13,15,16].
Rather thanasking listenersto choosefrom afixed listof
©H.Lee,E.Çelen,P.Harrison,M.Anglada-Tort,P.van
pre-definedemotionterms,weaskedthemtodescribethe
Rijn,M.Park,M.Schönwiesner,andN.Jacoby. LicensedunderaCre-
perceived emotion conveyed in the music using free-text
ativeCommonsAttribution4.0InternationalLicense(CCBY4.0).Attri-
bution:H.Lee,E.Çelen,P.Harrison,M.Anglada-Tort,P.vanRijn,M. tagsintheirnativelanguage,andatthesametime,ratethe
Park,M.Schönwiesner,andN.Jacoby,“GlobalMood: Across-cultural
benchmarkformusicemotionrecognition”,inProc. ofthe26thInt. So- 1All code and data: https://github.com/harin-git/
cietyforMusicInformationRetrievalConf.,Daejeon,SouthKorea,2025. GlobalMood
5202
nuJ
82
]RI.sc[
2v93590.5052:viXra

### Page 2

Figure1.Elicitationandrefinementofmusicemotiontermsthroughiterativeparticipantchains.(A)Schematicillustration
ofthecollaborativetaggingprocesswithinaparticipantchain. Participantscontributenewemotion-relatedwordtagsfor
eachsong, ratetherelevanceofexistingtags, andcanalsoflagirrelevantcontent, creatingadynamicrefinementsystem.
(B) Twenty most reliable emotion tags in each language, ranked by their tag scores. Y-axis labels display tags in their
originallanguage(left)andEnglishtranslations(right).
tagsprovidedbypreviouslisteners.Thisapproachwaskey clude the widely used MIREX 2007 mood dataset [10]
touncoveringemotiontermsthatwouldotherwisebeover- with240-250Westernsongsinfivemoodclustersderived
looked by predefined, English-based taxonomies (such as from AllMusic’s English tags (e.g., ‘passionate–rousing’,
‘appeal/plead’thatappearsinKoreanonly). ‘wistful–bittersweet’),andCAL500[17]with500Western
Inthesecondstage(Section4.2;Figure2),weselected pop/rocksongsannotatedusing18Englishmoodtermsby
the top 20 elicited terms per language and crowdsourced U.S.undergraduatelisteners.Overtime,largerdatasetsap-
ratings for each tag across the entire set of 1,180 songs. peared:theDEAMcorpus(MediaEval‘EmotioninMusic’
Thisresultedinatotalof988,925ratings,creatingthemost dataset [18]) containing 2,058 song excerpts with contin-
comprehensive open-source cross-cultural emotion anno- uous valence/arousal annotations; mood tags mined from
tation dataset in Music Emotion Recognition (MER) to large corpora of Spotify music playlists [19]; and the
date. MTG-Jamendo dataset [20], which provides mood/theme
WeleveragedGlobalMoodtotestseveralrecentmulti- tagsfor18,486songs.Notably,Jamendo’stagswerefreely
modal and multilingual models (Gemini, CLAP) by eval- crowdsourced(56uniquemoodlabels), whichintroduced
uating their performance under zero-shot, few-shot, and morelabelvarietybutstillalmostentirelyinEnglish.
fine-tuned scenarios (Section 4.3; Figure 3). Models A common limitation across these datasets is their re-
trained only on English data performed poorly in some liance on predefined English descriptors, many of which
cultural contexts, but fine-tuning with our cross-cultural stem from Western music psychology (for an exception,
data greatly improved their performance in non-English see Strauss et al. [21]). For instance, the Geneva Emo-
settings. This highlights the critical importance of cross- tional Music Scale (GEMS) defines 45 emotion descrip-
culturaldatainbothtrainingMERmodelsandestablishing tors (e.g., ‘joyful activation’) based on studies with Eu-
appropriatebenchmarksfortheirevaluation. ropean listeners [1], and this taxonomy has been used to
annotate datasets like Emotify [22]. Similarly, the mood
2. RELATEDWORKS categoriesinMIREXandCAL500werefixedinadvance
(drawnfromAllMusicorpriorliterature)andpresentedto
2.1 MusicEmotionandMoodAnnotationDatasets
annotatorsasaclosedsetofoptions. Consequently,these
Several datasets have been developed for MER systems top-down approaches restrict annotators to the moods the
withvaryingannotationapproaches.2 Earlyexamplesin- researchersenvisioned,leavinganyunlistedmoodnuances
2Notethatdatabasesoftenextendtheconceptofemotiontoinclude perspective,whileacknowledgingthatsubtledistinctionsbetweenthem
relatedconstructssuchasmoodorfeeling. Hereweadoptthisbroader doexist.

### Page 3

Figure 2. Association between emotion terms across languages. (A) MDS visualization of the emotion terms based
on mean ratings across the full song set. Terms positioned closer together exhibit similar rating patterns across songs,
suggesting similar interpretations across languages. (B) Comparison of terms with direct translation equivalents across
languages. Theareasizeindicatesthedegreeofsemanticdivergencedespiteapparenttranslationequivalence.
uncapturedandundocumented. MIR tasks, including emotion recognition. These mod-
Acknowledging these limitations, recent research has elscombinethereasoningcapabilitiesofLLMswithaudio
begun exploring MER beyond the Western-centric scope. perceptionsystems (audioLLMs), enablingmoreflexible
Huetal.[23]examinedmoodannotationsofK-popsongs andnuancedmusicunderstandingthantraditionalclassifi-
provided by both Korean and American listeners. Their cationapproaches[24–26].
approach involved translating the original MIREX mood ModelslikeMuLan[27]andMERT[24]havedemon-
categoriesintoKoreanforlocalannotators. Althoughthis strated potential for zero-shot music emotion and mood
alloweddirectcomparisonsofmoodclassificationbetween classificationbyembeddingaudioandnaturallanguagede-
KoreanandAmericanlisteners,itinherentlyrestrictedKo- scriptions in a shared semantic space. However, compre-
reanannotationstotermsoriginallydefinedwithinWestern hensive benchmarks such as the MuChoMusic [25] high-
contexts. lightacruciallimitation: thesemodelsrelyheavilyonlan-
More recently, we compiled a balanced set of Ameri- guagemodalityanddonotattendsufficientlytoaudio,of-
can, Brazilian, and Korean songs and gathered mood an- ten failing with more nuanced audio examples for down-
notations across nine categories, where annotators rated stream MIR tasks. This limitation could be particularly
songsbothfromtheirownandtheothertwocountries[12]. critical for non-Western music and non-English emotion
We showed that certain mood terms like ‘energetic’ and descriptors, given that their training data are largely from
‘sad’arehighlyconsistentacrosscultures,whilemoreab- Westerncontexts.
stractconceptslike‘love’and‘dreamy’divergeconsider- Similarly, closed-source models (e.g., Gemini) have
ably. Similar findings have been reported by other stud- shownpromiseinpsychologicaltextualanalysisinmulti-
ies [13,14], highlighting that when mood descriptors are lingualcontexts[28],whileevaluationsinspecializeddo-
imposedfromonelanguageontoanother,importantmean- mainssuchasMIRremainscarce. Theproprietarynature
ingscansimplybe‘lostintranslation’. of their training data complicates thorough assessment of
Insummary,whileexistingMERdatasetsandresearch cross-lingualorcross-culturalperformance. Weaimtoad-
havelaidasolidgroundwork,theyremainlimitedbyinsuf- dressthesefundamentalgapsbyprovidingalargesetofdi-
ficientlinguisticandculturaldiversity. Becausemanyare verse, multilingual descriptors and annotations to support
predominantlyEnglish-basedandrelyontop-downanno- broadercross-culturalgeneralizabilityofaudioLLMs.
tation strategies, they may overlook how people in other
culturalcontextsperceiveemotionandmoodinmusic.
3. METHOD
2.2 AudioLLMs: theNewFrontierinMusicTagging 3.1 Participants
Recent advances in multimodal large language models We recruited two independent sets of participants across
(LLMs) have opened promising avenues for downstream the two stages of our data collection: Stage 1 for emo-

### Page 4

tiontermelicitation(N=778; seeSection4.1)andStage We also fine-tuned CLAP on GlobalMood (train–test
2 for subsequent ratings on top 20 terms (N = 1,741; split = 1,000:180) to assess potential performance im-
see Section 4.2). Participants had to be at least 18 years provements. Topreservethecontinuousnatureofourrat-
old, reside in the target country, and speak the target lan- ings, we represented each term in proportion to its mean
guageastheirprimarylanguage. ParticipantsfromtheUS rating (e.g., the term ‘calm’, with a mean rating of 3.0,
were recruited through Prolific, while participants from appeared three times in the text). This method retained
the other four countries (France, Mexico, S. Korea, and the nuanced information in our soft labels rather than re-
Egypt) were recruited through the CINT platform. All ducing them to binary categories. To improve generaliz-
participantsprovidedinformedconsentunderanapproved ability, we created 10 augmented variations of each song
protocol (see Section 7). Participants were instructed to through pitch shifting (range of ±3 semitones), loudness
wear headphones and had to pass a headphone screening adjustment (range of ±15dB), and the addition of Gaus-
task [29], and a language proficiency test [30] before be- sian noise (amplitude of 0.005). Each augmented variant
ing eligible for the main experimental task. Experiments randomlyincludedoneortwoofthesemodifications.
wereconductedineachparticipant’snativelanguage(En-
glish, French, Spanish, Korean, and Egyptian Arabic),
4. RESULTS
with instructions translated using GPT-4o. Code to repli-
cate the experiment through the PsyNet framework [31] 4.1 Bottom-upTermElicitationAcrossLanguages
and all data are available at https://github.com/
4.1.1 Taggingpipeline
harin-git/GlobalMood
Many existing studies on music emotions rely on pre-
3.2 GloballyRepresentativeSongSelection defined taxonomies or web-scraped data that offer lim-
itedlinguisticdiversity[10,19]. Toovercomethislimita-
Tocreateagloballyrepresentativemusicdataset,weused
tion,weemployedabottom-up,participant-driventagging
weekly YouTube top 100 music charts (year 2017-2023)
method[13,15,16]. Specifically,weaskedparticipantsin
from59countries,spanningsixcontinents.Toensureeach
eachcountrytocompleteindependent‘chains’ofiterative
country’s charts reflected its distinct popular music, we
annotations. A subsample of 200 songs from the 1,180
excluded any track appearing in more than one country’s
entire set was used as stimuli. This subsample consisted
chart. Thisleftuswithacountry-exclusivepoolofsongs.
of180balancedsongsacrosscountries,withanadditional
Fromthispool,wesampled20songspercountry,yielding
20localsongsdrawnfromtheparticipatingcountry’spool.
1,180songsintotal.Thisdiversesetisdesignedtocapture
Thiswastoensurethatlocalparticipantsencounterenough
a wide range of musical traditions and serve as a robust
musicstronglytiedtotheirbackground,allowingthemto
testbed for cross-cultural emotion recognition. Each 15-
elicitculturallyspecificemotiondescriptors.
secondaudioexcerptwastrimmedfromarandomstarting
Figure1Aillustratesonesuchchain:(i)Thefirstpartic-
pointinthefulltrack,andnormalizedat-5dBloudness.
ipantannotatesthesongusingsingle-wordemotiontagsin
theirnativelanguage;(ii)Thesecondparticipant(fromthe
3.3 ModelEvaluation samecountry)ratestherelevanceofthesetags(1–5scale),
flagirrelevanttags(e.g.,genre-orlyrics-relatedratherthan
WeusedtheresultingGlobalMooddatasettoevaluatesev-
emotion), add new tags as necessary; (iii) The third par-
eralrecentmultimodalandmultilingualmodelscapableof
ticipant sees all tags from earlier participants and repeats
music understanding. Specifically, we assessed Google’s
these steps; (iv) This iterative process continues through
Gemini models (1.5 Flash, 2.0 Flash, and the latest 2.5
tenparticipantsperchain,systematicallyrefiningandval-
Pro),afamilyofmultimodallargelanguagemodelscapa-
idating emotion terms. In each country, we ran the entire
bleofprocessingandreasoningacrosstextandaudio(but
alsoimageandvideo).3 Wecomparedzero-shotandfew- elicitation experiment twice and aggregated the results to
increase the diversity of responses from a larger pool of
shotapproaches,wherethelatterincluded10human-rated
participants.
emotiontermsasexamples.
Given that Gemini is closed-source, we also included
4.1.2 Topemergingterms
CLAP (Contrastive Language-Audio Pretraining) [34] as
an alternative, open-source model that learns joint audio- Following the removal of tags flagged by more than two
textembeddings.CLAPhasdemonstratedpromiseinMIR participants in a chain, our STEP-Tag process yielded
applications [35] and serves as the foundation for music- an extensive, culturally specific lexicon of emotion terms
specific models like CLaMP [36]. Here, we conducted acrosslanguages(Nuniqueterms: English=644;French
zero-shot evaluations through: (1) extracting audio em- = 528; Spanish = 870; Korean = 629; Arabic = 283). To
beddings from CLAP, (2) computing cosine similarities identifythemostsalienttermsineachlanguage,wecalcu-
with text embeddings of emotion terms, and (3) compar- lated a composite score for every term by multiplying its
ingthesescorestohumanratings. frequency of occurrences across chains by its mean rele-
vancerating.Higherscoresindicatetermsfrequentlymen-
3Preliminarytestswithotherrecentmultimodalmodelsshowedper- tionedandconsistentlyratedashighlyrelevant.
formanceissues—Flamingo2[32]struggledwithratingconsistencyand
We consolidated closely related morphological vari-
GPT-4o[33]failedtogeneratemusicaldescriptionsorratingsfromaudio
alone—thusweexcludedthemfromfurtheranalysis. ants (e.g., ‘happy’ and ‘happiness’ in English; gendered

### Page 5

forms such as ‘joyeux’ and ‘joyeuse’ in French) manu- Spearman-Brown formula. Effectively, r serves as
within
allywithnativespeakers. Figure1Bpresentstheresulting measurement error to compare as baselines when evalu-
20 highest-ranking tags per language, displaying both the atingr .
between
original word and English translations to facilitate cross- The term calm showed the highest average agreement
culturalcomparisons. (r = 0.52 [0.49, 0.55]; r = 0.49 [0.38, 0.57]),
between within
Despite being explicitly asked to provide emotion followedbyfun(r =0.46[0.39,0.53];r =0.44
between within
terms, participants often gave broader affective descrip- [0.27, 0.54]), love (r = 0.44 [0.41, 0.47]; r =
between within
torslikemoodsorfeelings(e.g.,‘soft’and‘festive’). This 0.47[0.33, 0.66]), sad (r =0.41[0.37, 0.45]; r
between within
aligns with prior MIR literature that often includes both =0.43[0.32,0.58]),rhythmic(r =0.38[0.30,0.45];
between
emotion and mood, and given its relevance for practical r = 0.43 [0.25, 0.53]), and notably happy (r =
within between
use,wedidnotenforceastrictdistinction. 0.37[0.28,0.45];r =0.45[0.24,0.59]).
within
Overall, considering within-country agreement (mean
4.2 Large-scaleDiverseHumanRatings r = 0.43–0.48), most of these terms were compara-
within
ble in their between-country agreement (mean r =
4.2.1 Cross-culturalratingsacrosstheentireset between
0.39–0.52). However, despite being considered a basic
Having identified the top 20 terms for each language, we universal human emotion [37], happy exhibited a consid-
nextgatheredexhaustiveratingsfortheentire1,180songs erable gap between between- and within-country agree-
ofGlobalMood. Werecruited1,741newparticipants(see ment. This emphasizes the necessity of incorporating di-
Section 3.1) who listened to the 15-second excerpts and verse cultural perspectives when modeling nuanced mu-
ratedhoweffectivelyeachexcerptconveyedagivenemo- sical emotional responses. Reliance on either dictionary
tionandmoodterm(1–5scale). Foreachstimulus,partic- translationorLLM-basedtranslationalonecouldoverlook
ipants evaluated seven randomly selected terms from the important, context-specific nuances in emotion and mood
relevant language set. This systematic approach ensured perception—particularly relevant when building models
that,onaverage,eachsongineachlanguagereceived8.38 forglobalaudiences.
(SD=2.40)uniqueparticipantratings,resultinginanex-
tensive collection of 988,925 ratings spanning across five
languages.
4.2.2 Is‘happy’inmylanguagethesame‘happy’inyour
language?
To investigate differences in how each culture interprets
these terms, we constructed 100 rating vectors (5 lan-
guages×20termsperlanguage). Eachvectorwas1,180-
dimensional, capturing the mean rating per term across
the 1,180 song set. We then performed non-metric mul-
tidimensional scaling (MDS) using correlation as the dis-
tancemetric,projectingthesevectorsinatwo-dimensional
space. Inthisemotion‘space,’termsthatpositioncloseto
oneanother—eventhosefromdifferentlanguages—reflect
similar rating patterns across the musical examples, sug-
gesting comparable emotional interpretations across cul-
tures.
Figure 2A visualizes this emotion space. The terms
Figure3. Correlationsbetweenhumanratingsandmulti-
cluster into two main regions: one region of high arousal
modal model predictions. (A) Gemini models with zero-
andhighvalence(e.g.,happy,energetic,andlively;upper
shot prompting showing increase in performance with
regionofthefigure)andasecondregionoflowarousalthat
newer models. (B) CLAP models in zero-shot and fine-
spanspositivevalence(e.g.,peaceful;bottomleft)toneg-
tuned scenarios showing how the use of multilingual an-
ative (e.g., sad; bottom right). Notably, many translated
notations can substantially increase performance. Gray
‘equivalents’ appear close together, which might suggest
dashed lines represent split-half reliability of human rat-
a general cross-cultural consensus on what music evokes
ingsusingtheSpearman-Brownformulaasbaselinerefer-
whatemotions.
enceofcorrelationsachievedbetweenhumans. Errorbars
However, examining six commonly shared terms that
indicate95%CIofmeancorrelationacrosssongs.
have direct translations in at least four of the five lan-
guages (fun, happy, rhythmic, love, sad, and calm) re-
vealed varying degrees of cross-cultural agreement (see
4.3 Humanvs. MultimodalModels
Figure 2B). For each of these terms, between-country
agreement(r )wascomputedastheaverageofpair- Recent benchmarks have evaluated the capabilities of au-
between
wise correlation coefficients, while within-country agree- dioLLMsacrossvariousdownstreamMIRtasks,butthese
ment(r )wascalculatedusingsplit-halfreliabilitywith evaluations have also been restricted to English [25]. We
within

### Page 6

evaluated both closed-source (Gemini) and open-source increase was observed for French (from 0.07 to 0.17; z =
(CLAP)modelsagainstourGlobalMoodmultilingualhu- 0.10). These observations demonstrate the promising po-
manratings(seeSection3.3formodeldetails). tentialofhownative-languagetermsandratingsfromour
ForGemini(Figure3A),wereplicatedourhumanstudy GlobalMooddatasetcanbeusedtogeneralizetonewcul-
protocol by prompting the model with ‘Rate from a scale turesandlanguages,whenmodelingMERsystems.
of 1 to 5 how well this song expresses or conveys the
emotion[...]’ independentlyforthefivenativelanguages. 5. DISCUSSION
We then evaluated how well the model’s outputs predict
We introduce GlobalMood, a novel cross-cultural bench-
human judgments. We observed consistent improvement
mark dataset comprising emotion and mood descriptors
with each new model version. The earliest model, 1.5
andratingscollectedfromalargeandgloballydiversepar-
Flash, demonstrated modest alignment with human judg-
ticipant pool through a data-driven approach. Consistent
ments (mean correlation across countries: r = 0.34 (95%
withpreviousresearchinmusicconsumptionandpercep-
CI=[0.27,0.42]). Thismodelstruggledparticularlywith
tion[39–44]andmusicemotion[12–14,45,46],ourfind-
Koreanlanguageratings(r =0.27[0.21,0.33]). Thesub-
ings highlight both cross-cultural similarities and differ-
sequent 2.0 Flash version bridged this gap in Korean (r
ences. Specifically, we demonstrate that music emotion
= 0.42 [0.36, 0.47]), and achieved a substantially higher
descriptorsacrosslanguagesarebroadlyorganizedaround
mean correlation of r = 0.42 [0.36, 0.48]. The latest 2.5
clustersrelatingtovalenceandarousal[8,37].
Pro model demonstrated another leap with a mean corre-
Relying on dictionary translations for music emotion
lation of r = 0.50 [0.45, 0.55]. Few-shot approach with
termsmayfacelimitations(e.g.,[45]),wherecross-lingual
10 human-rated examples using 2.5 Pro did not improve
agreementvariedacrossterms.Forinstance,despitehappy
theresults(r =0.47[0.42,0.52]). Thisconsistentupward
being a basic emotion, it exhibited a relatively large gap
trajectoryacrossmodeliterationsprovidescompellingevi-
betweencross-andwithin-countryagreement. Thishigh-
dencethatthesegeneral-purposesystemsareprogressively
lights the need for incorporating multilingual descriptors
developing more sophisticated understanding of musical
from diverse annotators. Our future work aims to expand
emotionsacrossdiverselinguisticandculturalcontexts.
GlobalMood to reach over 20 languages [30,47] and a
This level of correlations between Gemini and human
broaderrangeofmusicalstyles,includingworksfromdif-
ratingsareonparwithalgorithmsspecificallydesignedfor
ferent historical periods, which will be critical for devel-
MER, such as Spotify’s mood estimation [12,38]. More-
opingmorerobusttoolsthatcangeneralizeacrossdiverse
over, given the subjective nature of emotion and mood
culturalcontexts.
perception in music (where even humans often disagree),
Notably, fine-tuning CLAP on cross-cultural data sig-
thelatestGeminimodelalreadyreacheshuman-levelper-
nificantly boosted performance in non-English contexts,
formance, matching the theoretical upper bound defined
highlighting the value of GlobalMood. These findings
byinter-raterhumanagreement(graydashedlinesinFig-
point to the potential for culturally-sensitive MER sys-
ure3).
tems, moving beyond one-size-fits-all models. Future
For CLAP, an open-source alternative (Figure 3B), we work should investigate more varied prompting and data
evaluated both a zero-shot approach and a fine-tuned ver- augmentation techniques, and alternative LLM architec-
sion trained on our GlobalMood dataset (see Section 3.3 tures.
forfine-tuningdetails). Thezero-shotapproachmeasured Ourtaggingpipelineisquicktodeployacrosscultures
thesimilaritybetweentheemotionterm’stextembedding and uses a bottom-up approach that helps minimize re-
and the song’s audio embedding. This zero-shot CLAP searcher bias. This offers an advantage over predefined
performedpoorly(meanr=0.08[0.03,0.13]),whilefine- termlists,whichoftenfailtocapturetheculturalsubtleties
tuning with GlobalMood substantially improved the per- of emotion terms [48]. However, it has drawbacks: early
formance(meanr=0.31[0.19,0.44]). Asacontrolexper- participants can bias the tag pool and there’s no theoret-
iment,wealsofine-tunedCLAPusingadatasetwhereall ical guarantee that all tags reflect clear emotion concepts
non-English emotion terms were first translated into En- (e.g.,‘étranger’inFrench). Unlikestructuredsystemsfor
glish using an LLM without any musical context (instead crowdsourcing tags (e.g., TagATune [49]), our approach
oforiginalemotiontermscollectedfromnativespeakers). tradescontrolforflexibilityandculturalresponsiveness.
This translation-based approach failed to improve perfor- BeyondMIR,theGlobalMoodandassociatedpipeline
mance (mean r = 0.13 [-0.05, 0.32]), showing that the offer timely implications for broader multimodal and
performancegainsfromfine-tuningcomefromculturally- cross-lingual research, particularly in Natural Language
specificinformationratherthanfrommereincreaseindata Processing (NLP) communities [50]. As NLP increas-
volume. inglytacklesmultimodaltasksinvolvingaudio–textmod-
Importantly, improvements through finetuning were elingandcross-culturalapplications,ourdatasetmaypro-
most pronounced for non-English languages. Based on vide a useful benchmark for evaluating language–audio
Fisher’sztestforcorrelationcomparisons,Arabicshowed models across diverse contexts. The iterative annotation
the largest increase from r = 0.11 to 0.46 (z = 0.39), fol- pipeline can also serve as an effective framework for col-
lowed by Spanish (from 0.04 to 0.32; z = 0.29) and Ko- lectingrepresentativesamplesandannotationsinotherdo-
rean (from 0.06 to 0.32; z = 0.27). The least substantial mains[15,16,31,51].

### Page 7

6. ACKNOWLEDGMENTS [7] P. N. Juslin and D. Västfjäll, “Emotional responses to
music: Theneedtoconsiderunderlyingmechanisms,”
H.L. was funded by the Max Planck Society. M.P. was
Behavioralandbrainsciences,vol.31,no.5,pp.559–
partiallysupportedbytheNYUADCenterforInteracting
575,2008.
UrbanNetworks(CITIES),fundedbyTamkeenunderthe
NYUADResearchInstituteAwardCG001. [8] T.EerolaandJ.K.Vuoskoski,“Areviewofmusicand
emotion studies: Approaches, emotion models, and
7. ETHICSSTATEMENT stimuli,”MusicPerception: AnInterdisciplinaryJour-
nal,vol.30,no.3,pp.307–340,2012.
We conducted our human experiment according to ethi-
cal best practices. All participants recruited via Prolific [9] M. Park, J. Thom, S. Mennicken, H. Cramer, and
orCINTprovidedinformedconsentbasedonanapproved M.Macy,“Globalmusicstreamingdatarevealdiurnal
protocol (Max Planck Ethics Council #202142). Partic- and seasonal patterns of affective preference,” Nature
ipantdatawascollectedanonymously(exceptforProlific humanbehaviour,vol.3,no.3,pp.230–236,2019.
orCINTIDs),andallpublisheddataarefullyanonymized.
Models were accessed through commercial APIs, with [10] X. Hu and J. S. Downie, “Exploring mood metadata:
fine-tuning performed locally. Conducting cross-cultural Relationshipswithgenre,artistandusagemetadata,”in
research requires sensitivity to diverse ethical considera- International Society for Music Information Retrieval
tions [52], and this study was designed accordingly. We Conference,Dec2007.
acknowledge that machine learning models and training
[11] J. C. Jackson, J. Watts, T. R. Henry, J.-M. List,
datasetsmaycontainbiasesoriginatingfromparticipants,
R.Forkel,P.J.Mucha,S.J.Greenhill,R.D.Gray,and
data selection processes, and the models themselves. De-
K. A. Lindquist, “Emotion semantics show both cul-
spitethesepotentialbiases,ourstudyaimstoaddresscrit-
tural variation and universal structure,” Science, vol.
icallimitationsandsocietalriskswithincurrentMIRtech-
366,no.6472,pp.1517–1522,2019.
nologies,whichpredominantlyfocusonEnglish-language
music and raters despite serving diverse global popula- [12] H. Lee, F. Höger, M. Schönwiesner, M. Park, and
tions[48,53,54]. N. Jacoby, “Cross-cultural mood perception in pop
songs and its alignment with mood detection algo-
8. REFERENCES rithms,”inProceedingsoftheInternationalSocietyfor
Music Information Retrieval Conference, Nov 2021,
[1] M. Zentner, D. Grandjean, and K. R. Scherer, “Emo-
pp.366–373.
tions evoked by the sound of music: Characteriza-
tion,classification,andmeasurement,”Emotion,vol.8, [13] E. Celen, P. van Rijn, H. Lee, and N. Jacoby,
no.4,pp.494–521,2008. “Are expressions for music emotions the same
across cultures?” 2025. [Online]. Available: https:
[2] A. S. Cowen, X. Fang, D. Sauter, and D. Keltner,
//arxiv.org/abs/2502.08744
“What music makes us feel: At least 13 dimensions
organizesubjectiveexperiencesassociatedwithmusic
[14] J. S. Gómez-Cañón, E. Cano, P. Herrera, and
acrossdifferentcultures,”ProceedingsoftheNational
E. Gómez, “Joyful for you and tender for us: the in-
AcademyofSciences, vol.117, no.4, pp.1924–1934,
fluence of individual characteristics and language on
Jan2020.
emotion labeling and classification,” in Proceedings
of the International Society of Music Information Re-
[3] T.EerolaandP.Saari,“Whatemotionsdoesmusicex-
trievalConference,Oct2020.
press? structureofaffecttermsinmusicusingiterative
crowdsourcingparadigm,” PLOSONE,vol.20, no.1,
[15] R. Marjieh, P. van Rijn, I. Sucholutsky, T. R. Sumers,
p.e0313502,Jan2025.
H. Lee, T. L. Griffiths, and N. Jacoby, “Words are all
[4] H. Tran, T. Le, A. Do, T. Vu, S. Bogaerts, and you need? language as an approximation for human
B.Howard,“Emotion-awaremusicrecommendation,” similarity judgments,” in The Eleventh International
inProceedingsoftheAAAIConferenceonArtificialIn- ConferenceonLearningRepresentations,2023.
telligence,vol.37,no.13,2023,p.13.
[16] P. van Rijn, S. Mertes, K. Janowski, K. Weitz, N. Ja-
[5] J. Kang and D. Herremans, “Are we there yet? a coby, and E. André, “Giving robots a voice: Human-
brief survey of music emotion prediction datasets, in-the-loopvoicecreationandopen-endedlabeling,”in
models and outstanding challenges,” 2024. [Online]. Proceedings of the 2024 CHI Conference on Human
Available: https://arxiv.org/abs/2406.08809 FactorsinComputingSystems,2024,pp.1–34.
[6] Y. Sun, M. Kuo, X. Wang, W. Li, and Q. Bai, [17] D. Turnbull, L. Barrington, D. Torres, and G. Lanck-
“Emotion-conditioned MusicLM: Enhancing emo- riet, “Towards musical query-by-semantic-description
tional resonance in music generation,” in 2024 IEEE usingtheCAL500dataset,”inProceedingsofthe30th
Congress on Evolutionary Computation (CEC), Jun annual international ACM SIGIR conference on Re-
2024,pp.1–8. search and development in information retrieval, ser.

### Page 8

SIGIR ’07. New York, NY, USA: Association for [28] S. Rathje, D.-M. Mirea, I. Sucholutsky, R. Marjieh,
ComputingMachinery,Jul2007,pp.439–446. C.E.Robertson,andJ.J.VanBavel,“GPTisaneffec-
tive tool for multilingual psychological text analysis,”
[18] A. Aljanaki, Y.-H. Yang, and M. Soleymani, “Devel-
ProceedingsoftheNationalAcademyofSciences,vol.
oping a benchmark for emotional analysis of music,”
121,no.34,p.e2308950121,Aug.2024.
PLOSONE,vol.12,no.3,p.e0173392,Mar2017.
[29] A. E. Milne, R. Bianco, K. C. Poole, S. Zhao, A. J.
[19] J. Affolter and M. A. Rohrmeier, “Utilizing listener-
Oxenham,A.J.Billig,andM.Chait,“Anonlinehead-
provided tags for music emotion recognition: A data-
phone screening test based on dichotic pitch,” Behav-
driven approach,” in Proceedings of the International
ior Research Methods, vol. 53, no. 4, pp. 1551–1562,
Society for Music Information Retrieval Conference,
2021.
Nov2024,pp.547–554.
[30] P. van Rijn, Y. Sun, H. Lee, R. Marjieh, I. Sucholut-
[20] D. Bogdanov, M. Won, P. Tovstogan, A. Porter,
sky, F. Lanzarini, E. André, and N. Jacoby, “Around
and X. Serra, “The MTG-Jamendo dataset for
theworldin60words:Agenerativevocabularytestfor
automatic music tagging,” in Machine Learning for
onlineresearch,”inProceedingsoftheAnnualMeeting
Music Discovery Workshop, International Conference
oftheCognitiveScienceSociety,2023.
on Machine Learning (ICML 2019), Long Beach,
CA, United States, 2019. [Online]. Available: http: [31] P. M. C. Harrison, R. Marjieh, F. Adolfi, P. van
//hdl.handle.net/10230/42015 Rijn,M.Anglada-Tort,O.Tchernichovski,P.Larrouy-
Maestri, and N. Jacoby, “Gibbs sampling with peo-
[21] H. Strauss, J. Vigl, P.-O. Jacobsen, M. Bayer, F. Ta-
ple,” in Advances in Neural Information Processing
lamini, W. Vigl, E. Zangerle, and M. Zentner, “The
Systems,2020,pp.10659–10671.
Emotion-to-Music mapping atlas (EMMA): A sys-
tematically organized online database of emotion- [32] S. Ghosh, Z. Kong, S. Kumar, S. Sakshi, J. Kim,
ally evocative music excerpts,” Behav. Res. Methods, W. Ping, R. Valle, D. Manocha, and B. Catanzaro,
vol.56,no.4,pp.3560–3577,Apr.2024. “Audio Flamingo 2: An audio-language model
with long-audio understanding and expert reasoning
[22] A. Aljanaki, F. Wiering, and R. C. Veltkamp, “Study-
abilities,” 2025. [Online]. Available: https://arxiv.org/
ing emotion induced by music through a crowdsourc-
abs/2503.03983
ing game,” Information Processing & Management,
vol.52,no.1,pp.115–128,Jan2016. [33] A. Hurst, A. Lerer, A. P. Goucher, A. Perelman,
A. Ramesh, A. Clark, A. Ostrow, A. Welihinda,
[23] X.Hu,J.H.Lee,K.Choi,andJ.S.Downie,“Across-
A. Hayes, A. Radford et al., “GPT-4o system card,”
cultural study on the mood of K-POP songs,” in Pro-
arXivpreprintarXiv:2410.21276,2024.
ceedings of the International Society for Music Infor-
mationRetrievalConference,Oct2014,pp.385–390. [34] Y.Wu,K.Chen,T.Zhang,Y.Hui,T.Berg-Kirkpatrick,
and S. Dubnov, “Large-scale contrastive language-
[24] Y. LI, R. Yuan, G. Zhang, Y. Ma, X. Chen, H. Yin,
audio pretraining with feature fusion and keyword-to-
C. Xiao, C. Lin, A. Ragni, E. Benetos, N. Gyenge,
caption augmentation,” in ICASSP 2023 - 2023 IEEE
R. Dannenberg, R. Liu, W. Chen, G. Xia, Y. Shi,
International Conference on Acoustics, Speech and
W. Huang, Z. Wang, Y. Guo, and J. Fu, “MERT:
Signal Processing (ICASSP). IEEE, Jun. 2023, pp.
Acoustic music understanding model with large-scale
1–5.
self-supervised training,” in The Twelfth International
ConferenceonLearningRepresentations,2024. [35] J.Barnett,H.F.Garcia,andB.Pardo,“Exploringmu-
sical roots: Applying audio embeddings to empower
[25] B. Weck, I. Manco, E. Benetos, E. Quinton,
influenceattributionforagenerativemusicmodel,”in
G. Fazekas, and D. Bogdanov, “MuChoMusic: Eval-
ProceedingsoftheInternationalSocietyforMusicIn-
uating music understanding in multimodal audio-
formationRetrievalConference,Nov2024.
languagemodels,”inProceedingsoftheInternational
Society for Music Information Retrieval Conference, [36] S. Wu, Z. Guo, R. Yuan, J. Jiang, S. Doh, G. Xia,
Nov2024. J. Nam, X. Li, F. Yu, and M. Sun, “CLaMP 3:
Universalmusicinformationretrievalacrossunaligned
[26] S.Doh,K.Choi,J.Lee,andJ.Nam,“LP-MusicCaps:
modalities and unseen languages,” 2025. [Online].
LLM-basedpseudomusiccaptioning,”inProceedings
Available: https://arxiv.org/abs/2502.10362
oftheInternationalSocietyforMusicInformationRe-
trievalConference,2023. [37] P.Ekman, “Aretherebasicemotions?” Psychological
Review,vol.99,no.3,pp.550–553,1992.
[27] Q. Huang, A. Jansen, J. Lee, R. Ganti, J. Y. Li, and
D. P. W. Ellis, “MuLan: A joint embedding of mu- [38] D.Duman,P.Neto,A.Mavrolampados,P.Toiviainen,
sicaudioandnaturallanguage,”inProceedingsofthe and G. Luck, “Music we move to: Spotify audio fea-
International Society for Music Information Retrieval tures and reasons for listening,” PLoS One, vol. 17,
Conference,2022. no.9,p.e0275228,Sep.2022.

### Page 9

[39] N. Jacoby, E. A. Undurraga, M. J. McPherson, soundannotation,”inProceedingsoftheInternational
J.Valdés,T.Ossandón,andJ.H.McDermott,“Univer- ConferenceonMusicInformationRetrieval,2007,pp.
salandnon-universalfeaturesofmusicalpitchpercep- 361–364.
tion revealed by sung reproduction,” Current Biology,
[50] D. Hershcovich, S. Frank, H. Lent, M. de Lhoneux,
vol.29,no.19,pp.3229–3243,2019.
M. Abdou, S. Brandl, E. Bugliarello, L. Cabello Pi-
[40] S. A. Mehr, M. Singh, D. Knox, D. M. Ketter, queras, I. Chalkidis, R. Cui, C. Fierro, K. Margatina,
D. Pickens-Jones, S. Atwood, C. Lucas, A. A. Egner, P.Rust,andA.Søgaard,“Challengesandstrategiesin
N. Jacoby, E. J. Hopkins et al., “Universality and di- cross-culturalNLP,”inProceedingsofthe60thAnnual
versityinhumansong,”Science,vol.366,no.6468,p. MeetingoftheAssociationforComputationalLinguis-
eaax0868,2019. tics (Volume 1: Long Papers), S. Muresan, P. Nakov,
and A. Villavicencio, Eds. Dublin, Ireland: Asso-
[41] N.Jacoby,R.Polak,J.A.Grahn,D.J.Cameron,K.M.
ciation for Computational Linguistics, May 2022, pp.
Lee, R. Godoy, E. A. Undurraga, T. Huanca, T. Thal-
6997–7013.
witzer,N.Doumbiaetal.,“Commonalityandvariation
inmentalrepresentationsofmusicrevealedbyacross- [51] D.-M.Huang,P.VanRijn,I.Sucholutsky,R.Marjieh,
culturalcomparisonofrhythmpriorsin15countries,” and N. Jacoby, “Characterizing similarities and
Nature Human Behaviour, vol. 8, no. 5, pp. 846–877, divergences in conversational tones in humans and
2024. LLMs by sampling with people,” in Proceedings
of the 62nd Annual Meeting of the Association for
[42] P.E.Savage,S.Brown,E.Sakai,andT.E.Currie,“Sta- Computational Linguistics (Volume 1: Long Papers),
tisticaluniversalsrevealthestructuresandfunctionsof L.-W. Ku, A. Martins, and V. Srikumar, Eds.
human music,” Proceedings of the National Academy Bangkok, Thailand: Association for Computational
ofSciences,vol.112,no.29,pp.8987–8992,2015. Linguistics, Aug. 2024, pp. 10486–10512. [Online].
Available: https://aclanthology.org/2024.acl-long.565/
[43] J.H.McDermott,A.F.Schultz,E.A.Undurraga,and
R. A. Godoy, “Indifference to dissonance in native [52] N. Jacoby, E. H. Margulis, M. Clayton, E. Hannon,
amazoniansrevealsculturalvariationinmusicpercep- H.Honing,J.Iversen,T.R.Klein,S.A.Mehr,L.Pear-
tion,”Nature,vol.535,no.7613,pp.547–550,2016. son,I.Peretzetal.,“Cross-culturalworkinmusiccog-
nition: Challenges, insights, and recommendations,”
[44] H. Lee, N. Jacoby, R. Hennequin, and M. Moussal-
MusicPerception,vol.37,no.3,pp.185–195,2020.
lam, “Mechanisms of cultural diversity in urban pop-
ulations,” Nature Communication, vol. 16, no. 1, p. [53] J.Henrich,S.J.Heine,andA.Norenzayan,“Mostpeo-
5192,Jun.2025. ple are not WEIRD,” Nature, vol. 466, no. 7302, pp.
29–29,2010.
[45] A. S. Cowen, X. Fang, D. Sauter, and D. Keltner,
“What music makes us feel: At least 13 dimensions [54] B. Amiri, N. Shahverdi, A. Haddadi, and Y. Ghahre-
organizesubjectiveexperiencesassociatedwithmusic mani,“Beyondthetrends: Evolutionandfuturedirec-
acrossdifferentcultures,”ProceedingsoftheNational tions in music recommender systems research,” IEEE
AcademyofSciences, vol.117, no.4, pp.1924–1934, Access,2024.
2020.
[46] T. Fritz, S. Jentschke, N. Gosselin, D. Sammler,
I. Peretz, R. Turner, A. D. Friederici, and S. Koelsch,
“Universalrecognitionofthreebasicemotionsinmu-
sic,” Current Biology, vol. 19, no. 7, pp. 573–576,
2009.
[47] J.P.Niedermann,I.Sucholutsky,R.Marjieh,E.Celen,
T.Griffiths, N.Jacoby, andP.vanRijn, “Studyingthe
effectofglobalizationoncolorperceptionusingmulti-
lingualonlinerecruitmentandlargelanguagemodels,”
inProceedingsoftheAnnualMeetingoftheCognitive
ScienceSociety,vol.46,2023.
[48] D.E.Blasi,J.Henrich,E.Adamou,D.Kemmerer,and
A.Majid,“Over-relianceonEnglishhinderscognitive
science,”TrendsinCognitiveSciences,vol.26,no.12,
pp.1153–1170,2022.
[49] E. L. M. Law, L. von Ahn, R. B. Dannenberg, and
M. Crawford, “TagATune: A game for music and
