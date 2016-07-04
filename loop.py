#coding=utf-8
import os
import time

print "Working~"
tmp = time.ctime(os.path.getmtime("loop.py"))
while True:
    t = time.ctime(os.path.getmtime("loop.py"))
    if t == tmp:
        time.sleep(5)
    else:
        print "modify"
        os.system("cat loop.py")
        tmp = t
        print "Working~"
        time.sleep(5)

