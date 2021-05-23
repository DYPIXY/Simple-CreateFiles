import os
import createFiles as cr

class crtFile:
    def crt():
        create = input("you want to create files to sort? [y/n]:")
        if create.lower() == ["yes", "y"]:            
            cr.start()

print(os.system("ls FilesCreated"))

