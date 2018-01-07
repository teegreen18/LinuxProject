import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# create a figure instance that will later be written to a pdf
fig = plt.figure()

# create a list to insert the appropriate data
x = []
y1 = []
y2 = []
# keep count of line number because I don't want to include the first and last ones
#count = 0
# go through list of winner births and averages
fin = open("winner_averages.txt")
for line in fin:
    fields = line.split("|")
    numBirths = float(fields[2])
    avgBirths = float(fields[3])
    year = int(fields[0])
    team = fields[1]
    if year < 2002 and year > 1993: 
        x.append(year)
        y1.append(numBirths)
        y2.append(avgBirths)
    
# do the scatter plot
plt.scatter(x, y1, c = 'b')
plt.scatter(x, y2, c = 'r')

# specify the x and y axis labels
plt.xlabel("Year")
plt.ylabel("Number of births")

# legend
red_patch = mpatches.Patch(color='red', label='Average Num of Births')
#plt.legend(handles=[red_patch])

blue_patch = mpatches.Patch(color='blue', label='Num of Births in Winning')
plt.legend(handles=[red_patch, blue_patch])

# save the plot into a pdf
fig.savefig("plot.pdf")

