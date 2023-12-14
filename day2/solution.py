#only 12 red cubes, 13 green cubes, and 14 blue cubes
def readInput():
    input = open('input.txt', 'r')
    return input.readlines()

def processLine(line, id):
    line = line.replace('Game ' + str(id) + ': ', '')
    line = line.replace(' ', '')
    line = line.replace(';', ',')
    line = line.split(',')
    return line

def discardImpossibleGameSets(lines):
    ids = []
    number = 0
    color = ''
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

def partOne():
    lines = readInput()
    #lines = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
    ids = discardImpossibleGameSets(lines)
    return sum(ids)


print(partOne())