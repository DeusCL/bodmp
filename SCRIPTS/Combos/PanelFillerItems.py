import Bladex
import BUIx
import Language
import string
import PanelFillerCommon
from PanelFillerCommon import relative, relativev, center, bottom, left, right, buttonOffset, buttonTextPosition

tilePosition = [
[0.31, 0.249], [0.31, 0.3], [0.31, 0.351], [0.31, 0.402], [0.31, 0.453], [0.31, 0.504], [0.31, 0.555], [0.31, 0.606], [0.31, 0.657], [0.31, 0.708],
[0.520, 0.249], [0.520, 0.3],  [0.520, 0.351], [0.520, 0.402], [0.520, 0.453], [0.520, 0.504], [0.520, 0.555], [0.520, 0.606], [0.520, 0.657], [0.520, 0.708]
]

nameOffset = [0.008,-0.005]
effectOffset = [0.008, 0.012]
effectOffset2 = [0.008, 0.0115]
infoOffset = [0.18, 0.021]
infoOffset2 = [0.19, 0.021]
infoOffset3 = [0.19, -0.01]
effectScale = 0.45

items = {}
elemToDisplay = ["name", "effect", "info"]

for lang in Language.ExistingLanguages:
	items[lang] = {}

def fillItemsText(parent):
	PanelFillerCommon.SetParentScale(parent)

	widget = parent
	language = PanelFillerCommon.GetLanguageFallback()
	execfile("../../SCRIPTS/Combos/" + language + "/PanelItemsLoca.py")

	for elem in elemToDisplay:
		for i in range(1, 20):
			name = language + elem + str(i)
			font = PanelFillerCommon.CheckFontChineseFallback(elem)
			try:
				text = items[language]["item_" + str(i) + "_" + str(elem)][0]
			except:
				continue
			ItemsWidget=PanelFillerCommon.InitWidget(widget, name, text, font, elem)
			alignY = bottom
			alignX = left
			if elem == "name":
				ItemsWidget.SetColor(255,255,255)
				currOffset = nameOffset
			elif elem == "effect":
				if i < 13:
					ItemsWidget.SetColor(253,251,1)
					currOffset = effectOffset
				else:
					ItemsWidget.SetColor(23,254,140)
					currOffset = effectOffset2
			elif elem == "info":
				ItemsWidget.SetColor(117,207,247)
				if i <= 10:
					currOffset = infoOffset
				else:
					if i == 14 or (i == 12 and Language.Current == "Russian"):
						currOffset = infoOffset3
					else:
						currOffset = infoOffset2
				alignX = right

			posX = tilePosition[i-1][0] + currOffset[0]
			posX = PanelFillerCommon.CorrectPosX(posX)
			posY = tilePosition[i-1][1] + currOffset[1]
			posY = PanelFillerCommon.CorrectPosY(posY)

			widget.AddWidget(ItemsWidget,posX,posY,relative,alignX,relativev,alignY)