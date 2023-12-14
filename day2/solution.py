#only 12 red cubes, 13 green cubes, and 14 blue cubes
def readInput():
    input = open('input.txt', 'r')
    return input.readlines()

def processLine(line, id):
    line = line.replace('Game ' + str(id) + ': ', '')
    line = line.replace('\n', '')
    line = line.replace(' ', '')
    line = line.replace(';', ',')
    line = line.split(',')
    return line

def discardImpossibleGameSets(lines):
    ids = []
    for l in range(len(lines)):
        id = l+1
        line = lines[l]
        processedLine = processLine(line, id)
        for part in processedLine:
            number = int(''.join(filter(str.isdigit, part)))
            color = part.replace(str(number), '')

            if(color == 'red' and number > 12):
                break
            if(color == 'green' and number > 13):
                break
            if(color == 'blue' and number > 14):
                break

        else:
            ids.append(id)
    return ids

def computeLowestNumberOfCubes(line, id):
    lowestPossibleSet = {'red': 0, 'green': 0, 'blue': 0}
    processedLine = processLine(line, id)
    for part in processedLine:
        currentNumber = int(''.join(filter(str.isdigit, part)))
        currentColor = part.replace(str(currentNumber), '')
        if(currentNumber > lowestPossibleSet[currentColor]):
            lowestPossibleSet[currentColor] = currentNumber
    return lowestPossibleSet

def computePower(set):
    return set['red'] * set['green'] * set['blue']


def partOne():
    lines = readInput()
    ids = discardImpossibleGameSets(lines)
    return sum(ids)

def partTwo():
    lines = readInput()
    totalPower = 0
    for l in range(len(lines)):
        id = l+1
        line = lines[l]
        currentSet = computeLowestNumberOfCubes(line, id)
        totalPower += computePower(currentSet)
    return totalPower

print(partOne())
print(partTwo())