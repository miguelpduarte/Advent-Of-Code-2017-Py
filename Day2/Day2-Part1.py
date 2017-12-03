#!/usr/bin/python3

inputfile = open("Day2.in")

totalchecksum = 0

for line in inputfile:
    #For removing stray '\n's
    line = line.strip()
    #Getting each number split into a different index of a list
    linelist = line.split('\t')
    #Transforming the list of strings into a list of integers so that min and max work as expected
    linelist = list(map(int, linelist))
    totalchecksum += max(linelist) - min(linelist)

inputfile.close()

print(totalchecksum)
