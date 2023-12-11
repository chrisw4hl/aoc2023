result = 0
result2 = 0

def getVals(lineSeg):
    out =[]
    for entry in lineSeg:
        if entry.isnumeric():
            out.append(int(entry))
    return out

def part1(line):
    output = 0  
    
    winners = getVals(line[0])
    card = getVals(line[1])

    points = 0
    for num in winners:
        if num in card:
            if points == 0:
                points = 1
            else:
                points = points*2

    output = output + points
    return output

def part2(line, duplicates, curLine):
    output = 0

    winners = getVals(line[0])
    card = getVals(line[1])

    count = 0
    for num in winners:
        if num in card:
            count = count + 1
    for j in range(duplicates[curLine]):
        for i in range(1,count+1):
            duplicates[curLine+i] = duplicates[curLine+i]+1
        
    return duplicates
        


with open("4.txt","r") as file:
    duplicates = [1, 1, 1, 1, 1, 1]
    fileLen = num_lines = sum(1 for _ in open('4.txt'))

    duplicates = [1]*fileLen
    lineNum = 0
    for line in file:
        line = line.split(":")
        line = line[1][1:-1]
        line = line.split("|")
        line[0] = line[0][:-1]
        line[1] = line[1][1:]
        
        line[0] = line[0].split(" ")
        line[1] = line[1].split(" ")
        result = result + part1(line)
        
        duplicates = part2(line, duplicates, lineNum)
        
        lineNum = lineNum + 1

print(result)

for line in duplicates:
    result2 = result2 + line

print(result2)

