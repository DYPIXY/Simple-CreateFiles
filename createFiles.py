import os

def start():

    typeOfFile = ""
    howMuch = 1 + int(input("how much files to write?: "))
    nameOf = input("choose a name for the files: ")

    #if empty, create empty files, else, what mensage do you want? If empty no file extension, if message, is a txt
    empty = input("do you want empty files? [y/n]")

    if empty.lower() == "y" or "yes":
        message = str("")
    elif empty.lower == "n" or "no":
        message = input("which message do you want to write?: ")
        typeOfFile = ".txt"
    else:
        unvalid = true

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
    for vari in range(1,howMuch) :
        open(nameOf+str(vari)+typeOfFile,"w+").write(message)




#this is just a debug
start()
print("end")
