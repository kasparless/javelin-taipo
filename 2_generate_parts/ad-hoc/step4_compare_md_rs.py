# quick script to compare the md and rs input information
# %%
import pandas as pd
# %%
md = pd.read_csv("keymap.csv")
rs = pd.read_csv("keymap_tangybbq.csv")
key_list = ["R","S","N","I","A","O","T","E","0","1"]
# %%
df = md.copy()
for key in key_list:
    df[key] = df[key].replace(0,"0")
    df[key] = df[key].replace(1, "1")
df["bin_code"] = df[key_list].agg(''.join, axis=1)
df = df[["bin_code","sendText"]]
md_codes = df
# %%
df = rs.copy()
for key in key_list:
    df[key] = df[key].replace(0,"0")
    df[key] = df[key].replace(1, "1")
df["bin_code"] = df[key_list].agg(''.join, axis=1)
df = df[["bin_code","rust_action"]]
rs_codes = df
# %%
df = pd.merge(md_codes,rs_codes,on="bin_code",how="outer")
df = pd.merge(df, pd.read_csv("include_mask.csv"), on="sendText", how="outer")
df.to_csv("compare_md_rs.csv")
# outcome -> backspace and space might be reversed (or my vision is blurring), some of the special keys not implemented, F11/12 different