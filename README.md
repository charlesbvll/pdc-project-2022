# 16QAM Modulation for complex AWGN communication

Transmission of a message over a complex AGWN channel with the following characteristics :

<img src="https://latex.codecogs.com/svg.image?Y&space;=&space;\exp{\Theta&space;i}&space;X&space;&plus;&space;Z&space;\text{&space;with&space;}&space;\Theta&space;\sim&space;U(0,&space;2\pi&space;)&space;\text{&space;and&space;}&space;Z&space;\sim&space;\mathcal{CN}\left(0,&space;\frac{\sigma^2}{2}\right)&space;\text{&space;where&space;}&space;\sigma^2&space;=&space;10^{-2.65}&space;\text{.}" />

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