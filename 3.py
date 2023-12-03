def part1(data):
    with open('output.html', 'w') as html:
        print("<html><body><table>", file=html)

        numberNotPart = []
        for h in range(len(data)):
            print("<tr>", file=html)
            isNumber = False
            currentNumber= ""
            currentIsNotPart = True
            for i in range(len(data[h])):
                if(data[h][i].isdigit()):
                    isNumber = True
                    currentNumber += data[h][i]
                    
                    for k in range(max(h-1,0), min(h+2, len(data))):
                        for j in range(max(i-1,0), min(i+2, len(data[h]))):
                            if(data[k][j] != "." and not data[k][j].isdigit()):
                                currentIsNotPart = False
                                break
                        if(not currentIsNotPart):
                            break
                        
                if(not data[h][i].isdigit() or i == len(data[h])-1):
                    if(isNumber):
                        isNumber = False
                        numberNotPart.append([currentNumber, currentIsNotPart])
                        currentIsNotPart= True
                        currentNumber = ""
                    else:
                        isNumber = False
                if(not data[h][i].isdigit() and data[h][i] != "."):
                    print("<td style=\"color:red;border: 1px solid #d5d5d5; text-align:center;min-width:1rem;\"><b>",data[h][i], "</b></td>", file=html)
                elif(currentIsNotPart):
                    print("<td style=\"border: 1px solid #d5d5d5; text-align:center;min-width:1rem;\"><b>",data[h][i], "</b></td>", file=html)
                else:
                    print("<td style=\"color:green;border: 1px solid #d5d5d5; text-align:center;min-width:1rem;\"><b>", data[h][i], "</b></td>", file=html)
                    
            print("<tr/>", file=html)


        print("</table><br/>", file=html)
        for pair in numberNotPart:
            if not pair[1]: print("+", pair[0], file=html)
        sumPart = sum(int(pair[0]) for pair in numberNotPart if not pair[1])
        print("<br/><br/>=", sumPart, file=html)
        print("part1: ", sumPart)
        print("</body></html>", file=html)
                    
                
def part2(data):
    digitAdjs = []
    for h in range(len(data)):
        for i in range(len(data[h])):
            if(data[h][i] == "*"):
                digitAdj = {}
                for k in range(max(h-1,0), min(h+2, len(data))):
                    for j in range(max(i-1,0), min(i+2, len(data[h]))):
                        if(data[k][j].isdigit()):
                            l=0
                            while(j-l >= 0 and data[k][j-l].isdigit()):
                                l += 1
                            
                            digitAdj[(h-k,j-i-l)] = ""
                            n=1
                            
                            while(j-l+n < len(data[k]) and data[k][j-l+n].isdigit()):
                                digitAdj[(h-k,j-i-l)] += data[k][j-l+n]
                                n += 1

                digitAdjs.append(digitAdj)

    result = [multiply_values_if_two_fields(d) for d in digitAdjs]
    filtered_result = [value for value in result if value is not None]
    print("part2:", sum(filtered_result))

def multiply_values_if_two_fields(d):
    if len(d) == 2:
        values = list(d.values())
        return int(values[0]) * int(values[1])
    return None


                


def main():
    f = open("3.txt", "r")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        data.append(line.rstrip("\n"))
    part1(data)
    part2(data)

if __name__ == "__main__":
    main()