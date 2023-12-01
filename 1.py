def part1(data):
    calibs = []
    for letters in data:
        numbers = [char for char in letters if char.isdigit()]
        calib = int(numbers[0] + numbers[-1])
        calibs.append(calib)
    print(sum(calibs))


def find_first_and_last_occurrences(text):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    words.extend(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    first_occurrence = None
    last_occurrence = None
    first_index = float('inf')
    last_index = -1

    for word in words:
        current_first = text.find(word)
        if 0 <= current_first < first_index:
            first_index = current_first
            first_occurrence = word

        current_last = text.rfind(word)
        if current_last > last_index:
            last_index = current_last
            last_occurrence = word

    if(not first_occurrence.isdigit()):
        first_occurrence = words.index(first_occurrence) +1

    if(not last_occurrence.isdigit()):
        last_occurrence = words.index(last_occurrence) +1

    return int(str(first_occurrence) + str(last_occurrence))

def part2(data):
    calibs = []
    for letters in data:
        calibs.append(find_first_and_last_occurrences(letters))
    print(sum(calibs))

def main():
    f = open("1.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    part2(data)

if __name__ == "__main__":
    main()