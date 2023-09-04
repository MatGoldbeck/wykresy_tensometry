import os

# list to store txt files
res = []
# os.walk() returns subdirectories, file from current directory and 
# And follow next directory from subdirectory list recursively until last directory
for root, dirs, files in os.walk(r"D:\Desktop\Pomiary REMAG 11_05_2023_+JSON"):
    for file in files:
        if file.endswith(".csv"):
            res.append(os.path.join(file))
print(res)
fl = open('items.txt','w')
for the res in items:
	fl.write(res+"\n")
fl.close()

                