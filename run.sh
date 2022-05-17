#!/bin/sh

python transmitter.py
#python client.py --input_file=input.txt --output_file=output.txt --srv_hostname=iscsrv72.epfl.ch --srv_port=80
python client.py --input_file=input.txt --output_file=output.txt
python receiver.py