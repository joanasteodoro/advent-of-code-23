import re

def readInput():
    input = open('input.txt', 'r')
    return input.readlines()

def cleanLines(lines):
    i = 1
    for line in lines:
        line = line.replace('\n', '')
        line = line.replace('Card ' + str(i) + ': ', '')
    return lines

def extractNumbers(line):
    winningPart = line.split('|')[0]
    chosenPart = line.split('|')[1]
    winningNumbers = list(re.findall(r'\d+', winningPart))
    chosenNumbers = list(re.findall(r'\d+', chosenPart))
    return [winningNumbers, chosenNumbers]


def computeCardTotal(numbers):
    winningNumbers = numbers[0]
    chosenNumbers = numbers[1]

    matches = [number for number in chosenNumbers if number in winningNumbers]
    print('matches', matches)
    if len(matches) == 0:
        return 0
    return pow(2, len(matches)-1)

def partOne():
    lines = readInput()
    lines = cleanLines(lines)
    cardTotal = 0
    for line in lines:
        numbers = extractNumbers(line)
        cardTotal += computeCardTotal(numbers)
        print('cardTotal', cardTotal)
        
    return cardTotal

print(partOne())