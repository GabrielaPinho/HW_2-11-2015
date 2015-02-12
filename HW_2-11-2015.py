
import re

a = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

# Write a program that will print only the accession names that satisfy the following criteria – treat each criterion separately:

#contain the number 5

for i in a:
    if re.search("5", i):
        print (i)

#contain the letter d or e

for i in a:
    if re.search("d|e", i):
        print (i)

#contain the letters d and e in that order

for i in a:
    if re.search("d.*e", i):
        print (i)

#contain the letters d and e in that order with a single letter between them

for i in a:
    if re.search("d\we", i):
        print (i)

#contain both the letters d and e in any order

for i in a:
    if re.search("d.*e", i) or re.search("e.*d", i):
        print (i)

#start with x or y

for i in a:
    if re.search("^[xy]", i):
        print (i)

#start with x or y and end with e

for i in a:
    if re.search("^[xy].*e$", i):
        print (i)

#contain three or more numbers in a row 

for i in a:
    if re.search("\d{3,}", i):
        print (i)

#end with d followed by either a, r or p

for i in a:
    if re.search("d[arp]$", i):
        print (i)

