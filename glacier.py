#!/usr/bin/python

from subprocess import Popen
import os, os.path
import sys
import json


if __name__ == '__main__':
    """ ~/pexpect/glacier.py 105CANON/ """
    with open('config.json','rw+') as config:
        src = config.read()
        js = json.loads(src)
        vault = js['vault']
        if not 'uploaded' in js:
            js['uploaded'] = []
        directory = sys.argv[1]

        for i,f in enumerate(os.listdir(directory)):
            dirname = directory.replace('/', '')
            pair = u'{}/{}'.format(dirname,f)
            if pair in js['uploaded']:
                print "skip ",pair
                continue
            command = 'glacier-cmd upload --name {} {} {}'.format(pair, vault, pair)
            print command
            p = Popen(command, shell=True)
            if p.wait() == 0:
                js['uploaded'].append(pair)
                config.seek(0)
                config.write(json.dumps(js))
                config.truncate()
