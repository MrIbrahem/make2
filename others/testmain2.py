#!/usr/bin/python3
"""

"""
#
# (C) Ibrahem Qasim, 2022
#
#
# ---
from make2 import printe
import sys
from make2.memory import print_memory

# ---
if True:
    OIUHNM = {}
    OIUHNM2 = {
        "Category:Egyptian male sport shooters": "تصنيف:لاعبو رماية ذكور مصريون",
        "Category:Female association football managers": "تصنيف:منظمات عسكرية حسب البلد",
        "Category:Military organization by country": "تصنيف:منظمات عسكرية حسب البلد",
        "Category:2000s in film": "تصنيف:عقد 2000 في الأفلام",
        "Category:Animals by year of formal description": "تصنيف:حيوانات حسب سنة الوصف",
        "Category:1994–95 in European rugby union by country": "تصنيف:اتحاد الرجبي الأوروبي حسب البلد في 1994–95",
        "Category:Olympic shooters of Egypt": "تصنيف:رماة أولمبيون من مصر",
        "Category:Peruvian documentary film directors": "تصنيف:مخرجو أفلام وثائقية بيروفيون",
        "Category:Books about automobiles": "تصنيف:كتب عن سيارات",
        "Category:Participants in British reality television series": "تصنيف:مشاركون في مسلسلات تلفزيونية واقعية بريطانية",
        "Category:21st-century films": "تصنيف:أفلام القرن 21",
        "Category:Tetrapods by century of formal description": "تصنيف:رباعيات أطراف حسب قرن الوصف",
        "Category:Women's universities and colleges in India": "تصنيف:جامعات وكليات نسائية في الهند",
        "Category:Songs about automobiles": "تصنيف:أغاني عن سيارات",
        "Category:Disney animated films": "تصنيف:أفلام ديزني رسوم متحركة",
        "Category:2000s in American cinema": "تصنيف:السينما الأمريكية في عقد 2000",
        "Category:documentary filmmakers by nationality": "تصنيف:صانعو أفلام وثائقية حسب الجنسية",
        "Category:Works about automobiles": "تصنيف:أعمال عن سيارات",
        "Category:Films about automobiles": "تصنيف:أفلام عن سيارات",
        "Category:yemeni war filmmakers": "تصنيف:صانعو أفلام حربية يمنيون",
        "Category:Egyptian female sport shooters": "تصنيف:لاعبات رماية مصريات",
        "Category:2000s films": "تصنيف:أفلام إنتاج عقد 2000",
        "Category:World Judo Championships": "تصنيف:بطولة العالم للجودو",
        "Category:Egyptian sport shooters": "تصنيف:لاعبو رماية مصريون",
        "Category:1902 films": "تصنيف:أفلام إنتاج 1902",
        "Category:Military alliances involving Yemen": "تصنيف:تحالفات عسكرية تشمل اليمن",
        "Category:Peruvian television actors": "تصنيف:ممثلو تلفزيون بيروفيون",
        "Category:Fish described in 1995": "تصنيف:أسماك اكتشفت في 1995",
        "Category:Military alliances involving Japan": "تصنيف:تحالفات عسكرية تشمل اليابان",
        "Category:2000s American films": "تصنيف:أفلام أمريكية عقد 2000",
        "Category:Berlin University of the Arts": "تصنيف:جامعة برلين للفنون",
        "Category:Vertebrates described in the 20th century": "تصنيف:فقاريات وصفت في القرن 20",
        "Category:Mammals by century of formal description": "تصنيف:ثدييات حسب قرن الوصف",
        "Category:21st century in film": "تصنيف:القرن 21 في الأفلام",
        "Category:songs about busan": "تصنيف:أغاني عن بوسان",
        "Category:British television chefs": "تصنيف:طباخو تلفاز بريطانيون",
        "Category:Films set in the 21st century": "تصنيف:أفلام تقع أحداثها في القرن 21",
        "Category:Treaties extended to Curaçao": "تصنيف:معاهدات امتدت إلى كوراساو",
        "Category:South Korean television series by production location": "تصنيف:مسلسلات تلفزيونية كورية جنوبية حسب موقع الإنتاج",
        "Category:Mystery films by genre": "تصنيف:أفلام غموض حسب النوع الفني",
        "Category:Israeli people of Northern Ireland descent": "تصنيف:إسرائيليون من أصل أيرلندي شمالي",
        "Category:Sports broadcasters by nationality": "تصنيف:مذيعون رياضيون حسب الجنسية",
        "Category:Spanish sports broadcasters": "تصنيف:مذيعون رياضيون إسبان",
        "Category:Canadian sports businesspeople": "تصنيف:رجال أعمال رياضيون كنديون",
        "Category:Spy films by genre": "تصنيف:أفلام تجسسية حسب النوع الفني",
        "Category:American_television_series_based_on_British_television_series": "تصنيف:مسلسلات تلفزيونية أمريكية مبنية على مسلسلات تلفزيونية بريطانية",
        "Category:films by country": "تصنيف:أفلام حسب البلد",
        "Category:Television shows by city of setting": "تصنيف:عروض تلفزيونية حسب مدينة الحدث",
        "Category:Afghan expatriates": "تصنيف:مغتربون أفغان",
        "Category:Ethnic groups of the Dominican Republic": "تصنيف:مجموعات عرقية في جمهورية الدومينيكان",
        "Category:1000s disestablishments in Asia": "تصنيف:انحلالات عقد 1000 في آسيا",
        "Category:Transport companies established in 1909": "تصنيف:شركات نقل أنشئت في 1909",
        "Category:parks in the Roman Empire": "تصنيف:متنزهات في الإمبراطورية الرومانية",
        "Category:Video games about diseases": "تصنيف:ألعاب فيديو عن الأمراض",
        "Category:Television shows set in Australia by city": "تصنيف:عروض تلفزيونية تقع أحداثها في أستراليا حسب المدينة",
        "Category:England amateur international footballers": "تصنيف:لاعبو منتخب إنجلترا لكرة القدم للهواة",
        "Category:War films by genre": "تصنيف:أفلام حربية حسب النوع الفني",
        "Category:Road bridges by country": "تصنيف:جسور طرق حسب البلد",
        "Category:Video games about slavery": "تصنيف:ألعاب فيديو عن العبودية",
        "Category:International women's basketball competitions hosted by Cuba": "تصنيف:منافسات كرة سلة نسائية دولية تستضيفها كوبا",
        "Category:Science fiction films by genre": "تصنيف:أفلام علمية خيالية حسب النوع الفني",
        "Category:Characters in children's literature": "تصنيف:شخصيات في أدب أطفال",
        "Category:Penal system in Afghanistan": "تصنيف:قانون العقوبات في أفغانستان",
        "Category:Afghanistan women's national football team coaches": "تصنيف:مدربو منتخب أفغانستان الوطني لكرة القدم للنساء",
        "Category:Television series by city of location": "تصنيف:مسلسلات تلفزيونية حسب مدينة الموقع",
        "Category:Lists of television characters by series": "تصنيف:قوائم شخصيات تلفزيونية حسب السلسلة",
        "Category:Decades in Oklahoma": "تصنيف:عقود في أوكلاهوما",
        "Category:Fantasy films by genre": "تصنيف:أفلام فانتازيا حسب النوع الفني",
        "Category:Women's national under-18 ice hockey teams": "تصنيف:منتخبات هوكي جليد وطنية نسائية تحت 18 سنة",
        "Category:Women's national ice hockey teams": "تصنيف:منتخبات هوكي جليد وطنية نسائية",
        "Category:1990s disestablishments in Europe": "تصنيف:انحلالات عقد 1990 في أوروبا",
        "Category:1st century BC": "تصنيف:القرن 1 ق م",
        "Category:Comics set in the 1st century BC": "تصنيف:قصص مصورة تقع أحداثها في القرن 1 ق م",
        "Category:Philippine films by subgenre": "تصنيف:أفلام فلبينية حسب النوع الفرعي",
        "Category:2017 American television seasons": "تصنيف:مواسم تلفزيونية أمريكية 2017",
        "Category:Dinosaurs in fiction": "تصنيف:ديناصورات في الخيال",
        "Category:Films shot in China by city": "تصنيف:أفلام مصورة في الصين حسب المدينة",
        "Category:Celtic mythology in popular culture": "تصنيف:أساطير كلتية في الثقافة الشعبية",
        "Category:Fantasy video games": "تصنيف:ألعاب فيديو فانتازيا",
        "Category:2017–18 in Emirati football": "تصنيف:كرة القدم الإماراتية في 2017–18",
        "Category:Rail transport in Sri Lanka by province": "تصنيف:السكك الحديدية في سريلانكا حسب الإقليم",
        "Category:History of the British Army": "تصنيف:تاريخ الجيش البريطاني",
        "Category:History of the Royal Navy": "تصنيف:تاريخ البحرية الملكية",
        "Category:Polish businesspeople": "تصنيف:رجال أعمال بولنديون",
        "Category:Historical fiction by setting": "تصنيف:خيال تاريخي حسب موقع الأحداث",
        "Category:Films by continent": "تصنيف:أفلام حسب القارة",
        "Category:Afghanistan national football team managers": "تصنيف:مدربو منتخب أفغانستان الوطني لكرة القدم",
        "Category:Films by topic": "تصنيف:أفلام حسب الموضوع",
        "Category:ugandan football": "تصنيف:كرة القدم الأوغندية",
        "Category:2017 events": "تصنيف:أحداث 2017",
        "Category:1270s in the Holy Roman Empire": "تصنيف:عقد 1270 في الإمبراطورية الرومانية المقدسة",
        "Category:Belgian athletics coaches": "تصنيف:مدربو ألعاب القوى بلجيكيون",
        "Category:19th-century people by religion": "تصنيف:أشخاص حسب الدين في القرن 19",
        "Category:18th-century people of the Dutch Empire": "تصنيف:أشخاص من الإمبراطورية الهولندية في القرن 18",
        "Category:Films by city of shooting location": "تصنيف:أفلام حسب مدينة التصوير",
        "Category:Films based on television series": "تصنيف:أفلام مبنية على مسلسلات تلفزيونية",
        "Category:History of the Royal Air Force": "تصنيف:تاريخ القوات الجوية الملكية",
        "Category:Ivorian diaspora in Asia": "تصنيف:شتات إيفواري في آسيا",
        "Category:Films by director": "تصنيف:أفلام حسب المخرج",
        "Category:Films by technology": "تصنيف:أفلام حسب التكنولوجيا",
        "Category:Canada men's international soccer players": "تصنيف:لاعبو منتخب كندا لكرة القدم للرجال",
        "Category:American people of the Iraq War": "تصنيف:أمريكيون من حرب العراق",
        "Category:Thriller films by genre": "تصنيف:أفلام إثارة حسب النوع الفني",
        "Category:Action films by genre": "تصنيف:أفلام حركة حسب النوع الفني",
        "Category:Pornographic films by genre": "تصنيف:أفلام إباحية حسب النوع الفني",
        "Category:football in 2050–51": "تصنيف:كرة القدم في 2050–51",
        "Category:10th millennium in fiction": "تصنيف:الألفية 10 في الخيال",
        "Category:2017 sports events": "تصنيف:أحداث رياضية 2017",
        "Category:Cartoonists by publication": "تصنيف:كارتونيون حسب المؤسسة",
        "Category:Video games set in the Byzantine Empire": "تصنيف:ألعاب فيديو تقع أحداثها في الإمبراطورية البيزنطية",
        "Category:Ivorian emigrants": "تصنيف:مهاجرون إيفواريون",
        "Category:2017 events by country": "تصنيف:أحداث 2017 حسب البلد",
        "Category:Women's national sports teams of Cuba": "تصنيف:منتخبات رياضية وطنية نسائية في كوبا",
        "Category:Association football players by women's national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني للنساء",
        "Category:19th-century publications": "تصنيف:منشورات القرن 19",
        "Category:20th-century disestablishments in India": "تصنيف:انحلالات القرن 20 في الهند",
        "Category:Political films by genre": "تصنيف:أفلام سياسة حسب النوع الفني",
        "Category:Penal systems by country": "تصنيف:قانون العقوبات حسب البلد",
        "Category:Ambassadors by mission country": "تصنيف:سفراء حسب بلد البعثة",
        "Category:Mammals described in 2017": "تصنيف:ثدييات اكتشفت في 2017",
        "Category:Films by studio": "تصنيف:أفلام حسب استوديو الإنتاج",
        "Category:Films by movement": "تصنيف:أفلام حسب الحركة",
        "Category:Argentina women's international footballers": "تصنيف:لاعبات منتخب الأرجنتين لكرة القدم للنساء",
        "Category:Attacks on diplomatic missions": "تصنيف:هجمات على بعثات دبلوماسية",
        "Category:Ivorian American": "تصنيف:أمريكيون إيفواريون",
        "Category:1000 disestablishments by country": "تصنيف:انحلالات سنة 1000 حسب البلد",
        "Category:Historical comics": "تصنيف:قصص مصورة تاريخية",
        "Category:multi-sport events at Yemen": "تصنيف:أحداث رياضية متعددة في اليمن",
        "Category:Lists of British television series characters by series": "تصنيف:قوائم شخصيات مسلسلات تلفزيونية بريطانية حسب السلسلة",
        "Category:18th-century Dutch explorers": "تصنيف:مستكشفون هولنديون في القرن 18",
        "Category:1370s conflicts": "تصنيف:نزاعات عقد 1370",
        "Category:2017 American television series": "تصنيف:مسلسلات تلفزيونية أمريكية 2017",
        "Category:History of the British National Party": "تصنيف:تاريخ الحزب الوطني البريطاني",
        "Category:Films by city": "تصنيف:أفلام حسب المدينة",
        "Category:Mystery films by country": "تصنيف:أفلام غموض حسب البلد",
        "Category:LGBT-related films by genre": "تصنيف:أفلام متعلقة بإل جي بي تي حسب النوع الفني",
        "Category:2006 Winter Paralympics events": "تصنيف:أحداث الألعاب البارالمبية الشتوية 2006",
        "Category:July 2018 events by continent": "تصنيف:أحداث يوليو 2018 حسب القارة",
        "Category:Films by setting": "تصنيف:أفلام حسب موقع الأحداث",
        "Category:women in business": "تصنيف:سيدات أعمال",
        "Category:Ambassadors of Afghanistan to Australia": "تصنيف:سفراء أفغانستان إلى أستراليا",
        "Category:British editorial cartoonists": "تصنيف:محررون كارتونيون بريطانيون",
        "Category:1000 disestablishments in Europe": "تصنيف:انحلالات سنة 1000 في أوروبا",
        "Category:Immigrants to the United Kingdom from Aden": "تصنيف:مهاجرون إلى المملكة المتحدة من عدن",
        "Category:Ambassadors of the Ottoman Empire": "تصنيف:سفراء الدولة العثمانية",
        "Category:landmarks in Yemen": "تصنيف:معالم في اليمن",
        "Category:Russian folklore characters": "تصنيف:شخصيات فلكلورية روسية",
        "Category:Comics adapted into films": "تصنيف:قصص مصورة تم تحويلها إلى أفلام",
        "Category:films by country": "تصنيف:أفلام حسب البلد",
        "Category:Multi-sport events in the Soviet Union": "تصنيف:أحداث رياضية متعددة في الاتحاد السوفيتي",
        "Category:Australian Internet celebrities": "تصنيف:مشاهير إنترنت أستراليون",
        "Category:Women in business by nationality": "تصنيف:سيدات أعمال حسب الجنسية",
        "Category:Association football players by amateur national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني للهواة",
        "Category:Films by shooting location": "تصنيف:أفلام حسب موقع التصوير",
        "Category:Cape Verde at the Paralympics": "تصنيف:الرأس الأخضر في الألعاب البارالمبية",
        "Category:Afghan emigrants": "تصنيف:مهاجرون أفغان",
        "Category:People of Ivorian descent": "تصنيف:أشخاص من أصل إيفواري",
        "Category:People by nationality and status": "تصنيف:أشخاص حسب الجنسية والحالة",
        "Category:Australia international soccer players": "تصنيف:لاعبو منتخب أستراليا لكرة القدم",
        "Category:Dinosaurs in video games": "تصنيف:ألعاب فيديو ديناصورات",
        "Category:1980 sports events in Europe": "تصنيف:أحداث 1980 الرياضية في أوروبا",
        "Category:IndyCar": "تصنيف:أندي كار",
        "Category:Historical webcomics": "تصنيف:ويب كومكس تاريخية",
        "Category:Paralympic competitors for Cape Verde": "تصنيف:منافسون بارالمبيون من الرأس الأخضر",
        "Category:Films set in national parks": "تصنيف:أفلام تقع أحداثها في متنزهات وطنية",
        "Category:Health in North Dakota": "تصنيف:الصحة في داكوتا الشمالية",
        "Category:Award winners by nationality": "تصنيف:حائزو جوائز حسب الجنسية",
        "Category:Horror films by genre": "تصنيف:أفلام رعب حسب النوع الفني",
        "Category:Sports films by genre": "تصنيف:أفلام رياضية حسب النوع الفني",
        "Category:Films by producer": "تصنيف:أفلام حسب المنتج",
        "Category:Historical poems": "تصنيف:قصائد تاريخية",
        "Category:Airlines established in 1968": "تصنيف:شركات طيران أنشئت في 1968",
        "Category:Films by genre": "تصنيف:أفلام حسب النوع الفني",
        "Category:Immigration to New Zealand": "تصنيف:الهجرة إلى نيوزيلندا",
        "Category:13th century establishments in the Roman Empire": "تصنيف:تأسيسات القرن 13 في الإمبراطورية الرومانية",
        "Category:Ambassadors to the Ottoman Empire": "تصنيف:سفراء لدى الدولة العثمانية",
        "Category:Polish women in business": "تصنيف:سيدات أعمال بولنديات",
        "Category:440s": "تصنيف:عقد 440",
        "Category:Association football players by under-21 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني تحت 21 سنة",
        "Category:1990s BC disestablishments in Asia": "تصنيف:انحلالات عقد 1990 ق م في آسيا",
        "Category:Musical films by genre": "تصنيف:أفلام موسيقية حسب النوع الفني",
        "Category:Olympic gold medalists for the United States in alpine skiing": "تصنيف:فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في التزلج على المنحدرات الثلجية",
        "Category:Association football": "تصنيف:كرة القدم",
        "Category:Olympic medalists in alpine skiing": "تصنيف:فائزون بميداليات أولمبية في التزلج على المنحدرات الثلجية",
        "Category:20th-century railway accidents": "تصنيف:حوادث سكك حديدية القرن 20",
        "Category:Emirati football in 2017": "تصنيف:كرة القدم الإماراتية في 2017",
        "Category:Airlines by year of establishment": "تصنيف:شركات طيران حسب سنة التأسيس",
        "Category:Television stations by country": "تصنيف:محطات تلفزيونية حسب البلد",
        "Category:November 2006 in Yemen": "تصنيف:نوفمبر 2006 في اليمن",
        "Category:Expatriate association football managers by country of residence": "تصنيف:مدربو كرة قدم مغتربون حسب بلد الإقامة",
        "Category:Films based on comics": "تصنيف:أفلام مبنية على قصص مصورة",
        "Category:Destroyed churches by country": "تصنيف:كنائس مدمرة حسب البلد",
        "Category:19th-century actors by religion": "تصنيف:ممثلون حسب الدين في القرن 19",
        "Category:19th-century actors": "تصنيف:ممثلون في القرن 19",
        "Category:April 1983 sports events": "تصنيف:أحداث رياضية أبريل 1983",
        "Category:Expatriate women's footballers by location": "تصنيف:لاعبات كرة قدم مغتربات حسب الموقع",
        "Category:American cinema by decade": "تصنيف:السينما الأمريكية حسب العقد",
        "Category:Sports coaches by nationality": "تصنيف:مدربون رياضيون حسب الجنسية",
        "Category:Films by type": "تصنيف:أفلام حسب الفئة",
        "Category:People by former country": "تصنيف:أشخاص حسب البلد السابق",
        "Category:Video games based on Egyptian mythology": "تصنيف:ألعاب فيديو مبنية على أساطير مصرية",
        "Category:Afghan criminal law": "تصنيف:القانون الجنائي الأفغاني",
        "Category:Video games based on mythology": "تصنيف:ألعاب فيديو مبنية على أساطير",
        "Category:Historical short stories": "تصنيف:قصص قصيرة تاريخية",
        "Category:National under-18 ice hockey teams": "تصنيف:منتخبات هوكي جليد وطنية تحت 18 سنة",
        "Category:Women's organizations based in Cuba": "تصنيف:منظمات نسائية مقرها في كوبا",
        "Category:Association football players by under-23 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني تحت 23 سنة",
        "Category:Publications by year of establishment": "تصنيف:منشورات حسب سنة التأسيس",
        "Category:Women's national youth association football teams": "تصنيف:منتخبات كرة قدم وطنية للشابات",
        "Category:Argentina at the Winter Olympics": "تصنيف:الأرجنتين في الألعاب الأولمبية الشتوية",
        "Category:Films by language": "تصنيف:أفلام حسب اللغة",
        "Category:21st-century in Qatar": "تصنيف:القرن 21 في قطر",
        "Category:2015 American television": "تصنيف:2015 التلفزة الأمريكية",
        "Category:Lists of action television characters by series": "تصنيف:قوائم شخصيات تلفزيونية حركة حسب السلسلة",
        "Category:00s establishments in the Roman Empire": "تصنيف:تأسيسات عقد 00 في الإمبراطورية الرومانية",
        "Category:977 by country": "تصنيف:977 حسب البلد",
        "Category:Swaziland at multi-sport events": "تصنيف:سوازيلاند في الأحداث الرياضية المتعددة",
        "Category:Publications by format": "تصنيف:منشورات حسب التنسيق",
        "Category:Association football players by youth national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني للشباب",
        "Category:Soviet Union at multi-sport events": "تصنيف:الاتحاد السوفيتي في الأحداث الرياضية المتعددة",
        "Category:21st century in the Czech Republic": "تصنيف:القرن 21 في التشيك",
        "Category:Television characters by series": "تصنيف:شخصيات تلفزيونية حسب السلسلة",
        "Category:Holocaust literature": "تصنيف:أدب هولوكوست",
        "Category:14th-century establishments in India": "تصنيف:تأسيسات القرن 14 في الهند",
        "Category:People executed by Afghanistan": "تصنيف:أشخاص أعدموا من قبل أفغانستان",
        "Category:Lists of association football players by national team": "تصنيف:قوائم لاعبو كرة قدم حسب المنتخب الوطني",
        "Category:Olympic medalists for the United States": "تصنيف:فائزون بميداليات أولمبية من الولايات المتحدة",
        "Category:Dark fantasy video games": "تصنيف:ألعاب فيديو فانتازيا مظلمة",
        "Category:2006 establishments by country": "تصنيف:تأسيسات سنة 2006 حسب البلد",
        "Category:Olympic gold medalists for the United States": "تصنيف:فائزون بميداليات ذهبية أولمبية من الولايات المتحدة",
        "Category:Female comics writers": "تصنيف:كاتبات قصص مصورة",
        "Category:Editorial cartoonists from Northern Ireland": "تصنيف:محررون كارتونيون من أيرلندا الشمالية",
        "Category:Emirati football in 2017–18": "تصنيف:كرة القدم الإماراتية في 2017–18",
        "Category:European women in business": "تصنيف:سيدات أعمال أوروبيات",
        "Category:Drama films by country": "تصنيف:أفلام درامية حسب البلد",
        "Category:Scottish traditions": "تصنيف:تراث إسكتلندي",
        "Category:Comics based on films": "تصنيف:قصص مصورة مبنية على أفلام",
        "Category:Airlines of Afghanistan": "تصنيف:شركات طيران أفغانستان",
        "Category:Video games set in prehistory": "تصنيف:ألعاب فيديو تقع أحداثها في ما قبل التاريخ",
        "Category:Ambassadors of Afghanistan to Argentina": "تصنيف:سفراء أفغانستان إلى الأرجنتين",
        "Category:African women's national association football teams": "تصنيف:منتخبات كرة قدم وطنية نسائية إفريقية",
        "Category:Women's national ice hockey teams": "تصنيف:منتخبات هوكي جليد وطنية نسائية",
        "Category:Expatriate women's association football players": "تصنيف:لاعبات كرة قدم مغتربات",
        "Category:Cargo airlines of the Philippines": "تصنيف:شركات الشحن الجوي في الفلبين",
        "Category:Films by culture": "تصنيف:أفلام حسب الثقافة",
        "Category:Television series by country of shooting location": "تصنيف:مسلسلات تلفزيونية حسب بلد التصوير",
        "Category:Films by date": "تصنيف:أفلام حسب التاريخ",
        "Category:Polish women by occupation": "تصنيف:بولنديات حسب المهنة",
        "Category:Equatorial Guinea women's national football team": "تصنيف:منتخب غينيا الاستوائية الوطني لكرة القدم للنساء",
        "Category:Television shows filmed in Algeria": "تصنيف:عروض تلفزيونية صورت في الجزائر",
        "Category:Drama television characters by series": "تصنيف:شخصيات تلفزيونية درامية حسب السلسلة",
        "Category:Drama films by genre": "تصنيف:أفلام درامية حسب النوع الفني",
        "Category:Romance films by genre": "تصنيف:أفلام رومانسية حسب النوع الفني",
        "Category:Television series produced in Seoul": "تصنيف:مسلسلات تلفزيونية أنتجت في سول",
        "Category:Rail transport in the United Kingdom": "تصنيف:السكك الحديدية في المملكة المتحدة",
        "Category:Teen films by genre": "تصنيف:أفلام مراهقة حسب النوع الفني",
        "Category:2017 in Emirati football": "تصنيف:كرة القدم الإماراتية في 2017",
        "Category:Awards by country": "تصنيف:جوائز حسب البلد",
        "Category:Nauru international soccer players": "تصنيف:لاعبو منتخب ناورو لكرة القدم",
        "Category:Ivorian diaspora by country": "تصنيف:شتات إيفواري حسب البلد",
        "Category:Ambassadors by country of origin": "تصنيف:سفراء حسب البلد الأصل",
        "Category:Works adapted for other media": "تصنيف:أعمال تم تحويلها إلى وسائط أخرى",
        "Category:Fantasy television characters by series": "تصنيف:شخصيات تلفزيونية فانتازيا حسب السلسلة",
        "Category:European national under-21 association football teams": "تصنيف:منتخبات كرة قدم وطنية أوروبية تحت 21 سنة",
        "Category:Comedy films by genre": "تصنيف:أفلام كوميدية حسب النوع الفني",
        "Category:Prisoners and detainees of Afghanistan": "تصنيف:سجناء ومعتقلون في أفغانستان",
        "Category:Prisons in Afghanistan": "تصنيف:سجون في أفغانستان",
        "Category:Nuclear power by country": "تصنيف:طاقة نووية حسب البلد",
        "Category:French comic": "تصنيف:قصص مصورة فرنسية",
        "Category:Immigrants to New Zealand": "تصنيف:مهاجرون إلى نيوزيلندا",
        "Category:Cape Verdean football managers": "تصنيف:مدربو كرة قدم أخضريون",
        "Category:Films based on American comics": "تصنيف:أفلام مبنية على قصص مصورة أمريكية",
        "Category:April 1983 events in Europe": "تصنيف:أحداث أبريل 1983 في أوروبا",
        "Category:Crime films by genre": "تصنيف:أفلام جريمة حسب النوع الفني",
        "Category:American television episodes": "تصنيف:حلقات تلفزيونية أمريكية",
        "Category:20th-century Albanian sports coaches": "تصنيف:مدربون رياضيون ألبان في القرن 20",
        "Category:Films by audience": "تصنيف:أفلام حسب الجمهور",
        "Category:Afghan diplomats": "تصنيف:دبلوماسيون أفغان",
        "Category:Internees at the Sheberghan Prison": "تصنيف:معتقلين في سجن شيبرغان",
        "Category:2017 American television episodes": "تصنيف:حلقات تلفزيونية أمريكية 2017",
        "Category:Ivorian expatriates": "تصنيف:مغتربون إيفواريون",
        "Category:Films by source": "تصنيف:أفلام حسب المصدر",
        "Category:Films by country": "تصنيف:أفلام حسب البلد",
        "Category:Historical television series": "تصنيف:مسلسلات تلفزيونية تاريخية",
        "Category:Women's sports teams in Cuba": "تصنيف:فرق رياضية نسائية في كوبا",
        "Category:Television programs by geographic setting": "تصنيف:برامج تلفزيونية حسب الموقع الجغرافي للأحداث",
        "Category:Erotic films by genre": "تصنيف:أفلام إغرائية حسب النوع الفني",
        "Category:South Africa international soccer players": "تصنيف:لاعبو منتخب جنوب إفريقيا لكرة القدم",
        "Category:Ambassadors of Afghanistan": "تصنيف:سفراء أفغانستان",
        "Category:2000s in the United States by state": "تصنيف:عقد 2000 في الولايات المتحدة حسب الولاية",
        "Category:Manufacturing companies established in the 2nd millennium": "تصنيف:شركات تصنيع أنشئت في الألفية 2",
        "Category:Historical novels": "تصنيف:روايات تاريخية",
        "Category:Handball competitions by country": "تصنيف:منافسات كرة يد حسب البلد",
        "Category:History of British Rail": "تصنيف:تاريخ السكك الحديدية البريطانية",
        "Category:Television series endings by year": "تصنيف:مسلسلات تلفزيونية حسب سنة انتهاء العرض",
        "Category:440s bc": "تصنيف:عقد 440 ق م",
        "Category:Association football players by under-20 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني تحت 20 سنة",
        "Category:Publications disestablished in 1946": "تصنيف:منشورات انحلت في 1946",
        "Category:Decades by country": "تصنيف:عقود حسب البلد",
        "Category:Documentary films by genre": "تصنيف:أفلام وثائقية حسب النوع الفني",
        "Category:Television series produced in Alberta": "تصنيف:مسلسلات تلفزيونية أنتجت في ألبرتا",
        "Category:Categories by province of Saudi Arabia": "تصنيف:تصنيفات حسب المقاطعة في المملكة العربية السعودية",
        "Category:Skiing coaches": "تصنيف:مدربو تزلج",
        "Category:French comic strips": "تصنيف:شرائط مصورة فرنسية",
        "Category:Olympic competitors for Cape Verde": "تصنيف:منافسون أولمبيون من الرأس الأخضر",
        "Category:Publications by year of disestablishment": "تصنيف:منشورات حسب سنة الانحلال",
        "Category:American award winners": "تصنيف:أمريكيون حائزو جوائز",
        "Category:Equatoguinean women's footballers": "تصنيف:لاعبات كرة قدم غينيات استوائيات",
        "Category:Airlines by dependent territory": "تصنيف:شركات طيران حسب الأقاليم التابعة",
        "Category:British Rail": "تصنيف:السكك الحديدية البريطانية",
        "Category:Scottish popular culture": "تصنيف:ثقافة شعبية إسكتلندية",
        "Category:Cuba women's national basketball team": "تصنيف:منتخب كوبا الوطني لكرة السلة للنساء",
        "Category:American people by status": "تصنيف:أمريكيون حسب الحالة",
        "Category:2017 American television series debuts": "تصنيف:مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017",
        "Category:Adventure films by genre": "تصنيف:أفلام مغامرات حسب النوع الفني",
        "Category:2017 American television series endings": "تصنيف:مسلسلات تلفزيونية أمريكية انتهت في 2017",
        "Category:Expatriate male actors in New Zealand": "تصنيف:ممثلون ذكور مغتربون في نيوزيلندا",
        "Category:Coaches of national cricket teams": "تصنيف:مدربو منتخبات كريكت وطنية",
        "Category:Expatriate male actors": "تصنيف:ممثلون ذكور مغتربون",
        "Category:Coaches of the West Indies national cricket team": "تصنيف:مدربو منتخب الهند الغربية الوطني للكريكت",
        "Category:Coaches of Yemen national cricket team": "تصنيف:مدربو منتخب اليمن الوطني للكريكت",
        "Category:Swedish oncologists": "تصنيف:أطباء أورام سويديون",
        "Category:Egyptian oncologists": "تصنيف:أطباء أورام مصريون",
        "Category:Vehicle manufacturing companies disestablished in 1904": "تصنيف:شركات تصنيع مركبات انحلت في 1904",
        "Category:2004 residency shows": "",
        "Category:American track and field coaches": "",
        "Category:Association football players by B national team": "",
        "Category:Comics publications": "",
        "Category:Economy of Oceania by country": "",
        "Category:Films based on works by comic book writers": "",
        "Category:Geography of Africa by country": "",
        "Category:History of association football clubs in the United Kingdom": "",
        "Category:History of companies of the United Kingdom": "",
        "Category:History of organisations based in England": "",
        "Category:History of organisations based in Northern Ireland": "",
        "Category:History of organisations based in Scotland": "",
        "Category:History of organisations based in Wales": "",
        "Category:History of organisations based in the United Kingdom": "",
        "Category:History of rail transport in the United Kingdom": "",
        "Category:Holding companies established in 1942": "",
        "Category:Ireland international rules football team coaches": "",
        "Category:January 2017 events by continent": "",
        "Category:January 2017 events": "",
        "Category:January 2017 sports events by country": "",
        "Category:January 2017 sports events": "",
        "Category:Martial arts films by genre": "",
        "Category:National association football team managers": "",
        "Category:Recipients of Afghan presidential pardons": "",
        "Category:Residency shows by artist": "",
        "Category:Residency shows in the Las Vegas Valley": "",
        "Category:Ugandan": "",
        "Category:United States Virgin Islands international soccer players": "",
        "Category:United States men's international soccer players": "",
        "Category:Western (genre) films by genre": "",
    }
    # ---
    for lango in OIUHNM2:
        OIUHNM[lango.lower()] = OIUHNM2[lango]
    # ---
    tittable2 = [
        "Category:Destroyed churches by country",
        "Category:Nuclear power by country",
        "Category:Handball competitions by country",
        "Category:Road bridges by country",
        "Category:Television stations by country",
        "Category:Mystery films by country",
        "Category:Decades in Oklahoma",
        "Category:Decades by country",
        "Category:parks in the Roman Empire",
        "Category:Economy of Oceania by country",
        "Category:Geography of Africa by country",
        "Category:2000s in the United States by state",
        "Category:10th millennium in fiction",
        "Category:2017 sports events",
        "Category:2017 events",
        "Category:January 2017 sports events by country",
        "Category:April 1983 sports events",
        "Category:April 1983 events in Europe",
        "Category:January 2017 events",
        "Category:January 2017 events by continent",
        "Category:January 2017 sports events",
        "Category:1980 sports events in Europe",
        "Category:1000 disestablishments in Europe",
        "Category:1990s disestablishments in Europe",
        "Category:1990s BC disestablishments in Asia",
        "Category:1000s disestablishments in Asia",
        "Category:00s establishments in the Roman Empire",
        "Category:13th century establishments in the Roman Empire",
        "Category:977 by country",
        "Category:2017 events by country",
        "Category:2006 establishments by country",
        "Category:1000 disestablishments by country",
    ]
    # ---
    OIUHNM2_list = [x.lower() for x in OIUHNM2]
    Yeee = """
        Category:Egyptian_oncologists
        Category:Vehicle_manufacturing_companies_disestablished_in_1904
        Category:Swedish_oncologists
        Category:Canadian_nuclear_medicine_physicians
        Category:Iranian_nuclear_medicine_physicians
        Category:Croatian_nuclear_medicine_physicians
        Category:Icelandic_male_runners
        Category:Icelandic_male_steeplechase_runners
        Category:American_nuclear_medicine_physicians
        Category:German_nuclear_medicine_physicians
        Category:Publishing_companies_disestablished_in_1905
        Category:design companies disestablished in 1905
        Category:Financial services companies disestablished in 1905
        Category:Pakistani psychiatrists
        Category:Portuguese healthcare managers
        Category:Icelandic_male_athletes
        Category:Icelandic_male_steeplechase_runners
        Category:Male_runners_by_nationality
        Category:Australian_male_sprinters
        Category:Male_steeplechase_runners
        Category:Male_long-distance_runners
        Category:Moroccan_male_middle-distance_runners
        Category:Medical_doctors_by_specialty_and_nationality
        Category:Subfields_by_academic_discipline
        Category:Scholars_by_subfield
        category:books about politics by country
        Category:Books_about_politics_by_country
        Category:Prehistory_of_Venezuela
        Category:1st-millennium_literature
        Category:1st-millennium_architecture
        Category:1st-century_architecture
        Category:10th-century_BC_architecture
        Category:Archaeology of Europe by period
        Category:National_youth_sports_teams_by_country
        Category:Hong_Kong_national_football_team_matches
        Category:Transport_disasters_in_2017
        Category:Irish_association_football_managers
        Category:Republic_of_Ireland_football_managers
        Category:Research_institutes_established_in_1900
        Category:Bridges_in_Wales_by_type
        Category:Basketball_coaches_from_Indiana
        Category:Basketball_players_from_Indiana
        Category:Basketball_people_from_Indiana
        Category:American_basketball_coaches_by_state
        """
    Yell = [x.strip() for x in Yeee.split("\n")]
    # ---
    indiana = """
        Category:Baseball players from Massachusetts
        Category:Basketball players from Massachusetts
        Category:Boxers from Massachusetts
        Category:Golfers from Massachusetts
        Category:Ice hockey people from Massachusetts
        Category:Kickboxers from Massachusetts
        Category:Lacrosse players from Massachusetts
        Category:Mixed martial artists from Massachusetts
        Category:Players of American football from Massachusetts
        Category:Professional wrestlers from Massachusetts
        Category:Racing drivers from Massachusetts
        Category:Soccer players from Massachusetts
        Category:Sports coaches from Massachusetts
        Category:Sportspeople from Boston
        Category:Sportswriters from Massachusetts
        Category:Swimmers from Massachusetts
        Category:Tennis people from Massachusetts
        Category:Track and field athletes from Massachusetts
        Category:1950s_criminal_comedy_films
        Category:1960s_black_comedy_films
        Category:1960s_criminal_comedy_films
        Category:1960s_sex_comedy_films
        Category:1970s_black_comedy_films
        Category:1970s_criminal_comedy_films
        Category:1970s_sex_comedy_films
        Category:1980s_black_comedy_films
        Category:1980s_criminal_comedy_films
        Category:American_basketball_players_by_ethnic_or_national_origin
        """
    indianalist = [x.strip() for x in indiana.split("\n")]
    # ---
    c21st = """
        Category:21st_century_in_film
        Category:21st-century_films
        Category:Films_set_in_the_21st_century
        Category:2000s_in_film
        Category:2000s_films
        Category:2000s_in_American_cinema
        Category:2000s_American_films
        Category:1902_films
        Category:Egyptian_sport_shooters
        Category:Egyptian_female_sport_shooters
        Category:Egyptian_male_sport_shooters
        Category:Olympic_shooters_of_Egypt
        Category:World_Judo_Championships
        Category:Berlin_University_of_the_Arts
        Category:Disney animated films
        Category:documentary_filmmakers_by_nationality
        Category:yemeni_war_filmmakers
        Category:Experimental_film_festivals
        Category:Works_about_automobiles
        Category:Books_about_automobiles
        Category:Films_about_automobiles
        Category:Songs_about_automobiles
        Category:Works_about_taxicabs
        Category:Peruvian documentary film directors
        Category:Peruvian_television_actors
        Category:British_television_chefs
        Category:Participants_in_British_reality_television_series
        Category:songs_about_busan
        Category:Military_alliances_involving_Yemen
        Category:Treaties extended to Curaçao
        Category:Military_organization_by_country
        Category:Military_alliances_involving_Japan
        Category:Dutch_Africanists
        Category:Organists_of_Ely_Cathedral
        Category:Fish_described_in_1995
        Category:1994–95_in_European_rugby_union_by_country
        Category:Animals_by_period_of_description
        Category:Animals_by_year_of_formal_description
        Category:Mammals_by_century_of_formal_description
        Category:Tetrapods_by_century_of_formal_description
        Category:Women's_universities_and_colleges_in_India
        Category:Vertebrates_described_in_the_20th_century

        """
    c21st_list = [x.strip() for x in c21st.split("\n")]
    # ---
    shar = """
        Category:Argentine_songwriters
        Category:Singers_from_Buenos_Aires
        Category:Illustrious_Citizens_of_Buenos_Aires
        Category:Rock_en_Español_musicians
        Category:Multi-instrumentalists
        Category:Argentine_multi-instrumentalists
        Category:EMI_Latin_artists
        Category:Latin_Grammy_Lifetime_Achievement_Award_winners
        Category:People_from_Buenos_Aires
        Category:Military_science_fiction_films
        Category:Films_set_in_China_by_city
        Category:Seasons in Omani football
        Category:American_Cinema_Editors
        Category:Crimes_in_Pennsylvania
        Category:Crime_in_Pennsylvania
        Category:Sports_organisations_of_Andorra
        Category:Multi-sport_clubs_by_country
        Category:Women's_sports_organizations_in_the_United_States
        """
    shar_list = [x.strip() for x in shar.split("\n")]
    # ---
    impooor = """
        Category:Spanish_sports_broadcasters
        Category:Sports_broadcasters_by_nationality
        Category:Canadian_sports_businesspeople
        Category:Moroccan_competitors_by_sports_event
        Category:Gymnastics_organizations
        Category:Sports organisations_by_decade of establishment
        Category:Table_tennis_clubs
        Category:Turkish expatriate sportspeople
        Category:Afghan competitors by sports event
        Category:Sports_competitors_by_nationality_and_competition
        Category:Figure_skating_reality_television_participants
        Category:Figure_skating_reality_television_series
        Category:Figure_skating_on_television
        Category:Figure_skating_media
        Category:Figure_skating_films
        Category:Films_about_Olympic_figure_skating
        Category:Films_about_the_Olympic_Games_by_athletic_event
        Category:Figure_skaters_by_competition
        Category:Films about Olympic boxing
        Category:Films about Olympic equestrian sports
        Category:Olympic figure skating
        Category:Films about Olympic figure skating
        Category:Films about Olympic gymnastics
        Category:Films about Olympic skiing
        Category:Films about Olympic swimming and diving
        Category:Films about Olympic track and field
        Category:Female_short_track_speed_skaters
        Category:Female_single_skaters_from_Georgia_(country)
        Category:Female_speed_skaters
        Category:Figure_skaters_at_the_2007_Winter_Universiade
        Category:Figure_skaters_at_the_2002_Winter_Olympics
        Category:Figure_skaters_at_the_2003_Asian_Winter_Games
        Category:Youth_athletics_competitions
        Category:Youth_sports_competitions
        Category:Youth_athletics
        Category:Norwegian_figure_skaters
        Category:Norwegian_male_pair_skaters
        Category:Norwegian_male_single_skaters
        Category:Norwegian_pair_skaters
        Category:Norwegian_short_track_speed_skaters
        Category:Olympic_figure_skaters_by_country
        Category:Olympic_figure_skaters_by_year
        Category:Olympic_figure_skaters_of_Argentina
        Category:Olympic_figure_skaters_of_Armenia
        Category:Olympic_figure_skaters_of_Australia
        Category:Olympic short track speed skaters of Japan
        Category:Argentina_at_the_Universiade
        Category:nations at the universiade
        Category:Universiade_medalists_in_water_polo
        Category:Water_polo_at_the_Summer_Universiade
        Category:Sports_at_the_Summer_Universiade
        Category:Universiade_medalists_by_sport
        Category:Ski_jumpers_at_the_2007_Winter_Universiade
        Category:Ski_jumping_at_the_Winter_Universiade
        Category:International sports competitions hosted by Mexico
        Category:Athletics_at_the_Summer_Universiade_navigational_boxes
        Category:Athletics_at_the_Universiade_navigational_boxes
        Category:Australia_at_the_Summer_Universiade
        Category:Roller_skaters_at_the_2003_Pan_American_Games
        Category:Cross-country_skiers_at_the_1992_Winter_Paralympics
        Category:Figure_skating_coaches
        Category:Figure_skating_people
        Category:Italian_defectors_to_the_Soviet_Union
        Category:2018 Summer Youth Olympics events
        Category:Nations_at_the_2010_Summer_Youth_Olympics
        Category:Years_in_north_korean_television
        Category:2006_in_Northern_Ireland_sport
        Category:2006_in_north_korean_sport
        Category:People_in_arts_occupations_by_nationality
        Category:Languages of the Cayman Islands
        Category:Government of Saint Barthélemy
        """
    impooor_list = [x.strip() for x in impooor.split("\n")]
    # ---
    manga = """
        Category:Action anime and manga
        Category:Adventure anime and manga
        Category:Apocalyptic anime and manga
        Category:Comedy anime and manga
        Category:Crime anime and manga
        Category:Drama anime and manga
        Category:Dystopian anime and manga
        Category:Ecchi anime and manga
        Category:Fantasy anime and manga
        Category:Harem anime and manga
        Category:Hentai anime and manga
        Category:Historical anime and manga
        Category:Horror anime and manga
        Category:Magical girl anime and manga
        Category:Martial arts anime and manga
        Category:Mecha anime and manga
        Category:Mystery anime and manga
        Category:Romance anime and manga
        Category:Science fiction anime and manga
        Category:Slice of life anime and manga
        Category:Sports anime and manga
        Category:Spy anime and manga
        Category:Superhero anime and manga
        Category:Supernatural anime and manga
        Category:Suspense anime and manga
        Category:Thriller anime and manga
        Category:Tragedy anime and manga
        Category:War anime and manga
        Category:Western (genre) anime and manga
        Category:Yaoi anime and manga
        Category:Yuri (genre) anime and manga
        """
    manga_list = [x.strip() for x in manga.split("\n")]
    # ---
    States = """
        Category:African-American history by state
        Category:American Civil War by state navigational boxes
        Category:American culture by state
        Category:Buildings and structures in the United States by state
        Category:Centuries in the United States by state
        Category:Communications in the United States by state
        Category:Crimes in the United States by state
        Category:Decades in the United States by state
        Category:Demographics of the United States by state
        Category:Disasters in the United States by state
        Category:Economic history of the United States by state
        Category:Economy of the United States by state
        Category:Education in the United States by state
        Category:Environment of the United States by state or territory
        Category:Forts in the United States by state
        Category:Geography of the United States by state
        Category:Health in the United States by state
        Category:Historians of U.S. states
        Category:Historic sites in the United States by state
        Category:Historic trails and roads in the United States by state
        Category:History of the American Revolution by state
        Category:History of the United States by period by state
        Category:History of the United States by state
        Category:Images of the United States by state
        Category:Labor relations in the United States by state
        Category:Landmarks in the United States by state
        Category:Legal history of the United States by state
        Category:Manufacturing in the United States by state
        Category:Military history of the United States by state
        Category:Native American history by state
        Category:Native American tribes by state
        Category:Nature reserves in the United States by state
        Category:Outlines of U.S. states
        Category:People by state in the United States
        Category:Political history of the United States by state or territory
        Category:Politics of the United States by state
        Category:Pre-statehood history of U.S. states
        Category:Protected areas of the United States by state
        Category:Riots and civil disorder in the United States by state
        Category:Science and technology in the United States by state
        Category:Slavery in the United States by state
        Category:Society of the United States by state
        Category:Sports in the United States by state
        Category:State governments of the United States
        Category:State law in the United States
        Category:States of the United States history-related lists
        Category:States of the United States-related lists
        Category:Timelines of states of the United States
        Category:Tourist attractions in the United States by state
        Category:Transportation in the United States by state
        Category:United States historical societies by state
        Category:United States symbols by state
        Category:United States wars by state
        Category:Wildlife management areas by state
        Category:Years in the United States by state
        """
    States_list = [x.strip() for x in States.split("\n")]
    # ---
    States2 = """
        Category:Alabama
        Category:Alaska
        Category:Arizona
        Category:Arkansas
        Category:California
        Category:Colorado
        Category:Connecticut
        Category:Delaware
        Category:Florida
        Category:Georgia (U.S. state)
        Category:Hawaii
        Category:Idaho
        Category:Illinois
        Category:Indiana
        Category:Iowa
        Category:Kansas
        Category:Kentucky
        Category:Louisiana
        Category:Maine
        Category:Maryland
        Category:Massachusetts
        Category:Michigan
        Category:Minnesota
        Category:Mississippi
        Category:Missouri
        Category:Montana
        Category:Nebraska
        Category:Nevada
        Category:New England states
        Category:New Hampshire
        Category:New Jersey
        Category:New Mexico
        Category:New York (state)
        Category:North Carolina
        Category:North Dakota
        Category:Ohio
        Category:Oklahoma
        Category:Oregon
        Category:Pennsylvania
        Category:Rhode Island
        Category:South Carolina
        Category:South Dakota
        Category:Tennessee
        Category:Texas
        Category:Utah
        Category:Vermont
        Category:Virginia
        Category:Washington (state)
        Category:West Virginia
        Category:Wisconsin
        Category:Wyoming
        """
    States2_list = [x.strip() for x in States2.split("\n")]
    States3 = """
        Category:Buildings and structures in Westchester County, New York
        Category:Cemeteries in Westchester County, New York
        Category:Christianity in Westchester County, New York
        Category:Churches in Westchester County, New York
        Category:Companies based in Westchester County, New York
        Category:County routes in Westchester County, New York
        Category:Culture of Westchester County, New York
        Category:Economy of Westchester County, New York
        Category:Education in Westchester County, New York
        Category:Films set in Westchester County, New York
        Category:Fire departments in Westchester County, New York
        Category:Geography of Westchester County, New York
        Category:Historic districts in Westchester County, New York
        Category:Hospitals in Westchester County, New York
        Category:Houses in Westchester County, New York
        Category:Images of Westchester County, New York
        Category:Landforms of Westchester County, New York
        Category:Museums in Westchester County, New York
        Category:National Register of Historic Places in Westchester County, New York
        Category:Parks in Westchester County, New York
        Category:People from Westchester County, New York
        Category:People from Westchester County, New York by city
        Category:People from Westchester County, New York by hamlet
        Category:People from Westchester County, New York by town
        Category:People from Westchester County, New York by village
        Category:Populated places in Westchester County, New York
        Category:Protected areas of Westchester County, New York
        Category:Schools in Westchester County, New York
        Category:Sports in Westchester County, New York
        Category:Sports venues in Westchester County, New York
        Category:Sportspeople from Westchester County, New York
        Category:Streetcar lines in Westchester County, New York
        Category:Tourist attractions in Westchester County, New York
        Category:Transportation buildings and structures in Westchester County, New York
        Category:Transportation in Westchester County, New York
        Category:Universities and colleges in Westchester County, New York
        Category:Westchester County, New York politicians
        """
    States3_list = [x.strip() for x in States3.split("\n")]
# ---
from make2.bot import event  # event(tab, **kwargs)


def maintest():
    printe.output("<<lightblue>> maintest ")
    # ---
    Test_Again = True
    # ---
    test_table = {
        "2": tittable2,
        "indiana": indianalist,
        "2x": OIUHNM2_list,
        "ye": Yell,
        "21": c21st_list,
        "sh": shar_list,
        "imp": impooor_list,
        "manga": manga_list,
        "States": States_list,
        "States2": States2_list,
        "States3": States3_list,
    }
    # ---
    # python3 core8/pwb.py make2/others/testmain2 test te:am
    # python3 core8/pwb.py make2/others/testmain2 test te:fe
    # python3 core8/pwb.py make2/others/testmain2 test te:indiana
    # python3 core8/pwb.py make2/others/testmain2 test te:manga
    # python3 core8/pwb.py make2/others/testmain2 test te:States3
    # python3 core8/pwb.py make2/others/testmain2 test te:States2
    # python3 core8/pwb.py make2/others/testmain2 test te:States
    # python3 core8/pwb.py make2/others/testmain2 test te:op
    # python3 core8/pwb.py make2/others/testmain2 test te:new
    # python3 core8/pwb.py make2/others/testmain2 test te:sh
    # python3 core8/pwb.py make2/others/testmain2 test te:ddd
    # python3 core8/pwb.py make2/others/testmain2 test te:21
    # python3 core8/pwb.py make2/others/testmain2 test te:imp
    # ---
    for x, lists in test_table.items():
        print(f"python3 core8/pwb.py make2/others/testmain2 test te:{x} #{len(lists)}")
    # ---
    newlist = []
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        # ---
        if arg == "te":
            if value in test_table:
                Test_Again = False
                newlist = test_table[value]
    # ---
    Same = 0
    Diff = 0
    if Test_Again:
        for kk, lal in test_table.items():
            for cat in lal:
                if cat not in newlist:
                    newlist.append(cat)
    # ---
    Fap = event(newlist, noprint=True, printfirst=True)
    for cate in Fap:
        cate2 = cate.lower()
        new_lab = Fap.get(cate, "")
        old_lab = OIUHNM.get(cate2, "")
        # ---
        if cate2 in OIUHNM:
            if new_lab == old_lab or old_lab == "":
                Same += 1
                # printe.output('["%s"] = "%s"' % (cate , new_lab)  )
            else:
                Diff += 1
                printe.output(f'Diff : Fap["{cate}"] = "{new_lab}",')
                printe.output(f'<<lightblue>>  must be like "{old_lab}" ')
        else:
            printe.output(f'Fap["{cate}"] = "{new_lab}",')
    # ---
    printe.output(f"<<lightblue>> find {int(Same)} same label from {len(newlist)} cat, find {int(Diff)} diffrent.")

    # ---


if __name__ == "__main__":
    maintest()
    print_memory()
# ---
