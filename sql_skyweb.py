#!/usr/bin/python
import pexpect
from secret import password

if __name__ == '__main__':
    child = pexpect.spawn('sudo su postgres')
    child.expect('.*password[^:]+: $', timeout=1)
    child.sendline(password)
    child.expect('postgres.+$', timeout=1)
    child.sendline('psql')
    child.expect('postgres=# $', timeout=1)
    child.sendline('\c skyweb')
    child.interact()    
