def convert(seeds, mapping):
    dest = mapping[0]
    source = mapping[1]
    ran = mapping[2]
    out = seeds.copy()
    for ind in range(len(seeds)):
        if ((seeds[ind] >= source) and (seeds[ind] <= source + ran)):
            diff = seeds[ind] - source
            newSeed = dest + diff
            out[ind] = newSeed
    return out


inst = [[],[],[],[],[],[],[]]
def backtrack(loc,seed):
    oldLoc = loc
    out = loc
    for i in reversed(range(7)):
        change = 0
        for test in inst[i]:
            in_ran = test[0]+test[2]
            diff = test[1]-test[0]
            if ((out < in_ran) and (out >= test[0]) and (change == 0)):
                out = out + diff
                change = 1
    for i in [0,2,4,6,8,10,12,14,16,18]:
        if ((out >= seed[i]) and (out <= (seed[i]+seed[i+1]-1))):
            return (out,i)
    return 0

with open("5.txt") as file:
    seeds = file.readline()
    seeds = seeds.split(":")
    seeds = seeds[1][1:-1]
    seeds = seeds.split(" ")
    for ind in range(len(seeds)):
        seeds[ind] = int(seeds[ind])
    constSeeds = seeds.copy()
    lastSeeds = seeds.copy()

    stepCount = -1
    change = [0]*len(seeds)
    for line in file:
        if line[0].isnumeric():
            line = line.split(" ")
            line = [int(line[0]),int(line[1]),int(line[2])]
            inst[stepCount].append(line)
            seedHold = convert(lastSeeds, line)
            for ind in range(len(seedHold)):
                if ((seedHold[ind] != lastSeeds[ind]) and (change[ind] == 0)):
                    seeds[ind] = seedHold[ind]
                    change[ind] = 1
        else:
            change = [0]*len(seeds)
            lastSeeds = seeds.copy()
            stepCount = stepCount + 1

    print(seeds)
    print(min(seeds))
    for i in range(1000000000):
        if (backtrack(i,constSeeds) == 0):
            pass
        else:
            print(i)
            break
        



