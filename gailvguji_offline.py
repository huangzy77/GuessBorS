# coding=utf-8
from numpy import *
from scipy import stats
from scipy import integrate
import matplotlib.pylab as plt


#需要填入的变量
j=-0.36 #当前的涨跌幅度百分比
b_zhang=1.84 #涨率1换几
b_die=1.96 #跌率1换几
p00=3117.71 #当前的上证值
k=21236   #当前的额度


bf=[-0.63752162945358115, -0.21189285354638068, 0.04848058416959234, 0.035820637866295253, 1.9415012556331526, 0.84399137588176809, 0.15012228367337155, -0.070145788381233587, 0.43033976542422603, 0.36149232489579641, 0.072118501231694873, 2.4023520560044491, -0.74582279883358493, 0.0011866337573650438, -0.39369609994801275, -0.66227266598455825, 1.2393744987971071, -0.73146416946587423, -0.5500012026265283, 0.29343770198625962, 0.054598542456305701, -0.74488195310300365, -0.22611690811467641, -0.58194808562126754, 0.38433412554637769, 0.8969621988530937, -0.40588027363650503, -0.13031675715285401, -0.37493775447435634, -0.0020953905598540727, 0.69444154630096666, -0.96980290007550018, -1.0653953777593457, 0.39287885810016016, -0.54402046471968524, 0.47560627921240994, 0.27794722868998784, -0.68341014414284673, 0.044937994209910709, -0.47257420586703142, -0.5820047321053583, -0.72854553632263197, -1.0127776971105054, 2.0055848246832855, 2.3329089164452395, -0.29070552340494638, -1.3626787193431042, 0.26770325277788631, -0.55770713387227033, -0.38071239157430919, -1.1240262318423948, 0.8661830787604069, -0.22947674712121421, 0.39745192702582005, -1.1354782267949199, -1.2828701002127429, 1.033849947000008, 1.4002743134190305, 1.169531125546482, 0.015374613438286699, 0.13026334319110144, 0.42285473932908269, -1.1357628652586451, 3.1616293169263976, -1.0424760990090216, 0.42988275527294828, 0.6573837428783269, -1.0965955790111135, 0.14763564570939841, -0.62245662296475246, 1.6109606864055177, 0.84773267211051018, -0.33299278871842508, 0.27688229659211377, 2.012961892384125, 0.083052940925926064, -0.21967955623032578, -0.12525528725921359, 0.31050587651618472, 0.09556348629128103, -0.21333694538743359, 0.19587764657892562, -0.62826960924490127, 1.1559662637913424, 0.46054253749743951, 0.34182127035939264, 0.92216039550710394, -0.4394710071210654, 0.59282780916279065, -0.35981701438037139, -0.15259138002657133, 0.46066011614516517, -0.5468924715880138, -0.26554492548611153, -0.62486774462576167, -0.0028929445215776037, 0.39260067079569394, 0.19054046824394569, 0.55921954893989223, -3.3062928696439542, -0.55605336102435243, 0.96425497974517971, 0.57004411899619167, -0.58953142704234629, 0.56307782056754641, 0.32303151351876713, -0.35514945519734986, -0.041668969798501543, -0.3133372111289951, -1.140187724382548, -0.87383342137699904, 0.10840995778648185, 0.38319187057792503, 0.21848856301419525, -0.68531249728395416, 1.868997870817833, 0.43241079895943235, 1.3769541360389306, 0.17026588652904789, 0.10280417503897947, -0.73701927981228932, 0.61366546779312803, 0.048368712593094471, 0.545776707955132, -0.53661379626159911, 1.4041449237209929, 0.40848173306407048, 0.11033253810636436, -0.14208688550546492, 0.17213825289944309, 0.44741900563494175, 0.40080898729202002, 0.22243302476203161, 0.52957186782871801, -0.28845994669492997, 0.2716136680323501, -0.40552175052301909, -0.76664111196293838, 0.56702689884137947, -0.75625560424315685, 0.70816313572774114, -0.35263178019569713, -0.1280039464339531, 0.60484041876827788, 0.14401409643861995, -0.16977568387767661, -0.32628099455913084, 1.1448910361842115, 0.32121263016459906, -0.1629503650674578, -0.02569871000900182, -0.3332941551790744, -0.90872036897993502, 0.21069242374322089, 0.11533275233376732, -0.85290150781574281, -0.62580566491307055, 0.70695154454495091, 0.12019651036749536, 0.50565230013302398, -0.64420389550832524, 0.36351461233080384, -0.26949536347434705, -0.15880454024783291, -0.14535136734730036, 0.22244969402088818, -1.0395491283712104, 0.34957139114962182, -0.62396621975983013, -0.88331407525096428, 0.64297922752060765, -0.054343920666859925, -0.4959312213478137, -0.11438568160409912, 0.016357985423202555, 1.5168598308311012, -1.2389477131317443, 0.25748727614583899, 0.77508970945710298, 0.71403876737272631, 0.041651028460003771, -0.53757715227649006, 0.060655730114409924, 0.37885621504600647, -0.43756694546365732, -0.29334142551059383, -0.11335805751873165, 0.51206680271854366, -0.46978959572021889, -0.63816865218406238, 0.086047998796286398, -0.63595098661774652, -0.1655943365787822, 0.012717193174163458, -0.056777050716113456, 0.6152249298200072, 0.64659498877214017, 0.18195743495718306, 0.29473332435984223, 0.40301732097352083, -0.10686270445553744, -0.90800322763149011, 0.68923718779951859, -0.29957861469582869, -0.20639493694801611, 0.22235602565865528, 0.51528192600931932, -0.05471207769114346, -0.10430841152514414, 0.47578306953751431, -0.29652088517680653, -0.41317910563435828, 0.82296920674912932, -0.48319714637433742, 0.27419220824922164, -0.12132078873128575, -0.23303924846055532, -0.41144840563743085, -0.17097534329791395, 0.64499673822942716, -0.45743257780564262, -0.08427163557198096, 0.2633084206694824, 0.67398712608859246, -0.26417644529090811, 0.046647724863248495, -0.80545879658346409, -0.22999080036798525, 0.15444052829312011, -0.89144176761845251, -0.41998437952833811, 0.0669097063352731, 0.096202706502811861, -0.59000852785435665, 2.2526086372389487, 0.43946205608556799, 0.18159250834310181, -0.080782312925171781, 0.10766651712982529, -0.48090804526972286, 0.32887838172771211, 0.22965237028940022, -0.55160386880925938, 0.23036100997119013, 0.20784741554435676, -0.00093934199093449538, 0.72397719920472936, -0.22129635309272527, -0.26676092847884314, -0.51326729672911164, 0.026142904864030925, -0.2668603947209211, 0.024262893301500416, 0.57304501246700812, -0.056982492129284641, 0.89453793326947095, 0.20384653674216174, 1.0632017011227262, 0.312409217976862, -0.64552949244884128, -0.29781123201325388, 0.33835312288829822, -0.10097314699642269, 0.53653788779168576, -0.60972625933429425, 0.14911648482739767, 0.37696574939993904, -0.12575802763694069, 1.4556557196825781, -0.1871472423012166, -0.10391733892813093, -0.38746106880024822, -0.4033226581265098, -0.12450904968214947, -0.55984692792856361, 0.30738690744463421, -0.72421197633903023, 1.263312184171947, -0.086046248629406186, 0.18274131731795237, 0.38173142467619486, 0.53386108027225954, 0.067987193334354962, 0.55404603215204495, -0.34565442292631959, 1.3854319870271841, -0.05273627237821496, -0.62586159360352411, 0.2261667516336891, 0.88187277031772715, -0.097351573618646492, -0.21675632706633022, 0.43521077543757924, 0.50953856187836288, -0.47463928316835174, 0.9036484807409918, 0.45776721164872103, 0.57198636066499786, 0.21838465518904823, -0.35592329918569543, -0.087821756962069772, -0.098866102050824967, -1.2755393973538507, 0.96962708666368869, 0.17617236462940014, -0.26687625233192136, 0.043784562438975272, 0.80747962810690155, 0.35906874894930052, -0.72170739760802793, 0.68237621357117528, -0.64550648095410845, -0.1707897282177577, 0.76783344713415647, 0.43597843950374404, 1.0026199540448035, 0.0012576559807914048, 1.4200364756933479, -0.17677650105859227, 0.60076077069379807, 0.12461699808756915, 0.73221016680898743, 0.18575800386344599, -0.48329031939901934, -0.58657388286044243, 0.65080111517920125, -0.22691786345464063, -0.56631175505084308, 0.22321428571429827, -1.8101097282694871, 0.48827531081937209, 1.6055252747819186, 0.28988094479086335, -0.79593653453421054, 1.1663455809766585, 0.55478680335698782, -0.99292894871357751, -0.030612420881984216, -0.11758043669027497, -0.27215156748836533, 0.18585962288196667, 0.13717542134026681, -1.3308042422903872, -0.79935520156594708, 0.49190252762220671, 0.48042527175680105, -0.1186076493339157, 0.051566770373183253, 0.040846862960916774, 0.25175618482481704, -0.18434099179791022, -0.18790364693752923, 0.1419328841030725, -0.028187541106835662, 0.13619752686865907, -0.23626247999390207, 0.11906055338259222, 0.16831455920936178, 0.35297299734030235, -0.4476279754028884, -0.58788285589435807, -0.18709715786151815, 1.1409665036933843, 0.59472769541872839, 0.32916512584517083, 0.75409365124962857, 0.34011017779706648, -0.45023286335341955, 0.7722639143786455, -1.0064501028505641, -0.53116179654174434, -0.0096581475672982663, -0.32133995597959547, 0.25927923070009801, 0.18373538519452937, 0.21458940258490561, 0.067220262876041353, 0.52525849070953656, 0.012490854909807111, 0.39623957323865844, 0.44425181493120169, 0.24216847625280141, 1.2390628533923473, -0.13763698570659758, 0.38322351947255301, -0.21712656181605194, -1.2394596025570341, 0.4701864063007628, 0.17167944433522644, 1.0622921129164311, -0.22753421599437526, 0.046618637958791162, -0.77676183904079033, -0.35191581757585005, -0.013200042240123165, 0.10535410440194454, -0.51691395712054922, -0.60377731721461458, 0.15244115631511879, 0.39283425737609173, -0.33511134941251514, 0.34714799565018445, 0.58187278571594447, -1.3934430107832059, 0.37183720502366763, -2.3200505505331135, 3.7579294057843642, 0.84593799899747768, -0.50055617352613735, 0.68779919519354438, 1.6030472155456887, 0.91888004264971312, 0.76345520321752158, -0.44366364935683933, -0.17307577535958074, -0.85562255400801401, 0.11256901856115586, 1.7851802667126238, 0.9491112734355871, -1.1046080290165678, -0.53850686294397077, 0.97518293845348292, -0.63605133114028334, -0.56513833603616881, -1.735828586927032, 1.1085445687368249, -0.20750635945960461, 0.7376984205624082, -0.50996047314092829, 0.29077016688112473, -0.16569087538328506, -0.34053463938383038, -0.40063542176619188, 0.85743257349067015, -0.55323882374271516, 0.84393996026203855, 0.59070494044131561, -0.99595137783753851, -0.5805021294801761, 0.95036179663634568, 1.0497968212748747, 0.23033141073228686, -0.35963031142656177, -0.90768461886288154, -3.807340302838663, 1.0470011967112307, -0.68951307631121872, -0.052072284044662943, -0.39847932195876351, -0.75825543368158099, 0.5240848892852612, 0.50357615514349829, 0.13438298196790838, 0.11456776922232788, -0.19880526596148679, 0.12692111327947239, 0.68240449182443985, 0.2402804213858955, -0.16040718022053913, 0.44732123578944194, 0.2078870254038917, 0.91127574094698893, -0.49679017607416132, 0.43681733376673443, 0.16124553215504248, 0.01792917974003097, -1.1604453650021191, 0.45740580327883967, 0.53321021518516354, 0.36873357521528982, -0.68842150910668887, -0.48469517289769243, 0.069491737432419279, 0.092513750489023244, 0.55487701674693191, 0.68282068673552532, -0.011409377595633404, 0.80165397682804962, -0.03082476345344811, -0.076505959411576854, -0.47062774570670818, -0.71676783073392403, -0.23465851728559461, 0.45830009868997451, -0.17926325961112066, -0.07460842022390099, -0.66549783827943565, -0.47035986262505258, 0.24051673517321859, 0.84795543259939032, 0.71276402336411393, -0.19852087964321061, 0.20791571488508864, 0.037229562133820823, 0.75475928036317441, -0.79701409495549203, -0.218363120062222, -0.01756468075005416, 0.29334854752054473, 0.39984893546711037, -1.0356480976779636, 0.092920860018311263, -0.67477701200741358, 1.415614686944664, -0.11795675222704584, 0.68718486915653054, 1.019459494117259, -0.26201666553141162, -0.82880071130788935, -0.17285136154741959, 0.090037242677653853, -0.44007213414798024, 0.044604439718666809, 1.0626510878323949, 0.76754286543292916, 0.0053294487573655475, -0.10447183928229666, 0.17284227023396967, 0.126600965388277, -0.21451188511797706, -0.34091268746806602, 0.061777745475694423, -0.31638100079888698, -0.20689591472932739, 0.10983283070852078, -0.11902271195108657, -0.87719298245613697, -1.4017962287708685, -0.16196072810663001, -0.58143125192980238, 0.21886523135481903, -0.45329261382734809, 0.55271091544241679, -0.23069093123031559, -0.043459776087678807, 0.099654058055602651, 0.12111774374945843, 0.14196131798846154, -0.11466099379366433, 0.23485572797920931, -1.1832935328232468, -0.19630588025341486, -0.13169599594476178, 0.23540117107137162, 0.39595706991768354, -0.044946928050333373, -0.39247832675062044, -0.28193982612876634, 0.21957073920484768, 0.4863308225014969, 0.076937778409405216, -0.17444290031973808, -0.3621324159965551, 0.11787182421382396, 0.26314116202745286, -0.36119483447279366, 0.75250218063009033, 0.25567703952902388, 0.42007379932884537, 0.24515393386544346, -0.62794199823834163, 0.3081518003176334, 0.39633658990680853, -0.27905882352940409, 0.41147827554048472, -0.84055431149188675, -0.16248411764983986, 0.27716748352206655, -2.1760352397485789, 0.2120838713161442, -0.31987613928488762, 1.3974634608177747, 0.12206300960101318, 0.611008844571586, -0.75074566979760315, 0.35227909469632462, -0.10145631067961872, -1.1843679251811665, -0.20446226424503103, 0.43690296631473374, -0.23765761492549967, -0.20413853538070026, 0.48462940250557324, -0.23104700254693872, 0.78364514633526394, -1.7985310272464392, 1.8848209221093217, 0.39452715046450937, -0.37732393958961458, -0.042140137754651925, -0.064455957537204456, -0.51939952347772844, -0.486966905826965, -0.010255558757028055, 0.19562329377071111, -0.58325914899620124, 0.38470164899996451, 0.58965090748713711, 0.17558468749254597, 1.3885523996826716, 0.4076554392546311, 0.47088213805942736, -0.61618344580376705, -0.083061603231333686, -0.30352401354694991, 0.065350747478982382, -1.272664710436525, 0.38306568777482197, 0.20114092951343723, -0.36134832331469674, -0.85826254168391347, -0.37889523695868904, 0.64712182728472911, 0.22108027637506489, 0.79448336208653902, -0.44279500849263065, -0.52162207639239266, -0.85699245826958725, 0.12097376412605484, 0.17029540641558821, -0.070169625323440774, 0.0078134537907499375, -0.38371286471169658, 0.37047676595576162, 0.049396514302536637, -0.039324807980456615, 0.66164920164641505, -0.58430923139728153, 0.68988384810676995, -0.014693061936151521, -0.12370587455635156, 0.56802295636818123, -0.45319504949045869, -0.068117220425358851, -0.2739846666438413, 0.26541617355048108, 0.82153884154625711, 0.12083787502897868, -0.33181822644139636, 0.69417871054465263, 0.3937681067375246, 0.066818186252030926, 0.020770137372714621, 0.53109457531711368, -0.12950738868648054, -0.026750062011516234, -1.0599341941224529, 0.65958408455391015, -0.14846748019612593, 0.054603949193737143, 0.05285438370306389, 0.10753796974205887, 0.27228234645343491, -0.097545273199923913, 0.2537661537558884, 0.68248706892337352, 0.092659072827113415, 0.14442715425013614, 0.33999853868823005, 0.36127764892369579, -0.90702727400876315, -0.20562632800337058, 0.065016645238871504, 0.60852420709295818, 0.13155094697337325, -0.26726874499473968, 0.25898901613437897, -0.23353957817517937, -0.053026654407300429, 0.022168461026883423, -0.074037393691457246, 0.42362774189239999, 0.52374582255982782, 0.33584255479899955, 0.11969292573536065, 0.022469333944733771, 0.92186389786610412, -0.81200441178472449, 0.61864721269335887, 0.19271735990756708, 0.35844564932067641, -0.74948166900312507, 0.038749618202287096, 0.27314645788541125, 0.083793974942904192, 0.71359638988188279, -0.68059362888743402, 0.13896134266338731, 0.17445215314213539, 0.46443992035616499, -0.079839429081175903, 0.4634780219532722, 0.2352888550915776, -0.02287221160832989, -0.5510647309560508, -0.13198396304449364, -0.24486532407175474, 0.70994790081621995, 0.25472793890118489, 1.0375516100553768, 0.36706340505029644, 0.56190795869171473, 0.52587004053129804, 0.11446423422998314, 0.41407688142934251, -0.76369302888639756, 0.70608049749524571, 0.45910369559149028, -1.936872309899575, 0.67395438920974238, -0.081111048791752099, 0.70249005706380774, -0.18221050107889064, 0.21912030789656337, 0.70039144577123336, -0.45124016759136698, 0.068624233305329782, 0.037762748109735685, 0.37323572872258964, 0.48878205128205748, 0.84751127975047069, -0.035362763010556013, 0.63502730659953266, -0.45144441116039241, 0.14006370367246035, -1.2788184438040429, 0.43284472071004082, 0.43297238096455054, -0.45059036272737563, -0.96542271297403137, -0.13705878781043618, -0.27068815425326886, 0.13640417606630864, 0.85372377139701672, 0.1189767995240997, 0.64145733719441467, 0.31044187193546546, -0.22951035054728122, 0.016459008838472775, 0.01819076322654754, 0.79862380746602135, -0.93648992433522427, 1.089906007355949, -1.4835291958864896, 1.3167835064945645, 0.03461112788007354, 0.23493637308381063, -0.87147802673333963, -0.27444755250434277, -0.02528950363232103, 0.15721922076436756, 0.80014592326867229, -0.092693759540550924, 0.65388173678515338, 0.93245332888938626, 0.60389337208857474, 1.1674780437955117, -0.82407314898073158, 2.3806348359562461, 0.16142631681354408, 2.6099635135948134, 1.9847386546686689, 1.3115699928886864, -6.6062629360659963, 2.5165281187235018, 0.11326190875401448, 0.44544876484545015, 1.2881276878862478, 1.5589182357805049, 0.29028622352694905, 0.17922380039644828, 2.2056721038844831, 0.26256311613368771, -2.251587802584281, -0.11391435253635422, 0.8988003953802215, 1.4600181859659624, -0.55654084595464237, 0.32609522360815218, 1.4916194456471936, 1.1184683080526081, 1.1355474950359299, 0.67615753933559475, -0.62579204634601959, -0.5560297598508479, 0.51172615029505342, -0.1129992343221236, -0.76464229953160434, 2.5344347537477119, 0.15216366047037583, -1.4564841370979711, -0.018590640400287708, 2.4218648883520024, 0.80411979485447971, -1.1367725570008542, 0.78436629578324701, 1.1504096543946278, -0.6013699206793075, -0.21380789100996797, -0.66064096097731262, -1.3848302298383104, 2.0285305887259222, -1.2512638636116105, -2.1547502448579801, -0.81229241236980609, 0.30820486062722646, 0.65811185338267453, 0.31354933398563106, 0.61285505486526781, -0.60157234070277155, 0.36409845920010636, -0.056637168141597402, -0.58928934291466917, 0.75050629392844881, -0.32129167080701176, 0.50277293280194402, -1.2916887241926891, 0.65712742317656536, -0.0080031027413632223, -0.38754686827709528, 2.8349271494720312, -0.43479314753879533, -0.1623056503602551, 0.35505937132020254, 0.27797928385400911, 0.43998730413867976, 0.4273663512773655, 1.2114936284828366, -0.13769305597752465, 1.2098218282746955, 0.27163421013992933, 1.4720192640728265, 0.20584636525138117, 0.25457763256415245, -0.12798207709770251, 0.93832386568107851, -1.1329912816386778, 0.23175184401864393, 0.20482142295886191, 1.1087095322329072, 0.71800139328882873, 0.73150436229763882, 0.30770088635091403, 0.52551317894359506, 0.65619169491359586, -0.59251674190308556, -0.15206411140285878, 0.73942790998143537, 0.097826112334273685, -2.669891708749164, 0.93088419894592522, 0.65010251528575802, 0.13723613234553975, 1.3691582963841387, 1.1478947815246401, -0.80596909085268054, 0.34159833952722657, -0.68865903775551218, -0.011827743422764733, -2.2273827286291414, -2.9157838435916692, -1.3872702071433112, 1.0018731088804633, 1.8058547563728768, 0.84572360808466518, -0.43346583811359718, -0.23287980257624638, -0.15317590897505579, -0.64550995982668713, 0.40814285909072395, -0.64216535925522222, 0.75911415181838449, 0.85445655610267413, 0.97031173309505991, 0.35782964366215053, 0.48537569339384545, -5.1417555140831546, -0.30545605475294613, 1.8334809565987515, 1.7159345359789082, 1.0269399411942597, 2.6426791542264985, 1.753042604566742, 1.2438767920802272, 0.895196678873593, 0.28931650203974146, 0.48953820556287703, 0.42623492483065045, -0.47081349494980912, -2.1623677546567284, 2.8742415771054497, -3.5341928929098554, -4.467767396219986, 4.7625697045169488, 1.5751220378479662, -3.8836868171175132, -3.5432228558808809, 0.51035970687796206, 5.5108514931595396, -4.8431697503767728, -2.2513733827309741, -2.6566056068054698, 0.26287768752604573, 1.9472473488277964, -2.1420439960267408, 4.385547729133898, -0.60236331479250504, 0.10461332143514582, -0.86292044004901436, -0.62642145970039964, -0.54032960886587966, 2.1303442456708015, 1.3578325458344658, 0.29206409433920555, 0.67440511317603691, 1.0732501170305839, -2.3853884169106596, -6.1864807969299225, -0.75161078808043325, 3.6799391465189903, -2.1927497789566734, -0.20646581193088917, 1.3330536326130999, 2.3131541748715096, -0.34929009148972406, -0.60210873790624253, 0.3615933696266872, 1.630887519467684, 0.38078103557107279, -0.59927105313638562, 2.3807797856366189, -0.5981164095969389, 0.78255515234716633, -4.7534826515417166, 4.4648191742727823, -3.0557253180732262, -1.3194022460783679, 0.03770997600274368, -3.5295840179602735, -2.2255103676784986, 3.7337684182197481, 2.8467520236216397, 1.877076728568801, -0.21082087788460802, -0.73502388827637177, -3.5263307928214145, 4.4846211899010315, 0.5762115794337721, -0.44951795114449805, 0.13673940660729478, 0.57312603929545858, -1.0021116158638048, 4.7279855147095606, -2.6319774852657241, 0.0022596316800414388, 1.1928843693998403, 0.26905660258609598, -0.052285149734407774, 0.58056360115856276, 0.1366522782395754, 0.4428118389810492, -0.17742497223628048, -0.21605614191063163, -0.83568623120967178, 0.57091763873267543, -0.12516024764718012, 0.45817687091430936, -0.97674390369753838, 0.80144223365030554, 1.289962247921248, -0.64278400873084063, 1.215951870172393, -3.4559753456120812, 1.1834177344458552, 1.2800878520760886, -0.22952927589185865, 1.9536711859475777, -1.1309944021489224, 0.19018660766840362, -0.35585511276600545, -1.6885509093220703, -0.27931533167568046, 1.5856699374719223, -0.97651199136486189, 1.3800562527533449, -0.035634206645497955, -0.63839427055472142, 0.69710729438507202, 0.55540181536418431, -0.2768200780888847, 1.2423162208437484, -1.4616198366987621, -1.2055294947901518, 1.4085375768892117, 0.27814375640463052, -0.95373677194252848, 0.88691857869832946, 0.66004232880151037, -0.61861362754155491, -4.0160216303181908, 2.1661452696191139, 0.78938773605814017, 1.9408745175915081, 0.73284364690874815, -0.50158633381884277, -0.11065138230872491, -0.58442842041030574, -0.62416827645417317, -0.71857285282904559, 0.26997918971218759, 1.955906670180386, -0.36331124136071929, -0.55798773727912443, 0.29893565459063948, -0.040777338971406604, 0.31533838976375284, 0.77907239881441959, -0.60792766098191753, 0.76483862239787836, 0.33797145219860664, -2.4186978961000865, 0.65697306579898107, 0.32290853545535719, -0.3381964918801928, -3.0334226525756036, -0.67071310096044356, 1.5572653755411212, 0.0, -0.42064208858484992, -3.0084204908255607, -0.21061388335026787, -2.4099733989756666, 3.0885609109043966, -1.9584848525813565, 0.35404813401480251, 1.5397703679446773, 0.35671658900719255, -3.7221241777635208, 1.5324416718305047, -0.27929169183570873, -4.4139781769136919, 2.3641847342069555, -2.3896802250839269, 0.92458443468739704, 0.031994166644969936, -0.11660939123359063, 0.78108328857035703, 0.45065214565308515, -0.52804734068592429, 0.90388007054673392, 0.41097927050294969, 1.3842775768247568, -0.62204727142713589, 0.38010803070346055, 0.25099301465552415, 0.48513285788929084, 1.1049780972007988, -2.8810622942920872, 0.50046669063677673, 0.51491842450667602, 1.4754420942812785, 1.8302923750920077, 0.13130206126729246, 0.87816280759389642, 0.052811249831720065, 1.8070872910884281, 1.6097486520351663, -0.91464060877121878, 0.44139301491086036, -0.79413264686596452, 1.3269139610734086, 0.081936347661149933, 0.67164567051933355, -0.13348653306748059, 0.37806366232964178, 0.14189796034202415, 0.7073025474936554, -0.74184573095102779, 0.52193686824382923, -1.1899353252445311, -0.16070958410412178, 1.2840072908931333, -0.25799468072743148, 1.6087755074479753, 0.47521415901245145, -0.19531761195591776, -0.6305511790217091, 0.11940699000469394, -0.20918850647300702, 0.33415406260992453, -0.62799333769710208, 0.45823420134927956, 0.11253276785075542, -0.12905009909204276, 0.229919890376305, 0.31147181399429763, -1.1175597879416033, 0.81627647106918522, 0.39829913662103505, 0.890924683173837, -0.42880403453355087, 0.41282026807750954, 0.046304335243376009, 0.20156564946327227, 0.16743295147458201, 0.49204614776131861, -0.97789953841238275, -0.54187122920134001, -0.16916955370956152, -0.48127516872694487, 0.22548312764183204, -0.35457868227846567, 0.61160460626850344, 0.12287910315858382, 0.4605244324850552, -0.4471726348787608, 0.55518385126766656, 0.10913379451162306, -0.0038982486232139756, -0.50540929316918937, 1.2454622415450711, 0.24518948883322106, -0.15317782070059863, 0.88375584126291395, -0.1798709040825556, 0.62503009913796326, 0.48246408873782032, -0.12389675724063789, 0.22393052691945142, 0.15396932930960153, -2.4711804646934858, 0.59694626775888215, 0.021478630494801507, -0.49357999632845756, -0.24997061203039814, 0.29998229271188409, -0.61628015370751754, 0.48833967967408326, 0.3431561343062407, -0.10257092446858586, 0.58180934021084074, 0.62876568459455917, 0.14620931845278431, 0.16000382915147685, -0.063387337527352899, 0.12330538857950303, 0.18962242143500033, 0.53980387126010276, 0.47793505412156234, -0.089274966898048411, -0.69004851230050257, 1.8326932709968311, -0.0052273061404464281, 0.19586292875772376, 0.057984688111172758, -0.21930112109093472, 0.4990865524636583, -0.27041180984878793, -0.33287856327643145, -0.19081819928574906, -0.12915061942624312, 0.6809614660971669, -0.15384050643894692, 0.69713713053918047, -0.45540048847798859, 0.37793948210055128, 0.57101079403333821, -0.056708554938511638, 0.29391093220879722, -0.081559224415402823, 0.65365170515651849, 0.43380996003769562, -0.13266021781419027, -0.59951403279947979, 1.351499506642889, 0.090636279492818828, 0.051150895140669644, 0.17686513791615616, -0.59245310813710328, 0.58934136813932003, -0.13887540060211595, -0.065658819952510411, -0.12589933878573073, 0.5205671528351048, -0.52840971677757376, -0.057946292251140057, 0.10776949699970845, 0.042474960848459892, -0.56480486641066807, 0.071118186681972395, -0.071561005757417057, 0.57729167548008076, -0.32977022461768635, 0.14912626886721203, -0.57096168937489022, 0.24347849162752919, 0.24401969398074125, -0.1084457987232742, 0.17047899632560135, -0.034391079483074419, 0.11151149362531115, -0.21810715785054874, -0.20361239305415479, -1.0547108425735336, 0.76866198366550897, -0.068898164499382769, -0.22328039158921853, 0.072919302638415298, 0.19591214195083909, 0.20136707321457867, 0.10539132256290093, 0.089255938952861685, 0.60220589925365042, -0.86512070617842274, 0.88391355835726793, -0.095864856461810699, 0.082740897690074727, 0.56023320276408572, -0.1044221336603305, 0.20957384518412686, -0.087169149812355587, 0.20960513097905117, -0.2996531346351467, 0.33428689776580917, 0.36164563228515034, -0.12071540779274291, 0.2068868335425699, -0.12687556926224428, -0.012126201850206596, -0.13609628891750991, 0.72369289409552939, 0.21458317320529324, 0.17364049522018379, 0.10508263174305865, 0.16303482136442654, 0.0758751401192094, 0.42628307449625019, -0.24743968657639925, -0.069245196308579518, 0.21719613366200591, -0.45180214076201414, -0.080447547274496503, 0.74090087864235821, -0.045141494183458031, -0.31609343734153134, -0.028606934567015168, 0.17168038681641912, -0.10808813340107361, 0.069946010423211982, -0.24504989851941622, 0.58875312950694803, -0.15092089695456931, -0.19731600822612824, -0.40715634930162187, 0.73466729245887685, -0.5431202655113766, -0.44672650694358718, 0.18285171688137791, -0.16457374120298515, 0.021919927793188416, 0.13404697388955863, 0.26277810416613506, -0.32784468558316671, 1.1553801641378652, -0.2565112547915796, -0.12748696156075065, -0.44783940793893684, 0.16977928692700195, 0.32792969187406218, 0.31630796200493633, 0.11132582094886229, -0.24603902469876809, -0.030893191518873795, -0.2419894243996035, -0.24646207664175546, -0.76407997073465495, -0.31799506194978805, 1.1446040328389209, 0.67716800632152541] #存储下午波幅百分比数据(（15：00数据-13：00数据）/9：30开盘数据)


#绘制数据柱状图
plt.hist(bf,100,normed=1)#第二个参数越大，柱子分得越细
#估计出概率密度函数
mdhs=stats.gaussian_kde(bf)
#密度函数积分求上涨概率
P_z=integrate.quad(mdhs,-j,10)[0]
#print(P_z_lisan)
P_d=1-P_z
print("涨概率： %.8f"%P_z+" 跌概率： %.8f"%P_d)

#购买额度
buy_bl=((P_z*(b_zhang-1)-P_d)/(b_zhang-1))
sell_bl=((P_d*(b_die-1)-P_z)/(b_die-1))
buy=((P_z*(b_zhang-1)-P_d)/(b_zhang-1))*k
sell=((P_d*(b_die-1)-P_z)/(b_die-1))*k
print("买涨额： %.d"%buy+"  买涨比例： %.2f"%buy_bl)
print("卖跌额： %.d"%sell+"  买跌比例： %.2f"%sell_bl)

#彩票系列
bf_pj=mean(bf)
zx=(1+bf_pj/100)*p00
print('彩票买入中心值： %.2f'%zx)
