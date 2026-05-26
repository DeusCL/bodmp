import Actions
import MenuText
import MenuWidget
import Language
import Menu
import cheats
import os
import string
import Bladex
import Raster

try:
    import DefFuncs
except:
    pass

MenuFontMed=Language.LetrasMenu
MenuFontBig=Language.LetrasMenuBig

def GoBack(count):
    for i in range(count):
        Menu._MainMenu.DeActivateMenuItem()

def ToggleInvincibility(option):
    Actions.ToggleInvincibility()
    GoBack(2)

def ToggleStats(option):
    Raster.SetRasterParameter("ToggleStats","")

def Teleport1(option):
    DefFuncs.IrPosicion1()
    GoBack(3)

def Teleport2(option):
    DefFuncs.IrPosicion2()
    GoBack(3)

def Teleport3(option):
    DefFuncs.IrPosicion3()
    GoBack(3)

def Teleport4(option):
    DefFuncs.IrPosicion4()
    GoBack(3)

def Teleport5(option):
    DefFuncs.IrPosicion5()
    GoBack(3)

def Teleport6(option):
    DefFuncs.IrPosicion6()
    GoBack(3)

def Teleport7(option):
    DefFuncs.IrPosicion7()
    GoBack(3)

def Teleport8(option):
    DefFuncs.IrPosicion8()
    GoBack(3)

def Teleport9(option):
    DefFuncs.IrPosicion9()
    GoBack(3)

def NextLevel(option):
    cheats.NextLevel()
    GoBack(2)

def LevelUp(option):
    cheats.LevelUp()
    GoBack(2)

def ChangeMap(option):
    name = option.MenuDescr["MapName"]
    Bladex.LoadLevel(name)

def BuildChangeMapDescription():
    result = []

    path = "../"
    first = 1
    for name in os.listdir(path):
        if string.find(name, "_") != -1:
            display_name = string.upper(name)
            display_name = string.replace(display_name, "_", " ")
            sep = 0
            if first:
                sep = 10
                first = 0
            result.append({
                        "Name": display_name,
                        "MapName": name,
                        "Font": MenuFontMed,
                        "VSep": sep,
                        "Command": ChangeMap
                })

    result.append({
                   "Name":"Back",
                   "Kind":MenuWidget.B_BackImageWidget
                })
    return result

def Init(menu_description):
    # :TODO: Early return here for release.
    return

    description = {
    "Name": "DEV / CHEATS",
    "Font": MenuFontBig,
    "VSep": 8,
    # "Command": ToggleInvincibility
    "Size":(640,480),
    "ListDescr":[
        {
            "Name":"Toggle Invincibility",
            "Font": MenuFontBig,
            "VSep": 100,
            "Command": ToggleInvincibility
        },
        {
            "Name":"Teleport",
            "VSep": 8,
            "Font": MenuFontBig,
            "Size":(640,480),
            "ListDescr":[
                {
                    "Name":"Teleport to position 1",
                    "Font": MenuFontBig,
                    "VSep": 100,
                    "Command": Teleport1
                },
                {
                    "Name":"Teleport to position 2",
                    "Font": MenuFontBig,
                    "VSep": 2,
                    "Command": Teleport2
                },
                {
                    "Name":"Teleport to position 3",
                    "Font": MenuFontBig,
                    "VSep": 2,
                    "Command": Teleport3
                },
                {
                    "Name":"Teleport to position 4",
                    "Font": MenuFontBig,
                    "VSep": 2,
                    "Command": Teleport4
                },
                {
                    "Name":"Teleport to position 5",
                    "Font": MenuFontBig,
                    "VSep": 2,
                    "Command": Teleport5
                },
                {
                    "Name":"Teleport to position 6",
                    "Font": MenuFontBig,
                    "VSep": 2,
                    "Command": Teleport6
                },
                {
                    "Name":"Teleport to position 7",
                    "Font": MenuFontBig,
                    "VSep": 2,
                    "Command": Teleport7
                },
                {
                    "Name":"Teleport to position 8",
                    "Font": MenuFontBig,
                    "VSep": 2,
                    "Command": Teleport8
                },
                {
                    "Name":"Teleport to position 9",
                    "Font": MenuFontBig,
                    "VSep": 2,
                    "Command": Teleport9
                },
                {
                   "Name":"Back",
                   "Kind":MenuWidget.B_BackImageWidget
                }
            ]
        },
        {
            "Name":"Complete current map",
            "Font": MenuFontBig,
            "VSep": 8,
            "Command": NextLevel
        },
        {
            "Name":"Level Up",
            "Font": MenuFontBig,
            "VSep": 8,
            "Command": LevelUp
        },
        {
            "Name":"Change map",
            "VSep": 8,
            "Font": MenuFontBig,
            "Size":(640,480),
            "ListDescr":    BuildChangeMapDescription()
        },
        {
            "Name":"Toggle Perf/stats display",
            "Font": MenuFontBig,
            "VSep": 8,
            "Command": ToggleStats
        },
        {
           "Name":"Back",
           "Kind":MenuWidget.B_BackImageWidget
        }
        ]
    }


    menu_description.insert(4, description)
