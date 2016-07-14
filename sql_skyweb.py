#!/usr/bin/python
import pexpect
from secret import password
import os

os.environ['LINES'] = "45"
os.environ['COLUMNS'] = "120"

if __name__ == '__main__':
    child = pexpect.spawn('sudo su postgres')
    child.setwinsize(640,480)
    child.expect('.*password[^:]+: $', timeout=1)
    child.sendline(password)
    child.expect('postgres.+$', timeout=1)
    child.sendline('psql')
    child.expect('postgres=# $', timeout=1)
    child.sendline('\c skyweb')
    child.interact()    
