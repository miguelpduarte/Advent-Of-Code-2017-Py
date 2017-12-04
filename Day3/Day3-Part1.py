#!/usr/bin/python3

input = 289326
#input = 1024

#The bottom right corner of level n is given by (2*n+1)^2 (This is the largest number in that certain loop of the spiral)
#Examples:
#The first level is n=0, with the only element being 1
##(2*0+1)^2 = 1^2 = 1 
#The second level is n=1, with the bottom right corner (and max element in this level) being 9
##(2*1 + 1)^2 = 3^2 = 9
#The third level is n=2, with the max element being 25
##(2*2 + 1)^2 = 5^2 = 25
#The fourth level is n=3, with the max element being 49
##(2*3 + 1)^2 = (6+1)^2 = 7^2 = 49

#The first element of a level always has distance equal to the n of that level + the n of the previous level
#The distance in a level varies between the level n (cardinal directions) and level n*2 (corners)

print("The input is %d" % (input))

######
i = 0
num = 0
lvlmaxes = []
while(num < input):
   num = (2*i + 1) ** 2
   lvlmaxes.append(num)
   i+=1

print(lvlmaxes)
#print("i = %d" % (i))

inputn = i - 1
#At this point inputn is the n of the level of the input (we have to decrement 1 due to how the loop is built)
print("input n: %d" % (inputn))

#The distance of the first element of a certain level is always its n + (n-1) which is the same as 2*n-1

#For each element in a line, its distance can be given by n+k, in which k belongs to [0,n]
#The value of k goes back and forth, by starting to lower until it is 0 and then come back up
#The initial value of k is the line n - 1
#k = inputn - 1
#The delta is the current step of k
#delta = -1

dist = 0

#Calculating each corner of level n
corners = []
for x in range(0, 4):
    corners.append(lvlmaxes[len(lvlmaxes)-1] - x*(inputn * 2))
    if input == corners[x]:
        dist = inputn*2
        break

print(corners)


if dist == 0:
    for y in range(0, 3):
        if (input < corners[y]) and (input > corners[y+1]):
            dist = inputn*2 - min(abs(input - corners[y]), abs(input - corners[y+1]))
            break

print("The distance is %d" % (dist))
