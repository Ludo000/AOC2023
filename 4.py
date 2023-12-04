def part1(data):
    count = 0
    for line in data:
        print(line)
        winningNumbers = list(set(line[0]) & set(line[1]))
        print(winningNumbers)
        if(len(winningNumbers) == 0): 
            points=0
        else: 
            points = max(1,2 ** (len(winningNumbers)-1))
        print("points", points)
        count += points
    print("part1: ", count)

def part2(data):
    cards = {i: 1 for i in range(len(data))}
    cardsN = len(data)
    print(cardsN)
    while not all(value == 0 for value in cards.values()):
        for key in cards:
            if(cards[key] !=0):
                cards[key] = max(0, cards[key] - 1)
                winningNumbers = list(set(data[key][0]) & set(data[key][1]))
                for j in range(key+1, key+len(winningNumbers)+1):
                    cardsN += 1
                    if j in cards:
                        cards[j] +=1
                    else:
                        cards[j]=1
                break
        
    print(cards)
    print("parts 2", cardsN)
            



def main():
    f = open("4.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append([line.rstrip("\n").split("|")[0].split(':')[1].strip().split(),line.rstrip("\n").split("|")[1].strip().split()])
    part1(data)
    part2(data)

if __name__ == "__main__":
    main()