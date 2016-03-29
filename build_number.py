import datetime
import sys,os
i = datetime.datetime.now()
y = i.year
m = i.month
d = i.day
local_build_number = str(y)[-1] + "." + str(m) + "." + str(d)

if len(os.sys.argv) == 1:
    build_number = local_build_number #不输入参数使用当前日期作为版本号
elif len(os.sys.argv) == 2:
    build_number = os.sys.argv[1]     #输入版本号参数

print "Build_Number:" + build_number

