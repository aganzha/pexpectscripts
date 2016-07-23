#!/usr/bin/python
import pexpect
from secret import password
import os

os.environ['LINES'] = "45"
os.environ['COLUMNS'] = "120"

if __name__ == '__main__':
    child = pexpect.spawn('ssh fn')
    child.setwinsize(640,480)
    child.expect(':~\$', timeout=5)
    print child.before+child.after
    child.sendline('sudo su postgres')
    child.expect('.*password[^:]+: $', timeout=1)
    print child.before+child.after
    child.sendline(password)
    child.expect('postgres.+$', timeout=1)    
    print child.before+child.after
    child.sendline('psql')
    child.expect('postgres=# $', timeout=1)
    print child.before+child.after
    child.sendline('\c app')
    child.interact()    
