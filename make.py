import os
uic = "C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py"
cmd = 'python %s %s > %s'
os.system(cmd%(uic, 'main.ui', 'mainGUI.py'))