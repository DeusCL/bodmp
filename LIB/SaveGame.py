import MenuText
import Bladex
import netwidgets
import MenuWidget
import os
import time
import string
import Reference
import AuxFuncs
import stat

EMPTY_SLOT  = MenuText.GetMenuText("<Empty Slot>")
DATE_FORMAT = MenuText.GetMenuText("%d/%m %H:%M")
SaveCounter = []

for i in range(2):
        SaveCounter.append("Awesome!")

for i in range(3):
        SaveCounter.append("Heroic")

for i in range(4):
        SaveCounter.append("Bold")

for i in range(5):
        SaveCounter.append("Normal")

for i in range(6):
        SaveCounter.append("Cautious")

for i in range(7):
        SaveCounter.append("Overcautious")

SaveCounter.append("Lame")
#
# Utils to save/load games.
#

def ElUsuarioPresionaLaTeclaEscape(Salio):
    return 1


def LoadGameAux(name):
	import Language
	import SplashImage

	SavePath = "../../Save/"
	path = SavePath + "%s_files"%(name,)
	ListDir = GetListDir(SavePath)
	cad = "save" + name[-1:] + ".pak"
	if cad in ListDir:
		execfile="execfile('../../Scripts/sys_init.py');execfile('%s/SaveGame.py');execfile('../../Scripts/after_load.py');"%(path,)
	else:
		execfile="execfile('../../Scripts/sys_init.py');execfile('../../Save/%s.py');execfile('../../Scripts/after_load.py');"%(name,)

	file_data_aux=open("%s/%saux"%(path,"aux"),"rt")
	text=file_data_aux.read()
	print text
	file_data_aux.close()
	scr_name="../../Data/Menu/Save/Cerrando_hi_empty.jpg"
	SplashImage.ShowImage(scr_name,0)
	Bladex.BeginLoadGame()
	Bladex.CloseLevel(execfile,text)

def LoadGameFromDisk(menu_class):
	LoadGameAux("SaveGame"+menu_class.MenuDescr["Clave"])

def SaveGameToDisk(menu_class):
	import Menu
	import Scorer
	import MenuText
	import GameText
	import GotoMapVars

	global SaveGameString

	# Back to game
	try:
		Menu._MainMenu.DeActivateMenuItem()
		Menu._MainMenu.DeActivateMenuItem()
		Menu._MainMenu.DeActivateMenuItem()
		Menu._MainMenu.DeActivateMenuItem()
	except:
		pass


	# :TRICKY: This file keeps the save partition open for the complete duration of
	# the save operation
	# At closure, the stdio replacement will commit all the changes to the save partition
	print "Start saving"
	sentinel = Bladex.CreateSentinel("../../Save/sentinel")

	# save aditional data
	file = open("../../Save/SaveGame"+menu_class.MenuDescr["Clave"] + "_files/SaveGame.sv","w")

	char = Bladex.GetEntity("Player1")
	if char.Kind[0] =="K":
		cad = MenuText.GetMenuText("Knight")
	if char.Kind[0] =="B":
		cad = MenuText.GetMenuText("Barbarian")
	if char.Kind[0] =="D":
		cad = MenuText.GetMenuText("Dwarf")
	if char.Kind[0] =="A":
		cad = MenuText.GetMenuText("Amazon")

	cadtime = time.strftime(DATE_FORMAT,time.localtime(time.time()))

	cad = `char.Level+1`+ " " + MenuText.GetMenuText("Lv.")+ " " +cad+" "+" - "+cadtime+" - "
	cad = cad + GameText.MapDescriptor(Bladex.GetCurrentMap())
	Reference.TimesSaved = Reference.TimesSaved+1

	nMaps = 1
	for v in GotoMapVars.VisitedMaps:
		if v:
			nMaps = nMaps + 1

	vismap = (Reference.TimesSaved-1)/nMaps

	if vismap >= len(SaveCounter):
	    DisgustingMessage = SaveCounter[(len(SaveCounter)-1)]
	else:
	    DisgustingMessage = SaveCounter[vismap]
	cad = cad + " - "+`Reference.TimesSaved`+" ("+MenuText.GetMenuText(DisgustingMessage)+")"
	file.write(cad)
	file.close()
	print cad

	# save Screen shoot
	Scorer.SetVisible(0)
	Bladex.SaveScreenShot('../../Save/SaveGame'+menu_class.MenuDescr["Clave"]+'_files/screenshot.BMP',160,120)
	SaveGameString = "import os;import GameState;state=GameState.WorldState();state.GetState();state.SaveState('../../Save/SaveGame"+menu_class.MenuDescr["Clave"]+"_files/SaveGame.py');state=None;GameState=None;"

	# Save the game
	Bladex.PauseSoundSystem()
	Bladex.StopTime()
	Bladex.SetRunString(SaveGameString+"os.close("+`sentinel`+");Scorer.SetVisible(1);Bladex.RestartTime();Bladex.ResumeSoundSystem()")

def GetBack(menu_class):
	import Menu
	Menu._MainMenu.DeActivateMenuItem()


SaveBitmaps = 	(
			("1"    , "../../SaveGame1_files/screenshot.BMP"   ),
			("2"    , "../../SaveGame2_files/screenshot.BMP"   ),
			("3"    , "../../SaveGame3_files/screenshot.BMP"   ),
			("4"    , "../../SaveGame4_files/screenshot.BMP"   ),
			("5"    , "../../SaveGame5_files/screenshot.BMP"   ),
			("6"    , "../../SaveGame6_files/screenshot.BMP"   ),
			("7"    , "../../SaveGame7_files/screenshot.BMP"   ),
			("8"    , "../../SaveGame8_files/screenshot.BMP"   ),
		)

SAVEGAMEIMAGE = "0"
LOADGAMEIMAGE = "0"

def GetSaveGameImage():
	return SAVEGAMEIMAGE

def GetLoadGameImage():
	return LOADGAMEIMAGE


def FocusOnBitmap(menu_class=0,parametro=0):
	netwidgets.ChangePlayer(menu_class.MenuDescr["Clave"])


# called when the menu is called
def CreateSaveMenu():
	import Menu
	import GameText

	index = InspectSaveList()

	if AllEmpty and  not GameText.MapList.has_key(string.upper(Bladex.GetCurrentMap())):
		try:
			Menu.GetMenuItem    (['GAME','LOAD GAME'])['Kind'     ] = MenuWidget.B_MenuItemTextNoFXNoFocus
		except:
			pass
		try:
			del Menu.GetMenuItem(['GAME','LOAD GAME'])['ListDescr']
		except:
			pass
	else:
		try:
			CreateMenu('LOAD GAME',0)
		except:
			pass
		try:
			del Menu.GetMenuItem    (['GAME','LOAD GAME'])['Kind'     ]
		except:
			pass

	if (Bladex.GetEntity("Player1").Life <= 0) or not GameText.MapList.has_key(string.upper(Bladex.GetCurrentMap())):
		try:
			Menu.GetMenuItem    (['GAME','SAVE GAME'])['Kind'     ] = MenuWidget.B_MenuItemTextNoFXNoFocus
		except:
			pass
	else:
		try:
			del Menu.GetMenuItem    (['GAME','SAVE GAME'])['Kind'     ]
		except:
			pass
		try:
			CreateMenu('SAVE GAME',1)
		except:
			pass

		try:
			Menu.GetMenuItem    (['GAME'])['iFocus'] = 1
		except:
			pass

	try:
		if GameText.MapList.has_key(string.upper(Bladex.GetCurrentMap())):
			Menu.GetMenuItem    (['GAME','LOAD GAME'])['iFocus'] = index[0]+1
		else:
			Menu.GetMenuItem    (['GAME','LOAD GAME'])['iFocus'] = index[0]
	except:
		pass

	try:
		Menu.GetMenuItem    (['GAME','SAVE GAME'])['iFocus'] = index[1]
	except:
		pass

def InspectSaveList():
	global SaveBitmaps
	global AllEmpty
	global FirstSaved
	global SAVEGAMEIMAGE
	global LOADGAMEIMAGE

	FirstSaved = None
	AllEmpty = 1

	lasttime       = 0
	indexsel       = 1

	firstime       = 10000000000000.0
	indexselfirst  = 2

	FirstEmptySlot = -1


	SaveBitmaps = []
	path = "../../Save/"

	try:
	    os.mkdir(path)
	except:
	    pass

	ListDir = GetListDir(path)

	for i in range(6):
		PakCad = "save" + `i+1` + ".pak"
		OldCad = `i+1`+".bmp"
		if OldCad in ListDir or PakCad in ListDir:
			if PakCad in ListDir:
				cad = "savegame" + `i+1` + "_files"
				image_name = path+cad+"/screenshot.BMP"
				try:
					file = open(path+cad+"/SaveGame.sv","r")
				except:
					SaveBitmaps.append(`i+1`,"../../Data/Empty.BMP",EMPTY_SLOT)
					if FirstEmptySlot == -1:
						FirstEmptySlot = i+2
					continue

				name = file.readline()
			elif OldCad in ListDir:
				cad = OldCad
				image_name = path+cad
				file = open(path+`i+1`+".sv","r")
				name = file.readline()
			
			file.close()

			try:
				print name
			except:
				SaveBitmaps.append(`i+1`,"../../Data/Empty.BMP",EMPTY_SLOT)
				if FirstEmptySlot == -1:
					FirstEmptySlot = i+2
				continue

			SaveBitmaps.append(`i+1`,image_name,name)
			AllEmpty = 0
			if not FirstSaved:
				FirstSaved = `i+1`
			filetime = os.stat(image_name)[stat.ST_MTIME]
			if lasttime<filetime:
				lasttime = filetime
				indexsel = i+2
			if firstime>filetime:
				firstime      = filetime
				indexselfirst = i+2
		else:
			SaveBitmaps.append(`i+1`,"../../Data/Empty.BMP",EMPTY_SLOT)
			if FirstEmptySlot == -1:
				FirstEmptySlot = i+2

	SaveBitmaps.append("0","../../Data/Empty.BMP",EMPTY_SLOT)
	if FirstEmptySlot == -1:
		FirstEmptySlot = indexselfirst
		SAVEGAMEIMAGE = `indexselfirst-1`
	else:
		SAVEGAMEIMAGE = "0"

	LOADGAMEIMAGE = `indexsel-1`

	return indexsel, FirstEmptySlot

def GetLastSaveIndex():
	lasttime       = 0
	indexsel       = 1
	path = "../../Save/"

	try:
	    os.mkdir(path)
	except:
	    pass

	ListDir = GetListDir(path)

	for i in range(6):
		cad = "savegame" + `i+1` + "_files"
		if cad in ListDir:
			try:
				file = open(path+cad+"/SaveGame.sv","r")
			except:
				continue

			name = file.readline()
			file.close()

			image_name = path+cad+"/screenshot.BMP"

			filetime = os.stat(image_name)[stat.ST_MTIME]
			if lasttime<filetime:
				lasttime = filetime
				indexsel = i+1

	return indexsel

def GetListDir(path):
	ListDir = []
	for filename in os.listdir(path):
		ListDir.append(string.lower(filename))
	return ListDir

def RestartLevel(menu_class):
	Bladex.LoadLevel(Bladex.GetCurrentMap())

def MenuStart(EntityName):
	import AuxFuncs
	Bladex.GetEntity(EntityName).Freeze()
	print EntityName, "is  death"
	if AuxFuncs.FadeActive:
		ActivaMenuDeRegreso()
	else:
		AuxFuncs.FadeTo(1.0,1.0)
		Bladex.AddScheduledFunc(Bladex.GetTime()+1.0,ActivaMenuDeRegreso,())

def ActivaMenuDeRegreso():
	import Menu
	if Bladex.GetEntity("Player1").Life<=0:
		Menu.GetMenuItem(["BACK TO GAME"])['Kind'     ] = MenuWidget.B_MenuItemTextNoFXNoFocus # :TODO: crash with TypeError : expected integer index
		Menu.EscapeFunction = ElUsuarioPresionaLaTeclaEscape

	Menu.Desc1["iFocus"]                 = 0
	Menu.GetMenuItem(['GAME'])["iFocus"] = 2

	Menu.ActivateMenu()
	Menu._MainMenu.ActivateMenuItem()
	Menu._MainMenu.ActivateMenuItem()

def CreateMenu(MenuName,SaveFlag):
	import Menu
	import MenuText
	import GameText
	global EmptyImage

	menuItem = Menu.GetMenuItem(['GAME',MenuName])

	if menuItem == 1:
		return

	Save_Menu = []

	EmptyImage = (not SaveFlag) and GameText.MapList.has_key(string.upper(Bladex.GetCurrentMap()))

	Save_Menu.append(  {"Name"    : MenuText.GetMenuText(MenuName),
	                    "VSep"    : 30,
	                    "Font"    : Menu.MenuFontBig,
	                    "Kind"    : MenuWidget.B_MenuItemTextNoFXNoFocus,
	                     })

	if SaveFlag:
		Save_Menu.append(  {"Name":"GameList",
		                    "Kind":netwidgets.B_ImageListWidget,
		                    "ImageList":SaveBitmaps,
		                    "MaxHeight":90,
		                    "GetCharType":GetSaveGameImage,
		                    "VSep":10
		                   })
	else:
		Save_Menu.append(  {"Name":"GameList",
		                    "Kind":netwidgets.B_ImageListWidget,
		                    "ImageList":SaveBitmaps,
		                    "MaxHeight":90,
		                    "GetCharType":GetLoadGameImage,
		                    "VSep":10
		                   })

	first_offset = 10
	other_offset = 10
	restart_offset = -10

	if Bladex.IsRunningOnSteamDeck():
		first_offset = -50
		other_offset = 0
		restart_offset = -50

	if EmptyImage:
		Save_Menu.append(  {"Name"           : MenuText.GetMenuText("Restart")+' "'+GameText.MapDescriptor(Bladex.GetCurrentMap())+'"',
		                    "VSep"           : restart_offset,
		                    "Clave"          : "0",
		                    "FocusCallBack"  : FocusOnBitmap,
		                    "Font"           : Menu.MenuFontMed,
		                    "Kind"           : MenuWidget.B_MenuItemTextNoFX,
		                    "Command"        : RestartLevel
		                     })


	####################################


	for i in range(6):
		SaveGameName = SaveBitmaps[i][2]
		if SaveFlag:
			val =              {"Name"           : SaveGameName,
			                    "VSep"           : other_offset,
			                    "Font"           : Menu.MenuFontMed,
			                    "FocusCallBack"  : FocusOnBitmap,
			                    "Clave"          : `i+1`,
			                    "iFocus"         : 2,
			                    "ListDescr"      : [
			                                        {"Name":MenuText.GetMenuText("Overwrite a previously saved game?"),
			                                         "VSep":200,
			                                         "Font":Menu.MenuFontBig,
			                                         "Kind":MenuWidget.B_MenuItemTextNoFXNoFocus
			                                        },
			                                        {"Name"    : MenuText.GetMenuText("Yes"),
			                                         "VSep"    : 20,
			                                         "Command" : SaveGameToDisk,
			                                         "Font"    : Menu.MenuFontMed,
			                                         "Clave"   :  `i+1`,
			                                        },
			                                        {"Name":MenuText.GetMenuText("No"),
			                                         "VSep":10,
			                                         "Font":Menu.MenuFontMed,
			                                         "Command" : GetBack
			                                        },
			                                        {"Name":"Back",
			                                         "Kind":MenuWidget.B_BackBlank
			                                        }
			                                      ]
			                     }
			if i == 0:
				val["VSep"] = first_offset
			if SaveGameName == EMPTY_SLOT:
				del val["ListDescr"]
				val["Command"] = SaveGameToDisk
			Save_Menu.append(val)
		else:
			val =              {"Name"           : SaveGameName,
			                    "VSep"           : other_offset,
			                    "Font"           : Menu.MenuFontMed,
			                    "FocusCallBack"  : FocusOnBitmap,
			                    "Clave"          : `i+1`,
			                    "iFocus"         : 2,
			                    "ListDescr"      : [
			                                        {"Name":MenuText.GetMenuText("ARE YOU SURE?"),
			                                         "VSep":200,
			                                         "Font":Menu.MenuFontBig,
			                                         "Kind":MenuWidget.B_MenuItemTextNoFXNoFocus
			                                        },
			                                        {"Name"    : MenuText.GetMenuText("Yes"),
			                                         "VSep"    : 20,
			                                         "Command" : LoadGameFromDisk,
			                                         "Font"    : Menu.MenuFontMed,
			                                         "Clave"   :  `i+1`,
			                                        },
			                                        {"Name":MenuText.GetMenuText("No"),
			                                         "VSep":10,
			                                         "Font":Menu.MenuFontMed,
			                                         "Command" : GetBack
			                                        },
			                                        {"Name":"Back",
			                                         "Kind":MenuWidget.B_BackBlank
			                                        }
			                                       ]
			                     }
			if i == 0 and not EmptyImage:
				val["VSep"] = first_offset


			if SaveGameName == EMPTY_SLOT:
				val["Kind"] = MenuWidget.B_MenuItemTextNoFXNoFocus
			Save_Menu.append(val)

	####################################

	Save_Menu.append(   Menu.BackOption  )
	Save_Menu.append(   {"Name":"Back",
	                     "Kind":MenuWidget.B_BackBlank
	                     })

	menuItem["ListDescr"] = Save_Menu

def LoadLastSave():
	print "LoadLastSave"
	result = GetLastSaveIndex()
	index = str(result)
	print index
	try:
		LoadGameAux("SaveGame" + index)
	except:
		print "No save? Not doing anything"
		# print "No save? Loading BARB_M1"
		# Bladex.LoadLevel("BARB_M1")



