import os
import sys
import time

tmp = time.ctime(os.path.getmtime("1.txt"))
while True:
    t = time.ctime(os.path.getmtime("1.txt"))
    print t
    if t == tmp:
        tmp = t
        time.sleep(5)
    else:
        print "modify"
        tmp = t
        time.sleep(5)

