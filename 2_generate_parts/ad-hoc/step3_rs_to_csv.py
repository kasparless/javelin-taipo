# Data extraction script
# This parses the TangyBBQ's rust implementation into a csv bitmask

# Input example:
"""
    Entry { code: 0x010, action: Action::Simple(Keyboard::R), },
"""


# Output example:
"""
R,S,N,I,A,O,T,E,0,1,sendText
1,0,0,0,0,0,0,0,0,0,r
0,0,1,1,0,0,0,0,0,0,y
0,1,0,1,0,0,0,0,0,0,f
"""

# Eventual output target:
#   if (taipoKeysPressed == getTaipoBitmap("RS")) sendText("b");
#  Order: RSNIAOTE01
#  01 = Thumb buttons
#  RSNIAOTE = buttons

# %%
import pandas as pd
# %%
in_df = pd.read_csv("taipo.rs", sep="blue zebra", names=["text_column"])
# %%
df = in_df.copy()
df = df[df["text_column"].str.contains("Entry { code")]
taipo_actions = df
# %%
df = taipo_actions.copy()
# Entry { code: 0x010, action: Action::Simple(Keyboard::R), },
df = df["text_column"].str.extract(
    r'Entry { code: 0x(?P<hex>.*), action: Action::(?P<rust_action>[\w\(\):]*)'
    , expand=True)
hex_actions = df
# %%
def hex2bin2(hex_val):
    return list((str(bin(int(hex_val, 16)))[2:]).zfill(2))
def hex2bin4(hex_val):
    return list((str(bin(int(hex_val, 16)))[2:]).zfill(4))
# %%
df = hex_actions.copy()
df[["thumb_hex","toprow_hex","botrow_hex"]] = df["hex"].apply(lambda x: pd.Series(list(x)))
df[["1","0"]] = df["thumb_hex"].apply(hex2bin2).to_list()
df[["I","N","S","R"]] = df["toprow_hex"].apply(hex2bin4).to_list()
df[["E","T","O","A"]] = df["botrow_hex"].apply(hex2bin4).to_list()
df = df[["R","S","N","I","A","O","T","E","0","1","rust_action"]].copy()
df.to_csv("keymap_tangybbq.csv",index=False)
