#!/usr/bin/python3

inputfile = open("Day2.in")

total = 0

def getdiv_if_evenlydiv(a,b):
    if (a%b == 0):
        return a/b
    else:
        return 0

for line in inputfile:
    #For removing stray '\n's
    line = line.strip()
    #Getting each number split into a different index of a list
    linelist = line.split('\t')
    #Transforming the list of strings into a list of integers
    linelist = list(map(int, linelist))
    ###
    #Using list comprehension to generate new list for each item
    for item in linelist:
        templist = [getdiv_if_evenlydiv(item, x) for x in linelist]
        #print(templist)
        #The -1 is to subtract the own element, which is divisible by itself and results in 1 (a/a = 1)
        total += sum(templist) - 1

inputfile.close()

print(total)
