import os
path = os.getcwd()
myList = []
for root, dirs, files in os.walk(path):
	for file in files:
            if(file.endswith(".txt")):
                #print(file)
                with open(file, encoding='utf-8') as f:
                    
                    text = f.read()
                    new_i = text.split("\n")
                    #print(new_i[0])
                    new = open("hashall.txt", 'a')
                    new.write(f'{new_i[0]}\n')
                    new.close
                    new2 = open("vseostalnoe.txt", 'a')
                    new2.write(f'{new_i[2]}\n' + f'{new_i[3]}\n'+ f'{new_i[1]}\n' + "*************************\n")
                    new2.close
                    
            