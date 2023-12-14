def readInput():
    input = open('input.txt', 'r')
    return input.readlines()

def extractNumbers(line):
    lineNumbers = []
    for char in line:
        if char.isdigit():
            lineNumbers.append(char)

    return lineNumbers

def renameExtendedNumbers(line):
    line = line.replace('zerone', '01')
    line = line.replace('oneight', '18')
    line = line.replace('twone', '21')
    line = line.replace('threeight', '38')
    line = line.replace('fiveight', '58')
    line = line.replace('sevenine', '79')
    line = line.replace('eightwo', '82')
    line = line.replace('eighthree', '83')
    line = line.replace('nineight', '98')
    line = line.replace('zero', '0')
    line = line.replace('one', '1')
    line = line.replace('two', '2')
    line = line.replace('three', '3')
    line = line.replace('four', '4')
    line = line.replace('five', '5')
    line = line.replace('six', '6')
    line = line.replace('seven', '7')
    line = line.replace('eight', '8')
    line = line.replace('nine', '9')
    return line

def getAllNumbers(lines, part):
    allNumbers = []
    for line in lines:
        if part == 2:
            line = renameExtendedNumbers(line)
        lineNumbers = extractNumbers(line)
        allNumbers.append(lineNumbers[0] + lineNumbers[-1])

    return allNumbers

def getSumOfNumbers(allNumbers):
    finalSum = 0
    for number in allNumbers:
        finalSum += int(number)

    return finalSum

def partOne():
    lines = readInput()
    allNumbers = getAllNumbers(lines, 1)
    finalSum = getSumOfNumbers(allNumbers)

    print(finalSum)


def partTwo():
    lines = readInput()
    allNumbers = getAllNumbers(lines, 2)
    finalSum = getSumOfNumbers(allNumbers)

    print(finalSum)


print('Part 1:')
partOne()
print('Part 2:')
partTwo()
