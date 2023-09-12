#! /usr/bin/python

TEMP_PATH="/sys/class/thermal/thermal_zone0/"

#f0 = open(TEMP_PATH + "temp", "r")
#temp = f0.read()
#print(temp)

def readTemp():
    f0 = open(TEMP_PATH + "temp", "r")
    temp = float(f0.read())
    print(temp*0.001)
#readTemp()


def avgTemp(n):
    
    temp = 0
    
    for i in range(0,n):
        f0 = open(TEMP_PATH + "temp", "r")
        temp += float(f0.read())
    
    print(temp/n*0.001)



