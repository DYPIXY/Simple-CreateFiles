# This is for sorting the files you want, with the names you want
#
import os
import random

class fil:

    def start():

        typeOfFile = ""
        message = ""
        nameOf = ""
        
        howMuch = 1 + int(input("how much files to write?: "))


        #if empty, create empty files, else, what mensage do you want? If empty no file extension, if message, is a txt        
        def FilePro():
            empty = input("do you want empty files? [y/n]: ")

            if empty.lower() in ["y", "yes"]:
                message = ""
                typeOfFile = ""
            elif empty.lower() in ["n", "no"]:
                message = input("which message do you want to write?: ")
                typeOfFile = ".txt"
            else:
                print("\n you put a wrong input, please write y or yes, n or no \n")
                FilePro()
        FilePro()


        #create a directory if it does not exists, remove everything inside if it already exists
        try:
            os.mkdir("FilesCreated")
        except OSError:
            print()

        #chose the path to the files directory to create
        PATH = str(os.getcwd()+"/FilesCreated")
        os.chdir(PATH)

        #remove the files inside the folder if you created files in it before
        try:
            for files in os.listdir():
                os.remove(files)
        except ValueError:
            print("")

        #create the files
        def name():
            a = input("type 'r' for random files or write any name you want")            
            if a.lower() == "y":
                randname = True


        list = []
        for vari in range(1, howMuch, 1):
            ran = random.randint(1, howMuch)
            for i in list:    
                if i == ran:
                    vari -= 1
                    continue                    
        
            list.append(ran)
            open(nameOf+str(ran)+typeOfFile,"w+").write(str(message))        

        for pri in list:


        print("end")
    start()