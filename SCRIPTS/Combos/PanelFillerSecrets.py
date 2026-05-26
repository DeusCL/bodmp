import Bladex
import BUIx
import Language
import string
import PanelFillerCommon
import GotoMapVars
from PanelFillerCommon import relative, relativev, center, bottom, left, right, buttonOffset, buttonTextPosition

textOffset = [0.5,0.5]

secrets = {}

for lang in Language.ExistingLanguages:
	secrets[lang] = {}

def FillSecrets(parent):
	global SecretsWidget
	PanelFillerCommon.SetParentScale(parent)

	inventory = Bladex.GetEntity("Player1").GetInventory()
	secret = ""
	if "ORCMURAL" in GotoMapVars.BaList:
		secret = "muralorc"
	if "ISLANDMURAL" in GotoMapVars.BaList:
		secret = "muralisla1"
	if "NEJEVMURAL" in GotoMapVars.BaList:
		secret = "muralnejev"
	if  "SALATABLILLAS" in GotoMapVars.BaList or (1 in GotoMapVars.PlacedTablets) or (inventory.nTablets > 0):
		secret = "tablillas"

	widget = parent
	language = PanelFillerCommon.GetLanguageFallback()

	global secrets
	execfile("../../SCRIPTS/Combos/" + language + "/PanelSecretsLoca.py")

	if language in secrets.keys() and secret:
		text = secrets[language][secret][0]
		elem = "Text"
		name = language + secret + elem
		font = PanelFillerCommon.CheckFontChineseFallback(elem)
		SecretsWidget=PanelFillerCommon.InitWidget(widget, name, text, font, elem, BUIx.B_TextWidget.B_TEXT_HCenter, [255, 255, 200], 1, 750)
		alignY = center
		alignX = center

		currOffset = textOffset
		currOffset[0] = PanelFillerCommon.CorrectPosX(currOffset[0])
		currOffset[1] = PanelFillerCommon.CorrectPosY(currOffset[1])
		widget.AddWidget(SecretsWidget,currOffset[0],currOffset[1],relative,alignX,relativev,alignY)
