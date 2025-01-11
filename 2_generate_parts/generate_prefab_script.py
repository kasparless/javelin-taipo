# Generates the new 'prefab' Javelin key press scripts

# Example output
# // #prefab <category name>:<name> <button config>
"""
// #prefab Taipo:E [{"t":"p","d":{"a":{"t":"s","script":"// Taipo RHS\\nE\npressTaipoE(1);"}}},{"t":"r","d":{"a":{"t":"s","script":"//\nreleaseTaipoE(1);"}}}]
// #prefab Taipo:E [{"t":"p","d":{"a":{"t":"s","script":"// Taipo RHS\\nE\npressTaipoE(1);"}}},{"t":"r","d":{"a":{"t":"s","script":"//\nreleaseTaipo{key}({side_val});"}}}]'
"""
# %%
key_list = ["R", "S", "N", "I", "A", "O", "T", "E", "Inner", "Outer"]
side_list = [("LHS", 0), ("RHS", 1)]
prefab_order = {
    "R_LHS": "Key01_LHS_R",
    "S_LHS": "Key02_LHS_S",
    "N_LHS": "Key03_LHS_N",
    "I_LHS": "Key04_LHS_I",
    "I_RHS": "Key05_RHS_I",
    "N_RHS": "Key06_RHS_N",
    "S_RHS": "Key07_RHS_S",
    "R_RHS": "Key08_RHS_R",
    "A_LHS": "Key09_LHS_A",
    "O_LHS": "Key10_LHS_O",
    "T_LHS": "Key11_LHS_T",
    "E_LHS": "Key12_LHS_E",
    "E_RHS": "Key13_RHS_E",
    "T_RHS": "Key14_RHS_T",
    "O_RHS": "Key15_RHS_O",
    "A_RHS": "Key16_RHS_A",
    "Inner_LHS": "Key17_LHS_Inner",
    "Outer_LHS": "Key18_LHS_Outer",
    "Outer_RHS": "Key19_RHS_Outer",
    "Inner_RHS": "Key20_RHS_Inner",
}

# %%
def prefab_template(key, side_txt, side_val):
    template = r'// #prefab <category name>:<key short name> [{"t":"p","d":{"a":{"t":"s","script":"<press script>"}}},{"t":"r","d":{"a":{"t":"s","script":"<release script>"}}}]'
    return (
        template.replace("<category name>", "Taipo")
        .replace("<key short name>", prefab_order[f"{key}_{side_txt}"])
        .replace(
            "<press script>",
            rf"// Taipo {side_txt}\\n{key}\npressTaipo{key}({side_val});",
        )
        .replace("<release script>", rf"//\nreleaseTaipo{key}({side_val});")
    )
    # f.writelines(f"{action}Taipo{key}({side_val});" + "\n")


# %%
with open("key_prefab_scripts.javelin-script", "w") as f:
    for side_txt, side_val in side_list:
        f.writelines(r"// Prefab for :" + side_txt + "\n")
        for key in key_list:
            f.writelines(prefab_template(key, side_txt, side_val) + "\n")
