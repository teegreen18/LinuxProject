import gzip
files = ["Nat2000us.pb.gz", "Nat2001pb.US.gz"]
code = 7040
year = 1999
for fileName in files:
    # initialize count for number of births that are in correct country and Nov of that year
    count = 0
    year += 1
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
            #print("dataCode expected: ", code, "dataCode actual: ", dataCode, "month1: ", month1, "month2: ", month2, "count: ", count)
    print(year, dataCode, count, sep="|")
        
