#!/usr/bin/python3

def isListInList(small, big):
    """Returns true if the small list is a list located inside the big list"""
    #Empty list is always found (empty is a subset of every set, good ole quick maths)
    if not small:
        return False

    try:
        #list.index raises ValueError when value is not found so this should suffice
        big.index(small)

    except ValueError:
        return False

    return True

def redistributeBlocks(banklist):
    #getting the index of the max value
    maxindex = banklist.index(max(banklist))
    #Clearing the index and redistributing the blocks
    blockstodistribute = banklist[maxindex]
    banklist[maxindex] = 0
    
    #Main redistribution
    #Starting at the value after the old maxblock
    i = maxindex + 1
    while blockstodistribute > 0:
        #Resetting the iteration in order to cycle through it
        if i == len(banklist):
            i = 0
        
        banklist[i] += 1
        blockstodistribute -= 1

        i += 1


inputfile = open("Day6.in")

banksstr = inputfile.readline()
inputfile.close()

#Removing newlines ughhhh
banksstr = banksstr.strip()

#Splitting the banks string into a banks list
bankslist = banksstr.split('\t')

#Because bankslist insists in being strings, converting them all into ints
bankslist = list(map(int, bankslist))

itercounter = 0
blockcyles = 0
configlist = []

# list() is used to actually copy the list into the configlist, otherwise we would be storing a reference:
# as bankslist was changed so was the contents of configlist - this is not what we want
configlist.append(list(bankslist))

print(bankslist)

while True:
    itercounter += 1

    #redistributeBlocks now returns the number of cycles (for part 2)
    redistributeBlocks(bankslist)

    print(bankslist)
    #print(configlist)

    
    #Lists are sadly not hashable so we have to go with this solution
    if isListInList(bankslist, configlist):
        break

    #Appending only after searching to not have false positives...
    configlist.append(list(bankslist))

print(itercounter)
#In part 2 what we want is the number of distributions that happened between the first and second ocurrence of the first value that is repeated
#As such, since after exiting the loop bankslist holds that repeated value, we need simply subtract from the total of iterations the index of the last configuration in the list of configurations
#Since the configurations were appended to the list in the order of their generation, this is an easy solution
print("Part 2 result: ", itercounter - configlist.index(bankslist))
