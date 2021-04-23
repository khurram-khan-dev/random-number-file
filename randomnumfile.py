import random
import os
# file having 10 number

def create_file(filename,NumQuant):

    save_path = 'C:/Users/CoreCom/Desktop/khurram/6th semester/design and analysis'

    completename = os.path.join(save_path,filename)


    f1 = open(completename,"w")
    for i in range(0,NumQuant):
        n = random.randint(1,1000)
        f1.write(str(n)+ " ")

    f1.close()

create_file("ten.txt",10)
create_file("hundred.txt",100)
create_file("thousand.txt",1000)
create_file("tenthousand.txt",10000)
create_file("lac.txt",100000)
