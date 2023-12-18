import re
def readInput():
    input = open('input.txt', 'r')
    return input.readlines()

def extractNumbersFromLine(lines):
    numbers = []
    for line in lines:
        numbers.append(re.findall(r'\d+', line))
    return numbers

def checkIfIsPartOfTheEngine(lines, numbers):
    engineNumbers = []
    lineNr = 0
    line = lines[lineNr].replace('\n', '')
    print('line', line)
    numbers = sum(numbers, [])
    for number in numbers:
       print('number',number)
       startIndex = line.find(number)
       endIndex = startIndex + len(str(number)) - 1
       numberIndexes = [i for i in range(startIndex, endIndex+1)]
       sideIndexes = [numberIndexes[0]-1, numberIndexes[-1]+1]
       topIndexes = [i for i in range(numberIndexes[0]+len(line)-11, numberIndexes[-1]+len(line)+2-10)]
       bottomIndexes = [i for i in range(numberIndexes[0]+len(line)-11, numberIndexes[-1]+len(line)+2-10)]
       
       for index in sideIndexes:
           if(index >= 0 and index < len(line) and int(number) not in engineNumbers):
               if(line[index] != '.'):
                   engineNumbers.append(int(number))
                
       if(lineNr != 0):
        print('top. lineNr', lineNr)
        for index in topIndexes:
            lines[lineNr-1] = lines[lineNr-1].replace('\n', '')
            if(index >= 0 and int(number) not in engineNumbers):
                    print('top index: ', index, '| char: ', lines[lineNr-1][index])
                    if(lines[lineNr-1][index] != '.'):
                        engineNumbers.append(int(number))
                        
       if(lineNr != len(lines)-1):
        print('bottom. lineNr', lineNr)
        for index in bottomIndexes:
                lines[lineNr+1] = lines[lineNr+1].replace('\n', '')
                if(index >= 0 and index < len(lines[lineNr]) and int(number) not in engineNumbers):
                    print('bottom index: ', index, '| char: ', lines[lineNr+1][index])
                    if(lines[lineNr+1][index] != '.'):
                        engineNumbers.append(int(number))
        
       lineNr += 1
    return engineNumbers

def partOne():
    lines = readInput()
    lines= ['467..114..\n', '...*......\n', '..35..633.\n']
    numbers = extractNumbersFromLine(lines)
    engineNumbers = checkIfIsPartOfTheEngine(lines, numbers)
    print('engineNumbers', engineNumbers)
    return sum(engineNumbers)


print(partOne())