#-------------------------------------------------------------------------------
# Name:        LIST
# Purpose:     Create/hold a list for Human Generator
#
# Author:      Rivan
#
# Created:     10/03/2014
# Copyright:   (c) Rivan 2015
# Licence:     GNU GENERAL PUBLIC LICENSE.
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import random


def giftMale(justMy_Female, justMy_Kingdoms, CFemale, lastName, lastName2, CKingdoms):
    if justMy_Female != True:
        SPeopleFemale = PeopleFemale
    else:
        SPeopleFemale = []
    if justMy_Kingdoms != True:
        SKingdoms = Kingdoms
    else:
        SKingdoms = []

    giftGen = ["A miniature air elemental floats above his shoulder.",
               "He is married to " + random.choice(SPeopleFemale + CFemale)  + " " + lastName +  ".",
               "He spends most of his evenings training at St. Arianas' cathedral.",
               "He trains with Kerae; the Duelist of Arlent.",
               "He is currently courting " + random.choice(SPeopleFemale + CFemale) + " " + lastName2 + ".",
               "He trained with the arch-wizard of " + random.choice(SKingdoms + CKingdoms) + ".",
               ]
    return list(giftGen)

def quirkMale(justMy_Tomes, justMy_Cities, CTomes, CCities):
    if justMy_Tomes != True:
        STomes = Tomes
    else:
        STomes = []

    if justMy_Cities != True:
        SCities = Cities
    else:
        SCities = []

    quirkGen = ["He has six fingers on his " + random.choice(["left", "right"]) + " hand.",
               "He has a sigil painted above his " + random.choice(["left", "right"]) + " eye.",
               "His ears are slightly pointed.",
               "He has a long beard.",
               "He has a braided beard.",
               "He has a well trimmed beard.",
               "He is constantly spinning a coin around his fingers.",
               "He carries " + random.choice(STomes + CTomes) + ".",
               "He has studied several secrets of the universe, but can't find a tome on how to use them.",
               "He has been searching for " + random.choice(STomes + CTomes) + " for " + str(random.randint(2, 8)) + " years.",
               "He died once, and was resurrected by the church of " + random.choice(SCities + CCities) + ".",
               ]
    return list(quirkGen)

def flawMale(justMy_Kingdoms, CKingdoms):
    if justMy_Kingdoms != True:
        SKingdoms = Kingdoms
    else:
        SKingdoms = []

    flawGen = ["He has a scar across his face.",
               "His " + random.choice(["left", "right"]) + " eye is blind.",
               "He has been banished from " + random.choice(SKingdoms + CKingdoms) + ".",
               "He is the exiled prince of " + random.choice(SKingdoms + CKingdoms) + ".",
               "He has " + random.choice(["minor", "slight", "moderate", "minor", "slight", "moderate", "minor", "slight", "major"]) + " anger issues.",
               "He dabbled in the occult " + str(random.randint(2, 7)) + " years ago.",
               ]
    return list(flawGen)


def giftFemale(justMy_Male, justMy_Villages, PeopleMale_Custom, LastName, LastName2, Villages_Custom):
    if justMy_Male != True:
        SPeopleMale = PeopleMale
    else:
        SPeopleMale = []
    if justMy_Villages != True:
        SVillages = Villages
    else:
        SVillages = []

    giftGen = ["She has a heart painted on her " + random.choice(["left", "right"]) + " arm.",
               "A small pale-blue light floats above her " + random.choice(["left", "right"]) + " shoulder.",
               "She has a small bird resting on her shoulder.",
               "She is married to " + random.choice(SPeopleMale + PeopleMale_Custom) + " " + LastName + ".",
               "She is being courted by " + random.choice(SPeopleMale + PeopleMale_Custom) + " " + LastName2 + ".",
               "She spends most of her evenings training at St. Arianas' cathedral.",
               "She trains with Kerae; the Duelist of Arlent.",
               "She has won seven blade duels, and lost only two.",
               "She has an enchantment on her " + random.choice(["left", "right"]) + " hand, keeping it from injuries.",
               "She learned from the mage of " + random.choice(SVillages + Villages_Custom) + ".",
               ]
    return list(giftGen)

def quirkFemale(justMy_Tomes, CTomes):
    if justMy_Tomes != True:
        STomes = Tomes
    else:
        STomes = []

    quirkGen = ["She has a sigil painted above her " + random.choice(["left", "right"]) + " eye.",
                "She has a small deck of cards she looks through every few minutes.",
                "She always carries " + random.choice(STomes + CTomes) + ".",
                "She always dances as she walks.",
                "She has been searching for " + random.choice(STomes + CTomes) + " for " + str(random.randint(2, 8)) + " years.",
                ]
    return list(quirkGen)

def flawFemale(justMy_Kingdoms, justMy_Animals, CKingdoms, CAnimals):
    if justMy_Kingdoms != True:
        SKingdoms = Kingdoms
    else:
        SKingdoms = []
    if justMy_Animals != True:
        SAnimalsPlural = AnimalsPlural
    else:
        SAnimalsPlural = []

    flawGen = ["She has a scar across her face.",
               "Her " + random.choice(["left", "right"]) + " eye is blind.",
               "She is the exiled princess of " + random.choice(SKingdoms + CKingdoms) + ".",
               "She is irrationally afraid of " + random.choice(SAnimalsPlural + CAnimals) + ".",
               ]
    return list(flawGen)



PeopleMale = [

"Harvey",
"Kris",
"Johnathan",
"Tony",
"Salvador",
"Rico",
"Zackary",
"Enrique",
"Ricardo",
"Shayne",
"Sherman",
"Bennie",
"Lorenzo",
"Larry",
"Julius",
"Anderson",
"Ryan",
"Millard",
"Harry",
"John",
"Jacob",
"Peter",
"Edmund",
"Gordon",
"Luther",
"Grant",
"Dominick",
"Jesse",
"Pedro",
"Joseph",
"Blake",
"Edward",
"Derrick",

]


PeopleFemale = [

"Rosalina",
"Kathrin",
"Philomena",
"Serena",
"Holli",
"Telma",
"Isis",
"Magdalen",
"Brande",
"Dot",
"Carisa",
"Sofia",
"Kristel",
"Keilly",
"Analisa",
"Delma",
"Latisha",
"Bernetta",
"Gretta",
"Gwynevere",
"Sarah",
"Susan",
"Lucy",
"Kelly",
"Rochelle",
"Sonya",
"Anna",
"Lydia",
"Amber",
"Sophie",
"Iris",
"Erika",
"Sophie",

]


LastNames = [

"Smith",
"Nery",
"Burne",
"Fordye",
"Wyne",
"Shancey",
"Folcey",
"Bourne",
"Awer",
"Enthyns",
"Weills",
"Cileir",
"Scrinun",
"Leonard",
"Figueroa",
"Martinez",
"Briggs",
"Castillo",
"Reid",
"Vera",

]


LastAndFirst = [

"Storm",
"Frost",
"Fire",
"Earth",
"Moon",
"Sun",
"Star",
"Ever",
"Emerald",
"Ruby",
"Diamond",
"Pure",
"Steel",
"Heaven",
"War",
"Bright",

]


LastAndLast = [

"leaf",
"eye",
"wing",
"fire",
"dragon",
"circle",
"hammer",
"wind",
"drink",
"spirit",
"wolf",
"fox",
"tree",
"rose",
"blade",
"dagger",
"rising",
"wood",

]

AnimalsPlural = [

"foxes",
"mice",
"dogs",
"cats",
"rats",
"camels",
"flies",
"dragons",
"pegasai",
"squirrels",
"sheep",
"cute little bunny rabbits",

]

Towns = [

"Nandolond",
"Byford",
"Hallmibekkr",
"Ragrove",
"Keliklif",
"Geheath",
"Beewick",
"Keford",
"Thoebrook",
"Abam, the Dragon's Lair",
"Lefield",
"Abed",
"Tabrycg",
"Pawold",
"Bawold",

]


Cities = [

"Chigate",
"Eithithlum",
"Cupool",
"Linevriath",
"Gamor, the City of Scepters",
"Eorcot, the City Beneath the Arch",
"Pastow, the City of Rings",
"The Five Cities of Hone",
"Camor, the City of Palaces",
"Huybury, the City of Spells",
"Hymoor, the City Beneath the Arch",
"The Mystical City of Beydon",
"Dublin City",

]


Villages = [

"Goldenwall Village",
"Craftsman's Borough",
"Feydale Farthing",
"Lake Borough",
"Knightstower Borough",
"Lion's Ward",
"Bridge Village",
"Hart's District",
"Crown District",
"Merchant's Village",

]


Kingdoms = [

"The Empire of Thithlonde",
"The Principality of Arenon",
"The Hallowed Realm of Londorthon",
"The Principality of Enond",
"The Peerless Dominion of Beliene",
"The Seventh Great Kingdom of Ellormen",
"The Dominion of Siregul",
"Ellothlon, the Dominion of Swords",
"Alithlon, the Magocracy of Lights",
"The Magocracy of Enor",
"Edherest, the Theocracy of Rings",
"Faline, the Kingdom of Chains",
"Menione, the Dominion of Veils",
"Manaquia, the kingdom of Blessings",

]

Tomes = [

"The Tome of Providence",
"Lima's Leaves of Mythology",
"The Elysian Compendium of Abal",
"The Elemental Esoterica of Prosido",
"The Phitusin Apocrypha",
"The Tome of Psycrystals",
"Buda's Parchments of Demiplanes",
"The Ziri Fragments",
"The Arcane Slates of Grainan",

]



#Apparel section begining

ApparelBeggarMale = [

"He wears dirty linen rags, which used to be white",
"He wears a tattered shirt and brown trousers",
"He wears ragged animal skins tied together",
"He wears worn trousers",

]


ApparelBeggarFemale = [

"She wears dirty linen rags, which used to be white",
"She wears a tattered shirt and brown trousers",
"She wears a threadbare dress and a torn cloak",
"She wears a torn long tunic",
"She wears a sack cloth shirt, and ragged trousers",

]


ApparelProfessionMale = [

"He wears a lightly faded bright " + random.choice(["red", "blue", "green", "purple"]) + " tunic, and fine black trousers",
"He wears a leather apron, soot covered linen shirt, and heavy gloves",
"He wears a hat to protect from the sun, a long dirt-covered tunic, and brown trousers with patched knees",
"He wears a long brown robe, and a satchel of leaves",
"He wears a dirty plain tunic, equally plain trousers, and carries a pick",
"He wears a dirty leather doublet, a long dark cloak, and a strung bow over his shoulder",
"He wears a slightly rusted plate breastplate, and a pike on his shoulder",

]


ApparelProfessionFemale = [

"She wears a lightly faded, " + random.choice(["red", "blue", "green"]) + " dress, and a jingling pouch at her side",
"She wears a leather apron, and soot covered linen shirt, and heavy gloves",
"She wears a hat to protect from the sun, a long dirt-covered tunic, and brown trousers with patched knees",
"She wears a long brown robe, and a satchel of leaves",
"She wears a dirty plain tunic, equally plain trousers, and carries a pick",
"She wears a dirty leather doublet, a long dark cloak, and a strung bow over her shoulder",
"She wears a slightly rusted plate breastplate, and a pike on her shoulder",

]


ApparelNobleMale = [

"He wears a well tailored " + random.choice(["red", "blue", "green", "purple"]) + " shirt, and matching trousers",
"He wears a long " + random.choice(["red", "blue", "green", "purple"]) + " robe with silver trim",
"He wears perfectly white robes",
"He wears a tabbard displaying his device, over fine " + random.choice(["red", "blue", "green", "purple"]) + " linen",

]


ApparelNobleFemale = [

"She wears a long, flowing dress the same color as her eyes",
"She wears a " + random.choice(["red", "blue", "green", "purple"]) + " tunic, matching skirt, a silver necklace, a thin circlet, a bracelet, and a single earring",
"She wears a medium-length " + random.choice(["red", "blue", "green", "purple"]) + " dress with gold trim",

]


ApparelAdventurerMale = [

"He wears dented platemail",
"He wears light chainmaille with a heraldic tabbard",
"He wears a long hardened leather doublet, and a sword at his side",
"He wears " + random.choice(["red", "blue", "green", "yellow", "purple", "black", "white"]) + " robes, covered in celtic forms which glow a faint white",
"He wears plain white robes, and cloth wraps on his fists",
"He wears a wolf pelt coat over bloodstained white linen, and he carries a claymore",
"He wears a " + random.choice(["red", "blue", "green", "gray", "yellow", "purple", "black", "white"]) + " robe with an arm torn off, and bandages beneath",

]


ApparelAdventurerFemale = [

"She wears white robes, with a gold cross on the front",
"She wears a decorative formed breastplate, and leather leggings",
"She wears a long cloak, covering her leather armor",
"She wears plain white robes, and cloth wraps on her fists",
"She wears rosewood armor",
"She wears a " + random.choice(["red", "blue", "green", "gray", "yellow", "purple", "black", "white"]) + " robe with an arm torn off, and bandages beneath",
"She wears a torn tunic and a collection of chainmaille pieces that used to be a hawberk",

]


ApparelRoyalMale = [

"He wears grand " + random.choice(["red", "blue", "green", "purple"]) + " robes, a gold chain, and a large crown with rubies",
"He wears a chain hauberk with a tabbard displaying fine heraldry, and a gold crown",

]


ApparelRoyalFemale = [

"She wears a long " + random.choice(["red", "blue", "green", "purple"]) + " dress with gold accents, three gold rings, and a small crown with emeralds",
"She wears a short dress that matches the large sapphire in her silver crown",
"She wears a silver dress with a long train, a gold necklace, and a crown with sapphires",

]

#Apparel section end

print("'Human_Generator_LIST.py' loaded")