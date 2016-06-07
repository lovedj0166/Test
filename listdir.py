#coding=utf-8
import os

path = "/home/lovedj/ota/6.4.26"

if os.listdir(path):
    print "exists"
else:
    print "empty"
