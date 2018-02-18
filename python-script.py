#!/usr/bin/env python3

import os
import argparse


def main(args):
    if args.name:
        name = args.name[0]
    else:
        name = input("What is your name? ")

    print("hello {}".format(name)) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some stuff.')
    parser.add_argument('--name', type=str, nargs=1, help="a name to say hello to")
    args = parser.parse_args()

    main(args)
