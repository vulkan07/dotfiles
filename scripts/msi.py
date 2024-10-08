import os, sys, subprocess

if not os.geteuid() == 0:
	print("\033[91mThis script must be run as root!\033[0m")
	exit(1)

try:
	sys.argv[1]
except:
	print("\033[91mOne argument is required! ('performance'/'battery')\033[0m")
	exit(2)


EC_IO_FILE = '/sys/kernel/debug/ec/ec0/io'
#EC_IO_FILE = './ec' # Used for debugging


def writeByte(addr, val, file):
	file.seek(hex(addr),0)
	file.write(bytes((hex(val),)))

def hex(x):
	return int('0x'+str(x),16)


addresses = 'D2 D4 EB 91 D3'.split(' ')
values = []

## Battery Mode ##
if sys.argv[1] == "battery":
	values = 'C2 1D 0F 53 80'.split(' ') # "Super Battery"    
	subprocess.run(["/usr/bin/cpupower","frequency-set", "--g", "powersave"], stdout=subprocess.DEVNULL)
	print("\033[34mSet CPU Governor\033[0m")

## Performance Mode ##
elif sys.argv[1] == "performance":
	values = 'C4 0D 00 64 81'.split(' ') # "Performance"   
	subprocess.run(["/usr/bin/cpupower","frequency-set", "--g", "performance"], stdout=subprocess.DEVNULL)
	print("\033[34mSet CPU Governor\033[0m")

else:
	print("\033[91mInvalid argument:", sys.argv[1], "\033[0m")
	exit(3)

if len(addresses) != len(values):
    print("\033[91mToo many or not enough values for the 5 addresses!", values, "\033[0m")
    exit(4)

else:
	with open(EC_IO_FILE,'r+b') as file:
		for i in range(len(addresses)):
			writeByte(addresses[i],values[i],file)
	#print("Wrote bytes to " + EC_IO_FILE)
	print("\033[34mSet EC  Bytes\033[0m")

'''

#if subprocess.check_output(["upower", "-i", "/org/freedesktop/UPower/devices/battery_BAT0"]).decode("utf-8") == 0:
if sys.argv[1] == "battery":
    # Set refresh rate to 90Hz
    subprocess.run(["xrandr", "--output", "eDP1", "--mode", "1920x1080",  "--rate", str(60)])
    print("\033[34mSet screen to 60Hz\033[0m")
elif sys.argv[1] == "performance":
    # Set refresh rate back to 144Hz
    subprocess.run(["xrandr", "--output", "eDP1", "--mode", "1920x1080",  "--rate", str(144)])
    print("\033[34mSet screen to 144Hz\033[0m")

'''

print("\033[1;34mEntered",sys.argv[1], "mode! :D\033[0m")
