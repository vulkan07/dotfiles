from random import randint
import os, shutil, subprocess, datetime

dir = "/home/barni/Pictures/"

## ----------- ##
_DAWN_START = 5
_DAWN_END = 9
_SUNSET_START = 16
_SUNSET_END = 19
## ----------- ##

NIGHT = 1
DAY = 2
SUNSET = 3
DAWN = 4

ANY = 0
NONE = -1

data = [
		[ANY],
		[NIGHT],
		[NIGHT,DAWN,SUNSET],
		[ANY],
		[ANY],
		[ANY],
		[NIGHT,SUNSET],
		[NIGHT,SUNSET,DAWN],
		[NIGHT,SUNSET],
		[NIGHT,SUNSET],
		[ANY],
		[DAY,SUNSET,DAWN],
		[ANY],
		[DAWN,DAY],
		[NIGHT],
		[NIGHT],
		[DAY,SUNSET],
		[NIGHT],
		[ANY],
		[DAWN,NIGHT,SUNSET],
		[NIGHT],
		[NIGHT],
		[SUNSET],
		[DAWN,DAY,SUNSET],
		[ANY],
		[ANY],
		[NIGHT],
		[SUNSET],
		[DAY,SUNSET],
		[ANY],
		[ANY],
		[ANY],
		[ANY],
		[ANY],
		[ANY],
		[ANY]
	]

time = ANY
index = 0
now = int(datetime.datetime.now().strftime("%H"))
#print(f"now is {now} hours")
if now < _DAWN_START or now > _SUNSET_END:
	time = NIGHT
elif now < _DAWN_END:
	time = DAWN
elif now < _SUNSET_START:
	time = DAY
else:
	time = SUNSET

def choice():
	global index, data, time
	while True:
		index = randint(0,len(data)-1)
		if time in data[index] or ANY in data[index]:
			break
choice()

	#f = choice(os.listdir(dir+"WallpaperRoll/"))
try:
	shutil.copyfile(dir+"WallpaperRoll/"+str(index)+".jpg",dir+"Wallpaper.jpg")
except shutil.SameFileError:
	choice()

	#subprocess.run(["feh", "--bg-scale","/home/olahb/Pictures/Wallpaper.jpg"])
subprocess.run(["swaymsg", "output","\"*\"", "bg", "~/Pictures/Wallpaper.jpg", "fill"])
