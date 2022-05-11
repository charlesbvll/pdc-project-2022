#!/bin/sh

let "sum = 0"
let "end = 10"

for (( i = 0; i <= $end; i++ ))
do
    python transmitter.py
    #python client.py --input_file=input.txt --output_file=output.txt --srv_hostname=iscsrv72.epfl.ch --srv_port=80
    python client.py --input_file=input.txt --output_file=output.txt
    python receiver.py

    echo "Result is : $(cat final.txt)"

    grep -o . initial.txt >> temp1
    grep -o . final.txt >> temp2

    let "val = $(diff temp1 temp2 | grep '^[1-9]' | wc -l)"

    echo "Number of different characters : $val"

    let "sum = $sum + $val"

    rm temp*

    # if [ "$i" -ne "$end" ] 
    # then
    #     sleep 30
    # fi 
done

let "total = $end + 1"
echo "The average is :"
echo "scale=2; $sum / $total" | bc -l