#!/usr/bin/python3

inputfile = open("Day5.in")

passphrases = inputfile.readlines()
inputfile.close()

passphrases = list(map(str.strip, passphrases))

#print(passphrases)

validcounter = 0

for passphrase in passphrases:
    #print(passphrase)
    passlist = passphrase.split(' ')
    #print(passlist)
    
    #Constructs a set (unique items only) and checks its length against the length of the original list
    #Pretty efficient since the C code or whatever inside Python is doing the heavy lifting, no?
    validcounter += (len(passlist) == len(set(passlist)))

print(validcounter)
