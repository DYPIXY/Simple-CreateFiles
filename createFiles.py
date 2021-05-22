import os

typeOfFile = ""
howMuch = 1 + int(input("how much files to write?: "))
nameOf = input("choose a name for the files: ")
#if empty, create empty files, else, what mensage do you want? If empty no file extension, if message, is a txt
empty = input("do you want empty files? [y/n]")

if empty.lower() == "y":
    message = str("")
else:
    message = input("which message do you want to write?: ")
    typeOfFile = ".txt"
#create a directory if it does not exists, remove everything inside if it already exists
try:
    os.mkdir("FilesCreated")
except OSError:
    print("")

PATH = str(os.getcwd()+"/FilesCreated")
os.chdir(PATH)

try:
    for files in os.listdir():
        os.remove(files)
except ValueError:
    print("")

for vari in range(1,howMuch) :
    open(nameOf+str(vari)+typeOfFile,"w+").write(message)

print("end")
