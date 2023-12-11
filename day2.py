result = 0
resultPart2 = 0
lineNum = 0

def part1 (line):
    global result
    count = 1
    for ele in line:
        num = int(ele[0])
        color = ele[1]
        if color == "red":
            if num > 12:
                count = 0
        elif color == "green":
            if num > 13:
                count = 0
        elif color == "blue":
            if num > 14:
                count = 0
    if count == 1:
        result = result + lineNum

def part2 (line):
    global resultPart2
    minRed = 0
    minBlue = 0
    minGreen = 0
    for ele in line:
        num = int(ele[0])
        color = ele[1]
        if ((color == "red") and (num > minRed)):
            minRed = num
        elif ((color == "blue") and (num > minBlue)):
            minBlue = num
        elif ((color == "green") and (num > minGreen)):
            minGreen = num

    resultPart2 = resultPart2 + minRed*minBlue*minGreen



with open("2.txt") as file:
    for line in file:
        lineNum = lineNum + 1
        line = line.split(":")
        line = line[1][:-1]
        line = line.replace(";",",")
        line = line.split(",")
        for ele in range(len(line)):
            line[ele] = line[ele][1:]
            line[ele] = line[ele].split(" ")
        print(line)
        #line = line.split(" ")
        part1(line)
        part2(line)
print("Part 1: ",result)
print("Part 2: ",resultPart2)


#part ii






