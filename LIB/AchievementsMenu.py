import GridWidget
import BUIx
import MenuWidget
import Raster
import KeybWidget
import ListWidget
import Bladex
import ScorerWidgets
import Language
import Menu

MaxColumn = 12
IconSize = 50

class AchievementDetails(BUIx.B_FrameWidget):

  def __init__(self, parent):
    BUIx.B_FrameWidget.__init__(self,parent,"Details",850,50)

    scale_factor = 1

    if Language.IsCurrentLanguageAsian():
      scale_factor = 1.5

    self.Title = BUIx.B_TextWidgetNoFocus(self,"DetailTitle","Detail Title",ScorerWidgets.font_server,Language.LetrasMenuBig)
    self.Title.SetColor(207,144,49)
    self.Title.SetAlpha(1)
    self.Title.SetScale(0.55 * scale_factor)

    self.Description = BUIx.B_TextWidgetNoFocus(self,"DetailDescription", "Detail Description",ScorerWidgets.font_server,Language.LetrasMenuBig)
    self.Description.SetColor(207,144,49)
    self.Description.SetAlpha(1)
    self.Description.SetScale(0.6 * scale_factor)
    self.Description.SetJustification(BUIx.B_TextWidget.B_TEXT_Left)
    self.Description.SetMaximumWidth(420)

    self.Background = BUIx.B_BitmapWidget(self,"Background",680,145,"Background","../../Data/achievements/UI_InfoPanel.png")
    self.Background.SetColor(255,255,255)
    self.Background.SetAlpha(1)
    self.Background.SetVisible(1)

    self.Icon = BUIx.B_BitmapWidget(self,"Icon",64,64,"Icon","../../Data/achievements/1.png")
    self.Icon.SetColor(255,255,255)
    self.Icon.SetAlpha(1)
    self.Icon.SetVisible(1)

    offset = -100
    relative_x = 0.38

    self.AddWidget(self.Title,relative_x - 0.2,offset + 40,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_Left, BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    self.AddWidget(self.Description,relative_x  - 0.2,offset + 70,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_Left, BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    self.AddWidget(self.Icon,relative_x - 0.25,offset + 40,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    self.AddWidget(self.Background,relative_x,offset,BUIx.B_FrameWidget.B_FR_HRelative,BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)

  def AcceptsFocus(self):
      return 0

class AchievementsMenuWidget(ListWidget.B_ListWidget):
  def __init__(self,Parent,menudesc,StackMenu,VertPos=0):
    self.ListDesc = menudesc["Achievements"]
    self.StackMenu = StackMenu
    ListWidget.B_ListWidget.__init__(self,Parent,menudesc,StackMenu,VertPos)

    details = AchievementDetails(self)
    self.AddMenuElement(details, 50)
    self.Details = details

    # self.AddLabel("Achievements")
    self.AddLabel("")
    self.AddGrid(0)

    # self.AddLabel("Category 2")
    # self.AddGrid(1)

    self.SetFocus_Idx(2)
    self.MenuItems[2].SetHasFocus(1)
    self.MenuItems[2].CallSelectionChangeCallback()

  def __del__(self):
    ListWidget.B_ListWidget.__del__(self)

  def FinalRelease(self):
    ListWidget.B_ListWidget.FinalRelease(self)

  def AddLabel(self, text):
    stext = BUIx.B_TextWidgetNoFocus(self,"Unnamed",text,ScorerWidgets.font_server,Language.LetrasMenuBig)
    stext.SetColor(207,144,49)
    stext.SetAlpha(1)
    self.AddMenuElement(stext, 10)


  def AddGrid(self, filter_achievements):
    menudesc = {}
    menudesc["Name"] = "Grid" + str(filter_achievements)

    # :TODO: Filter on category

    # if filter_achievements:
    #   menudesc["ListDescr"] = self.ListDesc[0:20]
    # else:
    #   menudesc["ListDescr"] = self.ListDesc[20:]

    menudesc["ListDescr"] = self.ListDesc

    grid = GridWidget.B_GridWidget(self,menudesc,self.StackMenu,MaxColumn, "../../Data/achievements/UI_Selector.png", IconSize)

    grid.SelectionChangeCallback = self.OnSelectionChange

    self.AddMenuElement(grid, -100)

  def DoScroll(self,amount):
    return

  def OnSelectionChange(self, item):
    self.Details.Title.SetText(item.Name)
    self.Details.Description.SetText(item.Description)
    self.Details.Icon.SetBitmap(item.Name)
    if item.Completed:
      self.Details.Icon.SetAlpha(1)
    else:
      self.Details.Icon.SetAlpha(0.5)

  def AcceptsFocus(self):
      return 1

  def NextFocus(self):
    current_focus = self.GetFocus()
    if current_focus != None:
      if current_focus.CanMoveDown():
        current_focus.MoveDown()
        return 1

    ListWidget.B_ListWidget.NextFocus(self)
    new_focus = self.GetFocus()
    if new_focus != current_focus:
      new_focus = self.GetFocus()
      new_focus.SetFocusFromTop()

  def PrevFocus(self):
    current_focus = self.GetFocus()
    if current_focus != None:
      if current_focus.CanMoveUp():
        current_focus.MoveUp()
        return 1

    ListWidget.B_ListWidget.PrevFocus(self)
    new_focus = self.GetFocus()
    if new_focus != current_focus:
      new_focus = self.GetFocus()
      new_focus.SetFocusFromBottom()

  def IncMenuItem(self):
    current_focus = self.GetFocus()
    if Menu.TBUDSoundAble:
      Menu.SndCorreGema.PlayStereo()
    if current_focus != None:
      if current_focus.CanMoveRight():
        current_focus.MoveRight()
        return 1

  def DecMenuItem(self):
    if Menu.TBUDSoundAble:
      Menu.SndCorreGema.PlayStereo()
    current_focus = self.GetFocus()
    if current_focus != None:
      if current_focus.CanMoveLeft():
        current_focus.MoveLeft()
        return 1

class AchievementItem(BUIx.B_FrameWidget,MenuWidget.B_MenuTreeItem):
  def __init__(self,Parent,MenuDescr,StackMenu):
    BUIx.B_FrameWidget.__init__(self,Parent,MenuDescr["Name"],45,45)
    MenuWidget.B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)
    self.HasFocus=0
    self.SetClipDraw(0)
    self.Id = MenuDescr["Id"]
    self.Name = MenuDescr["Name"]
    self.Description = MenuDescr["Description"]
    achData = Bladex.GetAchievementData(self.Id, 1)
    self.AchTexture = BUIx.B_BitmapWidget(Parent,"RootName",IconSize,IconSize,self.Name,"");
    self.Completed = achData[3]

    self.AchTexture.SetAlpha(1.0)

    self.AddWidget(self.AchTexture,0,0.5,
                               BUIx.B_FrameWidget.B_FR_HRelative,  BUIx.B_FrameWidget.B_FR_Left,
                               BUIx.B_FrameWidget.B_FR_HCenter,BUIx.B_FrameWidget.B_FR_HCenter)
    self.SetDrawFunc(self.Draw)

  def Draw(self,x,y,time):
    if(Bladex.GetAchievementData(self.Id, 1)[3]):
      colorValue = 255
    else:
      colorValue = 65

    self.AchTexture.SetColor(colorValue,colorValue,colorValue)
    self.DefDraw(x,y,time)

  def __del__(self):
    BUIx.B_FrameWidget.__del__(self)
    MenuWidget.B_MenuTreeItem.__del__(self)

  def SetHasFocus(self,foc):
    self.HasFocus=foc

  def GetHasFocus(self,foc):
    return self.HasFocus



