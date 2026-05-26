import BBLib
import BUIx
import Raster
import Language
import ScorerWidgets
import MenuText
import Bladex
import Menu
import MenuWidget
import BInput
import acts
import string

MAX_LENGTH = 32

class B_GamepadWidget(BUIx.B_FrameWidget):

	def __init__(self,Parent,MenuDesc,menuStack):
		self.controller = Bladex.GetLastUsedController()
		if self.controller == 0:
			self.controller = 2
		self.commands = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
		self.FillCommands()
		self.positionU = [[-390, 83], [-390, 146], [-390, 191], [-390, 307], [-390, 356], [-390, 405], [-390, 453], [-110, 522], [-110, 562], [110, 562], [110, 522], [360, 354], [360, 327], [360, 299], [360, 271], [380, 191], [380, 146], [380, 83]]

		self.positionX = [[-360, 83], [-380, 156], [-380, 198], [-380, 410], [-380, 449], [-380, 490], [-380, 532], [-380, 280], [-380, 330], [110, 563], [110, 523], [360, 349], [360, 322], [360, 295], [360, 267], [380, 198], [380, 156], [360, 83]]

		self.positionP = [[-390, 90], [-380, 146], [-380, 185], [-380, 283], [-380, 332], [-380, 381], [-380, 430], [-110, 522], [-110, 562], [110, 562], [110, 522], [360, 352], [360, 323], [360, 296], [360, 269], [380, 185], [380, 146], [370, 87]]

		self.positionS = [[-400, 289], [-420, 197], [-420, 228], [-400, 353], [-400, 395], [-400, 437], [-400, 482], [-270, 150], [-270, 108], [270, 108], [270, 150], [380, 451], [380, 420], [380, 351], [380, 386], [420, 228], [420, 197], [400, 289]]

		self.positionSW = [[-360, 89], [-395, 196], [-395, 146], [-385, 380], [-385, 430], [-385, 480], [-385, 530], [-385, 257], [-385, 302], [385, 440], [385, 395], [370, 334], [370, 306], [370, 278], [370, 250], [395, 146], [395, 196], [360, 89]]

		self.positionSWP = [[-365, 89], [-395, 192], [-395, 146], [-385, 358], [-385, 408], [-385, 458], [-385, 508], [-385, 250], [-385, 295], [385, 454], [385, 409], [370, 331], [370, 303], [370, 275], [370, 247], [395, 146], [395, 192], [370, 89]]
		self.PanelWidgets = []
		self.PanelWidgetsName = []
		self.vidw = 1
		self.vidh = 1
		self.controllerScale = 0.8
		BUIx.B_FrameWidget.__init__(self,Parent,MenuDesc["Name"],self.vidw,self.vidh)
		Size_X, Size_Y = Raster.GetUnscaledSize()
		Parent.SetSize(Size_X, Size_Y)
		self.DisplayController()
		self.gamepad = Raster.BmpHandle(self.gamepadName)
		Raster.SetPenColor(255,255,255);
		self.SetCommandTexts()
		self.SetDrawFunc(self.Draw)

		def MyGamepadChange(controllerType,widget=self):
			widget.OnGamepadChange(controllerType)

		Bladex.SetGamepadChangeFunc(MyGamepadChange)

	def OnGamepadChange(self,controllerType):
		self.controller = int(controllerType)
		self.DisplayController()
		self.SetCommandTexts()
		self.gamepad = Raster.BmpHandle(self.gamepadName)

	def DisplayController(self):
		if self.controller == 1:
			controllerStr = "Universal"
			self.positions = self.positionU
		elif self.controller == 3:
			controllerStr = "Playstation"
			self.positions = self.positionP
		elif self.controller == 4:
			controllerStr = "Playstation5"
			self.positions = self.positionP
		elif self.controller == 5:
			controllerStr = "Steamdeck"
			self.positions = self.positionS
		elif self.controller == 6:
			controllerStr = "Switch01"
			self.positions = self.positionSW
		elif self.controller == 7:
			controllerStr = "Switch02"
			self.positions = self.positionSWP
		elif self.controller == 9:
			controllerStr = "XboxSerieX"
			self.positions = self.positionX
		else:
			controllerStr = "Xbox"
			self.positions = self.positionX
		self.gamepadName = "gamepad" + str(self.controller)
		Bladex.ReadBitMap("../../DATA/LayoutController_" + controllerStr + ".png", self.gamepadName)

	def Draw(self,x,y,time):
		Size_X, Size_Y = Raster.GetSize()
		scale = (1.0 * Size_Y) / 1080.0
		image_height = Size_Y * self.controllerScale
		image_width = 1920.0 / (1080.0 / image_height)
		Raster.SetPenColor(255,255,255);
		Raster.SetPosition(Size_X/2 - image_width/2, Size_Y/2 - image_height/2 - image_height * 0.2)
		Raster.DrawBitmap(self.gamepad, image_width, image_height)
		self.DefDraw(x,y,time)

	def ResetTexts(self):
		for elem in self.PanelWidgetsName:
			self.RemoveWidget_Idx(0)

		self.PanelWidgets = []
		self.PanelWidgetsName = []
	def SetCommandTexts(self):
		self.ResetTexts()
		Size_X, Size_Y = Raster.GetSize()
		scale = 1
		if Size_Y < 800:
			scale = Size_Y / 800.0
		index = 0
		for pos in self.positions:
			textAlign = BUIx.B_FrameWidget.B_FR_Right
			if index >= (len(self.positions)/2):
				textAlign = BUIx.B_FrameWidget.B_FR_Left
			name = "command " + str(index)
			Widget=BUIx.B_TextWidget(self, name,"",ScorerWidgets.font_server,Menu.MenuFontMed)

			if Bladex.IsRunningOnSteamDeck():
				Widget.SetScale(0.55)

			Widget.SetAlpha(1)
			Widget.SetColor(207,144,49)
			commandText = MenuText.GetMenuText(self.commands[index])
			commandTextLength = len(commandText)
			if commandTextLength > MAX_LENGTH:
				commandText = commandText[:commandTextLength/2] + string.replace(commandText[commandTextLength/2:], " ", "\n", 1)
			Widget.SetText(commandText)
			self.PanelWidgets.append(Widget)
			self.PanelWidgetsName.append(name)
			self.AddWidget(
					Widget,
					pos[0] * scale,
					pos[1] * scale,
					BUIx.B_FrameWidget.B_FR_HRelative,
					textAlign,
					BUIx.B_FrameWidget.B_FR_VRelative,
					BUIx.B_FrameWidget.B_FR_HCenter
					)
			index = index + 1

	def FillCommands(self):
		IManager = BInput.GetInputManager()
		oldInputActionsSet = IManager.GetInputActionsSet()
		IManager.SetInputActionsSet("Default")
		IActions=IManager.GetInputActions()
		for i in acts.ConfigurableActions:
			IAction=IActions.Find(i[1])
			for j in range(IAction.nInputEvents()):
				IEvent=IAction.GetnInputEvent(j)
				IDevice=IEvent.GetDevice()
				IAction=IActions.Find(i[1])
				if IDevice == "Gamepad" :
					if self.GetCommandIndex(IEvent.GetKey()):
						self.commands[self.GetCommandIndex(IEvent.GetKey())] = MenuText.GetMenuText(i[0])

		self.commands[0] = MenuText.GetMenuText("Travel Book")
		self.commands[17] = MenuText.GetMenuText("Menu")
		self.commands[8] = MenuText.GetMenuText("Move")
		self.commands[9] = MenuText.GetMenuText("Camera")

		IManager.SetInputActionsSet(oldInputActionsSet)

	def GetCommandIndex(self, key):
		if key == "ButtonLeftTrigger":
			return 1
		elif key == "ButtonLeftShoulder":
			return 2
		elif key == "ButtonUp":
			return 3
		elif key == "ButtonDown":
			return 4
		elif key == "ButtonLeft":
			return 5
		elif key == "ButtonRight":
			return 6
		elif key == "ButtonLeftStick":
			return 7
		elif key == "ButtonRightStick":
			return 10
		elif key == "ButtonEast":
			return 11
		elif key == "ButtonSouth":
			return 12
		elif key == "ButtonNorth":
			return 13
		elif key == "ButtonWest":
			return 14
		elif key == "ButtonRightShoulder":
			return 15
		elif key == "ButtonRightTrigger":
			return 16

	def AcceptsFocus(self):
		return 0
