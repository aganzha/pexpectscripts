#!/usr/bin/python
import pexpect
from secret import password, fn_prod_env, fn_prod_folder, fn_prod_settings
import os

os.environ['LINES'] = "45"
os.environ['COLUMNS'] = "120"

if __name__ == '__main__':
    child = pexpect.spawn('ssh fn')
    child.setwinsize(640,480)
    child.expect(':~\$', timeout=5)
    print child.before+child.after
    child.sendline('sudo su app')
    child.expect('.*password[^:]+: $', timeout=1)
    print child.before+child.after
    child.sendline(password)
    child.expect('app.+$', timeout=1)
    print child.before+child.after
    child.sendline('export FNSITE_ENV=production')
    child.expect('app.+$', timeout=1)
    child.sendline('export DJANGO_SETTINGS_MODULE={}'.format(fn_prod_settings))
    child.expect('app.+$', timeout=1)
    child.sendline('cd ~/{}'.format(fn_prod_folder))
    child.expect('{}\$'.format(fn_prod_folder), timeout=1)
    print child.before+child.after
    child.sendline('{}bin/python manage.py shell'.format(fn_prod_env))
    child.expect('In', timeout=3)
    print child.before+child.after

    child.interact()
