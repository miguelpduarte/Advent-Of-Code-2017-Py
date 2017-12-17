#!/usr/bin/python3

#Map of comparison operations
oper_map = {
            '>' : (lambda a,b : a>b),
            '<' : (lambda a,b : a<b),
            '>=' : (lambda a,b : a>=b),
            '==' : (lambda a,b : a==b),
            '<=' : (lambda a,b : a<=b),
            '!=' : (lambda a,b : a!=b)
           }

inputfile = open("Day8.in")

#Starting empty register dictionary
reg_dict = dict()

max_reg_val = -5000000

#The format for a line is always:
#regtomodify howtomodify valuetomodifyby "if" regtocompare comparisonoption valuetocompareby

for line in inputfile:
    line = line.strip()
    instruction = line.split(' ')
    
    if instruction[4] not in reg_dict:
        #if the register to compare is not in the register dictionary, then add it
        reg_dict[instruction[4]] = 0
    
    #Verifying condition given
    if oper_map[instruction[5]](reg_dict[instruction[4]], int(instruction[6])):
        #if it verifies, we check if the given register exists and then operate over it
        if instruction[0] not in reg_dict:
            reg_dict[instruction[0]] = 0

        #Operating over given reg
        if instruction[1] == "inc":
            reg_dict[instruction[0]] += int(instruction[2])
        elif instruction[1] == "dec":
            reg_dict[instruction[0]] -= int(instruction[2])
        else:
            print("Operation not supported!")
            exit()

        #Updating the current maximum (by checking against the register that was just possibly updated)
        max_reg_val = max(max_reg_val, reg_dict[instruction[0]])


inputfile.close()

#Printing largest key,value set
key_with_largest_elem = max(reg_dict, key=reg_dict.get)
print(key_with_largest_elem, ": ", reg_dict[key_with_largest_elem])

print(max_reg_val)
