# Data extraction script
# This parses the .md documentation into a csv bitmask

# Input example:
"""
--##  y      Y     5     F5
----

-#-#  f      F     6     F6
----
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
in_df = pd.read_fwf("keymap_extract_from_docs_corrected.md")
# %%
df = in_df.copy()
df = df.rename(
    columns=dict(
        Input="input_top_row",
        Output="output_no_thumb",
        Outer="output_outer_thumb",
        Inner="output_inner_thumb",
        Both="output_both_thumb",
        ChartRow="chart_row",
    )
)
df["input_bottom_row"] = df["input_top_row"].shift(-1)
df = df.dropna(subset="output_no_thumb")
df = df[[
    "input_top_row",
    "input_bottom_row",
    "output_no_thumb",
    "output_outer_thumb",
    "output_inner_thumb",
    "output_both_thumb",
    "chart_row",
    ]]
df = df.fillna("unassigned")
df = df.rename(
    columns=dict(
        output_no_thumb="--",
        output_outer_thumb="#-",
        output_inner_thumb="-#",
        output_both_thumb="##",
    )
)
columns_defined = df.copy()
# %%
df = columns_defined.copy()
df = pd.melt(df,
             id_vars=["input_top_row","input_bottom_row","chart_row"],
             var_name="input_thumb",
             value_name="sendText",
             )
df["keymask"] = df[[
    "input_top_row",
    "input_bottom_row",
    "input_thumb",
    ]].agg(''.join, axis=1)
df["keymask"] = df["keymask"].str.replace("-","0")
df["keymask"] = df["keymask"].str.replace("#","1")
df[["R","S","N","I","A","O","T","E","0","1"]] = df["keymask"].apply(lambda x: pd.Series(list(x)))
df = df[["R","S","N","I","A","O","T","E","0","1","chart_row","sendText"]].copy()
# %%
df.to_csv("keymap.csv",index=False)