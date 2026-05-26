import Bladex
import sys
import ConsoleOutput

ConsoleOutput.InitConsole()

# execfile("../../SCRIPTS/generate_loca.py")

import_localization = 0

try:
  import_localization = IMPORT_LOCALIZATION
except:
  pass

if import_localization == 1:
    execfile("../../SCRIPTS/import_loca.py")

def BladeRawInput(prompt=None):
  "Provides raw_input() for Blade"
  # flush stderr/out first.
  try:
    sys.stdout.flush()
    sys.stderr.flush()
  except:
    pass
  if prompt is None: prompt = ""
  ret=Bladex.Input(prompt)
  if ret==0:
    raise KeyboardInterrupt, "operation cancelled"
  return ret


def BladeInput(prompt=None):
  "Provides input() for Blade apps"
  return eval(raw_input(prompt))



sys.modules['__builtin__'].raw_input=BladeRawInput
sys.modules['__builtin__'].input=BladeInput
sys.setcheckinterval(100)


Bladex.CloseDebugChannel("DefaultChannel")

try:
	os.mkdir("../../AnmPak")
except:
	pass

print "Executed sys_init.py"

