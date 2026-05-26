

import BBLib
import os


#Current = "Spanish"
#Current = "English"
Current = BBLib.GetCurrentLanguage()

ExistingLanguages = ["English", "Spanish", "French", "Italian", "German", "Chinese", "Russian", "Japanese", "Korean", "Portugese", "Polish"]
# ExistingLanguages = ["English"]

if Current == "EnglishUS":
    Current = "English"

if Current == "Chinese":
    MapaDeLetras = "../../Data/fontCN32.fnt"
    MapaDeLetrasHi = "../../Data/fontCN42.fnt"
    LetrasMenu = "../../Data/fontCN18.fnt"
    LetrasMenuSmall="../../Data/fontCN32.fnt"
    LetrasMenuBig="../../Data/fontCN32.fnt"
    MenuGrasHi="../../Data/fontCN72.fnt"
    CtrlMenu="../../Data/fontCN16.fnt"
elif Current == "Russian":
    MapaDeLetras = "../../Data/fontRu16.fnt"
    MapaDeLetrasHi = "../../Data/fontRu32.fnt"
    LetrasMenu = "../../Data/fontRu16.fnt"
    LetrasMenuSmall="../../Data/fontRu16.fnt"
    LetrasMenuBig="../../Data/fontRu30.fnt"
    MenuGrasHi="../../Data/fontRu100.fnt"
elif Current == "Korean":
    MapaDeLetras = "../../Data/fontKo16.fnt"
    MapaDeLetrasHi = "../../Data/fontKo32.fnt"
    LetrasMenu = "../../Data/fontKo16.fnt"
    LetrasMenuSmall="../../Data/fontKo16.fnt"
    LetrasMenuBig="../../Data/fontKo32.fnt"
    MenuGrasHi="../../Data/fontKo100.fnt"
elif Current == "Japanese":
    MapaDeLetras = "../../Data/fontJp16.fnt"
    MapaDeLetrasHi = "../../Data/fontJp32.fnt"
    LetrasMenu = "../../Data/fontJp16.fnt"
    LetrasMenuSmall="../../Data/fontJp16.fnt"
    LetrasMenuBig="../../Data/fontJp32.fnt"
    MenuGrasHi="../../Data/fontJp100.fnt"
else:
    MapaDeLetras = "../../Data/liberationSansBI16.fnt"
    MapaDeLetrasHi = "../../Data/liberationSansBI32.fnt"
    LetrasMenu = "../../Data/fontLatin16.fnt"
    LetrasMenuSmall="../../Data/fontLatin16.fnt"
    LetrasMenuBig="../../Data/fontLatin32.fnt"
    MenuGrasHi="../../Data/fontLatin100.fnt"

def CheckFallback():
    if not os.path.exists("../../SOUNDS/"+Current+"/kashgar-antepasados.ogg"):
        return "English"
    return Current

def GetTranslatedLanguages():
    import MenuText
    result = []
    for i in range(0,len(ExistingLanguages)):
        result.append(MenuText.GetMenuText(ExistingLanguages[i]))
    return result

def IsCurrentLanguageAsian():
    return Current == "Korean" or Current == "Japanese" or Current == "Chinese"

