#!/usr/bin/env python
# parse large json file to sent them to a rest api
# Usage: python t.py -f <JSON FILE> -u <REST URL> -s <NUMBER=200>
# Coded by <Abderrahman JIHAL>

import json, sys, requests, time, getopt


def main(argv):
    url = file = False

    #headers
    headers = {"Authorization" :  "Basic ==",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "X-CSRF-Token": "GTAudTQjJTvnFkr-LiWOxtu3uN5BGMVWMu9nKw9D0ig"}

    usage = "\033[93mHello man :)\nUsage: python t.py -f <JSON FILE> -u <REST URL> -s <NUMBER=200> --sleep <NUMBER=10>\033[0m"
    usage = """\033[93m
Hello world
Usage: python t.py -f <JSON FILE> -u <REST URL> -s <NUMBER=200> --sleep <NUMBER=10> --start=<START_FROM=0>
    \033[0m"""
    size = 200
    sleep = 10
    start = 0

    try:
        opts, args = getopt.getopt(argv,"hu:s:f:",["url=","size=", "file=", "sleep=", "start="])

    except getopt.GetoptError:
        print usage
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print usage
            sys.exit()
        elif opt in ("-s", "--size"):
            size = arg
        elif opt in ("-u", "--url"):
            url = arg
        elif opt in ("-f", "--file"):
            file = arg
        elif opt in ("--sleep"):
            sleep = arg
        elif opt in ("--start"):
            start = arg

    if url == False or file == False:
        print usage
        sys.exit()

    with open(file,'r') as infile:
        o = json.load(infile)
        globalNumber = len(o)
        interation = globalNumber/int(size)
        print "\033[93m=======================================================================================================\033[0m"
        print "Global number of items : \033[91m"+ str(globalNumber) +" / "+ str(size) + " = " + str(interation) + "\033[0m (interations) xD"
        print "\033[93m=======================================================================================================\033[0m"

        for i in xrange(0, len(o), int(size)):
            current = i / int(size)
            if int(start) > int(current):
                continue
            r = requests.post(url, headers=headers, data=json.dumps(o[i:i+int(size)]))
            print "\033[92m(iteration : "+str(current)+")\033[0m => "+r.text
            time.sleep(int(sleep))

if __name__ == "__main__":
   main(sys.argv[1:])
