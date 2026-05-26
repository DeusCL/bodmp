import PanelFillerCommon
languages = ["English", "Spanish", "EnglishUS", "French", "Italian", "German", "Chinese", "Russian"]
languages1 = ["English", "Spanish", "EnglishUS", "French", "Italian", "German"]
languages2 = ["Chinese", "Russian"]

def getLanguagesHeader():
    strLang = "Key,"
    for language in languages:
        strLang = strLang + language + ","
    return strLang[:-1] + "\n"

def getLanguagesHeaderFromLanguages(languages, printKey):
    strLang = ""
    if printKey:
        strLang = "Key,"
    for language in languages:
        strLang = strLang + language + ","
    return strLang[:-1] + "\n"

def getMenuLanguagesHeader():
    menuLanguages = languages
    strLang = ""
    for language in menuLanguages:
        strLang = strLang + language + ","
    return strLang[:-1] + "\n"

def getMenuLanguagesHeader(menuLanguages):
    strLang = ""
    for language in menuLanguages:
        strLang = strLang + language + ","
    return strLang[:-1] + "\n"

######################### MENU #########################
def generateMenu():
    texts = {}
    for language in languages:
        if language != "English":
            menu = {}
            execfile("../../DATA/Menu/" + language + ".py")
            texts[language] = ForeingDict

    f = open("../../Localization/menu.csv", "w")
    f.write(getMenuLanguagesHeader(languages1))
    f2 = open("../../Localization/menu2.csv", "w")
    f2.write(getMenuLanguagesHeader(languages2))

    for key in texts[languages[1]].keys():
        text = ''
        for language in languages1:
            if language != "English":
                if key in texts[language].keys():
                    text = text + ',"' + texts[language][key] + '"'
                else:
                    text = text + ','
        output = '"' + key + '"' + text + '\n'
        f.write(output)

        text = ''
        for language in languages2:
            if language != "English":
                if key in texts[language].keys():
                    text = text + ',"' + texts[language][key] + '"'
                else:
                    text = text + ','

        output = '"' + text + '\n'
        f2.write(output)

    f.close()
    f2.close()

######################### LEVELS #########################
def generateLevels():
    for i in range(1, 18):
        f=open("../../Localization/M" + str(i) + ".csv", "w")
        f2=open("../../Localization/M" + str(i) + "_2.csv", "w")
        texts = {}
        f.write(getLanguagesHeaderFromLanguages(languages1, 1))
        f2.write(getLanguagesHeaderFromLanguages(languages2, 0))
        for language in languages:
            Textos = {}
            execfile("../../DATA/Text/"+ language + "/M" + str(i) + ".py")
            texts[language] = Textos
    
        for key in texts[languages[0]].keys():
            text = ''
            for language in languages1:
                if texts[language].has_key(key):
                    currentText = texts[language][key][4]
                    currentText = string.replace(currentText, '"', '')
                    text = text + '"' + currentText + '",'
                else:
                    text = text + ','
            f.write(key + ',' + text + '\n')

            text = ''
            for language in languages2:
                if texts[language].has_key(key):
                    currentText = texts[language][key][4]
                    currentText = string.replace(currentText, '"', '')
                    text = text + '"' + currentText + '",'
                else:
                    text = text + ','
            f2.write(text + '\n')
        f.close()
        f2.close()
    
######################### Tutor #########################
def generateTutor():
    f=open("../../Localization/tutor.csv", "w")
    f2=open("../../Localization/tutor2.csv", "w")
    texts = {}
    f.write(getLanguagesHeaderFromLanguages(languages1, 1))
    f2.write(getLanguagesHeaderFromLanguages(languages2, 0))
    for language in languages:
        Textos = {}
        execfile("../../DATA/Text/"+ language + "/tutor.py")
        texts[language] = Textos
    
    for key in texts[languages[0]].keys():
        text = ''
        for language in languages1:
            if texts[language].has_key(key):
                currentText = texts[language][key]
                sentences = ""
                for sentence in currentText:
                    sentences = sentences + sentence + '\n'
                text = text + '"' + sentences[:-1] + '",'
            else:
                text = text + ','
        f.write(key + ',' + text + '\n')

        text = ''
        for language in languages2:
            if texts[language].has_key(key):
                currentText = texts[language][key]
                sentences = ""
                for sentence in currentText:
                    sentences = sentences + sentence + '\n'
                text = text + '"' + sentences[:-1] + '",'
            else:
                text = text + ','
        f2.write(text + '\n')
    f.close()
    f2.close()

######################### ObjIds #########################
def generateObjIds():
    texts = {}
    f=open("../../Localization/objIds.csv", "w")
    f2=open("../../Localization/objIds2.csv", "w")
    f.write(getLanguagesHeaderFromLanguages(languages1, 1))
    f2.write(getLanguagesHeaderFromLanguages(languages2, 0))
    for language in languages:
        execfile("../../DATA/ObjIds/" + language +".py")
        texts[language] = Reference.DefaultSelectionData
        Reference.DefaultSelectionData = {}
    for key in texts[languages[0]].keys():
        text = ''
        for language in languages1:
            text = text + "," + texts[language][key][2]
        f.write(key + text + "\n")

        text = ''
        for language in languages2:
            text = text + texts[language][key][2] +  ","
        f2.write(text + "\n")
    f.close()
    f2.close()

######################### Combos #########################
def resetArray():
    return  {
              "Knight_N"   : {},
              "Barbarian_N": {},
              "Amazon_N"   : {},
              "Dwarf_N"    : {},
              "Default"    : {},
            }
def generateCombos():
    texts = {}
    f=open("../../Localization/combos.csv", "w")
    f2=open("../../Localization/combos2.csv", "w")
    f.write(getLanguagesHeaderFromLanguages(languages1, 1))
    f2.write(getLanguagesHeaderFromLanguages(languages2, 0))
    for language in languages:
        ComboNames = resetArray()
        execfile("../../DATA/Text/" + language + "/Combos.py")
        texts[language] = ComboNames

    for key in texts[languages[0]].keys():
        for key2 in texts[languages[0]][key].keys():
            text = ''
            for language in languages1:
                text = text + "," + texts[language][key][key2]
            f.write(key + " " + key2 + text + "\n")
        
            text = ''
            for language in languages2:
                text = text + texts[language][key][key2] + ","
            f2.write(text + "\n")

    f.close()
    f2.close()

######################### Casa #########################
def generateCasa():

    characters = ["Bar", "Kgt", "Amz", "Dwf"]

    def fillData():
        data = {}
        for char in characters:
            for i in range(1, 5):
                data[('TextInfoChar' + char + str(i))] = globals()['TextInfoChar' + char + str(i)]
        return data

    f=open("../../Localization/casa.csv", "w")
    f2=open("../../Localization/casa2.csv", "w")
    f.write(getLanguagesHeaderFromLanguages(languages1, 1))
    f2.write(getLanguagesHeaderFromLanguages(languages2, 0))
    texts = {}
    for language in languages:
        execfile("../../DATA/Text/" + language + "/casa.py")
        texts[language] = fillData()

    for key in texts[languages[0]].keys():
        text = ''
        for language in languages1:
            text = text + texts[language][key] + '","'
        text = text[:-3]
        f.write(key + ',"' + text + '"\n')

        text = ''
        for language in languages2:
            text = text + texts[language][key] + '","'
        text = text[:-3]
        f2.write('"' + text + '"\n')

    f.close()
    f2.close()

######################### map2D #########################
def generateMap2D():
    levels = ["Monolith", "MONOLITH", "Tabriz", "TABRIZ", "Khazel", "KHAZEL", "Marakamda", "MARAKAMDA", "MINE", "Mine", "TellHa", "TELLHA", "QUEENST", "QueensT", "Karum", "KARUM", "SHALATUWAR", "Shalatuwar", "ORLOK", "Orlok", "NEMRUT", "Nemrut", "NEJEV", "Nejev", "ALFARUM", "Alfarum", "XATHRA", "Xathra", "Ianna", "IANNA", "DALGURAK", "DalGurak", "CHAOS", "Chaos"]

    def fillData2Dmap():
        data = {}
        for level in levels:
            data[level] = globals()[level]
        return data

    f=open("../../Localization/map2D.csv", "w")
    f2=open("../../Localization/map2D_2.csv", "w")
    f.write(getLanguagesHeaderFromLanguages(languages1, 1))
    f2.write(getLanguagesHeaderFromLanguages(languages2, 0))
    texts = {}
    for language in languages:
        MapList = {}
        execfile("../../DATA/Text/" + language + "/map2D.py")
        texts[language] = fillData2Dmap()

    for key in texts[languages[0]].keys():
        text = ''
        for language in languages1:
            text = text + texts[language][key] + '","'
        text = text[:-3]
        f.write(key + ',"' + text + '"\n')

        text = ''
        for language in languages2:
            text = text + texts[language][key] + '","'
        text = text[:-3]
        f2.write('"' + text + '"\n')

    f.close()
    f2.close()

######################## MapText ########################
def generateMapTexts():
    f=open("../../Localization/mapTexts.csv", "w")
    f2=open("../../Localization/mapTexts2.csv", "w")
    f.write(getLanguagesHeaderFromLanguages(languages1, 1))
    f2.write(getLanguagesHeaderFromLanguages(languages2, 0))
    maps = PanelFillerCommon.GetEmptyData()
    texts = {}
    maps2 = {
			     "English": {},
			     "French": {},
			     "Italian": {},
			     "German": {},
			     "Spanish": {},
			     "Russian": {},
			     "Chinese": {}
			    }
    for language in languages:
        if language == "EnglishUS":
            language = "English"
        execfile("../../SCRIPTS/Combos/" + language + "/PanelMapTextLoca.py")

    for character in maps[languages[0]].keys():
        for m in maps[languages[0]][character].keys():
            key = character + " " + m
            text = ''
            for lang in languages1:
                if lang == "EnglishUS":
                    lang = "English"
                texts = maps[lang][character][m]
                text = text + ',"' + texts[0] + "\n" + texts[1] + '"'
            f.write(key + text + '\n')

            text = ''
            for lang in languages2:
                if lang == "EnglishUS":
                    lang = "English"
                texts = maps[lang][character][m]
                text = text + '"' + texts[0] + ' ' + texts[1] + '",'
            f2.write(text + '\n')

    for m in maps2[languages[0]].keys():
        text = ''
        for lang in languages1:
            if lang is "EnglishUS":
                lang = "English"
            texts = maps2[lang][m]
            text = text + ',"' + texts[0] + "\n" + texts[1] + '"'
        f.write(m + text + '\n')

        text = ''
        for lang in languages2:
            if lang is "EnglishUS":
                lang = "English"
            texts = maps2[lang][m]
            text = text + '"' + texts[0] + ' ' + texts[1] + '",'
        f2.write(text + '\n')
    f.close()
    f2.close()

######################## Secrets ########################
def generateSecrets():
    f=open("../../Localization/secrets.csv", "w")
    f2=open("../../Localization/secrets2.csv", "w")
    f.write(getLanguagesHeaderFromLanguages(languages1, 1))
    f2.write(getLanguagesHeaderFromLanguages(languages2, 0))
    secrets = {
			     "English": {},
			     "French": {},
			     "Italian": {},
			     "German": {},
			     "Spanish": {},
			     "Russian": {},
			     "Chinese": {}
			    }
    for language in languages:
        if language == "EnglishUS":
            language = "English"
        execfile("../../SCRIPTS/Combos/" + language + "/PanelSecretsLoca.py")

    for secret in secrets[languages[0]].keys():
        text = ''
        for lang in languages1:
            if lang is "EnglishUS":
                lang = "English"
            text = text + ',"' + secrets[lang][secret][0] + '"'
        f.write(secret + text + '\n')

        text = ''
        for lang in languages2:
            if lang is "EnglishUS":
                lang = "English"
            text = text + '"' + secrets[lang][secret][0] + '",'
        f2.write(text + '\n')
    f.close()
    f2.close()

######################## Abilities ########################
def generateAbilities():
    f=open("../../Localization/abilities.csv", "w")
    f.write(getLanguagesHeader())
    abilities = PanelFillerCommon.GetEmptyData()
    for language in languages:
        if language == "EnglishUS":
            language = "English"
        execfile("../../SCRIPTS/Combos/" + language + "/PanelAbilitiesLoca.py")

    for character in abilities[languages[0]].keys():
        for ability in abilities[languages[0]][character].keys():
            key = character + " " + ability
            text = ''
            for lang in languages:
                if lang == "EnglishUS":
                    lang = "English"
                texts = abilities[lang][character][ability]
                text = text + ',"'
                for t in texts:
                    text = text + t + "\n"
                text = text + '"'
            f.write(key + text + '\n')
    f.close()

######################## Buttons ########################
def generateButtons():
    f=open("../../Localization/buttons.csv", "w")
    f2=open("../../Localization/buttons2.csv", "w")
    f.write(getLanguagesHeaderFromLanguages(languages1, 1))
    f2.write(getLanguagesHeaderFromLanguages(languages2, 0))
    buttons = {
			     "English": {},
			     "French": {},
			     "Italian": {},
			     "German": {},
			     "Spanish": {},
			     "Russian": {},
			     "Chinese": {}
			    }
    for language in languages:
        if language == "EnglishUS":
            language = "English"
        execfile("../../SCRIPTS/Combos/" + language + "/PanelButtonsLoca.py")

    text = ''
    for lang in languages:
        if lang is "EnglishUS":
            lang = "English"
        texts = buttons[lang]
        text = text + ',"'
        for t in texts:
            text = text + t + "\n"
        text = text + '"'
    f.write("Button" + text)
    f.close()

######################## Specials ########################
def generateSpecials():
    f=open("../../Localization/specials.csv", "w")
    f.write(getLanguagesHeader())
    specials = PanelFillerCommon.GetEmptyData()
    Reference.DefaultSelectionData = {}

    for language in languages:
        if language == "EnglishUS":
            language = "English"
        execfile("../../DATA/ObjIds/" + language + ".py")
        execfile("../../SCRIPTS/Combos/" + language + "/PanelSpecialsLoca.py")

    for character in specials[languages[0]].keys():
        for special in specials[languages[0]][character].keys():
            print specials[languages[0]][character].keys()
            key = character + " " + special
            text = ''
            for lang in languages:
                if lang == "EnglishUS":
                    lang = "English"
                texts = specials[lang][character][special]
                text = text + ',"'
                for t in texts:
                    text = text + str(t) + "\n"
                text = text + '"'
            f.write(key + text + '\n')
    f.close()

######################## Combos Panel ########################
def generateComboPanels():
    f=open("../../Localization/combosPanel.csv", "w")
    f.write(getLanguagesHeader())
    combos = PanelFillerCommon.GetEmptyData()

    for language in languages:
        if language == "EnglishUS":
            language = "English"
        execfile("../../SCRIPTS/Combos/" + language + "/PanelCombosLoca.py")

    for character in combos[languages[0]].keys():
        for combo in combos[languages[0]][character].keys():
            key = character + " " + combo
            text = ''
            for lang in languages:
                if lang == "EnglishUS":
                    lang = "English"
                texts = combos[lang][character][combo]
                text = text + ',"'
                for t in texts:
                    text = text + str(t) + "\n"
                text = text + '"'
            f.write(key + text + '\n')
    f.close()

generateSpecials()

print "Generate done !"