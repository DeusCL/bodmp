import Raster
import BUIx
import MenuWidget
import ScorerWidgets
import pdb
import Language
import math
import Bladex


class B_GridWidget(BUIx.B_GridWidget):
  def __init__(self,Parent,Menudesc,StackMenu,MaxColumn,selector_image,icon_size):

    width,height=Raster.GetSize()
    try:
      width,height=Menudesc["Size"]
    except:
      pass

    BUIx.B_GridWidget.__init__(self,Parent,"Grid"+Menudesc["Name"],MaxColumn,MaxColumn,width,height)
    self.Parent = Parent
    self.StackMenu = StackMenu
    self.nElements=0
    self.GridItems=[]
    self.WidgetsXPositions = []
    self.WidgetsYPositions = []
    self.SetClipDraw(1)
    self.Columns = MaxColumn
    self.Margin = 25
    self.SelectorOffsetX = 4
    self.SelectorOffsetY = 6
    self.SelectorSizeFactor = 1.15
    self.CurrentItemIndex = 0
    self.IconSize = icon_size
    self.SetDrawFunc(self.Draw)

    Bladex.ReadBitMap(selector_image, "GridSelector")
    self.Selector = Raster.BmpHandle("GridSelector")

    y = 0
    idx = 0
    for elem in Menudesc["ListDescr"]:
      x = math.fmod(idx,self.Columns)
      y = idx/self.Columns
      m_class=MenuWidget.B_MenuItemTextNoFX
      self.nElements = self.nElements + 1
      try:
        m_class=elem["Kind"]
      except:
        pass

      vsep=0
      try:
        vsep=elem["VSep"]
      except:
        pass

      wSubMenu=m_class(self,elem,StackMenu)

      self.AddMenuElement(wSubMenu, x, y, vsep)

      idx = idx + 1

  def Draw(self,x,y,time):

    if self.GetHasFocus() and self.CurrentItemIndex != None:
      pos_x, pos_y = self.WidgetsXPositions[self.CurrentItemIndex], self.WidgetsYPositions[self.CurrentItemIndex]
      Raster.SetPosition(x + pos_x - self.SelectorOffsetX, y + pos_y - self.SelectorOffsetY)
      Raster.SetPenColor(255, 255, 255)
      Raster.DrawBitmap(self.Selector, self.IconSize * self.SelectorSizeFactor, self.IconSize * self.SelectorSizeFactor)

    self.SetClipDraw(1)
    self.DefDraw(x,y,time)

  def __del__(self):
    BUIx.B_GridWidget.__del__(self)


  def __str__(self):
    print "B_GridWidget",self.Name()


  def AddMenuElement(self,widget,x,
                     y, vsep, HIndicator=BUIx.B_FrameWidget.B_FR_HRelative,HAnchor=BUIx.B_FrameWidget.B_FR_HCenter):
    vsep = vsep + self.Margin
    self.GridItems.append(widget)
    self.AddWidget(widget,x*vsep,y*vsep,
                   BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
                   BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
    self.WidgetsXPositions.append(x*vsep)
    self.WidgetsYPositions.append(y*vsep)

  def GetSize(self):
    width = self.Columns * self.IconSize + (self.Columns - 1) * self.Margin
    height = (int(self.nElements / self.Columns) + 1) * (self.Margin + self.IconSize)
    return width, height

  def CanMoveDown(self):
    return self.CurrentItemIndex + self.Columns < self.nElements

  def MoveDown(self):
      self.CurrentItemIndex = self.CurrentItemIndex + self.Columns
      self.CallSelectionChangeCallback()

  def CanMoveUp(self):
    return self.CurrentItemIndex - self.Columns >= 0

  def MoveUp(self):
      self.CurrentItemIndex = self.CurrentItemIndex - self.Columns
      self.CallSelectionChangeCallback()

  def CanMoveLeft(self):
    return self.CurrentItemIndex - 1 >= 0

  def MoveLeft(self):
      self.CurrentItemIndex = self.CurrentItemIndex - 1
      self.CallSelectionChangeCallback()

  def CanMoveRight(self):
    return self.CurrentItemIndex + 1 < self.nElements

  def MoveRight(self):
      self.CurrentItemIndex = self.CurrentItemIndex + 1
      self.CallSelectionChangeCallback()

  def SetFocusFromBottom(self):
    self.CurrentItemIndex = self.nElements - 1

  def SetFocusFromTop(self):
    self.CurrentItemIndex = 0

  def ActivateItem(self, value):
    if value == 0:
      self.StackMenu.Top()
      try:
        self.FinalRelease()
      except:
        pass
      self.StackMenu.Pop()

  def CallSelectionChangeCallback(self):
    item = self.GridItems[self.CurrentItemIndex]
    self.SelectionChangeCallback(item)

