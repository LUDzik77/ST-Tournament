from random import choice

def make_name(race):
    if race == "human":
        n1=human_name_1
        n2=human_name_2 
    elif race == "elf": 
        n1=elf_name_1
        n2=elf_name_2         
    elif race == "dwarf": 
        n1=dwarf_name_1
        n2=dwarf_name_2         
    elif race =="hobbit": 
        n1=hobbit_name_1
        n2=hobbit_name_2
    new_name = choice(n1)+ " " +choice(n2)
    return(new_name)


human_name_1 = ["Jared", "Yan", "Thomas", "Orlando", "Kartas", "Arturus", "Voislav", "Robb", "Garin",\
                "Bir", "Pavel", "Sir", "Boleslaw", "Geralt", "Wei", "Aryan", "Gaillart", "Drake", "Haliman"]
human_name_2 = ["Kowalski", "Ivovic", "Starglin", "Decraft", "Bousille", "Dune", "Mukeny", "Shield",\
                "Trupin", "Washirton", "Ambarass", "Ainsworth", "Longston", "Muller", "Lamerville", "Twardowski", "Sato"]

elf_name_1 = ["Elouin", "Bounty", "Galadriel", "Vafank", "Nils", "Fan-Tar", "Aoife", "Jean-Marc",\
              "Lian", "Daragh", "Aidan", "Parialas", "Aen", "Galarr", "Melian", "Gilien", "Li", "Ming" ]
elf_name_2 = ["Noldorin", "Sindarin", "Wave", "Birdgrass", "Kayleigh", "Dubghail", "Aen Seidhe", \
              "Faoiltian", "Goldenarrow", "Breeden", "Yllarona", "Delacroix", "Doudear", "Wiosna", "Warden",\
              "Di Nardo", "Frisina", "Lano"]

dwarf_name_1 = ["Yarpen", "Oink", "Axe", "Grr", "Rakshasan", "Janusz", "Yalgrar", "Doranoth", "Dan", "Hagrin",\
                "Xerxes",  "Murasa", "Datang", "Yong", "Jun", "Strobat", "Krishna", "Ritvik", "Ankh", "Hedrok",\
                "Mumbarak", "Nawaar", "Rezath", "Ragnor"]
dwarf_name_2 = ["Gargantua", "Zirgring", "Roach", "Zearhlot", "Minerock", "Longbeard", "Ahuramazda", "Dong"\
                "Tofplukt", "Chrobot", "Gruzowicz", "Onyx", "Bull", "Schneider", "Wagneron", "Kimura", "Mori", "Og",\
                "Porti", "Jawak", "Rahman", "Bashir", "Latimer"]

hobbit_name_1 = ["Sammy", "Rildo", "Tu-Tu", "Neol", "Merry", "Radosciek", "Smutasek", "Bodo", "Guntur",\
                 "Hobson", "Poziomka", "Tomek", "Klaus", "Fang", "Min", "Sicho", "Dodo", "Purnama", "Bagus",\
                 "Tarik", ]
hobbit_name_2 = ["Bilbum", "Gilgot","Tobolek", "Smallpack", "Hag", "Grey", "Daggerling", "Haystock", "Solo",\
                 "Weasley", "Pelawi", "Galpsi", "Mugwart", "Grasse-Matinee", "Asesino", "Gamgee", "Cul de Sac",\
                 "Wasp", "Toe", "Peaubleme", "Sano", "Gulo"]