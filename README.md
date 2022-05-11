# 16QAM Modulation for complex AWGN communication

Transmission of a message over a complex AGWN channel ($Y = \exp{\Theta i} X + Z$, with $\Theta ~ U\[0, 2\pi\]$ and $Z ~ cN(0, \frac{\sigma^2}{2})$ where $\sigma^2 = 10^{-2.65}$)

`numpy` is required to run the script : `pip install numpy`.

The simplest way to run the project is by using `run.sh` while connected to the VPN or without using the `srv_hostname` argument (the noisy channel will be emulated locally, the wanted behavior must be uncommented in the `run.sh` file).
You can also run `average.sh` to run 10 iterations of the program and get the average error (although this might take a while). If you want to use the channel for the server you must uncommment the lines that add a 30sec delay in `average.sh`.

The program can also be ran by hand using :
```sh
python transmitter.py #to generate the encoded input for the client from a file name 'initial.txt'
python client.py --input_file=input.txt --output_file=output.txt --srv_hostname=iscsrv72.epfl.ch --srv_port=80
python receiver.py #to write the decoded output to a file called 'final.txt'
```
or to run it with the locally emulated noisy channel :
```sh
python transmitter.py #to generate the encoded input for the client from a file name 'initial.txt'
python client.py --input_file=input.txt --output_file=output.txt
python receiver.py #to write the decoded output to a file called 'final.txt'
```