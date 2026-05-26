import Bladex
import BUIx
import Language
import string
import PanelFillerCommon
from PanelFillerCommon import relative, relativev, center, bottom, left, right, buttonOffset, buttonTextPosition


maps = PanelFillerCommon.GetEmptyData()
maps2 = {}

for lang in Language.ExistingLanguages:
	maps2[lang] = {}

def FillMapText(parent):
	titleOffset = [0.5,0.3]
	textOffset = [0.5,0.5]
	global MapTextWidget
	charKind = Bladex.GetEntity("Player1").Kind
	mapName = string.lower(Bladex.GetCurrentMap())
	PanelFillerCommon.SetParentScale(parent)

	widget = parent
	language = PanelFillerCommon.GetLanguageFallback()

	global maps
	global maps2
	execfile("../../SCRIPTS/Combos/" + language + "/PanelMapTextLoca.py")

	if language in maps.keys() and charKind in maps[language].keys():
		if mapName == "tower_m16":
			inv = Bladex.GetEntity("Player1").GetInventory()
			for i in range(inv.nWeapons):
				if (Bladex.GetEntity(inv.GetWeapon(i)).Kind == "BladeSword2") or (Bladex.GetEntity(inv.GetWeapon(i)).Kind == "BladeSword2Barbarian"):
					mapName = "contower_m16"
				else:
					mapName = "sintower_m16"
		if string.find(mapName,"_back") != -1:
			mapName = getOriginalMapName(mapName)
		if mapName in maps[language][charKind].keys():
			texts = maps[language][charKind][mapName]
		else:
			texts = maps2[language][mapName]

	for text in texts:

		if text == texts[0]:
			elem = "Title"
			name = language + charKind + mapName + elem
			font = PanelFillerCommon.CheckFontChineseFallback(elem)
			MapTextWidget=PanelFillerCommon.InitWidget(widget, name, text, font, elem, BUIx.B_TextWidget.B_TEXT_HCenter, [255, 200, 0], 2)
			alignY = center
			alignX = center

			currOffset = titleOffset
			currOffset[0] = PanelFillerCommon.CorrectPosX(currOffset[0])
			currOffset[1] = PanelFillerCommon.CorrectPosY(currOffset[1])
			widget.AddWidget(MapTextWidget,currOffset[0],currOffset[1],relative,alignX,relativev,alignY)
		else:
			elem = "Text"
			name = language + charKind + mapName + elem
			font = PanelFillerCommon.CheckFontChineseFallback(elem)

			scale = 1

			if Bladex.IsRunningOnSteamDeck():
				scale = 1.25

			MapTextWidget=PanelFillerCommon.InitWidget(widget, name, text, font, elem, BUIx.B_TextWidget.B_TEXT_HCenter, [255, 255, 200], scale, 750)

			alignY = center
			alignX = center

			currOffset = textOffset
			currOffset[0] = PanelFillerCommon.CorrectPosX(currOffset[0])
			currOffset[1] = PanelFillerCommon.CorrectPosY(currOffset[1])
			widget.AddWidget(MapTextWidget,currOffset[0],currOffset[1],relative,alignX,relativev,alignY)

def getOriginalMapName(name):
	if name == "btomb_back":
		return "btomb_m12"
	if name == "desert_back":
		return "desert_m13"
	if name == "ice_back":
		return "ice_m11"
	if name == "labyrinth_back":
		return "labyrinth_m6"
	if name == "mine_back":
		return "mine_m5"
	if name == "palace_back":
		return "palace_m15"
	if name == "tomb_back":
		return "tomb_m7"
		
