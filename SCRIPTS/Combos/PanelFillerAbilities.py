import Bladex
import Language
import PanelFillerCommon
import BUIx
from PanelFillerCommon import relative, relativev, center, bottom, left, right, buttonOffset, buttonTextPosition

AbilitiesCombosAmz = ["${AttackIcon:Attack} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}", "${Left:UseAndLeftRight}${Down}${Right:ignore}"]
AbilitiesCombosBarb = ["${AttackIcon:Attack}${Right} ${PlusIcon} ${AttackIcon:Attack}${Right}", "${JumpIcon:JumpAndSelectObj}${Right} ${PlusIcon} ${AttackIcon:Attack}", "${JumpIcon:JumpAndSelectObj}${Left} ${PlusIcon} ${AttackIcon:Attack}", "${Left:UseAndLeftRight}${Down}${Right:ignore}", "${AttackIcon:Attack}${Left} ${PlusIcon} ${AttackIcon:Attack}${Left}", "${AttackIcon:Attack}${Down} ${PlusIcon} ${AttackIcon:Attack}${Down}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${AttackIcon:Attack}${Up}", "${AttackIcon:Attack} ${PlusIcon} ${Up}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}", "${AttackIcon:Attack} ${PlusIcon} ${Up} ${PlusIcon} ${AttackIcon:Attack}"]
AbilitiesCombosDwarf = ["${JumpIcon:JumpAndSelectObj}${Right} ${PlusIcon} ${AttackIcon:Attack}", "${JumpIcon:JumpAndSelectObj}${Left} ${PlusIcon} ${AttackIcon:Attack}", "${Left:UseAndLeftRight}${Down}${Right:ignore}", "${AttackIcon:Attack} ${PlusIcon} ${Left:ignore}${Right:ignore}${ignore:UseAndLeftRight}"]
AbilitiesCombosKgt = ["${JumpIcon:JumpAndSelectObj}${Right} ${PlusIcon} ${AttackIcon:Attack}", "${JumpIcon:JumpAndSelectObj}${Left} ${PlusIcon} ${AttackIcon:Attack}", "${AttackIcon:Attack} ${PlusIcon} ${Down:ignore}${Up:ignore}${ignore:Turn Around}", "${Left:UseAndLeftRight}${Down}${Right:ignore}", "${AttackIcon:Attack}${Right} ${PlusIcon} ${AttackIcon:Attack}${Right}", "${AttackIcon:Attack}${Left} ${PlusIcon} ${AttackIcon:Attack}${Left}", "${AttackIcon:Attack}${Down} ${PlusIcon} ${AttackIcon:Attack}${Down}", "${AttackIcon:Attack}${Up} ${PlusIcon} ${AttackIcon:Attack}${Up}", "${AttackIcon:Attack} ${PlusIcon} ${Down:ignore}${Up:ignore}${ignore:Turn Around} ${PlusIcon} ${AttackIcon:Attack}"]

tilePosition = [
[0.31, 0.275], [0.31, 0.356], [0.31, 0.443], [0.31, 0.534], [0.31, 0.616], [0.31, 0.696],
[0.515, 0.275], [0.515, 0.361],  [0.515, 0.449], [0.515, 0.534], [0.515, 0.616], [0.515, 0.696]
]

titleOffset = [0,-0.008] # center
attackOffset = [0.027, -0.029] # left
comboOffset = [0.029, 0.011] # left
levelOffset = [0.173, 0.027] # right

abilities = PanelFillerCommon.GetEmptyData()
elemToDisplay = ["Title", "Attack", "Level", "Combo"]
textOutOfFrame = []

def FillTextOutOfFrame():
	charKind = Bladex.GetEntity("Player1").Kind
	language = PanelFillerCommon.GetLanguageFallback()
	if charKind == "Knight_N":
		if language == "Spanish":
			textOutOfFrame.append(abilities["Spanish"]["Knight_N"]["Attack"][1])
		if language == "Italian":
			textOutOfFrame.append(abilities["Italian"]["Knight_N"]["Attack"][0])
			textOutOfFrame.append(abilities["Italian"]["Knight_N"]["Attack"][1])
		if language == "Portugese":
			textOutOfFrame.append(abilities["Portugese"]["Knight_N"]["Attack"][0])
			textOutOfFrame.append(abilities["Portugese"]["Knight_N"]["Attack"][1])
		if language == "Russian":
			textOutOfFrame.append(abilities["Russian"]["Knight_N"]["Attack"][0])
	elif charKind == "Dwarf_N":
		if language == "Spanish":
			textOutOfFrame.append(abilities["Spanish"]["Dwarf_N"]["Attack"][1])
		if language == "Italian":
			textOutOfFrame.append(abilities["Italian"]["Dwarf_N"]["Attack"][0])
			textOutOfFrame.append(abilities["Italian"]["Dwarf_N"]["Attack"][1])
		if language == "Polish":
			textOutOfFrame.append(abilities["Polish"]["Dwarf_N"]["Attack"][0])
			textOutOfFrame.append(abilities["Polish"]["Dwarf_N"]["Attack"][1])
		if language == "Russian":
			textOutOfFrame.append(abilities["Russian"]["Dwarf_N"]["Attack"][0])
		if language == "Portugese":
			textOutOfFrame.append(abilities["Portugese"]["Dwarf_N"]["Attack"][0])
			textOutOfFrame.append(abilities["Portugese"]["Dwarf_N"]["Attack"][1])
	elif charKind == "Barbarian_N":
		if language == "Spanish":
			textOutOfFrame.append(abilities["Spanish"]["Barbarian_N"]["Attack"][2])
		if language == "French":
			textOutOfFrame.append(abilities["French"]["Barbarian_N"]["Attack"][1])
			textOutOfFrame.append(abilities["French"]["Barbarian_N"]["Attack"][2])
			textOutOfFrame.append(abilities["French"]["Barbarian_N"]["Attack"][5])
		if language == "Polish":
			textOutOfFrame.append(abilities["Polish"]["Barbarian_N"]["Attack"][2])
		if language == "Italian":
			textOutOfFrame.append(abilities["Italian"]["Barbarian_N"]["Attack"][1])
			textOutOfFrame.append(abilities["Italian"]["Barbarian_N"]["Attack"][2])
		if language == "Portugese":
			textOutOfFrame.append(abilities["Portugese"]["Barbarian_N"]["Attack"][1])
			textOutOfFrame.append(abilities["Portugese"]["Barbarian_N"]["Attack"][2])
		if language == "Russian":
			textOutOfFrame.append(abilities["Russian"]["Barbarian_N"]["Attack"][1])

def FillAbilitiesText(parent):
	global AbilitiesWidget
	charKind = Bladex.GetEntity("Player1").Kind
	PanelFillerCommon.SetParentScale(parent)

	widget = parent
	language = PanelFillerCommon.GetLanguageFallback()
	global abilities
	execfile("../../SCRIPTS/Combos/" + language + "/PanelAbilitiesLoca.py")
	FillTextOutOfFrame()
	for elem in elemToDisplay:
		index = 0
		if elem == "Combo":
			if charKind == "Amazon_N":
				texts = AbilitiesCombosAmz
			elif charKind == "Barbarian_N":
				texts = AbilitiesCombosBarb
			elif charKind == "Dwarf_N":
				texts = AbilitiesCombosDwarf
			else:
				texts = AbilitiesCombosKgt
		else:
			texts = abilities[language][charKind][elem]
		for text in texts:
			scale = 1
			name = language + charKind + elem + str(index)
			font = PanelFillerCommon.CheckFontChineseFallback(elem)
			if textOutOfFrame.count(text) > 0:
				scale = 0.8
			AbilitiesWidget=PanelFillerCommon.InitWidget(widget, name, text, font, elem, BUIx.B_TextWidget.B_TEXT_Left, [255, 255, 255], scale)
			alignY = bottom
			alignX = left
			if elem == "Attack":
				AbilitiesWidget.SetColor(238,225,183)
				currOffset = attackOffset
			elif elem == "Level":
				AbilitiesWidget.SetColor(141,215,251)
				currOffset = levelOffset
				alignX = right
			elif elem == "Title":
				currOffset = titleOffset
				alignX = center
				alignY = center
			elif elem == "Combo":
				currOffset = comboOffset
			
			if index >= len(tilePosition):
				break

			posX = tilePosition[index][0] + currOffset[0]
			posY = tilePosition[index][1] + currOffset[1]
			if elem == "Level":
				posX = PanelFillerCommon.CheckBarbRightLevelOffset(index, posX)

			posX = PanelFillerCommon.CorrectPosX(posX)
			posY = PanelFillerCommon.CorrectPosY(posY)
			widget.AddWidget(AbilitiesWidget,posX,posY,relative,alignX,relativev,alignY)
			index = index + 1
