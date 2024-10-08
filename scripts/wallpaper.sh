# Random goofy ass wrapping hack to work with cronjob
SWAYSOCK=/run/user/$(id -u)/sway-ipc.$(id -u).$(pgrep -x sway).sock   python /home/barni/.config/scripts/wallpaper.py
