#!C:\Users\MITCH\PycharmProjects\mitchasignatura.github.io\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'doit==0.32.0','console_scripts','doit'
__requires__ = 'doit==0.32.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('doit==0.32.0', 'console_scripts', 'doit')()
    )
