# LinuxProject
Linux Fall 2017 Project.
As a semester project, my hypothesis was that the “Superbowl Baby phenomenon” is real, meaning that the rise of births increase nine months later in the city of the team that won the Superbowl in February.  From scraping off a website that listed the Superbowl winners and the years, I created a pipe delimited text file that had the year, which team won the Superbowl, and then I hand inserted the corresponding MSA codes for the city.  I used CDC birth records from the years 1993-2002 to extract the number of births in the month of November (nine months after the Superbowl) for each winning city for each of the ten years.  I then calculated the average number of births in each city in the month of November by taking the number of births the year before and after the winning year, to consider that the average of all ten years might not be accurate if population size differed, and found the average of those two years (here I did not take into account teams that won two years in a row, which might be something to work on to make the data more accurate in the future).  When comparing the number of births in November of the winning year to the average number of births in November in the year before and after, I found that there was not a significant increase in the number of births in the winning year.  Therefore, my hypothesis is incorrect in that there is not an unusual surge of the amount of births in winning cities nine months after the Superbowl.  When looking at the PDF plot of data, it is important to recognize that the placement of the plot from year to year has no correlation, since different cities won each year and they have differing number of populations.  Rather, the placement of the red and blue dots for each year shows whether or not there was a significant increase in births.

