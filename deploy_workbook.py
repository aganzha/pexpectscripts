#!/usr/bin/python
import pexpect
from secret import hs_password
import os

os.environ['LINES'] = "45"
os.environ['COLUMNS'] = "120"

if __name__ == '__main__':
    child = pexpect.spawn('ssh hs')
    child.setwinsize(640,480)
    child.expect(':~\$', timeout=12)
    print child.before+child.after
    child.sendline('cd /var/hyperspots/public/workbook')
    child.expect('workbook\$', timeout=2)
    print child.before+child.after
    child.sendline('git pull bitbucket master')
    print child.before+child.after
    child.expect("Password for 'https://alexey_ganzha@bitbucket.org': $",timeout=2)
    print child.before+child.after
    child.sendline(hs_password)
    print child.before+child.after
    child.expect('workbook\$', timeout=4)
    print child.before+child.after
