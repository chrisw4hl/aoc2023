def countWays(time, dist):
    count = 0
    for i in range(time):
        if i > (dist//(time-i)):
            count = count + 1
    return count


with open("6.txt") as file:
    times = file.readline()
    times = times.split(":")
    times = times[1][:-1]
    times = times.strip()#.split(" ")

    dist = file.readline()
    dist = dist.split(":")
    dist = dist[1][:-1]
    dist = dist.strip()#.split(" ")

    #while "" in times:
    #    times.remove("")
    #while "" in dist:
    #    dist.remove("")

    print(times)
    print(dist)
    res = 1
    #for i in range(len(times)):
    res = res*countWays(int(times),int(dist))

    print(res)

    
