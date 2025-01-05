# %%
import pandas as pd

# %%
in_df = pd.read_fwf("keymap_extract.md")
# %%
df = in_df.copy()
df = df.rename(
    columns=dict(
        Input="input_top_row",
        Output="output_no_thumb",
        Outer="output_outer_thumb",
        Inner="output_inner_thumb",
        Both="output_both_thumb",
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
    ]]
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
             id_vars=["input_top_row","input_bottom_row"],
             var_name="input_thumb",
             value_name="output",
             )
df.head()
