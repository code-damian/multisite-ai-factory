
from pathlib import Path
import html

OUT = Path(r"C:\Users\damia\Documents\Codex\multisite-ai-factory\assets\portfolio")
OUT.mkdir(parents=True, exist_ok=True)

def esc(s): return html.escape(str(s), quote=True)

def svg(title, subtitle, body, bg="#0b1020"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 900" role="img" aria-label="{esc(title)}">
<defs>
 <linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#172554"/><stop offset=".55" stop-color="#0f766e"/><stop offset="1" stop-color="#111827"/></linearGradient>
 <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#f8d38b"/><stop offset="1" stop-color="#d99b4a"/></linearGradient>
 <filter id="shadow"><feDropShadow dx="0" dy="18" stdDeviation="22" flood-opacity=".22"/></filter>
</defs>
<rect width="1440" height="900" fill="{bg}"/>
{body}
<text x="80" y="850" font-family="Arial, sans-serif" font-size="14" fill="#8fa0bd">{esc(subtitle)}</text>
</svg>'''

def text(x,y,t,size=24,fill="#fff",weight=400,anchor="start"):
    return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{esc(t)}</text>'

def rect(x,y,w,h,fill,rx=22,stroke="none",sw=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def save(name, title, subtitle, body, bg="#0b1020"):
    (OUT/name).write_text(svg(title, subtitle, body, bg), encoding="utf-8")

# SALON — editorial / luxury / asymmetry
save("salon-home.svg","Salon Bella — strona główna","Salon Bella · Poznań · Rezerwacja online",
 rect(70,55,1300,790,"#f7efe8",34)+
 text(105,110,"BELLA",22,"#6e4b42",800)+text(104,138,"SALON PIĘKNA",11,"#9b786c",700)+
 text(1330,115,"USŁUGI   GALERIA   O NAS   KONTAKT",13,"#6e4b42",700,"end")+
 rect(95,205,770,500,"url(#g)",30)+
 text(145,300,"PIĘKNO",86,"#fff",800)+text(145,382,"które zostaje z Tobą.",58,"#f8d38b",800)+
 text(145,440,"Autorskie kolory • pielęgnacja • stylizacja",22,"#edf2f7",400)+
 rect(145,505,205,55,"#fff",14)+text(248,540,"UMÓW WIZYTĘ",14,"#1b2434",800,"middle")+
 rect(900,205,400,230,"#e7d4ca",28)+
 text(950,260,"NOWOŚĆ",12,"#7b5145",800)+text(950,305,"Jesienna metamorfoza",30,"#3a2924",800)+
 text(950,345,"Kolor + pielęgnacja",18,"#6e5148",400)+
 rect(900,465,400,240,"#201827",28)+
 text(945,520,"01",14,"#f8d38b",800)+text(945,565,"Indywidualna",28,"#fff",800)+text(945,600,"konsultacja przed usługą",18,"#cbd5e1",400)+
 text(945,665,"BEZPŁATNIE · 15 MIN",13,"#f8d38b",800),
 "#efe4dc")

save("salon-services.svg","Salon Bella — usługi","Oferta · ceny · pakiety · szybka rezerwacja",
 rect(60,55,1320,790,"#fbf7f4",30)+
 text(100,115,"USŁUGI I CENNIK",42,"#3d2924",800)+text(100,155,"Wybierz usługę. Resztą zajmiemy się na miejscu.",18,"#80685f")+
 rect(100,205,390,535,"#2b2023",24)+text(135,255,"PAKIET",13,"#f4c982",800)+text(135,305,"Bella Signature",38,"#fff",800)+
 text(135,350,"Pełna metamorfoza",18,"#d6c6c8")+text(135,405,"• konsultacja",17,"#fff")+text(135,440,"• koloryzacja",17,"#fff")+text(135,475,"• pielęgnacja",17,"#fff")+text(135,510,"• stylizacja",17,"#fff")+
 text(135,620,"od 420 zł",30,"#f4c982",800)+rect(135,660,190,48,"#f4c982",12)+text(230,691,"REZERWUJ",13,"#2b2023",800,"middle")+
 rect(535,205,380,245,"#efe0d8",22)+text(570,255,"Koloryzacja",25,"#3d2924",800)+text(570,295,"Kolor dopasowany do karnacji",16,"#725d55")+text(850,335,"od 220 zł",20,"#6e4b42",800,"end")+
 rect(955,205,380,245,"#e6edf2",22)+text(990,255,"Pielęgnacja",25,"#263447",800)+text(990,295,"Regeneracja i połysk włosów",16,"#65758b")+text(1290,335,"od 160 zł",20,"#263447",800,"end")+
 rect(535,480,800,260,"#fff",22,"#e7ddd7",2)+text(570,530,"Jak wygląda wizyta?",24,"#3d2924",800)+
 text(570,585,"01  Konsultacja",17,"#6e4b42",800)+text(790,585,"02  Usługa",17,"#6e4b42",800)+text(1010,585,"03  Stylizacja",17,"#6e4b42",800)+
 text(570,630,"Poznajemy potrzeby i planujemy efekt.",14,"#7c6d67")+text(790,630,"Pracujemy na sprawdzonych produktach.",14,"#7c6d67")+text(1010,630,"Wychodzisz z instrukcją pielęgnacji.",14,"#7c6d67"))

save("salon-gallery.svg","Salon Bella — galeria","Galeria efektów · filtrowanie: kolory / cięcia / stylizacje",
 rect(55,50,1330,800,"#f6f0ec",28)+text(95,110,"EFEKTY, KTÓRE MÓWIĄ SAME ZA SIEBIE",36,"#382a27",800)+
 text(95,150,"Przesuń wzrok po realizacjach i zobacz różne style.",17,"#7d6a63")+
 rect(95,205,300,270,"#d8b9ad",20)+text(120,250,"BLOND",14,"#5d4037",800)+text(120,430,"Naturalne rozświetlenie",22,"#fff",800)+
 rect(420,205,420,430,"#28354a",20)+text(450,250,"BRĄZ",14,"#f4d4a1",800)+text(450,410,"Głęboki kolor",30,"#fff",800)+text(450,450,"z miękkim przejściem",18,"#d6dfeb")+
 rect(865,205,440,195,"#cfa98f",20)+text(900,255,"CIĘCIE",14,"#fff",800)+text(900,335,"Lekka forma, mocny efekt",24,"#fff",800)+
 rect(865,425,210,210,"#dfe7e8",20)+text(900,480,"PAKIET",14,"#42545b",800)+text(900,550,"Ślubny",25,"#27363b",800)+
 rect(1095,425,210,210,"#ead7c5",20)+text(1130,480,"EVENT",14,"#6e4b42",800)+text(1130,550,"Wieczór",25,"#3d2924",800)+
 rect(95,505,300,130,"#201827",20)+text(120,550,"Zarezerwuj konsultację",20,"#fff",800)+text(120,585,"15 minut · bez opłat",14,"#f4c982"))

save("salon-contact.svg","Salon Bella — rezerwacja","Rezerwacja · wybór usługi · termin · dane klienta",
 rect(60,55,1320,790,"#faf6f2",30)+
 text(100,115,"UMÓW WIZYTĘ",44,"#382a27",800)+text(100,155,"Wybierz usługę i dogodny termin.",18,"#7d6a63")+
 rect(100,215,470,520,"#211a20",26)+text(140,270,"01",13,"#f3c77c",800)+text(140,315,"Wybierz usługę",27,"#fff",800)+
 rect(140,350,390,55,"#342932",12)+text(165,385,"Koloryzacja",16,"#fff")+text(500,385,"220 zł",14,"#f3c77c",800,"end")+
 rect(140,420,390,55,"#342932",12)+text(165,455,"Pielęgnacja",16,"#fff")+text(500,455,"160 zł",14,"#f3c77c",800,"end")+
 rect(140,490,390,55,"#f3c77c",12)+text(165,525,"Bella Signature",16,"#211a20",800)+text(500,525,"420 zł",14,"#211a20",800,"end")+
 rect(650,215,650,520,"#fff",26,"#e7ddd7",2)+text(690,270,"02",13,"#8a665c",800)+text(690,315,"Najbliższe terminy",27,"#382a27",800)+
 text(690,365,"Wt. 14.10",15,"#806b64",800)+text(900,365,"10:30   12:00   16:30",15,"#382a27",700)+
 text(690,425,"Śr. 15.10",15,"#806b64",800)+text(900,425,"09:00   13:30   17:00",15,"#382a27",700)+
 text(690,485,"Czw. 16.10",15,"#806b64",800)+text(900,485,"11:00   14:00",15,"#382a27",700)+
 rect(690,555,440,105,"#f4ebe5",18)+text(715,595,"03  Twoje dane",13,"#8a665c",800)+text(715,630,"Imię, telefon, e-mail",17,"#382a27",700)+
 rect(690,680,250,45,"#382a27",10)+text(815,709,"POTWIERDŹ WIZYTĘ",12,"#fff",800,"middle"))

# AUTO — technical / dashboard / bento
save("auto-home.svg","AutoKlinika Poznań — serwis","Diagnostyka · mechanika · szybki termin · Poznań",
 rect(50,45,1340,810,"#f3f6f9",28)+
 rect(50,45,1340,90,"#101923",28)+text(90,100,"AUTOKLINIKA",24,"#ff3b4d",900)+text(270,100,"POZNAŃ",14,"#dbe4ee",800)+
 text(1325,100,"USŁUGI   CENNIK   OPINIE   KONTAKT",12,"#c4d0dc",700,"end")+
 rect(85,175,760,300,"#111c27",24)+text(125,245,"AUTO NIE CZEKA.",55,"#fff",900)+text(125,305,"MY TEŻ NIE.",55,"#ff3b4d",900)+
 text(125,355,"Diagnostyka komputerowa, mechanika i serwis klimatyzacji.",18,"#c5d1dc")+rect(125,395,190,48,"#ff3b4d",10)+text(220,426,"UMÓW SERWIS",13,"#fff",900,"middle")+
 rect(875,175,430,140,"#dce7ef",22)+text(910,220,"NAJBLIŻSZY TERMIN",12,"#536579",800)+text(910,265,"Dziś · 15:30",31,"#152331",900)+text(1270,265,"→",30,"#ff3b4d",900,"end")+
 rect(875,335,205,140,"#fff",22)+text(905,380,"4.9 / 5",28,"#152331",900)+text(905,415,"248 opinii",14,"#66778a")+
 rect(1100,335,205,140,"#172532",22)+text(1130,380,"12 lat",28,"#fff",900)+text(1130,415,"doświadczenia",14,"#9fb0bf")+
 rect(85,510,1220,245,"#fff",22,"#dce4eb",2)+text(125,555,"SERWIS W 3 KROKACH",24,"#152331",900)+
 text(125,620,"01  DIAGNOZA",15,"#ff3b4d",900)+text(455,620,"02  WYCENA",15,"#ff3b4d",900)+text(785,620,"03  NAPRAWA",15,"#ff3b4d",900)+
 text(125,660,"Sprawdzamy przyczynę.",14,"#66778a")+text(455,660,"Znasz koszt przed startem.",14,"#66778a")+text(785,660,"Odbierasz sprawne auto.",14,"#66778a"))

save("auto-about.svg","AutoKlinika Poznań — o nas","O nas · zespół · standard obsługi · gwarancja",
 rect(55,50,1330,800,"#eef3f7",28)+text(95,110,"SERWIS, KTÓRY MYŚLI RAZEM Z TOBĄ",38,"#142331",900)+
 text(95,150,"Technologia + doświadczenie + jasna komunikacja.",18,"#617184")+
 rect(95,205,410,500,"#152331",24)+text(135,260,"12",58,"#ff3b4d",900)+text(135,305,"lat na rynku",18,"#fff",700)+
 text(135,380,"248",45,"#fff",900)+text(135,420,"opinii klientów",17,"#aebdca")+text(135,495,"98%",45,"#fff",900)+text(135,535,"napraw zakończonych",17,"#aebdca")+text(135,575,"w uzgodnionym terminie",17,"#aebdca")+
 rect(555,205,750,220,"#fff",22,"#dbe4eb",2)+text(595,255,"NASZ STANDARD",15,"#ff3b4d",900)+
 text(595,310,"Najpierw diagnoza.",27,"#152331",900)+text(595,350,"Potem konkretna wycena.",27,"#152331",900)+text(595,390,"Na końcu naprawa bez niespodzianek.",27,"#152331",900)+
 rect(555,460,230,245,"#d9e4ec",22)+text(590,510,"01",14,"#ff3b4d",900)+text(590,555,"Doświadczenie",21,"#152331",900)+text(590,595,"Mechanicy znający",14,"#617184")+text(590,620,"różne marki.",14,"#617184")+
 rect(815,460,230,245,"#f7d8d8",22)+text(850,510,"02",14,"#ff3b4d",900)+text(850,555,"Diagnostyka",21,"#152331",900)+text(850,595,"Nowoczesne testery",14,"#617184")+text(850,620,"i pomiary.",14,"#617184")+
 rect(1075,460,230,245,"#152331",22)+text(1110,510,"03",14,"#ff3b4d",900)+text(1110,555,"Gwarancja",21,"#fff",900)+text(1110,595,"Dokumentujemy",14,"#aebdca")+text(1110,620,"wykonane prace.",14,"#aebdca"))

save("auto-price.svg","AutoKlinika Poznań — cennik","Cennik · wyszukiwarka usług · części · szybka wycena",
 rect(50,45,1340,810,"#f4f7fa",28)+text(90,105,"CENNIK I CZĘŚCI",40,"#152331",900)+
 rect(90,145,700,52,"#fff",12,"#d8e1e8",2)+text(120,178,"⌕  Szukaj: hamulce, olej, diagnostyka...",15,"#8a99a8")+
 rect(820,145,450,52,"#152331",12)+text(1045,178,"POKAŻ DOSTĘPNE TERMINY →",13,"#fff",900,"middle")+
 rect(90,235,380,450,"#fff",20,"#d8e1e8",2)+text(125,280,"Hamulce",24,"#152331",900)+text(125,320,"Wymiana klocków + tarcz",15,"#66778a")+text(430,360,"od 380 zł",19,"#ff3b4d",900,"end")+
 text(125,410,"Diagnostyka",24,"#152331",900)+text(125,450,"Pełny skan komputerowy",15,"#66778a")+text(430,490,"od 150 zł",19,"#ff3b4d",900,"end")+
 text(125,540,"Klimatyzacja",24,"#152331",900)+text(125,580,"Serwis + kontrola szczelności",15,"#66778a")+text(430,620,"od 220 zł",19,"#ff3b4d",900,"end")+
 rect(510,235,380,450,"#152331",20)+text(550,280,"CZĘŚCI",14,"#ff3b4d",900)+text(550,325,"Filtr oleju",23,"#fff",900)+text(550,360,"Bosch · dostępny",14,"#aebdca")+text(840,360,"49 zł",18,"#fff",800,"end")+
 text(550,425,"Klocki hamulcowe",23,"#fff",900)+text(550,460,"ATE · 2–3 dni",14,"#aebdca")+text(840,460,"249 zł",18,"#fff",800,"end")+
 text(550,525,"Olej silnikowy 5W30",23,"#fff",900)+text(550,560,"5 l · Motul",14,"#aebdca")+text(840,560,"189 zł",18,"#fff",800,"end")+
 rect(930,235,340,450,"#ff3b4d",20)+text(970,285,"NIE WIESZ, CZEGO",14,"#fff",800)+text(970,325,"POTRZEBUJESZ?",31,"#fff",900)+text(970,385,"Wyślij model auta.",18,"#ffe5e8")+text(970,420,"Dobierzemy usługę i",18,"#ffe5e8")+text(970,455,"przygotujemy wycenę.",18,"#ffe5e8")+rect(970,530,220,48,"#fff",10)+text(1080,561,"POPROŚ O WYCENĘ",12,"#152331",900,"middle"))

save("auto-contact.svg","AutoKlinika Poznań — przyjęcie auta","Rezerwacja serwisu · dane auta · termin · opis usterki",
 rect(55,50,1330,800,"#eef3f7",28)+text(95,110,"UMÓW SERWIS",42,"#152331",900)+text(95,150,"Kilka informacji i od razu wiemy, jak Ci pomóc.",18,"#66778a")+
 rect(95,205,760,510,"#fff",24,"#dbe4eb",2)+
 text(135,255,"DANE AUTA",13,"#ff3b4d",900)+rect(135,285,300,52,"#f4f7fa",10)+text(155,318,"Marka i model",14,"#8a99a8")+rect(455,285,300,52,"#f4f7fa",10)+text(475,318,"Rok produkcji",14,"#8a99a8")+
 rect(135,365,620,52,"#f4f7fa",10)+text(155,398,"Objaw / problem, który zauważyłeś",14,"#8a99a8")+
 text(135,470,"WYBIERZ TERMIN",13,"#ff3b4d",900)+
 rect(135,500,180,52,"#152331",10)+text(225,533,"Dziś 15:30",14,"#fff",800,"middle")+rect(330,500,180,52,"#f4f7fa",10)+text(420,533,"Jutro 09:00",14,"#536579",800,"middle")+rect(525,500,180,52,"#f4f7fa",10)+text(615,533,"Jutro 13:30",14,"#536579",800,"middle")+
 rect(135,590,240,50,"#ff3b4d",10)+text(255,621,"POTWIERDŹ TERMIN",12,"#fff",900,"middle")+
 rect(895,205,410,510,"#152331",24)+text(935,255,"CO DZIEJE SIĘ DALEJ?",15,"#ff3b4d",900)+
 text(935,315,"01",16,"#fff",900)+text(980,315,"Potwierdzamy termin",18,"#fff",800)+text(980,345,"SMS lub telefon.",13,"#aebdca")+
 text(935,415,"02",16,"#fff",900)+text(980,415,"Przyjmujemy auto",18,"#fff",800)+text(980,445,"Wstępna diagnoza.",13,"#aebdca")+
 text(935,515,"03",16,"#fff",900)+text(980,515,"Dostajesz wycenę",18,"#fff",800)+text(980,545,"Bez kosztów w ciemno.",13,"#aebdca")+
 rect(935,610,280,58,"#ff3b4d",12)+text(1075,646,"697 944 846",18,"#fff",900,"middle"))

# RESTAURANT — editorial / magazine / warm luxury
save("rest-home.svg","Restauracja Stary Rynek — strona główna","Stary Rynek · Poznań · kuchnia autorska · rezerwacje",
 rect(50,45,1340,810,"#f6efe4",28)+text(90,105,"STARY RYNEK",30,"#3d2a1f",900)+text(1325,105,"MENU   HISTORIA   GALERIA   REZERWACJA",12,"#765743",800,"end")+
 rect(90,165,790,540,"#2c211a",24)+text(135,245,"KUCHNIA",16,"#dcb46b",900)+text(135,315,"która opowiada",65,"#fff",900)+text(135,385,"Poznań.",65,"#dcb46b",900)+
 text(135,440,"Sezonowe składniki · lokalni dostawcy · wieczory z winem",18,"#e5d8c9")+rect(135,500,190,50,"#dcb46b",10)+text(230,532,"ZAREZERWUJ STOLIK",12,"#2c211a",900,"middle")+
 rect(915,165,390,250,"#d9b47c",22)+text(955,215,"DANIE TYGODNIA",12,"#5a3b23",900)+text(955,265,"Kaczka · śliwka ·",27,"#2c211a",900)+text(955,300,"palony seler",27,"#2c211a",900)+text(955,355,"59 zł",22,"#fff",900)+
 rect(915,445,390,260,"#fffaf2",22)+text(955,500,"DZISIAJ",12,"#967257",900)+text(955,545,"Lunch 12:00–16:00",23,"#3d2a1f",900)+text(955,590,"Kolacja 17:00–23:00",23,"#3d2a1f",900)+text(955,650,"Kuchnia zamyka zamówienia 30 min przed końcem.",13,"#806d60"))

save("rest-menu.svg","Restauracja Stary Rynek — menu","Menu · przystawki · dania główne · desery · wino",
 rect(55,50,1330,800,"#faf5ec",28)+text(95,110,"MENU SEZONOWE",42,"#3b291e",900)+
 text(95,150,"Jesień 2026 · produkty od lokalnych dostawców",17,"#806c5d")+
 rect(95,205,570,500,"#fff",22,"#e8ded0",2)+text(130,255,"NA START",13,"#b27b3d",900)+
 text(130,315,"Tatar wołowy",22,"#3b291e",900)+text(130,345,"pikle · żółtko · chleb na zakwasie",14,"#806c5d")+text(610,345,"39 zł",16,"#3b291e",800,"end")+
 text(130,410,"Pieczona dynia",22,"#3b291e",900)+text(130,440,"orzech laskowy · kozi ser",14,"#806c5d")+text(610,440,"31 zł",16,"#3b291e",800,"end")+
 text(130,505,"Zupa dnia",22,"#3b291e",900)+text(130,535,"zapytaj obsługę o dzisiejszą wersję",14,"#806c5d")+text(610,535,"24 zł",16,"#3b291e",800,"end")+
 rect(700,205,605,500,"#2e2119",22)+text(740,255,"DANIA GŁÓWNE",13,"#dcb46b",900)+
 text(740,320,"Kaczka confit",25,"#fff",900)+text(740,350,"śliwka · seler · sos z czerwonego wina",14,"#cbbcae")+text(1255,350,"59 zł",16,"#dcb46b",900,"end")+
 text(740,420,"Sandacz",25,"#fff",900)+text(740,450,"ziemniak · por · beurre blanc",14,"#cbbcae")+text(1255,450,"64 zł",16,"#dcb46b",900,"end")+
 text(740,520,"Pierogi z kaczką",25,"#fff",900)+text(740,550,"cebula · majeranek · kwaśna śmietana",14,"#cbbcae")+text(1255,550,"38 zł",16,"#dcb46b",900,"end")+
 rect(740,610,210,48,"#dcb46b",10)+text(845,641,"PEŁNE MENU PDF",12,"#2e2119",900,"middle"))

save("rest-gallery.svg","Restauracja Stary Rynek — galeria","Galeria · wnętrze · kuchnia · wydarzenia",
 rect(55,50,1330,800,"#f4ecdf",28)+text(95,110,"ZOBACZ STARY RYNEK",40,"#3b291e",900)+
 text(95,150,"Miejsce na kolację, spotkanie i ważne okazje.",17,"#806c5d")+
 rect(95,205,520,430,"#2e2119",22)+text(130,255,"WNĘTRZE",13,"#dcb46b",900)+text(130,575,"Ciepłe światło.",31,"#fff",900)+text(130,610,"Dużo drewna. Zero pośpiechu.",18,"#d8c7b7")+
 rect(645,205,300,205,"#c9955e",20)+text(680,255,"KUCHNIA",13,"#fff",900)+text(680,355,"Z talerza",25,"#fff",900)+
 rect(970,205,335,205,"#e4d3bd",20)+text(1005,255,"WINO",13,"#6b4b36",900)+text(1005,355,"Dobieramy do dań",25,"#3b291e",900)+
 rect(645,435,660,200,"#fffaf2",20)+text(680,485,"WYDARZENIA",13,"#b27b3d",900)+text(680,535,"Kolacje degustacyjne · muzyka na żywo · prywatne spotkania",20,"#3b291e",800)+rect(680,565,190,45,"#3b291e",10)+text(775,594,"SPRAWDŹ DATY",12,"#fff",900,"middle"))

save("rest-booking.svg","Restauracja Stary Rynek — rezerwacja","Rezerwacja · liczba osób · data · godzina · okazja",
 rect(55,50,1330,800,"#faf4e9",28)+text(95,110,"ZAREZERWUJ STOLIK",42,"#3b291e",900)+text(95,150,"Wybierz termin — potwierdzenie otrzymasz od razu.",17,"#806c5d")+
 rect(95,205,780,500,"#fff",24,"#e8ded0",2)+text(135,255,"01  TERMIN",13,"#b27b3d",900)+
 rect(135,285,200,58,"#3b291e",10)+text(235,321,"18 PAŹ",16,"#fff",900,"middle")+
 rect(355,285,200,58,"#f5eee4",10)+text(455,321,"19 PAŹ",16,"#5f4a3a",900,"middle")+
 rect(575,285,200,58,"#f5eee4",10)+text(675,321,"20 PAŹ",16,"#5f4a3a",900,"middle")+
 text(135,390,"02  GODZINA",13,"#b27b3d",900)+
 text(135,435,"18:00",18,"#3b291e",800)+text(250,435,"19:30",18,"#3b291e",800)+text(365,435,"20:00",18,"#3b291e",800)+text(480,435,"21:00",18,"#3b291e",800)+
 text(135,500,"03  LICZBA OSÓB",13,"#b27b3d",900)+rect(135,530,160,50,"#f5eee4",10)+text(215,562,"2 osoby",15,"#3b291e",800,"middle")+
 rect(315,530,160,50,"#3b291e",10)+text(395,562,"4 osoby",15,"#fff",800,"middle")+
 rect(495,530,160,50,"#f5eee4",10)+text(575,562,"6 osób",15,"#3b291e",800,"middle")+
 rect(135,620,250,48,"#b27b3d",10)+text(260,651,"REZERWUJ STOLIK",12,"#fff",900,"middle")+
 rect(925,205,380,500,"#2e2119",24)+text(965,255,"DODAJ OKAZJĘ",13,"#dcb46b",900)+text(965,315,"Urodziny?",25,"#fff",900)+text(965,350,"Rocznica?",25,"#fff",900)+text(965,385,"Spotkanie firmowe?",25,"#fff",900)+
 text(965,465,"Napisz w komentarzu.",17,"#cbbcae")+text(965,500,"Przygotujemy stół",17,"#cbbcae")+text(965,535,"i mały akcent od nas.",17,"#cbbcae")+rect(965,600,230,48,"#dcb46b",10)+text(1080,631,"DODAJ INFORMACJĘ",12,"#2e2119",900,"middle"))

# BUSINESS APPS — clearly different dashboard compositions
save("fakturypro.svg","FakturyPro — panel","Aplikacja biznesowa · faktury · klienci · płatności",
 rect(45,40,1350,820,"#f4f7fb",28)+rect(45,40,235,820,"#111827",28)+text(80,100,"FakturyPro",24,"#fff",900)+
 text(80,160,"Pulpit",14,"#67e8f9",800)+text(80,205,"Faktury",14,"#b8c3d4")+text(80,250,"Klienci",14,"#b8c3d4")+text(80,295,"Raporty",14,"#b8c3d4")+text(80,340,"Ustawienia",14,"#b8c3d4")+
 text(320,100,"Dzień dobry, Damian",28,"#182334",900)+text(320,135,"Wtorek, 6 października",14,"#7b8a9e")+
 rect(320,185,300,150,"#fff",18,"#dce4ec",2)+text(350,230,"SPRZEDAŻ",12,"#7b8a9e",800)+text(350,285,"28 450 zł",34,"#182334",900)+text(350,315,"↑ 12,4% vs. poprzedni miesiąc",13,"#159b75",800)+
 rect(645,185,300,150,"#fff",18,"#dce4ec",2)+text(675,230,"NIEOPŁACONE",12,"#7b8a9e",800)+text(675,285,"4 820 zł",34,"#182334",900)+text(675,315,"7 faktur oczekuje",13,"#d66a3d",800)+
 rect(970,185,360,150,"#162033",18)+text(1000,230,"SZYBKA AKCJA",12,"#67e8f9",800)+text(1000,280,"+ Wystaw fakturę",22,"#fff",900)+text(1000,315,"Import PDF · e-mail · numeracja",13,"#b8c3d4")+
 rect(320,375,1010,360,"#fff",18,"#dce4ec",2)+text(350,420,"Ostatnie dokumenty",22,"#182334",900)+
 text(350,475,"FV/10/2026/184",14,"#182334",800)+text(650,475,"Studio Forma",14,"#6b7b90")+text(900,475,"2 450 zł",14,"#182334",800)+text(1200,475,"OPŁACONA",12,"#159b75",800)+
 text(350,535,"FV/10/2026/183",14,"#182334",800)+text(650,535,"AutoKlinika",14,"#6b7b90")+text(900,535,"1 280 zł",14,"#182334",800)+text(1200,535,"OCZEKUJE",12,"#d66a3d",800)+
 text(350,595,"FV/10/2026/182",14,"#182334",800)+text(650,595,"Bella Salon",14,"#6b7b90")+text(900,595,"840 zł",14,"#182334",800)+text(1200,595,"OPŁACONA",12,"#159b75",800))

save("serwisflow.svg","SerwisFlow — zlecenia","Aplikacja usługowa · kalendarz · zlecenia · klienci",
 rect(45,40,1350,820,"#eef5f2",28)+text(85,100,"SerwisFlow",28,"#12352b",900)+
 rect(85,145,1220,70,"#fff",16)+text(115,190,"DZISIAJ",14,"#5d766c",800)+
 text(320,190,"08:00",13,"#6f817b")+text(505,190,"10:00",13,"#6f817b")+text(690,190,"12:00",13,"#6f817b")+text(875,190,"14:00",13,"#6f817b")+text(1060,190,"16:00",13,"#6f817b")+
 rect(85,250,1220,470,"#fff",18,"#dbe7e1",2)+
 rect(120,290,260,105,"#dff3eb",14)+text(145,330,"08:30",14,"#197b5a",800)+text(145,360,"Przegląd klimatyzacji",18,"#12352b",900)+text(145,385,"Anna · Salon Bella",12,"#678078")+
 rect(420,430,300,110,"#ffe7d6",14)+text(445,470,"11:00",14,"#b65f2c",800)+text(445,500,"Naprawa ekspresu",18,"#3f2c21",900)+text(445,525,"Piotr · Stary Rynek",12,"#7d6b5d")+
 rect(760,300,340,110,"#e8e0f8",14)+text(785,340,"13:30",14,"#7451a8",800)+text(785,370,"Montaż klimatyzacji",18,"#31233f",900)+text(785,395,"Marek · Kłecko",12,"#7d6b89")+
 rect(760,560,410,105,"#12352b",14)+text(790,600,"NOWE ZLECENIE",13,"#7fe0bd",800)+text(790,635,"+ Dodaj wizytę",22,"#fff",900))

save("magazynpro.svg","MagazynPro — panel","System magazynowy · stany · zamówienia · skaner",
 rect(45,40,1350,820,"#f7f5ef",28)+
 rect(45,40,1350,82,"#20251f",28)+text(85,92,"MagazynPro",25,"#fff",900)+text(1290,92,"CENTRALA · POZNAŃ",12,"#c8d1c2",800,"end")+
 text(90,165,"STAN MAGAZYNU",15,"#67705f",800)+
 rect(90,205,285,150,"#fff",18,"#e0e0d7",2)+text(120,250,"1 284",38,"#20251f",900)+text(120,285,"aktywnych SKU",14,"#737c6d")+
 rect(400,205,285,150,"#20251f",18)+text(430,250,"37",38,"#d8f36a",900)+text(430,285,"produktów poniżej minimum",14,"#c0c9b8")+
 rect(710,205,285,150,"#fff",18,"#e0e0d7",2)+text(740,250,"96%",38,"#20251f",900)+text(740,285,"zgodności stanów",14,"#737c6d")+
 rect(1020,205,285,150,"#dce8c9",18)+text(1050,250,"SCAN",26,"#20251f",900)+text(1050,285,"Uruchom skaner",14,"#526044")+
 rect(90,400,1215,310,"#fff",18,"#e0e0d7",2)+text(120,445,"Ostatnie ruchy",22,"#20251f",900)+
 text(120,500,"SKU-18492",14,"#20251f",800)+text(330,500,"Kawa ziarnista 1 kg",14,"#67705f")+text(720,500,"+24",14,"#197b5a",900)+text(950,500,"Przyjęcie",12,"#67705f")+text(1190,500,"10:42",12,"#67705f")+
 text(120,550,"SKU-00931",14,"#20251f",800)+text(330,550,"Filtr oleju",14,"#67705f")+text(720,550,"-8",14,"#b64f3f",900)+text(950,550,"Wydanie",12,"#67705f")+text(1190,550,"10:18",12,"#67705f")+
 text(120,600,"SKU-88120",14,"#20251f",800)+text(330,600,"Koszulka robocza",14,"#67705f")+text(720,600,"+12",14,"#197b5a",900)+text(950,600,"Przyjęcie",12,"#67705f")+text(1190,600,"09:51",12,"#67705f"))

print("Generated", len(list(OUT.glob("*.svg"))), "SVG assets")
