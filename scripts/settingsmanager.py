import os

settingstemp = """
global autosave
global fullscreen

autosave = True
fullscreen = False
"""
settingstosave = """
global autosave
global fullscreen

autosave = __AUTOSAVE__
fullscreen = __FULLSCREEN__
"""
def load():
    settings = open("config/settings.py", 'r').read()
    exec(settings)
    return {
        'autosave': autosave,
        'fullscreen': fullscreen
    }

def write(newsettingsdata):
    settings = open("config/settings.py", 'w')
    settings.write(newsettingsdata)
    settings.close()