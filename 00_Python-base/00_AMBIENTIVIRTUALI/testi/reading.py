path = "bravostudente.txt"
path2 = "AMBIENTIVIRTUALI/testi/bravostudente.txt"

with open(path2, "r") as f:
    testo = f.readlines()
    
print(testo)