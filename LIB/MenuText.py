import Language
import Localization

execfile("../../Data/Menu/"+Language.Current+".py")

def GetMenuText(item):
  TrWord = item
  try:
    TrWord = Localization.GetTranslation(ForeingDict, item)
  except:
    pass
  return TrWord

def GetMenuTextEnglish(item):
  execfile("../../Data/Menu/English.py")
  Text = GetMenuText(item)
  execfile("../../Data/Menu/"+Language.Current+".py")
  return Text

def GetInverseMenuText(item):
  if Language.Current!="English":
    for i in ForeingDict.keys():
      if item == ForeingDict[i]:
        return i
    return item
  else:
    return item


def SetLanguage(l):
  print "SetLanguage("+l+")"
  print "This function does not work... yet"
