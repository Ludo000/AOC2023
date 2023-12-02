from functools import reduce
import operator

def part1(data):
    maxNCube = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    count = 0
    for h in range(len(data)):
        game = format_game_input(data[h])
        possible = True
        for i in range(len(game)):
            if "red" in game[i] and game[i]["red"] > maxNCube["red"]:  
                possible = False
            if "green" in game[i] and game[i]["green"] > maxNCube["green"]:  
                possible = False
            if "blue" in game[i] and game[i]["blue"] > maxNCube["blue"]:  
                possible = False
        if possible:
            count += h+1
    print("part1:", count)

def part2(data):
    count = 0
    for h in range(len(data)):
        maxNCube = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        game = format_game_input(data[h])
        for i in range(len(game)):
            if "red" in game[i] and game[i]["red"] > maxNCube["red"]:  
                maxNCube["red"] = game[i]["red"]
            if "green" in game[i] and game[i]["green"] > maxNCube["green"]:  
                maxNCube["green"] = game[i]["green"]
            if "blue" in game[i] and game[i]["blue"] > maxNCube["blue"]:  
                maxNCube["blue"] = game[i]["blue"]
        power = reduce(operator.mul, maxNCube.values(), 1)
        count += power
    print("part2:", count)




def format_game_input(input_str):
    _, game_str = input_str.split(':', 1)
    steps = game_str.split(';')
    formatted_games = []
    for step in steps:
        components = step.split(',')
        game_data = {}
        for component in components:
            parts = component.strip().split(' ')
            if len(parts) == 2:
                number, color = parts
                number = int(number)
                if color in game_data:
                    game_data[color] += number
                else:
                    game_data[color] = number
        if game_data:
            formatted_games.append(game_data)

    return formatted_games



def main():
    f = open("2.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    part1(data)
    part2(data)

if __name__ == "__main__":
    main()