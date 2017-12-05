#!/usr/bin/python3

inputfile = open("Day4.in")

cmds = inputfile.readlines()
inputfile.close()

cmds = list(map(str.strip, cmds))
cmds = list(map(int, cmds))


currindex = 0
shift = 0
nsteps = 0

while(currindex >= 0 and currindex < len(cmds)):
    shift = cmds[currindex]
    if shift >= 3:
        cmds[currindex] -= 1
    else:
        cmds[currindex] += 1

    currindex += shift
    nsteps += 1

print(nsteps)
