# Input example:
# 'include' is merged from a separate mask list, edited manually
"""
R,S,N,I,A,O,T,E,0,1,sendText,include
1,0,0,0,0,0,0,0,0,0,r,Y
0,1,0,0,0,0,0,0,0,0,s,Y
0,0,1,0,0,0,0,0,0,0,n,Y
"""

# Output example:
#   if (taipoKeysPressed == getTaipoBitmap("RS")) sendText("b");

#  Order: RSNIAOTE01
#  01 = Thumb buttons
#  RSNIAOTE = buttons
# %%
import csv
import pandas as pd
# %%
key_list = ["R","S","N","I","A","O","T","E","0","1"]

def javelin_keystring_template(row):
  text = row["sendText"]
  keypress = convertTextToKeypress(text)
  return rf'if (taipoKeysPressed == getTaipoBitmap("{row["taipoKeyString"]}")) {keypress}'

def convertTextToKeypress(text):
  # List of scan codes https://github.com/jthlim/javelin-steno/blob/main/script.md#constants-1
  keypress = rf'sendText("{text}");'
  # Modifiers, Arrows keys, Page up, page down, end & home already implemented within the script itself, no need to include those there
  if text.lower() == "tab": keypress = r"tapScanCode(0x2b); // tab" # SC_TAB
  if text.lower() == "space": keypress = r"tapScanCode(0x2c); // space" # SC_SPACE
  if text.lower() == "enter": keypress = r"tapScanCode(0x28); // enter" # SC_ENTER
  if text.lower() == "esc": keypress = r"tapScanCode(0x29); // esc" # SC_ESC
  if text.lower() == "del": keypress = r"tapScanCode(0x4c); // del" # SC_DELETE
  if text.lower() == "ins": keypress = r"tapScanCode(0x48); // ins" # SC_INSERT
  if text.lower() == "backspace": keypress = r"tapScanCode(0x2a); // backspace" # SC_BACKSPACE
  if text.lower() == "f1": keypress = f"tapScanCode(0x3a);" # 
  if text.lower() == "f2": keypress = f"tapScanCode(0x3b);" # 
  if text.lower() == "f3": keypress = f"tapScanCode(0x3c);" # 
  if text.lower() == "f4": keypress = f"tapScanCode(0x3d);" # 
  if text.lower() == "f5": keypress = f"tapScanCode(0x3e);" # 
  if text.lower() == "f6": keypress = f"tapScanCode(0x3f);" # 
  if text.lower() == "f7": keypress = f"tapScanCode(0x40);" # 
  if text.lower() == "f8": keypress = f"tapScanCode(0x41);" # 
  if text.lower() == "f9": keypress = f"tapScanCode(0x42);" # 
  if text.lower() == "f10": keypress = f"tapScanCode(0x43)" # 
  if text.lower() == "f11": keypress = f"tapScanCode(0x44)" # 
  if text.lower() == "f12": keypress = f"tapScanCode(0x45)" # 
  if text.lower() == "play/pause": keypress = r"tapScanCode(0xbd); // play pause" # SC_CONSUMER_PLAY_PAUSE
  if text.lower() == "volume up": keypress = r"tapScanCode(0x80); // vol up" # SC_VOLUME_UP 
  if text.lower() == "volume down": keypress = r"tapScanCode(0x81); // vol down" # SC_VOLUME_DOWN 
  if text.lower() == "next track": keypress = r"tapScanCode(0xa5); // next track" # SC_CONSUMER_SCAN_NEXT_TRACK 
  if text.lower() == "previous track": keypress = r"tapScanCode(0xa6); // prev track" # SC_CONSUMER_SCAN_PREVIOUS_TRACK 
  # TODO
  if text.lower() == "altgr": keypress = f"tapScanCode();" # 
  if text.lower() == "print screen": keypress = f"tapScanCode();" # 
  if text.lower() == "brightness up": keypress = f"tapScanCode();" # 
  if text.lower() == "brightness down": keypress = f"tapScanCode();" # 

  # Special
  #                                              press ctrl          press X               release X          release ctrl
  if text.lower() == "cut": keypress = r"pressScanCode(0xe0);pressScanCode(0x1b);releaseScanCode(0x1b);releaseScanCode(0xe0); // cut"
  #                                               press ctrl          press C               release C          release ctrl
  if text.lower() == "copy": keypress = r"pressScanCode(0xe0);pressScanCode(0x06);releaseScanCode(0x06);releaseScanCode(0xe0); // copy"
  #                                               press ctrl          press V               release V          release ctrl
  if text.lower() == "paste": keypress = r"pressScanCode(0xe0);pressScanCode(0x19);releaseScanCode(0x19);releaseScanCode(0xe0); // paste"
  #                                               press ctrl          press Z               release Z          release ctrl
  if text.lower() == "undo": keypress = r"pressScanCode(0xe0);pressScanCode(0x1d);releaseScanCode(0x1d);releaseScanCode(0xe0); // undo"
  
  return keypress
# %%
df = pd.merge(
  pd.read_csv("keymap.csv"),
  pd.read_csv("include_mask.csv"),
  how="left",
  on="sendText",
)
# %%
df = df[df["include"]=="Y"]
for key in key_list:
    df[key] = df[key].replace(0,"")
    df[key] = df[key].replace(1, key)
df["taipoKeyString"] = df[key_list].agg(''.join, axis=1)
df = df.apply(javelin_keystring_template, axis=1)
df.to_csv("keystring_list.javelin-script", index=False, quoting=csv.QUOTE_NONE, escapechar="\\")