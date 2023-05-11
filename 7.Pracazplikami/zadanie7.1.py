from os import path

dir_path = path.dirname(__file__)
filname="tekst.txt"
data_path=path.join(dir_path, filname)

with open(data_path,"r", encoding="utf-8") as f:
    file_lines = f.readlines()
    print(file_lines)

def ilosc_slow(filename):
    with open(filename, 'r') as file:
        ilosc=file.read()
        ilosc_slow = len(ilosc.split())
        return ilosc_slow

print(ilosc_slow)