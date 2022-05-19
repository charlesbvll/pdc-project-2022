# QAM modulation for complex AWGN communication

Transmission of a message over a complex AGWN channel with the following characteristics :

<img src="docs/channel.png" />

`numpy` and `jellyfish` are required to run the script : `pip install numpy jellyfish`.

The program can be ran using the following command :

```sh
python main.py --srv=False --comp=True --n=1 --m=256
```

In the above command all the values used are the default ones, when `--srv` the channel used is the one on the EPFL server (VPN required) otherwise it uses a simulated channel locally, the `--comp` argument tells the program to use a brute force approach to estimate the angle of Theta, the `--n` argument allows you to run the transmission multiple times and get an average difference and the `--m` argument is there to choose the number of points in the QAM constellation.