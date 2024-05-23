#!/usr/bin/python3
"""
!
"""

import re
import sys

from . import printe

from .helps import len_print
from ma_lists.ministers import ministrs_tab_for_pop_format
from ma_lists.male_keys import New_Company
from .helps.print_bot import output_main
# ---
Tit_ose_Nmaes = {
    "for-the-deaf": "للصم",
    "for-the-deafblind": "للصم وللمكفوفون",
    "for-the-blind": "للمكفوفون",
    "manufactured-by": "صنعتها",
    "manufactured by": "صنعتها",
    "manufactured in": "صنعت في",
    "manufactured-in": "صنعت في",
    "published by": "نشرتها",
    "published in": "نشرت في",
    "built-in": "بنيت في",
    "built in": "بنيت في",
    "built by": "بنتها",
    "built-by": "بنتها",
    "caused by": "بسبب",
    "who defected to": "انشقوا إلى",
    "regarding": "عن",
    "spies for": "لصالح",
    "concerning": "بشأن",
    "shot dead-by-law enforcement officers in": "قتلوا برصاص ضباط إنفاذ القانون في",
    "with physical disabilities": "بإعاقات جسدية",
    "qualification for": "تصفيات مؤهلة إلى",
    "with screenplays by": "كتب نصها السينمائي",
    "with disabilities": "بإعاقات",
    "concluded in": "أبرمت في",
    "used in": "تستخدم في",
    "entered into force in": "دخلت حيز التنفيذ في",
    "invented in": "اخترعت في",
    # "introduced in": "استحدثت في",
    "introduced in": "عرضت في",
    "that uses": "تستخدم",
    "using": "تستخدم",
    "created in": "أنشئت في",
    "written by": "كتبها",
    "opened in": "افتتحت في",
    "originating in": "نشأت في",
    "convicted of spying for": "أدينوا بالتجسس لصالح",
    "of works by": "أعمال بواسطة",
    "named after": "سميت بأسماء",
    "that closed in": "أغلقت في",
    "conducted by": "نفذت بواسطة",
    "acquired by": "حصل عليها",
    "during": "خلال",
    "written": "كتبت",
    "closed in": "أغلقت في",
    "demolished in": "هدمت في",
    "in-sport-in": "في الرياضة في",
    "in-sports-in": "في الرياضة في",
    "convicted-of-murder-by": "أدينوا بالقتل في",
    "convicted of espionage in": "أدينوا بالتجسس في",
    "convicted-of-murdering": "أدينوا بقتل",
    "convicted of": "أدينوا ب",
    "by language of": "حسب لغة",
    "by-firearm-in": "بإطلاق النار في",
    "by-car-bomb": "بسيارة مفخخة",
    "who died in": "توفوا في",
    "killed while": "قتلوا أثناء",
    "related to": "متعلقة ب",
    "designated for": "خصصت ل",
    "suspended due to": "معلقة بسبب",
    "curtailed and voided due to": "اختصرت وألغيت بسبب",
    "curtailed due to": "اختصرت بسبب",
    "voided due to": "ألغيت بسبب",
    "cancelled due to": "ألغيت بسبب",
    "postponed due to": "تأجلت بسبب",
    "killed in": "قتلوا في",
    "murdered in": "قتلوا في",
    "sentenced to": "حكم عليهم",
    # "sentenced-to-death" : "حكم عليهم بالإعدام",
    "executed-burning by": "أعدموا شنقاً من قبل",
    "executed-hanging by": "أعدموا حرقاً من قبل",
    "executed-decapitation by": "أعدموا بقطع الرأس من قبل",
    "executed-firearm by": "أعدموا بسلاح ناري من قبل",
    "who served in": "خدموا في",
    "collaborators with": "متعاونون مع",
    "convicted by": "أدينوا من قبل",
    "charged with": "أتهموا بتهمة",
    "executed for treason against": "أعدموا بتهمة الخيانة العظمى ضد",
    "executed for": "أعدموا بتهمة",
    # "executed by" : "أعدمتهم",
    "executed by": "أعدموا من قبل",
    "deported": "تم ترحيلهم",
    "executed": "أعدموا",
    "disestablished in": "انحلت في",
    # "established in" : "أنشئت في",
    "reestablished in": "أعيد تأسيسها في",
    "involved in": "مرتبطة مع",
    "established in": "أسست في",
    "associated with": "مرتبطة مع",  # مرتبطين مع
    "presented by": "قدمها",
    "directed by": "أخرجها",
    "named by": "سماها",
    "scored by": "سجلها",
    # "hosted by" : "تستضيفها",
    "hosted by": "استضافتها",
    "discontinued in": "توقفت في",
    "developed in": "مطورة في",
    "described in": "وصفت في",
    "discovered in": "اكتشفت في",
    "completed in": "اكتملت في",
    "scheduled for": "مقررة في",
    "headquartered in": "مقرها الرئيسي في",
    "based in": "مقرها في",
    # "remade in" : "أعيد إنتاجها في",
    "remadein": "أعيد إنتاجها في",
    # "based on" : "مبنية على",
    "basedon": "مبنية على",
    "set in": "تقع أحداثها في",
    "set on": "تقع أحداثها على",
    "filmed in": "صورت في",
    "shot in": "مصورة في",
    "adapted into": "تم تحويلها إلى",  #
    "adapted for": "تم تحويلها إلى",  #
    "recorded in": "سُجلت في",
    "recorded at": "سُجلت في",
    "produced in": "أنتجت في",
    "produced by": "من إنتاج",
    "who compete in": "يتنافسون في",
    "extended to": "امتدت إلى",
    "involving the": "تشمل",
    "involving": "تشمل",
    "between": "بين",
    "into": "إلى",
    "to": "إلى",
    "by": "حسب",
    "in": "في",
    "elections in": "انتخابات في",
    "from": "من",
    "of": "",
    "for": "في",
    "at": "",
    # "on" : "على",
    "on": "في",
    "about": "عن",
    "outside": "خارج",
    "under": "تحت",
    "against": "ضد",
    "and": "و",
}
# ---
# تم تحويلها إلى
# اقتبست في
# حولت إلى
tito_list_s = ["in", "from", "at", "by", "of"]
# ---
for_table = {
    "for national teams": "للمنتخبات الوطنية",
    "for member-of-parliament": "لعضوية البرلمان",
}
# ---
# ---
Dont_Add_min = [
    "women of",
    "founders of",
]
# ---
ar_lab_before_year_to_add_in = [
    # لإضافة "في" بين البداية والسنة في تصنيفات مثل :
    # tab[Category:1900 rugby union tournaments for national teams] = "تصنيف:بطولات اتحاد رغبي للمنتخبات الوطنية 1900"
    "كتاب بأسماء مستعارة",
    "بطولات اتحاد رغبي للمنتخبات الوطنية",
]
# ---
contry_before_year = [
    "men's road cycling",
    "women's road cycling",
    "track cycling",
    "motorsport",
    "pseudonymous writers",
    "space",
    "disasters",
    "spaceflight",
    "inventions",
    "sports",
    "introductions",
    "discoveries",
    "comics",
    "nuclear history",
    "military history",
    "military alliances",
]
# ---
# ---Tour de
Change_key2 = {
    " for the deafblind$": " for-the-deafblind",
    "charter airlines": "charter-airlines",
    " for the blind$": " for-the-blind",
    " for the deaf$": " for-the-deaf",
    " for the blind ": " for-the-blind ",
    " for the deaf ": " for-the-deaf ",
    "term of the Iranian Majlis": "Iranian Majlis",
    "orgadnisation for the prohibition of chemical weapons": "opcw",
    "country of residence": "country-of-residence",
    "serbia and montenegro": "serbia-and-montenegro",
    "qualification for the": "qualification for",
    " at the 2": " in 2",
    " in the 2": " in 2",
    "^tour de ": "tour of ",
    " of the ": " of ",
    "green party of quebec": "green party-of-quebec",
    "libertarian party of canada": "libertarian party-of-canada",
    "declarations of independence": "declarations-of-independence",
    "united states declaration of independence": "united-states-declaration-of-independence",
    "house of commons": "house-of-commons",
    "house of representatives": "house-of-representatives",
    " at the 1": " in 1",
    " in the 1": " in 1",
    " executed people$": " executed-people",
    r" \- men's tournament": " mens tournament",
    r" \- women's tournament": " womens tournament",
    " - men's tournament": " mens tournament",
    " - women's tournament": " womens tournament",
    "historians of philosophy": "historians-of-philosophy",
    " at ": " in ",
    " women's footballers$": " female footballers",
    "^women's footballers ": "female footballers ",
    "^women's footballers": "female footballers",
    " remade in ": " remadein ",
    " based on ": " basedon ",
    r"^men\’s events ": "mensvents",
}
# ---
# category = re.sub(r" {}".format(chk) , " {}".format(chk_lab) , category )
# category = re.sub(r"{} ".format(chk) , "{} ".format(chk_lab) , category )
# ---
Change_key = {
    # "people of the ottoman empire" :"people-of-the-ottoman-empire",
    # "sentenced to death" :"sentenced-to-death",
    "health care": "healthcare",
    "child soldiers": "child-soldiers",
    "labour and social security": "labour-and-social security",
    "accidents and incidents": "accidents-and-incidents",
    "for member of parliament": "for member-of-parliament",
    "in northern ireland": "in northern-ireland",
    "manufactured in": "manufactured-in",
    "united states department of the ": "united states department of ",
    "manufactured by": "manufactured-by",
    "built in": "built-in",
    "built by": "built-by",
    "caribbean people": "caribbeans people",
    r"publishers \(people\)": "publisherspeople",
    "publishers (people)": "publisherspeople",
    r"football \(soccer\)": "football",
    r"us open \(tennis\)": "us open tennis",
    r"\(tennis\)": "tennis",
    "lgbt-related": "lgbtrelated",
    "world war ii": "world-war-ii",
    "world war i": "world-war-i",
    "killed in action": "killed-in-action",
    "missing in action": "missing-in-action",
    "city of liverpool f.c.": "city-of-liverpool f.c.",
    "medallists": "medalists",
    "saudi arabian": "saudiarabian",
    "players in": "playerss in",
    r"athletes \(track and field\)": "track and field athletes",
    "athletes (track and field)": "track and field athletes",
    "world championships in athletics": "world championships-in-athletics",
    r" \– men's tournament": " mens tournament",
    r" \– women's tournament": " womens tournament",
    r" \- men's tournament": " mens tournament",
    "murderers of children": "murderersofchildren",
    "prisoners of conscience": "prisoners-of-conscience",
    "convicted of murder by ": "convicted-of-murder-by ",
    "convicted-of-murder by ": "convicted-of-murder-by ",
    "the university of reading": "the-university-of-reading",
    "the university of science and technology": "the university-of-science and technology",
    "governance of policing": "governance policing",
    # "university of " :"university-of ",
    "university of technology": "university-of-technology",
    "refusing to convert to christianity": "refusing-to-convert-to-christianity",
    "refusing to convert to islam": "refusing-to-convert-to-islam",
    # "austria-hungary" :"austriahungary",
    "convicted of murder": "convicted-of-murder",
    # "university of" :"university-of",
    "presidential elections": "presidential-elections",
    "presidential primaries": "presidential-primaries",
    "general elections": "general-elections",
    "local elections": "local-elections",
    "early modern": "early-modern",
    "sports culture": "sprts culture",
    "by firearm in": "by-firearm-in",
    "military equipment": "military-equipment",
    "military terminology": "military-terminology",
    "shot dead by law enforcement officers": "shot dead-by-law enforcement officers",
    "west coast of the united states": "west coast fo the united states",
    "future elections": "future-elections",
    "sports media": "spports-media",
    "by car bomb": "by-car-bomb",
    "television series endings": "television series-endings",
    "television series debuts": "television series-debuts",
    "television miniseries endings": "television miniseries-endings",
    "television miniseries debuts": "television miniseries-debuts",
    "television films endings": "television films-endings",
    "television films debuts": "television films-debuts",
    # "men\’s" : "men's",
    r"\’": "'",
    # "men" : "men's",
    # "women" : "women's",
    "basedon non-": "basedon non ",
    "television seasons": "television-seasons",
    "ministers for": "ministers-for",
    "sport ministers": "sport-ministers",
    "sports ministers": "sports-ministers",
    "british hong kong": "british-hong-kong",
    "scholars of islam": "scholars-of-islam",
    # "sports events" : "sports-events",
    "united states house of representatives": "united states house-of-representatives",
    "sports events": "sorts-events",
    "the war of ": "the war-of ",
    # "paintings by" : "paintings-by",
    "sportspeople": "sprtspeople",
    "at the": "in the",
    "architecture schools": "architecture-schools",
    " labor ": " labour ",
    "elections, ": "elections ",
    "harrow on the hill": "harrow-on-the-hill",
    "city of london": "city-of-london",
    "^labor ": "labour ",
    " labor$": " labour",
    "executions by": "executions in",
    "african american": "africanamerican",
    "african-american": "africanamerican",
    "in sports in": "in-sports-in",
    # "ancient romans" :"ancient-romans",
    "ancient roman": "ancient-roman",
    "ancient greek": "ancient-greek",
    "ancient macedonian": "ancient-macedonian",
    "in sport in": "in-sport-in",
    "kingdom of": "kingdom-of",
    "the national register of historic places": "the-national-register-of-historic-places",
    "national register of historic places": "national-register-of-historic-places",
    # "executed by guillotine" : "executed-guillotine",
    "executed by burning": "executed-burning",
    "executed by hanging": "executed-hanging",
    "executed by decapitation": "executed-decapitation",
    "executed by firearm": "executed-firearm",
    # " executed by " :" executed-by ",
    "emirate of": "emirate-of",
    "republic of": "republic-of",
    "duchy of": "duchy-of",
    "states of": "states-of",
    "comedy-": "comedy ",
    "domain of": "domain-of",
    "crown of": "crown-of",
    "county of": "county-of",
    "protectorate of": "protectorate-of",
    "canton of": "canton-of",
    "march of": "march-of",
    "margraviate of": "margraviate-of",
    "colony of": "colony-of",
    # "province of" :"province-of",
    "realm of": "realm-of",
    "isle of": "isle-of",
    "viceroyalty of": "viceroyalty-of",
}
# ---
for x in New_Company:
    Change_key[f"defunct {x} companies"] = f"defunct-{x}-companies"
# ---
NewFormat = {
    "### in american motorsport": "رياضة محركات في الولايات المتحدة في ###",
    "###_in_American_motorsport": "رياضة محركات في الولايات المتحدة في ###",
}
# ---
Tabl_with_in = {
    "sport in": "الرياضة في",
    # "conversion to" : "التحول إلى",
}
# --- Tour de
pp_start_with = {
    "wikipedia categories named after": "تصنيفات سميت بأسماء {}",
    "candidates for president of": "مرشحو رئاسة {}",
    # "candidates in president of" : "مرشحو رئاسة {}",
    "candidates-for": "مرشحو {}",
    # "candidates for" : "مرشحو {}",
    "categories named afters": "تصنيفات سميت بأسماء {}",
    "scheduled": "{} مقررة",
    # "defunct" : "{} سابقة",
}
# ---
pp_start_with2 = {
    "defunct": "{} سابقة",
    "scheduled": "{} مقررة",
}
# ---
pp_ends_with = {}
pp_ends_with_pase = {
    "-related professional associations": "جمعيات تخصصية متعلقة ب{}",
    "-related media": "إعلام متعلق ب{}",
    "-related lists": "قوائم متعلقة ب{}",
    "with disabilities": "{} بإعاقات",
    " mens tournament": "{} - مسابقة الرجال",
    " - telugu": "{} - تيلوغوي",
    # ---
    "first division": "{} الدرجة الأولى",
    "second division": "{} الدرجة الثانية",
    "third division": "{} الدرجة الثالثة",
    "forth division": "{} الدرجة الرابعة",
    # ---
    "candidates": "مرشحو {}",
    "candidates for": "مرشحو {} في",
    # ---
    "squads": "تشكيلات {}",
    "final tournaments": "نهائيات مسابقات {}",
    "finals": "نهائيات {}",
    # ---
    " - kannada": "{} - كنادي",
    " - tamil": "{} - تاميلي",
    " - qualifying": "{} - التصفيات",  # – Mixed Doubles
    " - mixed doubles": "{} - زوجي مختلط",  # – Mixed Doubles
    " - men's tournament": "{} - مسابقة الرجال",
    " - women's tournament": "{} - مسابقة السيدات",
    " - men's qualification": "{} - تصفيات الرجال",
    " - women's qualification": "{} - تصفيات السيدات",
    # ---
    " – kannada": "{} – كنادي",
    " – tamil": "{} – تاميلي",
    " – qualifying": "{} – التصفيات",  # – Mixed Doubles
    " – mixed doubles": "{} – زوجي مختلط",  # – Mixed Doubles
    " – men's tournament": "{} – مسابقة الرجال",
    " – women's tournament": "{} – مسابقة السيدات",
    " womens tournament": "{} – مسابقة السيدات",
    " – men's qualification": "{} – تصفيات الرجال",
    " – women's qualification": "{} – تصفيات السيدات",
}
# ---
# "mixed doubles" : " زوجي مختلط",
# "mixed team" : " فريق مختلط",
#  "womens team" : " فريق سيدات",
#  "mens team" : " فريق رجال",
#   "womens tournament" : " منافسة السيدات",
#   "mens tournament" : " منافسة الرجال",
# ---
key_5_suff = {
    "tournament": "مسابقة",
    "singles": "فردي",
    "qualification": "تصفيات",
    "team": "فريق",
    "doubles": "زوجي",
}
# ---
key_2_3 = {
    "girls": "فتيات",
    "mixed": "مختلط",
    "boys": "فتيان",
    "singles": "فردي",
    "womens": "سيدات",
    "ladies": "سيدات",
    "mens": "رجال",
    "men's": "رجال",
    # ---
}
fof = "{}"
# ---
for start, start_lab in key_2_3.items():
    for suff, suff_lab in key_5_suff.items():
        ke = f" - {start} {suff}"
        lab_ke = f"{fof} - {suff_lab} {start_lab}"
        pp_ends_with[ke] = lab_ke
# ---
fix_o = {
    "squad navigational boxes": "صناديق تصفح تشكيلات",
    "navigational boxes": "صناديق تصفح",
    "bids": "ترشيحات",
    "episodes": "حلقات",
    "treaties": "معاهدات",
    "seasons": "مواسم",
    "local elections": "انتخابات محلية",
    "presidential elections": "انتخابات رئاسية",
    "presidential primaries": "انتخابات رئاسية تمهيدية",
    "elections": "انتخابات",
    "champions": "أبطال",
    "organizations": "منظمات",
    "nonprofits": "منظمات غير ربحية",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "applications": "تطبيقات",
    "employees": "موظفو",
    "resolutions": "قرارات",
    # "ministries" : "وزارات",
    "campaigns": "حملات",
    "referees": "حكام",
    # "films" : "أفلام",
    "squad templates": "قوالب تشكيلات",
    "templates": "قوالب",
    "venues": "ملاعب",
    "stadiums": "استادات",
    "trainers": "مدربو",
    "scouts": "كشافة",
    "coaches": "مدربو",
    "teams": "فرق",
    "owners": "ملاك",
    "owners and executives": "رؤساء تنفيذيون وملاك {}",
    "uniforms": "بدلات",
    "announcers": "مذيعو",
    "playoffs": "تصفيات",
    "genres": "أنواع",
    "leaks": "تسريبات",
    "categories": "تصانيف",
    "qualification": "تصفيات",
    "counties": "مقاطعات",
    "occupations": "مهن",
    "equipment": "معدات",
    "trophies and awards": "جوائز وإنجازات",
    "logos": "شعارات",
    "tactics and skills": "مهارات",
    "terminology": "مصطلحات",
    "variants": "أشكال",
}
for i, i_lab in fix_o.items():
    pp_ends_with[f" {i}"] = i_lab + " {}"
# ---
pop_format33 = {
    "qualification for the": "تصفيات {} مؤهلة إلى {} ",
    "qualification for": "تصفيات {} مؤهلة إلى {} ",
}
# ---
pop_format = {
    "prehistory of": "{} ما قبل التاريخ",
    "naval units and formations of": "وحدات وتشكيلات {} البحرية",
    "military units and formations of": "وحدات وتشكيلات {} العسكرية",
    "the university of": "جامعة {}",
    "university of arts": "جامعة {} للفنون",
    "university of the arts": "جامعة {} للفنون",
    "the university of the arts": "جامعة {} للفنون",
    "university of": "جامعة {}",
    # "university of technology" : "جامعة {} للتكنولوجيا" ,
    "university of art": "جامعة {} للفنون",
    "military installations of": "منشآت {} العسكرية",
    "politics of": "سياسة {}",
    "acting presidents of": "رؤساء {} بالإنابة",
    "diplomatic missions of": "بعثات {} الدبلوماسية",
    "umayyad governors of": "ولاة {} الأمويون",
    "sports-events": "أحداث {} الرياضة",
    "fictional presidents of": "رؤساء {} الخياليون",
    "political history of": "تاريخ {} السياسي",
    "early-modern history of": "تاريخ {} الحديث المبكر",
    "early modern history of": "تاريخ {} الحديث المبكر",
    "modern history of": "تاريخ {} الحديث",
    "contemporary history of": "تاريخ {} المعاصر",
    "economic history of": "تاريخ {} الاقتصادي",
    "cultural history of": "تاريخ {} الثقافي",
    "geographic history of": "تاريخ {} الجغرافي",
    "military history of": "تاريخ {} العسكري",
    "ancient history of": "تاريخ {} القديم",
    "legal history of": "تاريخ {} القانوني",
    "islamic history of": "تاريخ {} الإسلامي",
    "demographic history of": "تاريخ {} الديموغرافي",
    "naval history of": "تاريخ {} العسكري البحري",
    "maritime history of": "تاريخ {} البحري",
    "natural history of": "تاريخ {} الطبيعي",
    "bilateral relations of": "علاقات {} الثنائية",
    "bilateral military relations of": "علاقات {} الثنائية العسكرية",
    "social history of": "تاريخ {} الاجتماعي",
    "foreign relations of": "علاقات {} الخارجية",
    "sports in": "الرياضة في {}",
    "national symbols of": "رموز {} الوطنية",
    "political history": "تاريخ {} السياسي",
    "nuclear history": "تاريخ {} النووي",
    "military history": "تاريخ {} العسكري",
    "natural history": "تاريخ {} الطبيعي",
    "social history": "تاريخ {} الاجتماعي",
    "military-equipment of": "عتاد {} العسكري",
    "permanent delegates of": "مندوبو {} الدائمون",
    "permanent representatives of": "مندوبو {} الدائمون",
    "military equipment of": "عتاد {} العسكري",
    "foreign relations": "علاقات {} الخارجية",
    "grand prix": "جائزة {} الكبرى",
    "motorcycle grand prix": "جائزة {} الكبرى للدراجات النارية",
    # "law" : "قانون {}" ,
}
# ---
for a, b in ministrs_tab_for_pop_format.items():
    pop_format[a] = b
# ---
pop_format2 = {
    "politics of {}": "سياسة {}",
    "military installations of": "منشآت {} العسكرية",
}
# ---produced


def change_cat(Cate):
    Cate = Cate.lower().strip()
    # Category:Basketball at the 2007 All-Africa Games – Women's tournament
    # output_main('change_cat :"%s" ' % Cate )
    category = Cate

    category = re.sub(r"[\s\t]+", " ", category, flags=re.IGNORECASE)

    # ---
    category = re.sub(r"(\w+) expatriate (\w+) people in ", r"\g<1> expatriate \g<2> peoplee in ", category, flags=re.IGNORECASE)
    # category = re.sub(r" deaf people" , " deaf-peopl" , category, flags = re.IGNORECASE)
    category = re.sub(r"organisations", "organizations", category, flags=re.IGNORECASE)
    # ---
    category = re.sub(r"rus'", "rus", category, flags=re.IGNORECASE)
    category = re.sub(r"the kingdom of", " kingdom of", category, flags=re.IGNORECASE)
    category = re.sub(r"-century", " century", category, flags=re.IGNORECASE)
    category = re.sub(r"association football", "football", category, flags=re.IGNORECASE)
    category = re.sub(r"austria-hungary", "austria hungary", category, flags=re.IGNORECASE)
    category = re.sub(r"austria hungary", "austria hungary", category, flags=re.IGNORECASE)
    category = re.sub(r"-millennium", " millennium", category, flags=re.IGNORECASE)
    # ---
    category = re.sub(
        r"unmanned military aircraft of",
        "unmanned military aircraft-oof",
        category,
        flags=re.IGNORECASE,
    )
    category = re.sub(
        r"unmanned aerial vehicles of",
        "unmanned aerial vehicles-oof",
        category,
        flags=re.IGNORECASE,
    )
    # ---
    category = re.sub(
        r"democratic republic of the congo",
        "democratic-republic-of-the-congo",
        category,
        flags=re.IGNORECASE,
    )
    category = re.sub(r"republic of the congo", "republic-of-the-congo", category, flags=re.IGNORECASE)
    category = re.sub(
        r"athletics \(track and field\)",
        "track-and-field athletics",
        category,
        flags=re.IGNORECASE,
    )
    category = re.sub(r"twin people", "twinpeople", category, flags=re.IGNORECASE)
    # ---
    # category = re.sub(r"\–" , "-" , category, flags = re.IGNORECASE)
    # category = re.sub(r"–" , "-" , category, flags = re.IGNORECASE)
    # category = category.replace("–" , "-")
    # ---
    # category = category.replace("^signers of " , "signers on ")
    # ---
    category = category.replace("secretaries of ", "secretaries-of ")
    # ---
    category = category.replace("roller hockey (quad)", "roller hockey")
    category = category.replace("victoria (australia)", "victoria-australia")
    category = re.sub(r"\%27", "'", category, flags=re.IGNORECASE)

    # category = re.sub(r"assassinated (.*) people" , r"\g<1> assassinated people" , category, flags = re.IGNORECASE)
    # category = re.sub(r"'" , " " , category, flags = re.IGNORECASE)
    # ---
    category = category.replace("national women's youth", "national youth women's")
    category = category.replace("national youth women's", "national youth women's")
    category = category.replace("women's youth national", "national youth women's")
    category = category.replace("women's national youth", "national youth women's")
    category = category.replace("youth national women's", "national youth women's")
    category = category.replace("youth women's national", "national youth women's")
    # ---
    category = category.replace("national women's junior", "national junior women's")
    category = category.replace("national junior women's", "national junior women's")
    category = category.replace("women's junior national", "national junior women's")
    category = category.replace("women's national junior", "national junior women's")
    category = category.replace("junior women's national", "national junior women's")
    category = category.replace("junior women's national", "national junior women's")
    # ---
    category = category.replace("national men's junior", "national junior men's")
    category = category.replace("national junior men's", "national junior men's")
    category = category.replace("men's junior national", "national junior men's")
    category = category.replace("men's national junior", "national junior men's")
    category = category.replace("junior men's national", "national junior men's")
    category = category.replace("junior men's national", "national junior men's")
    # ---
    category = category.replace(" men's national", " national men's")
    category = category.replace("women's national", "national women's")
    # ---
    category = category.replace("junior national", "national junior")
    category = category.replace("youth national", "national youth")
    category = category.replace("amateur national", "national amateur")
    category = category.replace("heads of mission ", "heads-of-mission ")
    category = category.replace("house of commons of canada", "house-of-commons-of-canada")
    # ---
    # ---
    for chk2, chk2_lab in Change_key2.items():
        category = re.sub(chk2, chk2_lab, category, flags=re.IGNORECASE)
    # ---
    for chk, chk_lab in Change_key.items():
        # chk2 = chk.replace("
        category = re.sub(rf"^category\:{chk} ", f"category:{chk_lab} ", category, flags=re.IGNORECASE)
        category = re.sub(rf"^{chk} ", f"{chk_lab} ", category, flags=re.IGNORECASE)
        category = re.sub(rf" {chk} ", f" {chk_lab} ", category, flags=re.IGNORECASE)
        # category = re.sub(r" {}".format(chk) , " {}".format(chk_lab) , category , flags = re.IGNORECASE)
        category = re.sub(rf" {chk}$", f" {chk_lab}", category, flags=re.IGNORECASE)
        category = re.sub(rf"category\:{chk} ", f"category:{chk_lab} ", category, flags=re.IGNORECASE)
    # ---
    category = re.sub(r"category\:ministers of ", "category:ministers-of ", category, flags=re.IGNORECASE)
    # ---
    category = category.replace("party of ", "party-of ")
    # ---
    if category != Cate:
        output_main(f'change_cat to :"{category}", orginal: {Cate}.')
        # print(dodd)
    # ---
    return category


# ---
Lenth1 = {"Change_key": sys.getsizeof(Change_key), "Change_key2": sys.getsizeof(Change_key2)}
# ---

len_print.lenth_pri("pop_format.py", Lenth1)


def main():
    # ---
    """
    if sys.argv and sys.argv[1]:
        La = sys.argv[1].lower()
        La = re.sub(r"_", " " , La)
        cat = change_cat(La)
        print( "La: " + La)
        print( "cat: " + cat)"""


# ---
if __name__ == "__main__":
    main()
# ---
