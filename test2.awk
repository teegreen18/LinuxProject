BEGIN{
    input_path = "/data/raw/CDCbirths/"
    file_name = "Nat2000us.pb.gz"

    inputCommand = "zcat " input_path file_name

    while((inputCommand | getline) > 0){
       	nPos = split($0, arr, "")
	region = arr[11]
	division = arr[12]
	state = arr[13]
	month1 = arr[172]
	month2 = arr[173]
	# for 2000, need to access St. Louis average # births per month
	if((region == 2) && (division == 4) && (state == 3)){
	    #print region division state                         # this is Missouri code
	    if((month1 == 0) && (month2 == 1))
		MJanCount++
	    else if((month1 == 0) && (month2 == 4))
		MAprCount++
	    else if((month1 == 0) && (month2 == 7))
		MJulCount++
	    else if((month1 == 1) && (month2 == 0))
		MOctCount++
	    else if((month1 == 1) && (month2 == 1))
		MNovCount++
	}
	# compare to births in another city of similar population, in this year's case, Tennessee 
	else if((region == 3) && (division == 6) && (state == 2)){
	    if((month1 == 0) && (month2 == 1))
		JanCount++
	    else if((month1 == 0) && (month2 == 4))
		AprCount++
	    else if((month1 == 0) && (month2 == 7))
		JulCount++
	    else if((month1 == 1) && (month2 == 0))
		OctCount++
	    else if((month1 == 1) && (month2 == 1))
		NovCount++
	}
    }
    # compare amount of Nov births to the rest
    print "Missouri- Jan: " MJanCount " April: " MAprCount " July: " MJulCount " October: " MOctCount " November: " MNovCount
    print "Tennessee- Jan: " JanCount " April: " AprCount " July: " JulCount " October: " OctCount " November: " NovCount
}
