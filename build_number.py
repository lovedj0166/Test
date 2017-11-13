import datetime
import sys,os

i = datetime.datetime.now()
y = i.year
m = i.month
d = i.day
local_build_number = str(y)[-1] + "." + str(m) + "." + str(d)

def buildNumber():
    if len(os.sys.argv) == 1:
        build_number = local_build_number
    elif len(os.sys.argv) == 2:
        build_number = os.sys.argv[1]
    return build_number

print buildNumber()
print buildNumber()

if __name__ == '__main__':
    buildNumber()
