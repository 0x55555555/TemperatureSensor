import time, json, datetime, calendar, sys
from os import listdir, path

def read_sensor(name):
    f = open(name)
    out = f.read().split("\n")
    f.close()
    return float(out[1].split(" ")[9][2:])/1000

sensor_root = sys.argv[1]
sensors = [path.join(sensor_root, f) for f in listdir(sensor_root) ]
print("Using sensors {}".format(sensors))


output = sys.argv[2]
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
