# Input example:
# 'include' is a column added manually in spreadsheet during dev phase
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
  return rf'if (taipoKeysPressed == getTaipoBitmap("{row["taipoKeyString"]}")) sendText("{row["sendText"]}");'
# %%
df = pd.read_csv("keymap.csv")
df = df[df["include"]=="Y"]
for key in key_list:
    df[key] = df[key].replace(0,"")
    df[key] = df[key].replace(1,key)
df["taipoKeyString"] = df[key_list].agg(''.join, axis=1)
df = df.apply(javelin_keystring_template, axis=1)
df.to_csv("keystring_list.javelin-script", index=False, quoting=csv.QUOTE_NONE)