from zipfile import ZipFile
from tkinter import *
#create a zipfile object and load zip in it
with ZipFile('do_not_unzip_me.zip', 'r') as zipObj:
    zip.printdir()
    #extract all the contents of zip file into current directory
    zipObj.extractall(path = 'c:\')
    zipObj.close()
print('\nDone!\n')
