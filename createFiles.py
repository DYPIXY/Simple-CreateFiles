# This is for sorting the files you want, with the names you want
#
import os
import random, string
class fil:

    def start():

        typeOfFile = ""
        message = ""
        nameOf = ""
        howMuch = int(input("how much files to write?: "))


        #if empty, create empty files, else, what message do you want? If empty no file extension, if message, is a txt        
        empty = input("do you want empty files? [y/n]: ")
        if empty.lower() in ["y", "yes"]:
            message = ""
            typeOfFile = ""
        elif empty.lower() in ["n", "no"]:
            message = input("which message do you want to write?: ")
            typeOfFile = ".txt"
        else:
            print("\n you put a wrong input, please write [y or yes], [n or no] \n")


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

        #"random" names if True, else the input is the name
        def randomword(length):
            letters = string.ascii_letters
            return ''.join(random.choice(letters) for i in range(length))

        
        name = input("type 'r' for random name files or write a name that you want: ")            
        if name.lower() == "r":
            nameOf = randomword(5)+"_"
        else:
            nameOf = name

        #"random" numbers in a "random" order, if name is 
        list = []
        while len(list) < howMuch:
            ran = random.randint(1, howMuch)
            if ran in list:    
                continue                
            else:         
                #create the files
                list.append(ran)
                with open(nameOf+str(ran)+typeOfFile,"w+") as file:
                    file.write(str(message))



        print("\n end")
    
    start()
