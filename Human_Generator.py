#-------------------------------------------------------------------------------
# Name:        Human Generator
# Purpose:     Generate a fantasy-style character
#
# Author:      Rivan
#
# Created:     07/08/2014
# Copyright:   (c) Rivan 2015
# Licence:     All rights reserved.
#-------------------------------------------------------------------------------

try:
    from tkinter import *
    from tkinter import ttk
except:
    #This module has a different name in older versions of python
    print("This program was designed for python 3.3, please consider updating.")
    from time import sleep
    time.sleep(4)
    exit()
import math
import random
try:
    import Human_Generator_LIST
except:
    print ("Failed to access Human_Generator_LIST.py, please make sure that it is in the same folder,\nand under the same name." *7)
    import time
    time.sleep(4)
    exit()

PeopleMale_Custom               = []
PeopleFemale_Custom             = []
LastNames_Custom                = []
LastAndFirst_Custom             = []
LastAndLast_Custom              = []
Kingdoms_Custom                 = []
Cities_Custom                   = []
Towns_Custom                    = []
Villages_Custom                 = []
Tomes_Custom                    = []
Animals_Custom                  = []
Male_GiftCustom                 = []
Female_GiftCustom               = []
Male_QuirkCustom                = []
Female_QuirkCustom              = []
Male_FlawCustom                 = []
Female_FlawCustom               = []
Male_UniqueCustom               = []
Female_UniqueCustom             = []
ApparelBeggarMale_Custom        = []
ApparelBeggarFemale_Custom      = []
ApparelProfessionMale_Custom    = []
ApparelProfessionFemale_Custom  = []
ApparelNobleMale_Custom         = []
ApparelNobleFemale_Custom       = []
ApparelAdventurerMale_Custom    = []
ApparelAdventurerFemale_Custom  = []
ApparelRoyalMale_Custom         = []
ApparelRoyalFemale_Custom       = []



def main():
    pass

if __name__ == '__main__':
    main()

def GenerateHuman(*args):

    Factors = options.get()

    if MEN.get() & WOMEN.get() == True:
      Gender = random.choice(("Male", "Female"))
    elif MEN.get() == True:
      Gender = "Male"
    elif WOMEN.get() == True:
      Gender = "Female"
    else:
      Gender = "Neither!"


    if Gender == "Male":
      if JustMy_Men.get() == False:
        FirstName = random.choice(Human_Generator_LIST.PeopleMale + PeopleMale_Custom)
      else:
        try:
          FirstName = random.choice(PeopleMale_Custom)
        except:
          FirstName = random.choice(Human_Generator_LIST.PeopleMale)
    elif Gender == "Female":
      if JustMy_Women.get() == False:
        FirstName = random.choice(Human_Generator_LIST.PeopleFemale + PeopleFemale_Custom)
      else:
        try:
          FirstName = random.choice(PeopleFemale_Custom)
        except:
          FirstName = random.choice(Human_Generator_LIST.PeopleFemale)
    else:
      FirstName = random.choice(Human_Generator_LIST.PeopleMale or Human_Generator_LIST.PeopleFemale or PeopleMale_Custom or PeopleFemale_Custom)


    if NonCompound_Switch.get() == True and Compound_Switch.get() == True:
        LastNameAA = random.choice(["Simple", "Complex"])
    elif NonCompound_Switch.get() == True:
        LastNameAA = "Simple"
    elif Compound_Switch.get() == True:
        LastNameAA = "Complex"
    else:
        LastNameAA = "None"

    if LastNameAA == "Simple":
      if JustMy_NonCompound.get() == False:
        LastName = random.choice(Human_Generator_LIST.LastNames + LastNames_Custom)
      else:
        try:
            LastName = random.choice(LastNames_Custom)
        except:
            LastName = random.choice(Human_Generator_LIST.LastNames)
    elif LastNameAA == "Complex":
      if JustMy_Compound.get() == False:
        LastName = (random.choice(Human_Generator_LIST.LastAndFirst + LastAndFirst_Custom) + random.choice(Human_Generator_LIST.LastAndLast + LastAndLast_Custom))
      else:
       try:
        LastName = (random.choice(LastAndFirst_Custom) + random.choice(LastAndLast_Custom))
       except:
        LastName = (random.choice(Human_Generator_LIST.LastAndFirst + LastAndFirst_Custom) + random.choice(Human_Generator_LIST.LastAndLast + LastAndLast_Custom))
    else:
        LastName = ""

    #Second last name for extra things
    if NonCompound_Switch.get() == True and Compound_Switch.get() == True:
        LastNameAA = random.choice(["Simple", "Complex"])
    elif NonCompound_Switch.get() == True:
        LastNameAA = "Simple"
    elif Compound_Switch.get() == True:
        LastNameAA = "Complex"
    else:
        LastNameAA = "None"

    if LastNameAA == "Simple":
      if JustMy_NonCompound.get() == False:
        LastName2 = random.choice(Human_Generator_LIST.LastNames + LastNames_Custom)
      else:
        try:
            LastName2 = random.choice(LastNames_Custom)
        except:
            LastName2 = random.choice(Human_Generator_LIST.LastNames)
    elif LastNameAA == "Complex":
      if JustMy_Compound.get() == False:
        LastName2 = (random.choice(Human_Generator_LIST.LastAndFirst + LastAndFirst_Custom) + random.choice(Human_Generator_LIST.LastAndLast + LastAndLast_Custom))
      else:
       try:
        LastName2 = (random.choice(LastAndFirst_Custom) + random.choice(LastAndLast_Custom))
       except:
        LastName2 = (random.choice(Human_Generator_LIST.LastAndFirst + LastAndFirst_Custom) + random.choice(Human_Generator_LIST.LastAndLast + LastAndLast_Custom))
    else:
        LastName2 = ""


    if random.randint(1, 7) != 1:
       HairColour = random.choice(("brown", "blonde", "black", "dark brown", "light blonde"))
    else:
       HairColour = random.choice(("brown", "blonde", "black", "dark brown", "light blonde",
                                   "red", "blue", "bright silver", "purple", "pink", "green"))

    HairLength = random.choice(("short", "medium length", "long", "very long"))

    if random.randint(1, 17) != 1:
       EyeColour = random.choice(("blue eyes", "brown eyes", "green eyes", "hazel eyes"))
    else:
       #Heteros is latin for 'different'
       Heteros1 = 1
       Heteros2 = 1
       while Heteros1 == Heteros2:#Make sure the eyes are different colors so you don't have things like "one blue and one blue eye"
         Heteros1 = random.choice(("amber", "blue", "brown", "green", "hazel", "gray"))
         Heteros2 = random.choice(("amber", "blue", "brown", "green", "hazel", "gray"))
       EyeColour = random.choice(("gray eyes", "one " + Heteros1 + " and one " + Heteros2 + " eye"))

    #These values are assumed for a starting point.
    #Male
    #Height:  5' 5.3" - 6' 5"
    #Weight:  130.0 - 210.0
    #Female
    #Height: 5' 2" - 5' 10"
    #Weight:  100.0 - 175.0

    #Weight
    if Gender =="Male":
       Weight = random.normalvariate(150, 7)
    elif Gender == "Female":
       Weight = random.normalvariate(116, 5)
    else:
       Weight = random.normalvariate(150, 10)
       if Factors == "Qdebug":#Debug
        print("Gender expected, using generic weight range instead.")

    #Height
    if Gender == "Male":
       Height = random.normalvariate(56.4, 1.6)
    elif Gender == "Female":
       Height = random.normalvariate(55.5, 1.3)
    else:
       Height = random.normalvariate(50, 2)
       if Factors == "Qdebug":#Debug
        print("Gender expected, generic height.")

    if Factors == "Qdebug":
      print("Beginning Height: " + str(Height))

    #Multiply Height by weight for a more realistic size.
    if Gender == "Male":
      Height = (((Height / 2) * (Weight/100)) + (Height/2))
    elif Gender == "Female":
      Height = (((Height / 2) * (Weight/80)) + (Height/2))
    else:
      Height = (((Height / 2) * (Weight/90)) + (Height/2))
      if Factors == "Qdebug":#Debug
        print("Gender expected, weight multiplier using generic.")

    #self-explanitory, it's creating the feet/inches measurements we're used to.
    Height_Feet = Height // 12
    Height_Inches = Height % 12

    Apparel_GEN1 = []

    if ApparelBeggar_Switch.get() == True:
        Apparel_GEN1.append("Beggar")
    if ApparelProfession_Switch.get() == True:
        Apparel_GEN1.append("Profession")
    if ApparelNoble_Switch.get() == True:
        Apparel_GEN1.append("Noble")
    if ApparelAdventurer_Switch.get() == True:
        Apparel_GEN1.append("Adventurer")
    if ApparelRoyal_Switch.get() == True:
        Apparel_GEN1.append("Royal")

    Apparel_GEN2 = random.choice(Apparel_GEN1)

    if Gender == "Male" or Gender == "Female":
        if Apparel_GEN2 =="Beggar":
           if Gender == "Male":
            if JustMy_Beggar.get() == False:
              Apparel_DESC = random.choice(Human_Generator_LIST.ApparelBeggarMale + ApparelBeggarMale_Custom)
            else:
             try:
                Apparel_DESC = random.choice(ApparelBeggarMale_Custom)
             except:
                Apparel_DESC = ""
           else:
            if JustMy_Beggar.get() == False:
              Apparel_DESC = random.choice(Human_Generator_LIST.ApparelBeggarFemale + ApparelBeggarFemale_Custom)
            else:
             try:
                Apparel_DESC = random.choice(ApparelBeggarFemale_Custom)
             except:
                Apparel_DESC = ""
        elif Apparel_GEN2 == "Profession":
           if Gender == "Male":
            if JustMy_Profession.get() == False:
             Apparel_DESC = random.choice(Human_Generator_LIST.ApparelProfessionMale + ApparelProfessionMale_Custom)
            else:
             try:
                Apparel_DESC = random.choice(ApparelProfessionMale_Custom)
             except:
                Apparel_DESC = ""
           else:
            if JustMy_Profession.get() == False:
             Apparel_DESC = random.choice(Human_Generator_LIST.ApparelProfessionFemale + ApparelProfessionFemale_Custom)
            else:
             try:
                Apparel_DESC = random.choice(ApparelProfessionFemale_Custom)
             except:
                Apparel_DESC = ""
        elif Apparel_GEN2 == "Noble":
           if Gender == "Male":
            if JustMy_Noble.get() == False:
             Apparel_DESC = random.choice(Human_Generator_LIST.ApparelNobleMale + ApparelNobleMale_Custom)
            else:
             try:
                Apparel_DESC = random.choice(ApparelNobleMale_Custom)
             except:
                Apparel_DESC = ""
           else:
            if JustMy_Noble.get() == False:
             Apparel_DESC = random.choice(Human_Generator_LIST.ApparelNobleFemale + ApparelNobleFemale_Custom)
            else:
             try:
                Apparel_DESC = random.choice(ApparelNobleFemale_Custom)
             except:
                Apparel_DESC = ""
        elif Apparel_GEN2 == "Adventurer":
           if Gender =="Male":
            if JustMy_Adventurer.get() == False:
             Apparel_DESC = random.choice(Human_Generator_LIST.ApparelAdventurerMale + ApparelAdventurerMale_Custom)
            else:
             try:
                Apparel_DESC = random.choice(ApparelAdventurerMale_Custom)
             except:
                Apparel_DESC = ""
           else:
            if JustMy_Adventurer.get() == False:
             Apparel_DESC = random.choice(Human_Generator_LIST.ApparelAdventurerFemale + ApparelAdventurerFemale_Custom)
            else:
             try:
                Apparel_DESC = random.choice(ApparelAdventurerFemale_Custom)
             except:
                Apparel_DESC = ""
        elif Apparel_GEN2 == "Royal":
           if Gender =="Male":
            if JustMy_Royal.get() == False:
             Apparel_DESC = random.choice(Human_Generator_LIST.ApparelRoyalMale + ApparelRoyalMale_Custom)
            else:
             try:
                Apparel_DESC = random.choice(ApparelRoyalMale_Custom)
             except:
                Apparel_DESC = ""
           else:
            if JustMy_Royal.get() == False:
             Apparel_DESC = random.choice(Human_Generator_LIST.ApparelRoyalFemale + ApparelRoyalFemale_Custom)
            else:
             try:
                Apparel_DESC = random.choice(ApparelRoyalFemale_Custom)
             except:
                Apparel_DESC = ""
        else:
          if Factors == "Qdebug":#Debug
            print("ERROR at 'generate apparel': expected one of five results, got other.")
    else:
      Apparel_DESC = ""
      if Factors == "Qdebug":#Debug
        print("Gender expected, no apparel description")


    if Gender == "Male":
       if Gift_Switch.get() == True and random.randrange(1, 23) != 1:
        if JustMy_Gift.get() == False:
            GiftGen = Human_Generator_LIST.giftMale((JustMy_Women.get()), (JustMy_Kingdom.get()), PeopleFemale_Custom, LastName, LastName2, Kingdoms_Custom)
            Gift = random.choice(Male_GiftCustom + (GiftGen))
        else:
            try:
                Gift = random.choice(Male_GiftCustom)
            except:
                Gift = " "
       else:
         Gift = ""

       if Quirk_Switch.get() == True and random.randrange(1, 23) != 1:
        if JustMy_Quirk.get() == False:
            QuirkGen = Human_Generator_LIST.quirkMale((JustMy_Tomes.get()), (JustMy_Cities.get()), Tomes_Custom, Cities_Custom)
            Quirk = random.choice(Male_QuirkCustom + (QuirkGen))
        else:
            try:
                Quirk = random.choice(Male_QuirkCustom)
            except:
                Quirk = " "
       else:
         Quirk = ""

       if Flaw_Switch.get() == True and random.randrange(1, 23) != 1:
        if JustMy_Flaw.get() == False:
            FlawGen = Human_Generator_LIST.flawMale((JustMy_Kingdom.get()), Kingdoms_Custom)
            Flaw = random.choice(Male_FlawCustom + (FlawGen))
        else:
            try:
                Flaw = random.choice(Male_FlawCustom)
            except:
                Flaw = " "
       else:
         Flaw = ""

       #Unique start
       if Unique_Switch.get() == True and random.randint(1, 23) != 1:
           Unique_GEN1 = []
           if Gift_Switch.get() == True:
            Unique_GEN1.append("Gift")
           if Quirk_Switch.get() == True:
            Unique_GEN1.append("Quirk")
           if Flaw_Switch.get() == True:
            Unique_GEN1.append("Flaw")

           try:
            Unique_GEN2 = (random.choice(Unique_GEN1))
           except:
            Unique_GEN2 = "None"

           if Unique_GEN2 == "Gift":
            if JustMy_Gift.get() == False:
                GiftGen = Human_Generator_LIST.giftMale((JustMy_Women.get()), (JustMy_Kingdom.get()), PeopleFemale_Custom, LastName, LastName2, Kingdoms_Custom)
                Unique = random.choice(Male_UniqueCustom + Male_GiftCustom + (GiftGen))
            else:
                try:
                    Unique = random.choice(Male_UniqueCustom + Male_GiftCustom)
                except:
                    Unique = " "
           elif Unique_GEN2 == "Quirk":
            if JustMy_Quirk.get() == False:
                QuirkGen = Human_Generator_LIST.quirkMale((JustMy_Tomes.get()), (JustMy_Cities.get()), Tomes_Custom, Cities_Custom)
                Unique = random.choice(Male_UniqueCustom + Male_QuirkCustom + (QuirkGen))
            else:
                try:
                    Unique = random.choice(Male_UniqueCustom + Male_QuirkCustom)
                except:
                    Unique = " "
           elif Unique_GEN2 == "Flaw":
            if JustMy_Flaw.get() == False:
                FlawGen = Human_Generator_LIST.flawMale((JustMy_Kingdom.get()), Kingdoms_Custom)
                Unique = random.choice(Male_UniqueCustom + Male_FlawCustom + (FlawGen))
            else:
                try:
                    Unique = random.choice(Male_UniqueCustom + Male_FlawCustom)
                except:
                    Unique = " "
           else:
            try:
                Unique = random.choice(Male_UniqueCustom)
            except:
                Unique = ""
       else:
        Unique = ""

       if Unique == Gift or Unique == Quirk or Unique == Flaw:
        Unique = ""
       #Unique end


    elif Gender == "Female":
     if Gift_Switch.get() == True and random.randrange(1, 23) != 1:
        if JustMy_Gift.get() == False:
            GiftGen = Human_Generator_LIST.giftFemale((JustMy_Men.get()), (JustMy_Villages.get()), PeopleMale_Custom, LastName, LastName2, Villages_Custom)
            Gift = random.choice(Female_GiftCustom + (GiftGen))
        else:
            try:
                Gift = random.choice(Female_GiftCustom)
            except:
                Gift = " "
     else:
      Gift = ""

     if Quirk_Switch.get() == True and random.randrange(1, 23) != 1:
        if JustMy_Quirk.get() == False:
            QuirkGen = Human_Generator_LIST.quirkFemale((JustMy_Tomes.get()), Tomes_Custom)
            Quirk = random.choice(Female_QuirkCustom + QuirkGen)
        else:
            try:
                Quirk = random.choice(Female_QuirkCustom)
            except:
                Quirk = " "
     else:
      Quirk = ""

     if Flaw_Switch.get() == True and random.randrange(1, 23) != 1:
        if JustMy_Flaw.get() == False:
            FlawGen = Human_Generator_LIST.flawFemale((JustMy_Kingdom.get()), (JustMy_Animals.get()), Kingdoms_Custom, Animals_Custom)
            Flaw = random.choice(Female_QuirkCustom + (FlawGen))
        else:
            try:
                Flaw = random.choice(Female_QuirkCustom)
            except:
                Flaw = " "
     else:
      Flaw = ""

     #Unique start
     if Unique_Switch.get() == True and random.randint(1, 23) != 1:
       Unique_GEN1 = []
       if Gift_Switch.get() == True:
        Unique_GEN1.append("Gift")
       if Quirk_Switch.get() == True:
        Unique_GEN1.append("Quirk")
       if Flaw_Switch.get() == True:
        Unique_GEN1.append("Flaw")

       try:
        Unique_GEN2 = (random.choice(Unique_GEN1))
       except:
        Unique_GEN2 = "None"

       if Unique_GEN2 == "Gift":
        if JustMy_Gift.get() == False:
            GiftGen = Human_Generator_LIST.giftFemale((JustMy_Men.get()), (JustMy_Villages.get()), PeopleMale_Custom, LastName, LastName2, Villages_Custom)
            Unique = random.choice(Female_UniqueCustom + Female_GiftCustom + (GiftGen))
        else:
            try:
                Unique = random.choice(Female_UniqueCustom + Female_GiftCustom)
            except:
                Unique = " "
       elif Unique_GEN2 == "Quirk":
        if JustMy_Quirk.get() == False:
            QuirkGen = Human_Generator_LIST.quirkFemale((JustMy_Tomes.get()), Tomes_Custom)
            Unique = random.choice(Female_UniqueCustom + Female_QuirkCustom + (QuirkGen))
        else:
            try:
                Unique = random.choice(Female_UniqueCustom + Female_QuirkCustom)
            except:
                Unique = " "
       elif Unique_GEN2 == "Flaw":
        if JustMy_Flaw.get() == False:
            FlawGen = Human_Generator_LIST.flawFemale((JustMy_Kingdom.get()), (JustMy_Animals.get()), Kingdoms_Custom, Animals_Custom)
            Unique = random.choice(Female_UniqueCustom + Female_FlawCustom + (FlawGen))
        else:
            try:
                Unique = random.choice(Female_UniqueCustom + Female_FlawCustom)
            except:
                Unique = " "
       else:
        try:
            Unique = random.choice(Female_UniqueCustom)
        except:
            Unique = " "
     else:
        Unique = ""

     if Unique == Gift or Unique == Quirk or Unique == Flaw:
        Unique = ""
     #Unique end


    else:
       Gift = ""
       Quirk = ""
       Flaw = ""
       Unique = ""
       if Factors == "Qdebug":#Debug
        print("Gender expected, no traits.")


    Fertility_Total = (round(random.normalvariate(0.35, 1.7)))

    #Debug section
    if Factors == "Qdebug":
        print("Gender: " + Gender)
        print("First name: " + FirstName)
        print("Hair color: " + HairColour)
        print("Eye color: " + EyeColour)
        print("Height in inches: " + str(Height))
        print("Feet: " + str(Height_Feet))
        print("Inches: " + str(Height_Inches))
        print(str(Weight) + " Pounds")
        print("Fertility Mod. " + str(Fertility_Total))
        print(Apparel_GEN2)
        print(Apparel_DESC)
        print("Gift:" + Gift)
        print("Quirk: " + Quirk)
        print("Flaw:" + Flaw)
        print("Unique: " + Unique)
        print("UniqueGEN: " + Unique_GEN2)
        print("")
    else:
        pass
    #Debug section

    print("")
    #If there are no inches, don't print them.
    if int(Height_Inches) != 0:
      Output_First = str(FirstName + " " + LastName + " has " +
                   HairLength + " " +
                   HairColour + " hair, " +
                   EyeColour + ", is " +
                   str(int(Height_Feet)) + "' " +
                   str(int(Height_Inches)) + '" ' + "tall, and weighs " +
                   str(int(Weight)) + " pounds.")
    else:
      Output_First = (FirstName + " " + LastName + " has " +
                HairLength + " " +
                HairColour + " hair, " +
                EyeColour + ", is " +
                str(int(Height_Feet)) + "' " + "tall, and weighs " +
                str(int(Weight)) + " pounds.")
    print(Output_First)

    #Don't waste space printing nothing.
    if Quirk != "":
     print(Quirk)

    CharWidget = Tk()
    CharWidget.title(FirstName + " " + LastName)

    NewFrame = ttk.Frame(CharWidget, padding="3 3 10 10")
    NewFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    NewFrame.columnconfigure(0, weight=1)
    NewFrame.rowconfigure(0, weight=1)


    ttk.Label(NewFrame, text=(Output_First)).grid(column=1, row=1, sticky=N)
    try:
      ttk.Label(NewFrame, text=(Apparel_DESC)).grid(column=1, row=2, sticky=N)
    except:
      print("No apparel generated.")
    descriptorsPositions = 3
    try:
        if Gift != " " and Gift != "":
            ttk.Label(NewFrame, text=(Gift)).grid(column=1, row=descriptorsPositions, sticky=N)
            descriptorsPositions = descriptorsPositions+1
    except:
      pass
    try:
        if Quirk != " " and Quirk != "":
            ttk.Label(NewFrame, text=(Quirk)).grid(column=1, row=descriptorsPositions, sticky=N)
            descriptorsPositions = descriptorsPositions+1
    except:
      pass
    try:
        if Flaw != " " and Flaw != "":
            ttk.Label(NewFrame, text=(Flaw)).grid(column=1, row=descriptorsPositions, sticky=N)
            descriptorsPositions = descriptorsPositions+1
    except:
      pass
    try:
        if Unique != " " and Unique != "":
            ttk.Label(NewFrame, text=(Unique)).grid(column=1, row=descriptorsPositions, sticky=N)
    except:
      pass


    def saveCharacter():
        import json
        from os.path import exists as pathExists
        from os.path import abspath as absPath
        from os import makedirs as makeDirs

        if not pathExists("Characters"):
            makeDirs("Characters")

        Path = absPath('Characters')

        with open((Path + '\\' + FirstName + ' ' + LastName + '.txt'), 'w') as charFile:
            saveObject = json.dumps( (Output_First, Apparel_DESC, Gift, Quirk, Flaw, Unique),  charFile, indent=2)
            charFile.writelines((Output_First, '\n', Apparel_DESC, '\n', Gift, '\n', Quirk, '\n', Flaw, '\n', Unique))
    ttk.Button(NewFrame, text="Save to file", command=saveCharacter).grid(column=1, row=10, sticky=W)

    CharWidget.mainloop()
    #</GenerateHuman>




def Exit():
    exit()
    #This is here because for some reason if I put the exit() function directly
    #into a button, the game activates it immediately.



def NewName():
    if AddToHere.get() == "First names: Male":
      PeopleMale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "First names: Female":
      PeopleFemale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Last names":
      LastNames_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Component last names: First":
      LastAndFirst_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Component last names: Last":
      LastAndLast_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Kingdoms":
      Kingdoms_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Cities":
      Cities_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Towns":
      Towns_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Villages":
      Villages_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Tomes":
      Tomes_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Animals":
      Animals_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Men's gift":
      Male_GiftCustom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Women's gift":
      Female_GiftCustom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Men's quirk":
      Male_QuirkCustom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Women's quirk":
      Female_QuirkCustom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Men's flaw":
      Male_FlawCustom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Women's flaw":
      Female_FlawCustom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Men's 'unique":
      Male_UniqueCustom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Women's 'unique'":
      Female_UniqueCustom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Men's beggar clothes":
      ApparelBeggarMale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Women's beggar clothes":
      ApparelBeggarFemale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Men's professional clothes":
      ApparelProfessionMale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Women's professional clothes":
      ApparelProfessionFemale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Men's noble clothes":
      ApparelNobleMale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Women's noble clothes":
      ApparelNobleFemale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Men's adventurer outfits":
      ApparelAdventurerMale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Women's adventurer outfits":
      ApparelAdventurerFemale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Royal men's clothes":
      ApparelRoyalMale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    elif AddToHere.get() == "Royal women's clothes":
      ApparelRoyalFemale_Custom.append(NameAdd.get())
      print("'" + NameAdd.get() + "' Succesfully added to " + AddToHere.get() + ".")
    else:
      print("Unrecognized list: " + AddToHere)




def about():
    HelpWindow = Tk()
    HelpWindow.title("Help window")

    HelpFrame = ttk.Frame(HelpWindow, padding="3 3 10 10")
    HelpFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    HelpFrame.columnconfigure(0, weight=2)
    HelpFrame.rowconfigure(0, weight=2)

    ttk.Label(HelpFrame, text="Pressing the 'Generate' button will create a new window with a character in it.").grid(column=2, row=1, sticky=W)
    ttk.Label(HelpFrame, text="The large text box below it is used to add personal touches to the lists.\nExample: you could add your own name to the list of names to use by typing it in the box on the left,\nand then selecting the appropriate gender list, and pressing 'Add my name/description to this list!'").grid(column=2, row=2, sticky=W)
    ttk.Label(HelpFrame, text="Component last names are the ones like 'Puredragon,' the 'Pure' would be the first, and 'dragon' the second part.").grid(column=2, row=3, sticky=W)
    ttk.Label(HelpFrame, text="The 'advanced' settings allow you to turn on or off different parts of the generation, allowing you to only get \na male character for example.").grid(column=2, row=4, sticky=W)
    ttk.Label(HelpFrame, text="This program was made entirely by Rivan Wells, 2015").grid(column=2, row=999, sticky=E)




def checkBoxesWindow():

    checkFrame = ttk.Frame(root, padding="2 2 9 9")
    checkFrame.grid(column=0, row=1, sticky=(N, W, E, S))
    checkFrame.columnconfigure(0, weight=1)
    checkFrame.rowconfigure(0, weight=1)


    ttk.Checkbutton(checkFrame, text="Generate male characters", variable=MEN).grid(column=1, row=1, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom male first names", variable=JustMy_Men).grid(column=3, row=1, sticky=W)

    ttk.Checkbutton(checkFrame, text="Generate female characters", variable=WOMEN).grid(column=1, row=2, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom female first names", variable=JustMy_Women).grid(column=3, row=2, sticky=W)

    ttk.Checkbutton(checkFrame, text="Generate non-compound last names", variable=NonCompound_Switch).grid(column=1, row=3, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom last names", variable=JustMy_NonCompound).grid(column=3, row=3, sticky=W)

    ttk.Checkbutton(checkFrame, text="Generate compound last names", variable=Compound_Switch).grid(column=1, row=4, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom compound last names", variable=JustMy_Compound).grid(column=3, row=4, sticky=W)

    ttk.Checkbutton(checkFrame, text="Only custom kingdoms", variable=JustMy_Kingdom).grid(column=1, row=5, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom cities", variable=JustMy_Cities).grid(column=3, row=5, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom towns", variable=JustMy_Towns).grid(column=1, row=6, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom villages", variable=JustMy_Villages).grid(column=3, row=6, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom tomes", variable=JustMy_Tomes).grid(column=1, row=7, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom animals", variable=JustMy_Animals).grid(column=3, row=7, sticky=W)

    ttk.Checkbutton(checkFrame, text="Generate gift", variable=Gift_Switch).grid(column=1, row=8, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom gifts", variable=JustMy_Gift).grid(column=3, row=8, sticky=W)

    ttk.Checkbutton(checkFrame, text="Generate quirk", variable=Quirk_Switch).grid(column=1, row=9, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom quirks", variable=JustMy_Quirk).grid(column=3, row=9, sticky=W)

    ttk.Checkbutton(checkFrame, text="Generate flaw", variable=Flaw_Switch).grid(column=1, row=10, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom flaws", variable=JustMy_Flaw).grid(column=3, row=10, sticky=W)

    ttk.Checkbutton(checkFrame, text="Generate extra 'unique'", variable=Unique_Switch).grid(column=1, row=11, sticky=W)

    ttk.Checkbutton(checkFrame, text="Use beggar clothes", variable=ApparelBeggar_Switch).grid(column=1, row=12, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom beggar clothes", variable=JustMy_Beggar).grid(column=3, row=12, sticky=W)

    ttk.Checkbutton(checkFrame, text="Use profession clothes", variable=ApparelProfession_Switch).grid(column=1, row=13, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom profession clothes", variable=JustMy_Profession).grid(column=3, row=13, sticky=W)

    ttk.Checkbutton(checkFrame, text="Use noble clothes", variable=ApparelNoble_Switch).grid(column=1, row=14, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom noble clothes", variable=JustMy_Noble).grid(column=3, row=14, sticky=W)

    ttk.Checkbutton(checkFrame, text="Use adventurer outfits", variable=ApparelAdventurer_Switch).grid(column=1, row=15, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom adventurer outfits", variable=JustMy_Adventurer).grid(column=3, row=15, sticky=W)

    ttk.Checkbutton(checkFrame, text="Use royal clothes", variable=ApparelRoyal_Switch).grid(column=1, row=16, sticky=W)
    ttk.Checkbutton(checkFrame, text="Only custom royal clothes", variable=JustMy_Royal).grid(column=3, row=16, sticky=W)




def saveCustoms():
    from os.path import exists as pathExists
    from os.path import abspath as absPath
    from os import makedirs as makeDirs
    import json
    if not pathExists("Generator custom presets"):
        makeDirs("Generator custom presets")

    Path = absPath('Generator custom presets')
    with open(( Path + "\\PeopleMale.txt" ), 'w') as fileSave:
        json.dump(PeopleMale_Custom, fileSave)
    with open(( Path + "\\PeopleFemale.txt"), 'w') as fileSave:
        json.dump(PeopleFemale_Custom, fileSave)
    with open(( Path + "\\LastNames.txt"), 'w') as fileSave:
        json.dump(LastNames_Custom, fileSave)
    with open(( Path + "\\LastAndFirst.txt"), 'w') as fileSave:
        json.dump(LastAndFirst_Custom, fileSave)
    with open(( Path + "\\LastAndLast.txt"), 'w') as fileSave:
        json.dump(LastAndLast_Custom, fileSave)
    with open(( Path + "\\Kingdoms.txt"), 'w') as fileSave:
        json.dump(Kingdoms_Custom, fileSave)
    with open(( Path + "\\Cities.txt"), 'w') as fileSave:
        json.dump(Cities_Custom, fileSave)
    with open(( Path + "\\Towns.txt"), 'w') as fileSave:
        json.dump(Towns_Custom, fileSave)
    with open(( Path + "\\Villages.txt"), 'w') as fileSave:
        json.dump(Villages_Custom, fileSave)
    with open(( Path + "\\Tomes.txt"), 'w') as fileSave:
        json.dump(Tomes_Custom, fileSave)
    with open(( Path + "\\Animals.txt"), 'w') as fileSave:
        json.dump(Animals_Custom, fileSave)
    with open(( Path + "\\MaleGift.txt"), 'w') as fileSave:
        json.dump(Male_GiftCustom, fileSave)
    with open(( Path + "\\FemaleGift.txt"), 'w') as fileSave:
        json.dump(Cities_Custom, fileSave)
    with open(( Path + "\\MaleQuirk.txt"), 'w') as fileSave:
        json.dump(Male_QuirkCustom, fileSave)
    with open(( Path + "\\FemaleQuirk.txt"), 'w') as fileSave:
        json.dump(Female_QuirkCustom, fileSave)
    with open(( Path + "\\MaleFlaw.txt"), 'w') as fileSave:
        json.dump(Male_FlawCustom, fileSave)
    with open(( Path + "\\FemaleFlaw.txt"), 'w') as fileSave:
        json.dump(Female_FlawCustom, fileSave)
    with open(( Path + "\\MaleUnique.txt"), 'w') as fileSave:
        json.dump(Male_UniqueCustom, fileSave)
    with open(( Path + "\\FemaleUnique.txt"), 'w') as fileSave:
        json.dump(Female_UniqueCustom, fileSave)
    with open(( Path + "\\ApparelBeggarMale.txt"), 'w') as fileSave:
        json.dump(ApparelBeggarMale_Custom, fileSave)
    with open(( Path + "\\ApparelBeggarFemale.txt"), 'w') as fileSave:
        json.dump(ApparelBeggarFemale_Custom, fileSave)
    with open(( Path + "\\ApparelProfessionMale.txt"), 'w') as fileSave:
        json.dump(ApparelProfessionMale_Custom, fileSave)
    with open(( Path + "\\ApparelProfessionFemale.txt"), 'w') as fileSave:
        json.dump(ApparelProfessionFemale_Custom, fileSave)
    with open(( Path + "\\ApparelNobleMale.txt"), 'w') as fileSave:
        json.dump(ApparelNobleMale_Custom, fileSave)
    with open(( Path + "\\ApparelNobleFemale.txt"), 'w') as fileSave:
        json.dump(ApparelNobleFemale_Custom, fileSave)
    with open(( Path + "\\ApparelAdventurerMale.txt"), 'w') as fileSave:
        json.dump(ApparelAdventurerMale_Custom, fileSave)
    with open(( Path + "\\ApparelAdventurerFemale.txt"), 'w') as fileSave:
        json.dump(ApparelAdventurerFemale_Custom, fileSave)
    with open(( Path + "\\ApparelRoyalMale.txt"), 'w') as fileSave:
        json.dump(ApparelRoyalMale_Custom, fileSave)
    with open(( Path + "\\ApparelRoyalFemale.txt"), 'w') as fileSave:
        json.dump(ApparelRoyalFemale_Custom, fileSave)



def loadCustoms():
    from os.path import exists as pathExists
    from os.path import abspath as absPath
    import json
    if not pathExists("Generator custom presets"):
        print("Saves either don't exist or their path was renamed.")
        pass

    Path = absPath('Generator custom presets')
    with open(( Path + "\\PeopleMale.txt" ), 'r') as fileLoad:
        PeopleMale_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\PeopleFemale.txt"), 'r') as fileLoad:
        PeopleFemale_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\LastNames.txt"), 'r') as fileLoad:
        LastNames_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\LastAndFirst.txt"), 'r') as fileLoad:
        LastAndFirst_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\LastAndLast.txt"), 'r') as fileLoad:
        LastAndLast_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\Kingdoms.txt"), 'r') as fileLoad:
        Kingdoms_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\Cities.txt"), 'r') as fileLoad:
        Cities_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\Towns.txt"), 'r') as fileLoad:
        Towns_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\Villages.txt"), 'r') as fileLoad:
        Villages_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\Tomes.txt"), 'r') as fileLoad:
        Tomes_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\Animals.txt"), 'r') as fileLoad:
        Animals_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\MaleGift.txt"), 'r') as fileLoad:
        Male_GiftCustom.extend(json.load(fileLoad))
    with open(( Path + "\\FemaleGift.txt"), 'r') as fileLoad:
        Female_GiftCustom.extend(json.load(fileLoad))
    with open(( Path + "\\MaleQuirk.txt"), 'r') as fileLoad:
        Male_QuirkCustom.extend(json.load(fileLoad))
    with open(( Path + "\\FemaleQuirk.txt"), 'r') as fileLoad:
        Female_QuirkCustom.extend(json.load(fileLoad))
    with open(( Path + "\\MaleFlaw.txt"), 'r') as fileLoad:
        Male_FlawCustom.extend(json.load(fileLoad))
    with open(( Path + "\\FemaleFlaw.txt"), 'r') as fileLoad:
        Female_FlawCustom.extend(json.load(fileLoad))
    with open(( Path + "\\MaleUnique.txt"), 'r') as fileLoad:
        Male_UniqueCustom.extend(json.load(fileLoad))
    with open(( Path + "\\FemaleUnique.txt"), 'r') as fileLoad:
        Female_UniqueCustom.extend(json.load(fileLoad))
    with open(( Path + "\\ApparelBeggarMale.txt"), 'r') as fileLoad:
        ApparelBeggarMale_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\ApparelBeggarFemale.txt"), 'r') as fileLoad:
        ApparelBeggarFemale_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\ApparelProfessionMale.txt"), 'r') as fileLoad:
        ApparelProfessionMale_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\ApparelProfessionFemale.txt"), 'r') as fileLoad:
        ApparelProfessionFemale_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\ApparelNobleMale.txt"), 'r') as fileLoad:
        ApparelNobleMale_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\ApparelNobleFemale.txt"), 'r') as fileLoad:
        ApparelNobleFemale_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\ApparelAdventurerMale.txt"), 'r') as fileLoad:
        ApparelAdventurerMale_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\ApparelAdventurerFemale.txt"), 'r') as fileLoad:
        ApparelAdventurerFemale_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\ApparelRoyalMale.txt"), 'r') as fileLoad:
        ApparelRoyalMale_Custom.extend(json.load(fileLoad))
    with open(( Path + "\\ApparelRoyalFemale.txt"), 'r') as fileLoad:
        ApparelRoyalFemale_Custom.extend(json.load(fileLoad))




print("\n \n \n")
print("Feel free to minimize this window, it should just show a little debug stuff. \n" *2)
#print("\n")

root = Tk()
root.title("Character Generator: Human")

PrimaryFrame = ttk.Frame(root, padding="3 3 12 12")
PrimaryFrame.grid(column=0, row=0, sticky=(N, W, E, S))
PrimaryFrame.columnconfigure(0, weight=1)
PrimaryFrame.rowconfigure(0, weight=1)

ttk.Label(PrimaryFrame, text="Debug options:").grid(column=2, row=1, sticky=E)
options = StringVar()
special_options = ttk.Entry(PrimaryFrame, width=8, textvariable=options).grid(column=3, row=1, sticky=W)

ttk.Button(PrimaryFrame, text="Generate", command=GenerateHuman).grid(column=2, row=0, sticky=EW)

NameAdd = StringVar()
ttk.Entry(PrimaryFrame, width=14, textvariable=NameAdd).grid(column=1, row=3, sticky=EW)

AddToHere = StringVar()
NameBoxes = ttk.Combobox(PrimaryFrame, textvariable=AddToHere, values=("First names: Male", "First names: Female",
                                                                       "Last names", "Component last names: First", "Component last names: Last",
                                                                       "Kingdoms", "Cities", "Towns", "Villages", "Tomes", "Animals",
                                                                       "Men's gift", "Women's gift", "Men's quirk", "Women's quirk", "Men's flaw", "Women's flaw", "Men's 'unique'", "Women's 'unique'",
                                                                       "Men's beggar clothes", "Women's beggar clothes",
                                                                       "Men's professional clothes", "Women's professional clothes",
                                                                       "Men's noble clothes", "Women's noble clothes",
                                                                       "Men's adventurer outfits", "Women's adventurer outfits",
                                                                       "Royal men's clothes", "Royal women's clothes")).grid(column=2, row=3, sticky=W)

ttk.Button(PrimaryFrame, text="Add to this list", command=NewName).grid(column=3, row=3, sticky=W)

ttk.Button(PrimaryFrame, text="Help!", command=about).grid(column=1, row=10, sticky=W)

ttk.Button(PrimaryFrame, text="Save custom entries", command=saveCustoms).grid(column=1, row=11, sticky=EW)
ttk.Button(PrimaryFrame, text="Load previous custom entries", command=loadCustoms).grid(column=2, row=11, sticky=W)

ttk.Button(PrimaryFrame, text="Close all windows", command=Exit).grid(column=3, row=12, sticky=E)

ttk.Button(PrimaryFrame, text="Advanced control", command=checkBoxesWindow).grid(column=1, row=12, sticky=EW)

MEN                             = BooleanVar()
MEN.set(True)
WOMEN                           = BooleanVar()
WOMEN.set(True)
NonCompound_Switch              = BooleanVar()
NonCompound_Switch.set(True)
Compound_Switch                 = BooleanVar()
Compound_Switch.set(True)
Gift_Switch                     = BooleanVar()
Gift_Switch.set(True)
Quirk_Switch                    = BooleanVar()
Quirk_Switch.set(True)
Flaw_Switch                     = BooleanVar()
Flaw_Switch.set(True)
Unique_Switch                   = BooleanVar()
Unique_Switch.set(True)
ApparelBeggar_Switch            = BooleanVar()
ApparelBeggar_Switch.set(True)
ApparelProfession_Switch        = BooleanVar()
ApparelProfession_Switch.set(True)
ApparelNoble_Switch             = BooleanVar()
ApparelNoble_Switch.set(True)
ApparelAdventurer_Switch        = BooleanVar()
ApparelAdventurer_Switch.set(True)
ApparelRoyal_Switch             = BooleanVar()
ApparelRoyal_Switch.set(True)
JustMy_Men                      = BooleanVar()
JustMy_Women                    = BooleanVar()
JustMy_NonCompound              = BooleanVar()
JustMy_Compound                 = BooleanVar()
JustMy_Kingdom                  = BooleanVar()
JustMy_Cities                   = BooleanVar()
JustMy_Towns                    = BooleanVar()
JustMy_Villages                 = BooleanVar()
JustMy_Tomes                    = BooleanVar()
JustMy_Animals                  = BooleanVar()
JustMy_Gift                     = BooleanVar()
JustMy_Quirk                    = BooleanVar()
JustMy_Flaw                     = BooleanVar()
#Unique doesn't get a JustMy switch, it uses the other lists.
JustMy_Beggar                   = BooleanVar()
JustMy_Profession               = BooleanVar()
JustMy_Noble                    = BooleanVar()
JustMy_Adventurer               = BooleanVar()
JustMy_Royal                    = BooleanVar()


for child in PrimaryFrame.winfo_children(): child.grid_configure(padx=5, pady=5)
root.bind('<Return>', GenerateHuman)

root.mainloop()
