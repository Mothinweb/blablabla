#!/usr/bin/python3

b=["A", "T", "G", "C"]
nuc= []
dna = list(input())

for nuc in dna:
    if nuc not in b:
        print ("sth went wrong")
        break

print("Number of nucleotids:")
print("A: ", dna.count("A"))
print("T: ", dna.count("T"))
print("G: ", dna.count("G"))
print("C: ", dna.count("C"))

com = []

for nuc in dna:

    if nuc=="A":
        com.append("T")
    elif nuc=="T":
        com.append("A")
    elif nuc=="G":
        com.append("C")
    elif nuc=="C":
        com.append("G")

print("Compliment dna: ", com)

s = list(input('Choose dna for searching: '))

pos = []
for i in range (len(dna)-len(s)+1):
    if dna[i:i + len(s)] == s:
        pos.append(i)

print("Founded on positions: ", pos)

