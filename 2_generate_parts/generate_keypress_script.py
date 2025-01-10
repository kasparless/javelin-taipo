# %%
key_list = ["R","S","N","I","A","O","T","E","Inner","Outer"]
side_list = [("left",0),("right",1)]
action_list = ["press","release"]
# %%
with open("key_trigger_scripts.javelin-script","w") as f:
    for side_txt, side_val in side_list:
        f.writelines(side_txt+"\n")
        for key in key_list:
            for action in action_list:
                f.writelines(f"{action}Taipo{key}({side_val});"+"\n")