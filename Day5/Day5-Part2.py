#!/usr/bin/python3

#Ended up not using this function but keeping it because it looks cool

def isAnagram(w1, w2):
    """True if one word is an anagram of another"""
    #Don't believe it's necessary to create a list from the strings beforehand
    #If checking for strictly anagrams should also check if w1 is different from w2, 'w1 !== w2' should suffice
    return sorted(w1) == sorted(w2)
    
def sortString(s):
    """Returns a sorted string"""
    #Looked ugly doing it in the code
    #Explanation:
    #Sorted returns a list of the elements of s, sorted.
    #join joins every element of that list
    #We must return because a string is an immutable type
    return "".join(sorted(s))

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
    
    #If after sorting each element there are only unique items (see Part 1) then there are no anagrams    

    #Can't use map since we can't modify strings (they are returned, not altered by sortString)
    #Thus, we use list comprehension to generate a new list and assign the old one to that new one
    passlist = [sortString(pw) for pw in passlist]

    validcounter += (len(passlist) == len(set(passlist)))
    

print(validcounter)
