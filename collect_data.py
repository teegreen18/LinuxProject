import gzip

files = ["Nat1993.gz", "Nat1994.gz", "Nat1995.gz", "Nat1996.gz", "Nat1997.gz", "Nat1998.gz", "Nat1999.gz", "2000", "2001", "2002"]
masterData = {}
usedCodes = []

# open the text file of superbowl winners
textFile = open("superbowl_winner.txt")
# for each line of the winners
for line in textFile:
    # extract the county code, which is the 4 field of the pipe delimited file
    fields = line.split("|")
    team = fields[1]
    code = fields[3].rstrip()
    # start year the year before, files go in choronological order
    year = 1992
    # if that country code is not already in the usedCodes, then search for it in the births dataset
    if code not in usedCodes:
        # add it to usedCodes list
        usedCodes.append(code)
        # loop through all the qzip files of birth records
        for fileName in files:
            # add 1 to the year, because the list of CDC records are in chronological order
            year += 1
            # initialize count for number of births that are in correct country and Nov of that year
            count = 0
            # open the file
            dataFile = gzip.open(fileName, "rt")
            # for each line in births dataset
            for line in dataFile:
                line = str(line) # make sure it is a string
                # turn the string of numbers into separate numbers using list()
                fields = list(line)
                # the 4 number code of the county are these fields
                dataCode = str(fields[53] + fields[54] + fields[55] + fields[56])
                month1 = fields[171]
                month2 = fields[172]
                # if the county code is correct and the month is Nov
                if (dataCode == str(code)) and (month1 == str(1)) and (month2 == str(1)):
                    # add 1 to count
                    count += 1
            masterData[year, code] = team, count
            dataFile.close()
# write the contents of the dictionary to a pipe-delimited file
fout = open("totalBirths.txt", "w")
# the key in the master dict is the year
for key in masterData:
    code = key[1]
    births = masterData[key][1]
    team = masterData[key][0]
    year = key[0]
    # don't use sep="|" because .write doesn't take arguments
    fout.write(str(year) + "|" + str(team) + "|" + str(code) + "|" + str(births) + '\n')
fout.close()

    
