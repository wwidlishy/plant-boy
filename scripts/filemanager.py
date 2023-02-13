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
    'pos': [100, 100]
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
        tosave = """
global save_name
global player_stats
global inventory
global hasBackpack
global backpack

save_name = __SAVE_NAME__

player_stats = __PLAYER_STATS__
inventory = __INVENTORY__
hasBackpack = __HASBACKPACK__
backpack = __BACKPACK__
"""
        info = {
            'save_name': save_name,
            'player_stats': player_stats,
            'inventory': inventory,
            'hasBackpack': hasBackpack,
            'backpack': backpack
        }
        return [info, tosave]
    else:
        return 1

def delete(name):
    saves = os.listdir('saves')
    oname = name
    name = name.replace(' ', '_')
    if f"{name}.py" in saves:
        os.remove(f"saves/{name}.py")
        return 0
    else:
        return 1