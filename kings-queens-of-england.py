# Kings & Queens of England - www.101computing.net/kings-queens-of-england/

print("*****************************")
print("*       Kings & Queens      *")
print("*         of England        *")
print("*****************************")
print("")

year = int(input("Enter a year between 757 and 2017:"))

file = open("Files/Monarchs-of-England.csv", "r")
for line in file.readlines():
    data =line.strip().split(",")
    start = int(data[0])
    end = int(data[1])
    rng = range(start,end+1)
    if year in rng:
        print(res[2])
    
        

file.close()
