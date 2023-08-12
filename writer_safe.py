#!/usr/bin/env python3
#

import json
import os
import time
import datetime
import string
import random
from Classes.GracefulKiller import GracefulKiller

def run():
    gk = GracefulKiller()
    basepath = "/tmp/{}".format(os.path.basename(__file__))
    if not os.path.isdir(basepath):
        print("Creating work path {}".format(basepath))
        os.mkdir(basepath)

    print("Generating dataset")
    ds = []
    for x in range(0, 1000):
        ds.append(get_random_string(100))

    data = []
    for x in range(0, 1000):
        data.append(ds)

    print("Entering write loop")
    while True:
        start_time = datetime.datetime.now()
        destination = "{}/{}".format(basepath, int(start_time.timestamp()))
        with open(destination, "w") as fd:
            fd.write(json.dumps(data, indent=4))

        runtime = datetime.datetime.now() - start_time
        print("Wrote data in {} seconds".format(runtime.microseconds / 1000000))
        if gk.kill_now:
            print("Exiting write loop")
            break
        time.sleep(1)

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

if __name__ == '__main__':
    run()
