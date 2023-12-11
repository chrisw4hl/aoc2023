def countWays(time, dist):
    count = 0
    for i in range(time):
        if (dist//(time-i)) > i:
            count = count + 1

    return count


with open("6_test.txt") as file:
    times = file.readline()
    times = times.split(":")
    times = times[1][1:-1]
    times = times.strip().split(" ")
    times = times.remove(" ")
    dist = file.readline()
    dist = dist.split(":")
    dist = dist[1][1:-1]
    dist = dist.strip().split(" ")
    dist = dist.remove(" ")
    print(times)
    print(dist)
    res = []
    for i in range(len(times)):
        res[i] = countWays(int(times[i]),int(dist[i]))

    print(res)

    
