BEGIN{
    if (system("wget www.pro-football-reference.com/super-bowl/ -O superbowl.html")){
	print "wget did not run correctly" > "/dev/stderr"
	exit 1
    }

    input = "./superbowl.html"
    regex = "\"game_date\" >[^,]+, ([^<]+)[^A-Z]+[A-Z]+[^A-Z]+([^<]+)"

    while ((getline < input) > 0){
	line = $0
	if(match(line, regex, arr))
	    print arr[1] "|" arr[2] > "./superbowl_winner.txt"
    }

    if (close(input)){
	print "Could not close" input > "/dev/stderr"
	exit 1
    }
}
    
    
