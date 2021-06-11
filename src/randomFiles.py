import random, string, os

os.chdir =str(os.getcwd())+"/FilesCreated"
howMuch = int(random.randint(1, 100000))

list = []
for num in range(howMuch):
    print()
print(num)


'''
with open(str(nome_rand)+".txt","w") as file:
    for i in range(10):
        list.append(random.randint(1,10)) 
        file.write(str(list[i]))
        file.write("\n")
'''

