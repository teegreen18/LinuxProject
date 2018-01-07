BEGIN{
    input_path = "/data/raw/CDCbirths/"
    file_name = "Nat2000us.pb.gz"
    command = "zcat " input_path file_name

    
    n = split(command, arr, "\n")
    for (i=1; i <= length(arr); i++){
	print arr[i]
    }
}

    
