all: totalBirths.txt winner_averages.txt plot.pdf

totalBirths.txt: collect_data.py superbowl_winner.txt Nat1993.gz Nat1994.gz Nat1995.gz Nat1996.gz Nat1997.gz Nat1998.gz Nat1999.gz 2000 2001 2002 
	python3 collect_data.py

winner_averages.txt: process_data.py superbowl_winner.txt totalBirths.txt
	python3 process_data.py

plot.pdf: plot.py
	python3 plot.py

clean:
	 rm totalBirths.txt winner_averages.txt plot.pdf
