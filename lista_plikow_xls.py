import glob
import os

# absolute path to search all text files inside a specific folder
path = r'D:\Desktop\data processing\12 Pomiary REMAG 11_05_2023'
files_lst=[]
for file in os.listdir(path):
    if file.endswith('.xlsx'):
        files_lst.append(file)
print(files_lst)