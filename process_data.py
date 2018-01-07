masterDict = {}
winnerFile = open("superbowl_winner.txt")
for line in winnerFile:
    fields = line.split("|")
    # take year as an int because want to add one to it later
    year = int(fields[0])
    code = fields[3].rstrip()
    team = fields[1]
    count = 0
    dataFile = open("totalBirths.txt")
    for line in dataFile:
        fields = line.split("|")
        yearAbove = year+1
        yearBelow = year-1
        # find the year before the year they won and they year after and find the average num of  births for those two births
        if (fields[0] == str(yearAbove) or fields[0] == str(yearBelow)) and fields[2] == str(code):
            births = int(fields[3].rstrip())
            count += births
    avg = count/2
    dataFile.close()
    # go through the file again to find the total births for the winning year
    dataFile = open("totalBirths.txt")
    for line in dataFile:
        fields = line.split("|")
        if fields[0] == str(year) and fields[2] == str(code):
            numBirths = int(fields[3].rstrip())
            masterDict[year] = team, numBirths, avg, code
    dataFile.close()

fout = open("winner_averages.txt", "w")    
for key in masterDict:
    year = key
    team = masterDict[key][0]
    numBirths = masterDict[key][1]
    avgBirths = masterDict[key][2]
    code = masterDict[key][3]
    fout.write(str(year) + "|" + str(team) + "|" + str(numBirths) + "|" + str(avgBirths) + "|" + str(code) + '\n')
fout.close()
    
            
        
