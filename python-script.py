#!/usr/bin/env python3

import os
import argparse
import requests 


def main(args):
    if args.name:
        name = args.name[0]
    else:
        name = input("What is your name? ")

    print("hello {}".format(name)) 

def getWebsiteSource(sites):
    sources = []
    for site in sites:
        if site[:4] != "http":
            site = "http://" + site
        page = requests.get(site)
        sources.append(page.text)

    return sources

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some stuff.')

    # base command
    parser.add_argument("command",
        help="the command to be executed",
        choices=["add", "get", "set"],
        nargs='?',
        default="get"
    )
    # type of object to work on
    parser.add_argument("type",
        help="the command to be executed",
        choices=["host", "network", "site"],
        nargs='?',
        default="site"
    )
    # specify name + details
    parser.add_argument("--name", help="the command to be executed", nargs=1)
    parser.add_argument("--ipaddress", help="the command to be executed", nargs=1)
    parser.add_argument("--color", help="the command to be executed", nargs=1)

    args = parser.parse_args()

    # lets act on the arguments
    # add command
    if args.command == "add":
        pass
    # get command
    elif args.command == "get":
        # getting what?
        # getting a site
        if args.type == "site":
            print(getWebsiteSource(args.name))
    # set command
    elif args.command == "set":
        pass
    # not a recognized command
    else:
        print("error")


