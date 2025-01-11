# Input example:
"""
R,S,N,I,A,O,T,E,0,1,sendText
1,0,0,0,0,0,0,0,0,0,r
0,1,0,0,0,0,0,0,0,0,s
0,0,1,0,0,0,0,0,0,0,n
"""

# Output example:

# LHS
"""
sendText,stenoKeyString
r,S
s,T
n,P
i,H
a,S
o,K
t,W
e,R
c,KR
u,KW
"""

# RHS
"""

"""

# # %%
# # used for one-off generation
# used_keys = duckdb.sql(pyprql.compile("""
#     from in_df
#     join side:left mask (in_df.sendText == mask.sendText)
#     filter (mask.include == "Y" || mask.notes == "Jav: in javelin-script taipoOneshotUpdate")
#     select {in_df.sendText}
# """)).df()
# used_keys.to_csv("used_keys.csv", index=False)

# %%
import pandas as pd
import pyprql
import duckdb
# %%
def query(df, query_prql):
    return duckdb.sql(pyprql.compile(query_prql)).df()

in_df = pd.read_csv("../keymap.csv")
LHS_map = pd.read_csv("TT_LHS_map.csv", index_col=0).to_dict()["Steno"]
RHS_map = pd.read_csv("TT_RHS_map.csv", index_col=0).to_dict()["Steno"]
LHS_key_list = ["S", "T", "K", "P", "W", "H", "R", "A", "O"]
RHS_key_list = ["E", "U", "F", "R", "P", "B", "L", "G", "T", "S"]
mask = pd.read_csv("../include_mask.csv")
drill_keys = pd.read_csv("drill_keys.csv")

# %%
drill_keys = duckdb.sql(pyprql.compile("""
    from drill_keys
    join side:left in_df (==sendText)
""")).df()
# %%
key_list = LHS_key_list
map = LHS_map
df = drill_keys.copy().rename(columns=map)
df = query(df,"""
    from df
    derive {
        S = case [
           (SLT==1 || SLB==1) => 1,
           true => 0, # 'else'
        ],
        T = TL,
        P = PL,
        R = RL,
    }
    select {S, T, K, P, W, H, R, A, O, sendText}
""")
for key in key_list:
    df[key] = df[key].replace(0,"")
    df[key] = df[key].replace(1, key)
df["stenoKeyString"] = df[key_list].agg(''.join, axis=1)
# df[["sendText","stenoKeyString"]].to_csv("LHS_tt_drill.csv",index=False)
# %%
key_list = RHS_key_list
map = RHS_map
df = drill_keys.copy().rename(columns=map)
df = query(df,"""
    from df
    derive {
        R = RR,
        P = PR,
        T = TR,
        S = SR,
    }
    select {E, U, F, R, P, B, L, G, T, S, sendText}
""")
for key in key_list:
    df[key] = df[key].replace(0,"")
    df[key] = df[key].replace(1, key)
df["stenoKeyString"] = df[key_list].agg(''.join, axis=1)
df["stenoKeyString"] = "'-" + df["stenoKeyString"]
df.head()
df[["sendText","stenoKeyString"]].to_csv("RHS_tt_drill.csv",index=False)