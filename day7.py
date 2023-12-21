score = {"A":"e","K":"d","Q":"c","J":"b","T":"a"}
ranking = [0]

def order(line):
    line = line.split(" ")
    val = line[1][:-1] 
    #hand = line[0]
    hand = sorted(line[0])
    secondPair = 0
    firstPair = 0
    notPair = 0
    count = 0
    for i in range(1,len(hand)):
        if (hand[i] == hand[i-1]):
            if (firstPair == 0):
                count = count + 1
                firstPair = 1
            elif (notPair == 1):
                count = count + .5
                notPair = 0 
            elif (firstPair == 1):
                count += 1
                secondPair = 1
        elif (firstPair == 1):
            notPair = 1


    return [count, line[0], val]

allHands = []
with open("7.txt","r") as file:
    for line in file:
        newLine = order(line)
        allHands.append(newLine)


allHands.sort(key = lambda k: k[0],reverse=True)

fiveOfKind = []
fourOfKind = []
fullHouse = []
threeOfKind = []
twoPair =[]
onePair = []
highCard = []

for hand in allHands:
    if hand[0] == 4:
        fiveOfKind.append(hand)
    elif hand[0] == 3:
        fourOfKind.append(hand)
    elif hand[0] == 2.5:
        fullHouse.append(hand)
    elif hand[0] == 2:
        threeOfKind.append(hand)
    elif hand[0] == 1.5:
        twoPair.append(hand)
    elif hand[0] == 1:
        onePair.append(hand)
    else:
        highCard.append(hand)

buckets = [fiveOfKind,fourOfKind,fullHouse,threeOfKind,twoPair,onePair,highCard]
for bucket in buckets:
    for hand in bucket:
        hold = ""
        for char in hand[1]:
            if char in score.keys():
                hold= hold + score[char]
            else:
                hold = hold + char
        hand.append(hold)


for bucket in buckets:
    bucket.sort(key=lambda k: k[3],reverse=True)

rank = 1
result = 0

for bucket in reversed(buckets):
    for hand in reversed(bucket):
        result += int(hand[2])*rank
        rank += 1

print(result)


