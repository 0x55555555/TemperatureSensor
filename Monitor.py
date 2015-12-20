import sys

def read_sensor(name):
    f = open(name)
    out = f.read().split("\n")
    f.close()
    return float(out[1].split(" ")[9][2:])/1000

sensors = [
    "/sys/bus/w1/devices/28-000007215308/w1_slave",
    "/sys/bus/w1/devices/28-000007481742/w1_slave",
    "/sys/bus/w1/devices/28-00000748446c/w1_slave"
]

import time, json, datetime, calendar

output = sys.argv[1]
print("Writing to {}".format(output))

while True:
    with open(output, 'a') as file:
        temps = {
		'time': time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
		'epoch': calendar.timegm(time.gmtime()),
		'temps': [read_sensor(s) for s in sensors]
        }
        file.write(json.dumps(temps) + ',\n')
        file.flush()
        print("Flushed to file", temps)
        time.sleep(60)
