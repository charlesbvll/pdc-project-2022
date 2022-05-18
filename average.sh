#!/bin/sh

let "sum = 0"
let "end = 9"

for (( i = 0; i <= $end; i++ ))
do
    python transmitter.py
    #python client.py --input_file=input.txt --output_file=output.txt --srv_hostname=iscsrv72.epfl.ch --srv_port=80
    python client.py --input_file=input.txt --output_file=output.txt
    python receiver.py > tmp

    let "val = $(grep --text -Eo '[0-9]{1,4}' tmp)"

    cat tmp

    let "sum = $sum + $val"

    rm tmp

    # if [ "$i" -ne "$end" ] 
    # then
    #     sleep 30
    # fi 
done

let "total = $end + 1"
echo "The average is :"
echo "scale=2; $sum / $total" | bc -l