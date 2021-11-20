#!/usr/bin/python
import sys

sys.stdout.write('badchars = ("')
sys.stdout.flush()
for x in range(0, 256):
    if x > 15 and x % 16 == 0 :
        sys.stdout.write('\\\n')
        sys.stdout.flush()
    sys.stdout.write('\\' + 'x' + hex(x).split('x')[1].rjust(2,'0'))
    sys.stdout.flush()
sys.stdout.write('")')
