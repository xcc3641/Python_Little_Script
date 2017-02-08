# encoding: utf-8
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-p', action='store', dest='apk_path',
        help='Set a apk path to batch install')

results = parser.parse_args()

def extract_lines(content):
    """ Extract lines from terminal response. """
    return content.strip().split('\n')[1:]


def extract_id(line):
    """ Extract device id from line """
    return line.split('\t')[0].strip()


def install(device_id):
    """ Execute adb tasks """
    defalut_path = 'app/build/outputs/apk/app-debug.apk'
    if results.apk_path is not None:
        defalut_path = results.apk_path
    os.system('adb -s %s install -r %s' %(device_id,defalut_path))
    os.system('adb -s %s shell am start -n "com.ruguoapp.jike/com.ruguoapp.jike.business.main.ui.SplashActivity" -a android.intent.action.MAIN -c android.intent.category.LAUNCHER' % device_id)

map(install, map(extract_id, extract_lines(os.popen('adb devices').read())))

"""
# encoding: utf-8
import os
import time

devices = os.popen('adb devices').read()
# print devices

# 根据换行符来分割，并且忽略掉第一行
list = devices.strip().split("\n")

# adb -s 192.168.56.103:5555 install -r app/build/outputs/apk/app-debug.apk
print "----------ADB Prepare----------"

print "There are " + str(len(list)-1) + " Android Phone to test ..."

print "-----------ADB Start-----------"

for index in range(1, len(list)):
    device_ip = list[index].replace("device", "").replace(" ","")
    # print list[index].replace("device","")
    # print "Now "+ device_ip + " install apk....."
    os.system('adb -s ' + device_ip + ' install -r app/build/outputs/apk/app-debug.apk')
    os.system('adb -s '+ device_ip +' shell am start -n "com.ruguoapp.jike/com.ruguoapp.jike.business.main.ui.SplashActivity" -a android.intent.action.MAIN -c android.intent.category.LAUNCHER')

"""