#!/usr/bin/python3

input_file = open("Day1.in", "r")

rawtext = input_file.read()

input_file.close()

#Temporary testing
#rawtext = "1212"

#Removing whitespace (Trimming the string)
rawtext = rawtext.strip()

#Removing any undesired newlines
rawtext = rawtext.replace('\n', '')

halfsum = 0

for i in range(0, len(rawtext) // 2):
    if  (rawtext[i] == rawtext[i + len(rawtext) // 2]):
        halfsum += int(rawtext[i])

#Because we were not accounting for circularity
sum = halfsum*2

print(sum)
