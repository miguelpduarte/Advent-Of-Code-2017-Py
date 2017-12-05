#!/usr/bin/python3

inputfile = open("Day4.in")

cmds = inputfile.readlines()
inputfile.close()

cmds = list(map(str.strip, cmds))
cmds = list(map(int, cmds))


currindex = 0
oldindex = 0
nsteps = 0

while(currindex >= 0 and currindex < len(cmds)):
    currindex += cmds[currindex]
    cmds[oldindex] += 1
    nsteps += 1
    oldindex = currindex

print(nsteps)
