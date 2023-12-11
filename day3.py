allNums = {}
symbols = {}
surround = []
lenLine = 0

def part1():
    global surround
    result = 0
    for k,j in symbols:
        y = k
        x = j
        surround = (list (set(surround+[(y-1,x),(y-1,x-1),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)])))
             
    for key,val in allNums:
        partNum = allNums[(key,val)]
        lenNum = len(partNum)
        if ((lenNum == 3) and (((key,val) in surround) or ((key,val+1) in surround) or ((key,val+2) in surround))):
            result = result + int(partNum)
        elif ((lenNum == 2) and (((key,val) in surround) or ((key,val+1) in surround))):
            result = result + int(partNum)
        elif (key,val) in surround:
            result = result + int(partNum)

    return result

def part2():
    global symbols
    global allNums
    nums = {}
    gearSum = 0

    for key,value in allNums:
        if len(allNums[(key,value)]) == 3:
            nums[(key,value)] = int(allNums[(key,value)])
            nums[(key,value+1)] = int(allNums[(key,value)])
            nums[(key,value+2)] = int(allNums[(key,value)])
        
        elif len(allNums[(key,value)]) == 2:
            nums[(key,value)] = int(allNums[(key,value)])
            nums[(key,value+1)] = int(allNums[(key,value)])
        
        elif len(allNums[(key,value)]) == 1:
            nums[(key,value)] = int(allNums[(key,value)])

    for key,val in symbols:
        count = 0
        gearVal = 1
        y = key
        x = val
        gearVals = []
        for tup in [(y-1,x),(y-1,x-1),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]:
            if tup in nums.keys():
                if nums[tup] in gearVals:
                    pass
                else:
                    count = count + 1
                    gearVal = gearVal*nums[tup]
                    gearVals.append(nums[tup])
            
        if count == 2:
            gearSum = gearSum + gearVal
    return gearSum
        

with open("3.txt","r") as file:
    lineNum = 0
    for line in file:
        cont = 0
        holdStart = 0
        
        lenLine = len(line)
        for ind in range(lenLine):
            if ((cont == 0) and line[ind].isnumeric()):
                allNums[(lineNum,ind)] = line[ind]     
                holdStart = ind
                cont = 1
            elif line[ind].isnumeric():
                allNums[(lineNum,holdStart)] = allNums[(lineNum, holdStart)] + line[ind]
            elif line[ind] in ["+","*","/","&","%","@","=","#","$","-"]:
                symbols[(lineNum,ind)] = line[ind]
                holdStart = 0
                cont = 0
            else:
                cont = 0
                holdStart = 0
        lineNum = lineNum + 1

    output = part1()
    print(output)
    output2 = part2()
    print(output2)
