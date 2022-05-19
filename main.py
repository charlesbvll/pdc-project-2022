import qam
import utils

import argparse
import subprocess

import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(description="Transmission through a black-box channel simulator",
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog="To promote efficient communication schemes, transmissions are limited to 100 a samples.")

    parser.add_argument('--srv', action='store_true',
                        help='If set, it runs the program on the EPFL server (requires VPN)')
    parser.add_argument('--no_comp', action='store_true',
                        help='If set, it does not use the brute force approach for Theta estimation')
    parser.add_argument('--n', type=int, default=1,
                        help='Number of times to test the transmission')
    parser.add_argument('--m', type=int, default=256,
                        help='Number of points in the qam constellation')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    
    n = args.n
    comp = not args.no_comp
    qam = qam.QAM(args.m)
    cmd = "--srv_hostname=iscsrv72.epfl.ch --srv_port=80" if args.srv else ""

    utils.encode(qam)

    tot = 0
    for i in range(n):
        subprocess.call("python client.py --input_file=input.txt --output_file=output.txt" + cmd, shell=True)
        utils.decode(qam, comp)

        tot += utils.compute_score()

    if n > 1:
        print("Average difference is : ", tot/n)
