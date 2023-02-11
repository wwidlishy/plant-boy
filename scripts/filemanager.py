import os
stemp = """
global save_name
global player_stats
global inventory
global hasBackpack
global backpack

save_name = __SAVE_NAME__

player_stats = {
    'hp': 3,
}
inventory = [
    '', '', '', '', '', '', '', '', '', '', '', ''
]
hasBackpack = False
backpack = [
    '', '', '', '', '', ''
]
"""
def new(name):
    saves = os.listdir('saves')
    oname = name
    name = name.replace(' ', '_')
    if f"{name}.py" in saves:
        return 1
    else:
        sf = open(f"saves/{name}.py", 'w')
        nstemp = stemp.replace("__SAVE_NAME__", f"'{oname}'")
        sf.write(nstemp)
        sf.close()
        return 0
def load(name):
    saves = os.listdir('saves')
    oname = name
    name = name.replace(' ', '_')
    if f"{name}.py" in saves:
        f = open(f"saves/{name}.py", 'r').read()
        f = exec(f)
        info = {
            'save_name': save_name,
            'player_stats': player_stats,
            'inventory': inventory,
            'hasBackpack': hasBackpack,
            'backpack': backpack
        }
        return info
    else:
        return 1