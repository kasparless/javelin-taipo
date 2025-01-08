# Input example:
# 'include' is merged from a separate mask list, edited manually
"""
R,S,N,I,A,O,T,E,0,1,sendText,include
1,0,0,0,0,0,0,0,0,0,r,Y
0,1,0,0,0,0,0,0,0,0,s,Y
0,0,1,0,0,0,0,0,0,0,n,Y
"""

# Output example:
"""
top_row,bottom_row,thumb_row,sendText
1000,0000,00,r
0100,0000,00,s
"""

#  Order: RSNIAOTE01
#  01 = Thumb buttons
#  RSNIAOTE = buttons
# %%
import csv
import pandas as pd
# %%
key_list = ["R","S","N","I","A","O","T","E","0","1"]
top_row_key_list = ["R","S","N","I"]
bottom_row_key_list = ["A","O","T","E"]
thumb_row_key_list = ["0","1"]
thumb_sort_order = pd.DataFrame({'sort_order': [1,2,3,4], 'thumb_row': ["00","10","01","11"]})

# %%
df = pd.merge(
  pd.read_csv("keymap.csv"),
  pd.read_csv("include_mask.csv"),
  how="left",
  on="sendText",
)
df = df[df["include"]=="Y"]
for key in key_list:
    df[key] = df[key].replace(0,"0")
    df[key] = df[key].replace(1, "1")
df["top_row"] = df[top_row_key_list].agg(''.join, axis=1)
df["bottom_row"] = df[bottom_row_key_list].agg(''.join, axis=1)
df["thumb_row"] = df[thumb_row_key_list].agg(''.join, axis=1)
df = pd.merge(df,thumb_sort_order,on="thumb_row",how="left")
df = df.sort_values(by=["chart_row","top_row","bottom_row","sort_order"])
df = df[["sendText","top_row","bottom_row","thumb_row"]]
df.to_csv("checking_list.csv", index=False)
