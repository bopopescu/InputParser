#!C:\Users\Betis\PycharmProjects\InputParser\py\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'toil==3.19.0','console_scripts','cwltoil'
__requires__ = 'toil==3.19.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('toil==3.19.0', 'console_scripts', 'cwltoil')()
    )
