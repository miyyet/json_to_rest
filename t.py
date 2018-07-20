#!/usr/bin/env python
# parse large json file to sent them to a rest api
# Usage: python t.py -f <JSON FILE> -u <REST URL> -s <NUMBER=200>
# Coded by <Abderrahman JIHAL>

import json, sys, requests, time, getopt


def main(argv):
    url = file = False

    headers = {"Authorization" :  "Basic ZGFtaWVuLmhfMjAxNw==",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "X-CSRF-Token": "GTAudTQjJTvnFkr-LiWOxtu3uN5BGMVWMu9nKw9D0ig"}

    usage = "Hello man :)\nUsage: python t.py -f <JSON FILE> -u <REST URL> -s <NUMBER=200>"
    size = 200

    try:
        opts, args = getopt.getopt(argv,"hu:s:f:",["url=","size=", "file="])

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

    if url == False or file == False:
        print usage
        sys.exit()

    with open(file,'r') as infile:
        o = json.load(infile)
        for i in xrange(0, len(o), int(size)):
            r = requests.post(url, headers=headers, data=json.dumps(o[i:i+int(size)]))
            print r.text
            time.sleep(30)

if __name__ == "__main__":
   main(sys.argv[1:])
