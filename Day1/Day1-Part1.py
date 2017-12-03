#!/usr/bin/python3

input_file = open("Day1.in", "r")

rawtext = input_file.read()

input_file.close()

#Removing whitespace (Trimming the string)
rawtext = rawtext.strip()

#Removing any undesired newlines
rawtext = rawtext.replace('\n', '')

sum = 0

for i in range(0, len(rawtext)-1):
    if  (rawtext[i] == rawtext[i+1]):
        sum += int(rawtext[i])

#Because the list is circular, we should also check the beggining with the end
if (rawtext[0] == rawtext[len(rawtext)-1]):
    sum += int(rawtext[0])

print(sum)
