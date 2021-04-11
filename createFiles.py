import os

message = input("which message do you want to write?: ")
howMuch = int(input("how much files to write?: "))
nameOf = input("choose a name for the files: ")

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

for vari in range(howMuch) :
    open(nameOf+str(vari)+".txt","w+").write(message)
    vari+=1

print("end")