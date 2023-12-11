#AOC2023 day 1
result = 0
with open("1.txt","r") as file:
    with open("output.txt","w") as output:
        for line in file:
            #line = line.split()
            replaceDict = {"one":"o1e","two":"t2o","three":"t3e","four":"f4r","five":"f5e","six":"s6x","seven":"s7n","eight":"e8t","nine":"n9e"}
            left = 0
            leftLen = 3
            right = len(line)
            rightLen = 3
            while(left < len(line)) and (right>0):
                rightChange = 0
                for leftLen in [3,4,5]:
                    leftVal = line[left:(left+leftLen)]
                    if line[left:(left+leftLen)] in replaceDict.keys():
                        line = line.replace(leftVal,replaceDict[leftVal])
                left = left + 1
            output.write(line)
            firstNum = 0
            lastNum = 0
            for char in line:
                if char.isnumeric():
                    if firstNum == 0:
                        firstNum = int(char)
                    else:
                        lastNum = int(char)
            if lastNum == 0:
                lastNum = firstNum
            result = result + firstNum*10 + lastNum
            if firstNum == 0:
                print("error")
            print(firstNum,lastNum)

print(result)
