import random
import os

os.chdir =str(os.getcwd())+"/FilesCreated"
howMuch=random.randint(1, 100000)
list = []
for num in howMuch:
    print("")


'''
with open(str(nome_rand)+".txt","w") as file:
    for i in range(10):
        list.append(random.randint(1,10)) 
        file.write(str(list[i]))
        file.write("\n")
'''

