# -*- coding: utf-8 -*-
""" 这里是input.txt中的点经过纠正过的路径 """

import socket
import time

poss = [
    [117.14112364303995, 34.210311754345234],
    [117.14112364303995, 34.210311754345234],
    [117.14112364361056, 34.21032008767882],
    [117.14112364361056, 34.21032008767882],
    [117.14112197765311, 34.2103300877579],
    [117.14112197765311, 34.2103300877579],
    [117.1411219785662, 34.21034342109164],
    [117.1411219785662, 34.21034342109164],
    [117.14112198004992, 34.21036508775897],
    [117.14112198004992, 34.21036508775897],
    [117.1411219815337, 34.210386754426324],
    [117.1411219815337, 34.210386754426324],
    [117.14112364954548, 34.21040675434814],
    [117.14112364954548, 34.21040675434814],
    [117.14111865110256, 34.21042842125183],
    [117.14111865110256, 34.21042842125183],
    [117.14112198587075, 34.2104500877616],
    [117.14112198587075, 34.2104500877616],
    [117.14111865407001, 34.210471754586486],
    [117.14111865407001, 34.210471754586486],
    [117.14111365585528, 34.21049675482356],
    [117.14111365585528, 34.21049675482356],
    [117.14110699077008, 34.210518421806015],
    [117.14110699077008, 34.210518421806015],
    [117.1410953259864, 34.2105434223582],
    [117.1410953259864, 34.2105434223582],
    [117.14108866112953, 34.210568422674086],
    [117.14108866112953, 34.210568422674086],
    [117.14108699619926, 34.210593422753625],
    [117.14108699619926, 34.210593422753625],
    [117.14108699791129, 34.21061842275439],
    [117.14108699791129, 34.21061842275439],
    [117.14108866649384, 34.21064675600984],
    [117.14108866649384, 34.21064675600984],
    [117.14108700167779, 34.2106734227561],
    [117.14108700167779, 34.2106734227561],
    [117.14108367033361, 34.210701756247865],
    [117.14108367033361, 34.210701756247865],
    [117.14108867197234, 34.210726756012306],
    [117.14108867197234, 34.210726756012306],
    [117.14109700723797, 34.210756755619336],
    [117.14109700723797, 34.210756755619336],
    [117.14110034257683, 34.21078675546271],
    [117.14110034257683, 34.21078675546271],
    [117.14110201093112, 34.210811755384704],
    [117.14110201093112, 34.210811755384704],
    [117.14110201264317, 34.210836755385486],
    [117.14110201264317, 34.210836755385486],
    [117.14110034782706, 34.210863422131744],
    [117.14110034782706, 34.210863422131744],
    [117.14110034988154, 34.210893422132656],
    [117.14110034988154, 34.210893422132656],
    [117.14109701887983, 34.210926755624584],
    [117.14109701887983, 34.210926755624584],
    [117.14109702082008, 34.210955088958784],
    [117.14109702082008, 34.210955088958784],
    [117.14109702287456, 34.210985088959724],
    [117.14109702287456, 34.210985088959724],
    [117.14109869145712, 34.21101342221512],
    [117.14109869145712, 34.21101342221512],
    [117.14107442817529, 34.211029476381086],
    [117.14104733450456, 34.21104979091769],
    [117.14101651079287, 34.21107010973648],
    [117.14098500887928, 34.21109042932703],
    [117.14094571905348, 34.211117518984686],
    [117.14090576226778, 34.21115137052207],
    [117.14085902732164, 34.21118748353892],
    [117.14080890139495, 34.211223600430515],
    [117.14076047464361, 34.21126196906029],
    [117.14109038095934, 34.21134508928589],
    [117.14109038095934, 34.21134508928589],
    [117.14108704995765, 34.211378422777805],
    [117.14108704995765, 34.211378422777805],
    [117.14105843218256, 34.21140135671439],
    [117.14108871876859, 34.21141008936668],
    [117.14108871876859, 34.21141008936668],
    [117.14109872067645, 34.21144008889494],
    [117.14109872067645, 34.21144008889494],
    [117.1411087228127, 34.211473421756644],
    [117.1411087228127, 34.211473421756644],
    [117.14111205837995, 34.211506754933446],
    [117.14111205837995, 34.211506754933446],
    [117.14111539394717, 34.211540088110254],
    [117.14111539394717, 34.211540088110254],
    [117.14112039627086, 34.21157508787499],
    [117.14112039627086, 34.21157508787499],
    [117.14112206508173, 34.211606754463865],
    [117.14112206508173, 34.211606754463865],
    [117.14112206725042, 34.211638421131504],
    [117.14112206725042, 34.211638421131504],
    [117.14111373609379, 34.211668421526305],
    [117.14111373609379, 34.211668421526305],
    [117.1411004052387, 34.21170175549089],
    [117.1411004052387, 34.21170175549089],
    [117.14109374106667, 34.211736755807074],
    [117.14109374106667, 34.211736755807074],
    [117.14109040983675, 34.21176675596554],
    [117.14109040983675, 34.21176675596554],
    [117.1410887453632, 34.211798422711986],
    [117.1410887453632, 34.211798422711986],
    [117.14109041406, 34.21182842263414],
    [117.14109041406, 34.21182842263414],
    [117.14109874955398, 34.2118617555746],
    [117.14109874955398, 34.2118617555746],
    [117.1411004185932, 34.211896755496895],
    [117.1411004185932, 34.211896755496895],
    [117.1411004209902, 34.21193175549797],
    [117.1411004209902, 34.21193175549797],
    [117.14110542308556, 34.21196342192928],
    [117.14110542308556, 34.21196342192928],
    [117.14110709201067, 34.21199675518486],
    [117.14110709201067, 34.21199675518486],
    [117.1411104280346, 34.21203675502853],
    [117.1411104280346, 34.21203675502853],
    [117.1411137638302, 34.21207342153878],
    [117.1411137638302, 34.21207342153878],
    [117.14111376622718, 34.21210842153987],
    [117.14111376622718, 34.21210842153987],
    [117.14110876835501, 34.21213842177711],
    [117.14110876835501, 34.21213842177711],
    [117.14110543758176, 34.21217508860248],
    [117.14110543758176, 34.21217508860248],
    [117.14111043979132, 34.21220842170049],
    [117.14111043979132, 34.21220842170049],
    [117.14111044207418, 34.21224175503487],
    [117.14111044207418, 34.21224175503487],
    [117.14110544443034, 34.212275088605544],
    [117.14110544443034, 34.212275088605544],
    [117.14110378029926, 34.21231175535211],
    [117.14110378029926, 34.21231175535211],
    [117.14110544911028, 34.212343421941],
    [117.14110544911028, 34.212343421941],
    [117.14109878493834, 34.212378422257196],
    [117.14109878493834, 34.212378422257196],
    [117.1410787877427, 34.212415089870326],
    [117.1410787877427, 34.212415089870326],
    [117.14107545617043, 34.21244009002866],
    [117.14107545617043, 34.21244009002866],
    [117.14105746929178, 34.21245158595903],
    [117.1410452767477, 34.21246061481277],
    [117.14103308420106, 34.21246964366528],
    [117.14102427888851, 34.212476414913986],
    [117.14102224804823, 34.21247867095711],
    [117.1410181826132, 34.21248092933935],
    [117.1410114081391, 34.212485444544065],
    [117.14100497276334, 34.2124899593586],
    [117.14099819828779, 34.21249447456259],
    [117.14098837567222, 34.212501246978086],
    [117.14097618311368, 34.21251027582492],
    [117.14096195595695, 34.212519307008726],
    [117.14094874234279, 34.212526083317975],
    [117.14093213773334, 34.212532863521986],
    [117.14109549206168, 34.21296842243293],
    [117.14109549206168, 34.21296842243293],
    [117.14109216106009, 34.213001755924864],
    [117.14109216106009, 34.213001755924864],
    [117.14105333284598, 34.21302177887813],
    [117.14108216383212, 34.21304008973205],
    [117.14108216383212, 34.21304008973205],
    [117.14108049970112, 34.213076756478614],
    [117.14108049970112, 34.213076756478614],
    [117.14107550205742, 34.21311009004932],
    [117.14107550205742, 34.21311009004932],
    [117.1410671713575, 34.21314675711102],
    [117.1410671713575, 34.21314675711102],
    [117.14105550725901, 34.213181757663584],
    [117.14105550725901, 34.213181757663584],
    [117.14105550988445, 34.21322009099806],
    [117.14105550988445, 34.21322009099806],
    [117.14105717915209, 34.21325842425383],
    [117.14105717915209, 34.21325842425383],
    [117.14108884718095, 34.21328508942447],
    [117.14108884718095, 34.21328508942447],
    [117.14108718305006, 34.21332175617105],
    [117.14108718305006, 34.21332175617105],
    [117.14108551880496, 34.2133567562509],
    [117.14108551880496, 34.2133567562509],
    [117.14109052112876, 34.21339175601564],
    [117.14109052112876, 34.21339175601564],
    [117.14109552356682, 34.21342842244709],
    [117.14109552356682, 34.21342842244709],
    [117.14109719272037, 34.213465089036106],
    [117.14109719272037, 34.213465089036106],
    [117.14109552881773, 34.21350508911611],
    [117.14109552881773, 34.21350508911611],
    [117.14109386480098, 34.213543422529426],
    [117.14109386480098, 34.213543422529426],
    [117.1410955338404, 34.213578422451725],
    [117.1410955338404, 34.213578422451725],
    [117.14110053616429, 34.21361342221645],
    [117.14110053616429, 34.21361342221645],
    [117.14110553848818, 34.21364842198118],
    [117.14110553848818, 34.21364842198118],
    [117.14110554122779, 34.21368842198242],
    [117.14110554122779, 34.21368842198242],
    [117.14110554373917, 34.213725088650214],
    [117.14110554373917, 34.213725088650214],
    [117.14111721240367, 34.213756754766365],
    [117.14111721240367, 34.213756754766365],
    [117.14112888141071, 34.21379342088271],
    [117.14112888141071, 34.21379342088271],
    [117.14114055030353, 34.21382842033232],
    [117.14114055030353, 34.21382842033232],
    [117.14114721938378, 34.21386508668497],
    [117.14114721938378, 34.21386508668497],
    [117.14115388857829, 34.213903419704366],
    [117.14115388857829, 34.213903419704366],
    [117.14116222430079, 34.21394008597823],
    [117.14116222430079, 34.21394008597823],
    [117.14117555995006, 34.21397675201578],
    [117.14117555995006, 34.21397675201578],
    [117.14119389552603, 34.21401341781697],
    [117.14119389552603, 34.21401341781697],
    [117.14121556427226, 34.21404841679388],
    [117.14121556427226, 34.21404841679388],
    [117.14123556626217, 34.21408174918287],
    [117.14123556626217, 34.21408174918287],
    [117.14125390172401, 34.21411674831732],
    [117.14125390172401, 34.21411674831732],
    [117.14127723677007, 34.21414674721528],
    [117.14127723677007, 34.21414674721528],
    [117.14129890528807, 34.21417841285875],
    [117.14129890528807, 34.21417841285875],
    [117.14132827716546, 34.21420015158317],
    [117.14136188252972, 34.21422039622596],
    [117.1413937961437, 34.214242896517256],
    [117.14142129386323, 34.21426089447652],
    [117.14145217889146, 34.21427663481565],
    [117.14148306393118, 34.21429237514695],
    [117.14151225345023, 34.21430811742657],
    [117.1415431385125, 34.2143238577426],
    [117.14158148769961, 34.21434184314278],
    [117.14162051134576, 34.21435757404461],
    [117.14165647927493, 34.21437105475555],
    [117.14169550672084, 34.214389039336545],
    [117.14173656127706, 34.2144025141476],
    [117.14177393063036, 34.214650057086594],
    [117.14177393063036, 34.214650057086594],
    [117.14180893171547, 34.21467338876621],
    [117.14180893171547, 34.21467338876621],
    [117.14184656860567, 34.21468635411811],
    [117.14184726608498, 34.21469672028821],
    [117.14184726608498, 34.21469672028821],
    [117.14188893362487, 34.21471838498595],
    [117.14188893362487, 34.21471838498595],
    [117.14193060116467, 34.21474004968367],
    [117.14193060116467, 34.21474004968367],
    [117.14197393523258, 34.214760047635906],
    [117.14197393523258, 34.214760047635906],
    [117.14201726895796, 34.214775045588006],
    [117.14201726895796, 34.214775045588006],
    [117.14206226966809, 34.21479504346143],
    [117.14206226966809, 34.21479504346143],
    [117.1421056035077, 34.214811708080234],
    [117.1421056035077, 34.214811708080234],
    [117.14214727059093, 34.21482670611108],
    [117.14214727059093, 34.21482670611108],
    [117.14219060420214, 34.21484003739645],
    [117.14219060420214, 34.21484003739645],
    [117.14223227128528, 34.21485503542732],
    [117.14223227128528, 34.21485503542732],
    [117.14227393825436, 34.21486836679146],
    [117.14227393825436, 34.21486836679146],
    [117.14231560453837, 34.21487169815531],
    [117.14231560453837, 34.21487169815531],
    [117.14236227074917, 34.21487502928282],
    [117.14236227074917, 34.21487502928282],
    [117.14240893673158, 34.21487502707689],
    [117.14240893673158, 34.21487502707689],
    [117.14246060298318, 34.21488002463475],
    [117.14246060298318, 34.21488002463475],
    [117.1425072695364, 34.21488835576239],
    [117.1425072695364, 34.21488835576239],
    [117.1425522691049, 34.2148916869687],
    [117.1425522691049, 34.2148916869687],
    [117.14259893542979, 34.214896684762905],
    [117.14259893542979, 34.214896684762905],
    [117.14263893518579, 34.21490168287227],
    [117.14263893518579, 34.21490168287227],
    [117.1426756017714, 34.21490834780589],
    [117.1426756017714, 34.21490834780589],
    [117.1427122685854, 34.214918346072956],
    [117.1427122685854, 34.214918346072956],
    [117.1427489353994, 34.21492834434003],
    [117.1427489353994, 34.21492834434003],
    [117.14279060179761, 34.21493334237056],
    [117.14279060179761, 34.21493334237056],
    [117.14283393460967, 34.21493500698893],
    [117.14283393460967, 34.21493500698893],
    [117.14288060093453, 34.214940004783145],
    [117.14288060093453, 34.214940004783145],
    [117.14292231359111, 34.21494202797967],
    [117.14296674828046, 34.214948737316625],
    [117.14301865479773, 34.21496219904717],
    [117.14307768262178, 34.214975652448906],
    [117.14313570456973, 34.214995868117725],
    [117.14319203099923, 34.21501608573845],
    [117.14324530928556, 34.21503856060028],
    [117.14330163958476, 34.21506103187311],
    [117.14335593907361, 34.215085759200754],
    [117.14340819630023, 34.215105981477656],
    [117.14346215291964, 34.21512845545168],
    [117.14351713453898, 34.21515543561688],
    [117.14356974624661, 34.215184672238465],
    [117.14362405736439, 34.21521616055453],
    [117.14355561489556, 34.21528830621914],
    [117.14355561489556, 34.21528830621914],
    [117.1435822833402, 34.21531997162618],
    [117.1435822833402, 34.21531997162618],
    [117.14360150521834, 34.215315350073766],
    [117.14361228529759, 34.21535497020904],
    [117.14361228529759, 34.21535497020904],
    [117.14364062049867, 34.21538830220399],
    [117.14364062049867, 34.21538830220399],
    [117.14366728917159, 34.21542330094442],
    [117.14366728917159, 34.21542330094442],
    [117.14369895765707, 34.21545663278178],
    [117.14369895765707, 34.21545663278178],
    [117.14373395919873, 34.21548663112817],
    [117.14373395919873, 34.21548663112817],
    [117.14377229402476, 34.21551662931697],
    [117.14377229402476, 34.21551662931697],
    [117.14380396228186, 34.21554662782092],
    [117.14380396228186, 34.21554662782092],
    [117.14383063084064, 34.21557995989461],
    [117.14383063084064, 34.21557995989461],
    [117.14385729939949, 34.215613291968346],
    [117.14385729939949, 34.215613291968346],
    [117.14388230165856, 34.215651624120966],
    [117.14388230165856, 34.215651624120966],
    [117.14391396980159, 34.21567995595819],
    [117.14391396980159, 34.21567995595819],
    [117.14394397187311, 34.215716621207754],
    [117.14394397187311, 34.215716621207754],
    [117.14397397371643, 34.21574995312389],
    [117.14397397371643, 34.21574995312389],
    [117.1440039753314, 34.21577995170659],
    [117.1440039753314, 34.21577995170659],
    [117.14403064366184, 34.21580995044686],
    [117.14403064366184, 34.21580995044686],
    [117.14405731199231, 34.21583994918714],
    [117.14405731199231, 34.21583994918714],
    [117.1440823135664, 34.21586828133949],
    [117.1440823135664, 34.21586828133949],
    [117.14410898178272, 34.215896613413044],
    [117.14410898178272, 34.215896613413044],
    [117.14413564999906, 34.21592494548661],
    [117.14413564999906, 34.21592494548661],
    [117.14416231821545, 34.21595327756015],
    [117.14416231821545, 34.21595327756015],
    [117.14419065318815, 34.21598327622164],
    [117.14419065318815, 34.21598327622164],
    [117.14421732151862, 34.216013274961895],
    [117.14421732151862, 34.216013274961895],
    [117.14424398984917, 34.216043273702155],
    [117.14424398984917, 34.216043273702155],
    [117.14426565836715, 34.21607493934548],
    [117.14426565836715, 34.21607493934548],
    [117.14428566058537, 34.216111605067724],
    [117.14428566058537, 34.216111605067724],
    [117.14433164458501, 34.21613033498],
    [117.14438492387457, 34.21615280934017],
    [117.1444432899001, 34.216175277686744],
    [117.14450098157603, 34.21620000050664],
    [117.14455594882662, 34.21621796539],
    [117.14460787947465, 34.216244948655756],
    [117.14466219936214, 34.21628094390828],
    [117.14472160601201, 34.2163169331346],
    [117.14478203391087, 34.21635517483304],
    [117.14484076629076, 34.21639341850363],
    [117.14489645054779, 34.21643391945338],
    [117.14495621967673, 34.216483430376464],
    [117.14502751493356, 34.21653067393509],
    [117.1451028796554, 34.216577912637504],
    [117.14474568329292, 34.21654158333462],
    [117.14474568329292, 34.21654158333462],
    [117.14478204559279, 34.21656026212411],
    [117.14478235147674, 34.21657158160211],
    [117.14478235147674, 34.21657158160211],
    [117.14481901954647, 34.21659991320292],
    [117.14481901954647, 34.21659991320292],
    [117.14485402120224, 34.21663157821596],
    [117.14485402120224, 34.21663157821596],
    [117.14488735610168, 34.216661576641044],
    [117.14488735610168, 34.216661576641044],
    [117.14492235764325, 34.216691574987344],
    [117.14492235764325, 34.216691574987344],
    [117.14495569265681, 34.216723240079126],
    [117.14495569265681, 34.216723240079126],
    [117.14498736102814, 34.216754905249694],
    [117.14498736102814, 34.216754905249694],
    [117.14501902951368, 34.21678823708697],
    [117.14501902951368, 34.21678823708697],
    [117.14505069788501, 34.21681990225754],
    [117.14505069788501, 34.21681990225754],
    [117.14508403301272, 34.21685323401603],
    [117.14508403301272, 34.21685323401603],
    [117.14511570161243, 34.21688823252003],
    [117.14511570161243, 34.21688823252003],
    [117.14514403669934, 34.21691989784817],
    [117.14514403669934, 34.21691989784817],
    [117.1451723720145, 34.216954896509705],
    [117.1451723720145, 34.216954896509705],
    [117.14520404027168, 34.21698489501356],
    [117.14520404027168, 34.21698489501356],
    [117.14523570864306, 34.21701656018411],
    [117.14523570864306, 34.21701656018411],
    [117.14526404384418, 34.21704989217895],
    [117.14526404384418, 34.21704989217895],
    [117.1452890455324, 34.21707989099793],
    [117.1452890455324, 34.21707989099793],
    [117.14531571386293, 34.21710988973814],
    [117.14531571386293, 34.21710988973814],
    [117.1453457153637, 34.21713822165406],
    [117.1453457153637, 34.21713822165406],
    [117.14537071693786, 34.21716655380634],
    [117.14537071693786, 34.21716655380634],
    [117.14539738492587, 34.21719155254639],
    [117.14539738492587, 34.21719155254639],
    [117.14542071974361, 34.21721821811075],
    [117.14542071974361, 34.21721821811075],
    [117.14544405467556, 34.217246550341805],
    [117.14544405467556, 34.217246550341805],
    [117.14546572330778, 34.217279882651766],
    [117.14546572330778, 34.217279882651766],
    [117.14548239189918, 34.21731154853136],
    [117.14548239189918, 34.21731154853136],
    [117.14550072724695, 34.217344880998915],
    [117.14550072724695, 34.217344880998915],
    [117.1455240626355, 34.2173798798968],
    [117.1455240626355, 34.2173798798968],
    [117.14554906420967, 34.217408212049065],
    [117.14554906420967, 34.217408212049065],
    [117.1455807323527, 34.217436543886166],
    [117.1455807323527, 34.217436543886166],
    [117.14561073373935, 34.21746320913536],
    [117.14561073373935, 34.21746320913536],
    [117.14564073524012, 34.21749154105126],
    [117.14564073524012, 34.21749154105126],
    [117.14566907021282, 34.21752153971265],
    [117.14566907021282, 34.21752153971265],
    [117.14569740495729, 34.21754820504063],
    [117.14569740495729, 34.21754820504063],
    [117.14572573981584, 34.217576537035306],
    [117.14572573981584, 34.217576537035306],
    [117.14575407467446, 34.21760486902998],
    [117.14575407467446, 34.21760486902998],
    [117.14578074289078, 34.217633201103446],
    [117.14578074289078, 34.217633201103446],
    [117.14581074450578, 34.21766319968603],
    [117.14581074450578, 34.21766319968603],
    [117.14584574604737, 34.21769319803228],
    [117.14584574604737, 34.21769319803228],
    [117.14587908117514, 34.217726529790724],
    [117.14587908117514, 34.217726529790724],
    [117.14591408294508, 34.21775986147036],
    [117.14591408294508, 34.21775986147036],
    [117.1459490843725, 34.217788193149865],
    [117.1459490843725, 34.217788193149865],
    [117.14598241938614, 34.2178198582416],
    [117.14598241938614, 34.2178198582416],
    [117.14600575443228, 34.21784985713932],
    [117.14600575443228, 34.21784985713932],
    [117.14602742272196, 34.21787818944913],
    [117.14602742272196, 34.21787818944913],
    [117.14605075742556, 34.21790318834675],
    [117.14605075742556, 34.21790318834675],
    [117.14607409247174, 34.217933187244476],
    [117.14607409247174, 34.217933187244476],
    [117.14610242767279, 34.21796651923924],
    [117.14610242767279, 34.21796651923924],
    [117.14612742947529, 34.21799818472489],
    [117.14612742947529, 34.21799818472489],
    [117.14615576433393, 34.21802651671955],
    [117.14615576433393, 34.21802651671955],
    [117.14618909911911, 34.218054848477834],
    [117.14618909911911, 34.218054848477834],
    [117.14622243379017, 34.21808151356941],
    [117.14622243379017, 34.21808151356941],
    [117.14625243506265, 34.21810651215185],
    [117.14625243506265, 34.21810651215185],
    [117.14628243656345, 34.21813484406771],
    [117.14628243656345, 34.21813484406771],
    [117.14631077142207, 34.21816317606236],
    [117.14631077142207, 34.21816317606236],
    [117.14633577345295, 34.218198174881415],
    [117.14633577345295, 34.218198174881415],
    [117.14636077548379, 34.21823317370046],
    [117.14636077548379, 34.21823317370046],
    [117.14638411087242, 34.21826817259828],
    [117.14638411087242, 34.21826817259828],
    [117.14641244630187, 34.21830483792646],
    [117.14641244630187, 34.21830483792646],
    [117.14644677189787, 34.218327445131365],
    [117.14647935885547, 34.21834543586456],
    [117.14650788025703, 34.21836568515139],
    [117.14653979289895, 34.218385930379725],
    [117.14657611805501, 34.21840842403233],
    [117.14661686353962, 34.21843767350759],
    [117.14666100418759, 34.21846917261515],
    [117.14671363466667, 34.21850742266882],
    [117.14676830384131, 34.218547923965836],
    [117.14681718842192, 34.21857716363376],
    [117.14686438132917, 34.218608659013455],
    [117.14690920040576, 34.218640157218196],
    [117.14695299431811, 34.218667149223165],
    [117.14699916212575, 34.218694138367155],
    [117.14687247334851, 34.218798149526236],
    [117.14687247334851, 34.218798149526236],
    [117.14690985248089, 34.21882045289573],
    [117.14690247496351, 34.21882814810876],
    [117.14690247496351, 34.21882814810876],
    [117.14692914329412, 34.21885814684888],
    [117.14692914329412, 34.21885814684888],
    [117.1469574782669, 34.21888814551017],
    [117.1469574782669, 34.21888814551017],
    [117.14698081308472, 34.21891481107445],
    [117.14698081308472, 34.21891481107445],
    [117.1470058146589, 34.21894314322661],
    [117.1470058146589, 34.21894314322661],
    [117.14703748291603, 34.21897314173035],
    [117.14703748291603, 34.21897314173035],
    [117.14707415098579, 34.219001473331005],
    [117.14707415098579, 34.219001473331005],
    [117.14711248558345, 34.21902813818617],
    [117.14711248558345, 34.21902813818617],
    [117.14714415372647, 34.21905647002317],
    [117.14714415372647, 34.21905647002317],
    [117.14717248904184, 34.21909146868459],
    [117.14717248904184, 34.21909146868459],
    [117.14719415755995, 34.21912313432778],
    [117.14719415755995, 34.21912313432778],
    [117.14721749249186, 34.219151466558706],
    [117.14721749249186, 34.219151466558706],
    [117.14723916089584, 34.21918146553516],
    [117.14723916089584, 34.21918146553516],
    [117.14726249594203, 34.21921146443281],
    [117.14726249594203, 34.21921146443281],
    [117.14729249755703, 34.21924146301531],
    [117.14729249755703, 34.21924146301531],
    [117.14732416547167, 34.21926646151892],
    [117.14732416547167, 34.21926646151892],
    [117.14736416659746, 34.21929145962856],
    [117.14736416659746, 34.21929145962856],
    [117.147405834137, 34.219313124326],
    [117.147405834137, 34.219313124326],
    [117.14744750133406, 34.21932978902333],
    [117.14744750133406, 34.21932978902333],
    [117.14749083494497, 34.219343120308466],
    [117.14749083494497, 34.219343120308466],
    [117.14753583451306, 34.219346451514575],
    [117.14753583451306, 34.219346451514575],
    [117.147580833396, 34.219339782720446],
    [117.147580833396, 34.219339782720446],
    [117.14762749869278, 34.219329780514144],
    [117.14762749869278, 34.219329780514144],
    [117.1476708307052, 34.219319778465405],
    [117.1476708307052, 34.219319778465405],
    [117.14771416260345, 34.219308109749974],
    [117.14771416260345, 34.219308109749974],
    [117.14775416110307, 34.21929477452539],
    [117.14775416110307, 34.21929477452539],
    [117.14778749303382, 34.219281439615976],
    [117.14778749303382, 34.219281439615976],
    [117.14783082493206, 34.21926977090053],
    [117.14783082493206, 34.21926977090053],
    [117.14787082388834, 34.219263102342794],
    [117.14787082388834, 34.219263102342794],
    [117.14791415612912, 34.21925643362747],
    [117.14791415612912, 34.21925643362747],
    [117.14795069161512, 34.21924515210899],
    [117.14799238836201, 34.21923608698105],
    [117.14803950717418, 34.219224761588976],
    [117.14808595166501, 34.219215690698476],
    [117.14813578346065, 34.219204361993725],
    [117.14819645543251, 34.21918625905442],
    [117.14825745466062, 34.21916139457294],
    [117.14831541357006, 34.21914329485426],
    [117.14837439378239, 34.21912744757818],
    [117.1484364261025, 34.21911159657993],
    [117.14850354132729, 34.21909348569046],
    [117.14858083028543, 34.21907536243984],
    [117.14865810733484, 34.21905047803828],
    [117.1487367448, 34.21902784564379],
    [117.14860080609681, 34.21915973449789],
    [117.14860080609681, 34.21915973449789],
    [117.14862810327912, 34.21915193115039],
    [117.14864080471051, 34.21914806594007],
    [117.14864080471051, 34.21914806594007],
    [117.14867913702459, 34.219141397461144],
    [117.14867913702459, 34.219141397461144],
    [117.14872913594832, 34.21913639509742],
    [117.14872913594832, 34.21913639509742],
    [117.14877746788729, 34.219126392812335],
    [117.14877746788729, 34.219126392812335],
    [117.14882079989962, 34.21911639076365],
    [117.14882079989962, 34.21911639076365],
    [117.14886746473967, 34.21909972189057],
    [117.14886746473967, 34.21909972189057],
    [117.14890746266833, 34.21907805333253],
    [117.14890746266833, 34.21907805333253],
    [117.14894579463981, 34.21906638485349],
    [117.14894579463981, 34.21906638485349],
    [117.1489891267664, 34.21905804947151],
    [117.1489891267664, 34.21905804947151],
    [117.14904412527414, 34.21904804687132],
    [117.14904412527414, 34.21904804687132],
    [117.14909079045667, 34.219036377998364],
    [117.14909079045667, 34.219036377998364],
    [117.14914412197967, 34.21902137547685],
    [117.14914412197967, 34.21902137547685],
    [117.1491907872764, 34.21901137327058],
    [117.1491907872764, 34.21901137327058],
    [117.14924578578412, 34.219001370670405],
    [117.14924578578412, 34.219001370670405],
    [117.14930411780468, 34.21899470124604],
    [117.14930411780468, 34.21899470124604],
    [117.14935911688326, 34.21899303197935],
    [117.14935911688326, 34.21899303197935],
    [117.14941411561934, 34.21898636271258],
    [117.14941411561934, 34.21898636271258],
    [117.14946078114446, 34.21897969383972],
    [117.14946078114446, 34.21897969383972],
    [117.14950411315672, 34.218969691791074],
    [117.14950411315672, 34.218969691791074],
    [117.14953744543001, 34.21896135688183],
    [117.14953744543001, 34.21896135688183],
    [117.14958411095495, 34.218954688009],
    [117.14958411095495, 34.218954688009],
    [117.1496257768959, 34.21895301937261],
    [117.1496257768959, 34.21895301937261],
    [117.1496691093649, 34.218949683990765],
    [117.1496691093649, 34.218949683990765],
    [117.14971910794604, 34.21893968162695],
    [117.14971910794604, 34.21893968162695],
    [117.14976577312854, 34.21892801275401],
    [117.14976577312854, 34.21892801275401],
    [117.14980910502659, 34.218916344038654],
    [117.14980910502659, 34.218916344038654],
    [117.14985910360772, 34.21890634167486],
    [117.14985910360772, 34.21890634167486],
    [117.14990076886356, 34.21889467303828],
    [117.14990076886356, 34.21889467303828],
    [117.14994243400528, 34.21888133773501],
    [117.14994243400528, 34.21888133773501],
    [117.14998743300222, 34.218876335607696],
    [117.14998743300222, 34.218876335607696],
    [117.15003243211339, 34.21887300014705],
    [117.15003243211339, 34.21887300014705],
    [117.15007743111036, 34.21886799801971],
    [117.15007743111036, 34.21886799801971],
    [117.15011742972406, 34.218856329461936],
    [117.15011742972406, 34.218856329461936],
    [117.15015576158135, 34.218842994316255],
    [117.15015576158135, 34.218842994316255],
    [117.1502081921914, 34.21882547259039],
    [117.1502701719254, 34.21878032255654],
    [117.15031042364137, 34.21872167688784],
    [117.15033001677494, 34.218678832467575],
    [117.150341143808, 34.218642759538724],
    [117.15031495123603, 34.21859771752942],
    [117.15027451951548, 34.21855494666698],
    [117.1504274131857, 34.21868131480428],
    [117.1504274131857, 34.21868131480428],
    [117.150429077202, 34.21864298139139],
    [117.150429077202, 34.21864298139139],
    [117.15041705143109, 34.21861111459015],
    [117.15042574152001, 34.21860798154827],
    [117.15042574152001, 34.21860798154827],
    [117.1504174059114, 34.21857298194153],
    [117.1504174059114, 34.21857298194153],
    [117.15040907041696, 34.218539649001485],
    [117.15040907041696, 34.218539649001485],
    [117.15039573522428, 34.21850964963118],
    [117.15039573522428, 34.21850964963118],
    [117.15038739950151, 34.21847298335771],
    [117.15038739950151, 34.21847298335771],
    [117.15037573095101, 34.218442983908616],
    [117.15037573095101, 34.218442983908616],
    [117.1503707289693, 34.21841298414438],
    [117.1503707289693, 34.21841298414438],
    [117.1503740600845, 34.21838131731952],
    [117.1503740600845, 34.21838131731952],
    [117.15037572467165, 34.21835131724014],
    [117.15037572467165, 34.21835131724014],
    [117.15036405680617, 34.218331317791254],
    [117.15036405680617, 34.218331317791254],
    [117.15036072146673, 34.218301317948224],
    [117.15036072146673, 34.218301317948224],
    [117.15035238631484, 34.218272985008255],
    [117.15035238631484, 34.218272985008255],
    [117.15034738410478, 34.21823965191064],
    [117.15034738410478, 34.21823965191064],
    [117.15033904861045, 34.21820631897056],
    [117.15033904861045, 34.21820631897056],
    [117.15033237952987, 34.21816965261831],
    [117.15033237952987, 34.21816965261831],
    [117.15032071109356, 34.218141319835915],
    [117.15032071109356, 34.218141319835915],
    [117.15031070952784, 34.218116320308155],
    [117.15031070952784, 34.218116320308155],
    [117.15027070885911, 34.21809798886528],
    [117.15027070885911, 34.21809798886528],
    [117.15025237419651, 34.218074656398116],
    [117.15025237419651, 34.218074656398116],
    [117.1502290393789, 34.21804799083391],
    [117.1502290393789, 34.21804799083391],
    [117.15021403765823, 34.21801965820907],
    [117.15021403765823, 34.21801965820907],
    [117.15019070272659, 34.217991325978154],
    [117.15019070272659, 34.217991325978154],
    [117.15016570126684, 34.217964660492726],
    [117.15016570126684, 34.217964660492726],
    [117.15014569984781, 34.217939661437654],
    [117.15014569984781, 34.217939661437654],
    [117.15012903171325, 34.21791466222499],
    [117.15012903171325, 34.21791466222499],
    [117.15011403022095, 34.217889662933544],
    [117.15011403022095, 34.217889662933544],
    [117.15009402880195, 34.21786466387847],
    [117.15009402880195, 34.21786466387847],
    [117.1500633555019, 34.21785204899942],
    [117.1500484222146, 34.217845306151624],
    [117.1500569082172, 34.2178498031816],
    [117.15007015789115, 34.217863309206166],
    [117.15007217263445, 34.217852038211305],
    [117.15009757469758, 34.21783397747985],
    [117.15011178977568, 34.217818184141265],
    [117.15012125716446, 34.21780239661213],
    [117.15013039742209, 34.217793370600546],
    [117.15014529872342, 34.21778208382992],
    [117.15016595706653, 34.21776628259714],
    [117.15017949787918, 34.21775274378204],
    [117.15017848051889, 34.21775274502775],
    [117.15017204523456, 34.21775726031914],
    [117.1501923382012, 34.217536325890336],
    [117.1501923382012, 34.217536325890336],
    [117.15023400368551, 34.21752799058725],
    [117.15023400368551, 34.21752799058725],
    [117.15025334909748, 34.21751826790792],
    [117.15024400239706, 34.217511323447546],
    [117.15024400239706, 34.217511323447546],
    [117.15023733548576, 34.217506323762585],
    [117.15023733548576, 34.217506323762585],
    [117.15023400265801, 34.217512990586975],
    [117.15023400265801, 34.217512990586975],
    [117.1502356683869, 34.21749965717457],
    [117.1502356683869, 34.21749965717457],
    [117.15023566804439, 34.21749465717448],
    [117.15023566804439, 34.21749465717448],
    [117.15023400094556, 34.21748799058645],
    [117.15023400094556, 34.21748799058645],
    [117.1502340004889, 34.21748132391966],
    [117.1502340004889, 34.21748132391966],
    [117.15024899798543, 34.21744798987661],
    [117.15024899798543, 34.21744798987661],
    [117.15026399582445, 34.217419655833666],
    [117.15026399582445, 34.217419655833666],
    [117.15027066147998, 34.217406322184935],
    [117.15027066147998, 34.217406322184935],
    [117.15028232649125, 34.21738465496637],
    [117.15028232649125, 34.21738465496637],
    [117.15027399316607, 34.217382988693586],
    [117.15027399316607, 34.217382988693586],
    [117.15027232698056, 34.21738965543917],
    [117.15027232698056, 34.21738965543917],
    [117.15027566003658, 34.217386321948176],
    [117.15027566003658, 34.217386321948176],
    [117.15027066033834, 34.21738965551796],
    [117.15027066033834, 34.21738965551796],
    [117.15025566124345, 34.217399656227194],
    [117.15025566124345, 34.217399656227194],
    [117.15026232792648, 34.21740132257876],
    [117.15026232792648, 34.21740132257876],
    [117.15031232662176, 34.21739298688177],
    [117.15031232662176, 34.21739298688177],
    [117.15034232629561, 34.21739465213035],
    [117.15034232629561, 34.21739465213035],
    [117.15036065981653, 34.21740131793054],
    [117.15036065981653, 34.21740131793054],
    [117.15038399337817, 34.21740965016107],
    [117.15038399337817, 34.21740965016107],
    [117.15039899395714, 34.217421316118916],
    [117.15039899395714, 34.217421316118916],
    [117.15044232688281, 34.217424647403945],
    [117.15044232688281, 34.217424647403945],
    [117.15046399345978, 34.21742797971317],
    [117.15046399345978, 34.21742797971317],
    [117.1504673269725, 34.217431312889005],
    [117.1504673269725, 34.217431312889005],
    [117.15046232750251, 34.21743797979216],
    [117.15046232750251, 34.21743797979216],
    [117.15045899456065, 34.21744297994981],
    [117.15045899456065, 34.21744297994981],
    [117.15046232818756, 34.217447979792325],
    [117.15046232818756, 34.217447979792325],
    [117.1504706618552, 34.217454646065214],
    [117.1504706618552, 34.217454646065214],
    [117.15048732861973, 34.2174596452775],
    [117.15048732861973, 34.2174596452775],
    [117.15050732832623, 34.21745964433209],
    [117.15050732832623, 34.21745964433209],
    [117.15051472579323, 34.21747061960365],
    [117.15052153221944, 34.21748413348711],
    [117.15052358697318, 34.2174953994957],
    [117.15052495948132, 34.21750441263546],
    [117.15052565375142, 34.21751342660759],
    [117.15052736537918, 34.21752243933113],
    [117.15052839876898, 34.217531452887],
    [117.15052977127812, 34.217540466026676],
    [117.15053114378767, 34.21754947916631],
    [117.15053285942493, 34.21756074559081],
    [117.15053491418206, 34.21757201159906],
    [117.15053629070087, 34.21758327843967],
    [117.15053834946737, 34.21759679814889],
    [117.15053905175645, 34.21761031952299],
    [117.15059732848928, 34.217481306744865],
    [117.15059732848928, 34.217481306744865],
    [117.15059749487587, 34.217484040239725],
    [117.15059899501736, 34.2174796399994],
    [117.15059899501736, 34.2174796399994],
    [117.15060066165954, 34.21747963992061],
    [117.15060066165954, 34.21747963992061],
]

#UDP_IP = "180.123.139.174"
UDP_IP = "127.0.0.1"
UDP_PORT = 8887

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

if __name__ == "__main__":
    for pos in poss:
        time.sleep(0.25)
        msg = ','.join(['V2', 'XHC#2', str(pos[0]), str(pos[1]), "ORI", "V", "ACC", "TS"])
        print msg
        sock.sendto(msg, (UDP_IP, UDP_PORT))
