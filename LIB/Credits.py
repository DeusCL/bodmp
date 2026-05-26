import Bladex
import Scorer
import Raster
import BBLib
import BUIx
import Sounds
import Language
import ScorerWidgets
import MenuText
import string

from os import listdir, path

StayImage = 8
FadeImage = 3.0
StateImage = 0

musiccredits             = None

scaledCenteredSizeFactor = Raster.GetScaledCenteredSizeFactor()
TextsPositions = [(0.5, 0.135), (0.88 ,0.4), (0.88, 0.375), (0.85 ,0.365), (0.88, 0.17), (0.88, 0.32), (0.88, 0.305), (0.14, 0.27), (0.88, 0.37), (0.83, 0.24), (0.93, 0.37), (0.5, 0.15), (0.85, 0.33), (0.5, 0.02), (0.5, 0.075), (0.85, 0.1), (0.85, 0.09), (0.77, 0.2), (0.85, 0.25), (0.85, 0.25), (0.9, 0.35), (0.905, 0.05), (0.83, 0.12), (0.18, 0.2), (0.84, 0.18), (0.73, 0.18), (0.48, 0.175), (0.84, 0.05)]
TextsOffset = [0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.21, 0.1, 0.15, 0.12, 0.08, 0.1, 0.11, 0.1, 0.15, 0.15, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
TextsExceptionIndex = [7, 22, 23, 26]
TextSpecialOffset = [0.34, 0.45, 0.25]
OffsetText = 0.1
BaseDescrScale = 0.9

class B_CreditsImageWidget(BUIx.B_FrameWidget):
    def __init__(self,Parent,MenuDescr,StackMenu = 0):
        import Menu

        self.ResX = Raster.GetSize()[0]
        self.ResY = Raster.GetSize()[1]
        self.BitmapsHandler = []
        self.path = "../../Data/Credits"
        self.OldSndNewMenuVol = Menu.SndNewMenu.Volume
        self.OldSndCorreGemaVol= Menu.SndCorreGema.Volume
        Menu.SndNewMenu.Volume = 0
        Menu.SndCorreGema.Volume = 0

        currentmap = Bladex.GetCurrentMap()

        Credits = []
        for f in listdir(self.path):
            Credits.append("/" + f)
        Credits.sort()
        self.BitmapsNames = Credits

        type = 0

        self.StateImage = 0
        self.FadeImage = 3
        self.image1 = 0
        self.image2 = 1
        self.Pages = 0
        self.Cache = 0
        self.Fade = 0
        self.StackMenu = StackMenu

        for i in self.BitmapsNames:
            self.Pages = self.Pages + 1

        BUIx.B_FrameWidget.__init__(self,Parent,MenuDescr["Name"], 640, 480)

        if type:
            self.SetDrawFunc(self.DrawFadeImage)
            Bladex.ReadBitMap(self.BitmapsNames[0],self.BitmapsNames[0])
            self.BitmapsHandler.append(Raster.BmpHandle(self.BitmapsNames[0]))
        else:
            self.SetDrawFunc(self.DrawSlice)

        char = Bladex.GetEntity("Player1")

        global musiccredits

        if not musiccredits:
                musiccredits             = Bladex.CreateSound('../../Sounds/tema.wav', 'MusicCreditos')
                musiccredits.Volume      = 1.0
                musiccredits.MinDistance = 100000
                musiccredits.MaxDistance = 200000
        musiccredits.PlayStereo(0)
        self.MusicVolume = Bladex.GetMusicVolume()
        Bladex.SetMusicVolume(0)
        self.StayImage = (((60.0 * 4) + 37.0) / self.Pages)
        self.StateImage = 1
        self.StartImageTime = 0

        self.Selected=0
        self.Solid=0
        self.Border=0
        self.WidgetListText=[]

        self.bitmap = BBLib.B_BitMap24()
        self.bitmap.ReadFromFile(self.path+self.BitmapsNames[self.image1])
        Raster.SetBackgroundImage(4256,2394,"RGB","Normal","Cover",self.bitmap)
        Raster.SetTextShadow(0, 0)

        self.InitCopyrights()
        self.InitWidgets()

    def InitCopyrights(self):
        self.CopyrightsWidget = BUIx.B_TextWidget(self,"Copyrights", "Copyrights", ScorerWidgets.font_server, Language.LetrasMenuBig)
        self.CopyrightsWidget.SetScale(0.5)
        self.CopyrightsWidget.SetMaximumWidth(800)
        self.CopyrightsWidget.SetText(MenuText.GetMenuText("COPYRIGHTS"))
        self.CopyrightsWidget.SetAlpha(1)
        self.CopyrightsWidget.SetColor(0,0,0)
        self.CopyrightsWidget.SetVisible(1)

        self.AddWidget(self.CopyrightsWidget, 0.5, self.ResY * 0.8,
              BUIx.B_FrameWidget.B_FR_HRelative,
              BUIx.B_FrameWidget.B_FR_HCenter,
              BUIx.B_FrameWidget.B_FR_AbsoluteTop,
              BUIx.B_FrameWidget.B_FR_Top)

    def InitWidgets(self):
        Texts = MenuText.GetMenuText("Credits_Text")
        TextToReplace = MenuText.GetMenuText("Credits_Translatable")
        TextToReplace = string.split(TextToReplace, "|")
        TextKeys = MenuText.GetMenuTextEnglish("Credits_Translatable")
        TextKeys = string.split(TextKeys, "|")
        for i in range(0,len(TextKeys)):
            Texts = string.replace(Texts, TextKeys[i], TextToReplace[i], 1)
        Texts = string.replace(Texts, " and", " " + MenuText.GetMenuText("and"))
        Texts = string.replace(Texts, " AND", " " + MenuText.GetMenuText("and"))
        Texts = string.replace(Texts, " from", " " + MenuText.GetMenuText("from"))
        Texts = string.replace(Texts, " FROM", " " + MenuText.GetMenuText("from"))
        Texts = string.split(Texts, "|")
        index=0
        for elem in Texts:
            self.InitPageWidgets(elem, index)
            index = index + 1

    def InitPageWidgets(self, text, index):
        scale = BaseDescrScale
        if index not in TextsExceptionIndex:
            if index == 27:
                scale = 0.8
            if index == 14:
                texts = string.split(text, "\n\n\n")
                scale = 0.5
            else:
                texts = string.split(text, "\n\n")
            name = "txt" + str(index) + "title"
            WidgetTitle = self.InitWidget(name, texts[0], index)
            if index == 13:
                TextsPositions[index] = (TextsPositions[index][0] + 0.1, TextsPositions[index][1])
                if Language.Current == "Russian":
                    TextsPositions[index] = (TextsPositions[index][0] + 0.09, TextsPositions[index][1])
                if Language.Current == "Polish" or Language.Current == "French":
                    TextsPositions[index] = (TextsPositions[index][0], TextsPositions[index][1])
            name = "txt" + str(index) + "descr"
            WidgetText = self.InitWidget(name, texts[1], index, scale, TextsOffset[index])
            self.WidgetListText.append([WidgetTitle, WidgetText])
        else:
            if index == 7:
                if Language.Current == "Polish":
                    TextsPositions[index] = (TextsPositions[index][0] + 0.17, TextsPositions[index][1])
                name = "txt" + str(index)
                Widget = self.InitWidget(name, text, index)
                self.WidgetListText.append([Widget])
            if index == 22 or index == 23 or index == 26:
                if index == 22:
                    currOffset = TextSpecialOffset[0]
                elif index == 23:
                    currOffset = TextSpecialOffset[1]
                else:
                    currOffset = TextSpecialOffset[2]
                texts = string.split(text, "\n\n\n")
                Widgets = []
                ElemIdx = 0
                for elem in texts:
                    textTitleDescr = string.split(elem, "\n\n")
                    name = "txt" + str(index) + "title"
                    WidgetTitle = self.InitWidget(name, textTitleDescr[0], index, scale, ElemIdx * currOffset)
                    Widgets.append(WidgetTitle)
                    name = "txt" + str(index) + "descr"
                    WidgetText = self.InitWidget(name, textTitleDescr[1], index, scale, TextsOffset[index] + ElemIdx * currOffset)
                    Widgets.append(WidgetText)
                    ElemIdx = ElemIdx + 1
                self.WidgetListText.append(Widgets)


    def InitWidget(self, name, text, index, scale=1.1, offset=0):
        Widget = BUIx.B_TextWidget(self, name,"",ScorerWidgets.font_server,Language.LetrasMenuBig)
        Widget.SetScale(scale)
        Widget.SetAlpha(1)
        Widget.SetText(text)
        Widget.SetVisible(index == 0)
        Widget.SetColor(51,17,8)
        self.AddWidget(Widget, TextsPositions[index][0], self.ResY * (TextsPositions[index][1] + offset),
            BUIx.B_FrameWidget.B_FR_HRelative,
            BUIx.B_FrameWidget.B_FR_HCenter,
            BUIx.B_FrameWidget.B_FR_AbsoluteTop,
            BUIx.B_FrameWidget.B_FR_Top)
        return Widget

    def ActivateItem(self,act):
        if act==0:
            w=self.StackMenu.Top()
            try:
                w.FinalRelease()
            except:
                pass
            self.StackMenu.Pop()
            musiccredits.Stop()
            Bladex.SetMusicVolume(self.MusicVolume)

    def __del__(self):
        Bladex.TriggerEventInner()
        import Menu
        Raster.RemoveBackgroundImage()
        Menu.SndNewMenu.Volume = self.OldSndNewMenuVol
        Menu.SndCorreGema.Volume = self.OldSndCorreGemaVol
        Raster.SetTextShadow(2, 2)

    def DrawSlice(self,x,y,time):
        self.DefDraw(x,y,time)

        if self.StartImageTime == 0:
            self.StartImageTime = time

        stime = time - self.StartImageTime

        if stime >= self.StayImage:
            self.StartImageTime = time
            self.image1 = self.image1 + 1

            if self.image1 >= self.Pages:
                global musiccredits
                if not musiccredits:
                        musiccredits             = Bladex.CreateSound('../../Sounds/tema.wav', 'MusicCreditos')
                        musiccredits.Volume      = 1.0
                        musiccredits.MinDistance = 100000
                        musiccredits.MaxDistance = 200000
                musiccredits.PlayStereo(0)
                self.image1 = 0
                Bladex.TriggerEvent(22)

            Raster.RemoveBackgroundImage()
            self.bitmap.ReadFromFile(self.path+self.BitmapsNames[self.image1])

            Raster.SetBackgroundImage(4256,2394,"RGB","Normal","Cover",self.bitmap)
            Raster.Cls(0,0,0) # Trigger texture creation
            Raster.SwapBuffers() # Trigger texture upload
            Raster.Cls(0,0,0) # Actual render of the background

            if self.image1 == 0:
                self.CopyrightsWidget.SetVisible(1)
                for elem in self.WidgetListText[0]:
                    elem.SetVisible(1)
            else:
                self.CopyrightsWidget.SetVisible(0)
                if self.image1 < len(TextsPositions) + 1:
                    for elem in self.WidgetListText[self.image1-1]:
                        elem.SetVisible(0)
                if self.image1 < len(TextsPositions):
                    for elem in self.WidgetListText[self.image1]:
                        elem.SetVisible(1)


    def DrawFadeImage(self,x,y,time):    
        if self.StartImageTime == 0:
            self.StartImageTime = time

        x = y = 0

        stime = time - self.StartImageTime

        if self.StateImage >= 1:
            if self.StateImage == 1:
                self.StateImage = 2
            elif self.StateImage == 2: #and self.Cache <> 1:
                Bladex.ReadBitMap(self.BitmapsNames[self.image2],self.BitmapsNames[self.image2])
                self.BitmapsHandler.append(Raster.BmpHandle(self.BitmapsNames[self.image2]))
                self.StateImage = 3

            Raster.SetPenColor(255,255,255)    
            Raster.SetPosition(x,y)
            Raster.SetAlpha(1.0)
            Raster.DrawBitmap(self.BitmapsHandler[self.image1],self.ResX,self.ResY)

            if stime >= self.StayImage:
                self.StartImageTime = time
                self.StateImage = 0
                self.alpha = 0
        else:
            #self.alpha = stime / self.FadeImage

            #if self.alpha >= 1.0:
            #    self.alpha = 1.0
            #    self.StateImage = 1
            #    self.StartImageTime = time
            self.StateImage = 1

            Raster.SetPenColor(255,255,255)
            Raster.SetPosition(x,y)
            #Raster.SetAlpha(1.0 - self.alpha)
            Raster.SetAlpha(1.0)
            Raster.DrawBitmap(self.BitmapsHandler[self.image1],self.ResX,self.ResY)

            #Raster.SetPenColor(255,255,255)
            #Raster.SetPosition(x,y)
            #Raster.SetAlpha(self.alpha)
            #Raster.DrawBitmap(self.BitmapsHandler[self.image2],self.ResX,self.ResY)

            if self.StateImage:
                self.image1 = self.image2  

                self.image2 = self.image1 + 1

                if self.image2 >= self.Pages:
                #if self.image2 >= 2:
                    self.image2 = 0
                    self.Cache = 1


def NoExitMenu(val):
    return 1

def Show(type = 0,r = 255,g = 255,b = 255):
    import Menu
    Menu.ActivateMenu("credits")
    if not Bladex.IsConsole():
        Menu._MainMenu.MenuPrevItem()
    Menu._MainMenu.MenuPrevItem()
    Menu._MainMenu.ActivateMenuItem()

    Menu.EscapeFunction = NoExitMenu

