import os
from src import createFiles as cr, randomFiles

class filesToSort:
    def __init__(self):    
        create = str(input("you want to create files to sort, create random files or use the default files? [c/r/d]:"))
        if create.lower() in ["create", "c"]:            
            cr.fil.start()
        elif create.lower() in ["random", "r"]:
            randomFiles()
        elif create.lower() in ["default", "d"]:
            print()




