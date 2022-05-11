#!/bin/sh

python transmitter.py
#python client.py --input_file=input.txt --output_file=output.txt --srv_hostname=iscsrv72.epfl.ch --srv_port=80
python client.py --input_file=input.txt --output_file=output.txt
python receiver.py

echo "Result is : $(cat final.txt)"

grep -o . initial.txt >> temp1
grep -o . final.txt >> temp2
echo "Number of different characters : $(diff temp1 temp2 | grep '^[1-9]' | wc -l)"

rm temp*