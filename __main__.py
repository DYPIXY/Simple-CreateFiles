import os
from src import createFiles
import src

class crtFile:

    create = str(input("you want to create files to sort? [y/n]:"))
    if create.lower() == ["yes", "y"]:            
        createFiles.start()
    
#print(os.system("ls FilesCreated"))

