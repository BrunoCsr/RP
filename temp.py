#! /usr/bin/python

TEMP_PATH="/sys/class/thermal/thermal_zone0/"

f0 = open(TEMP_PATH + "temp", "r")
temp = f0.read()
print(temp)

