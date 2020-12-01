#!/usr/bin/env python3
import time
import os
import random

PATH = "/sdcard/Pictures/wallpaperd"

try:
    with open("~/.wallpaperpath", "r") as f:
        PATH = f.read().strip()
except OSError:
    pass

while True:
    chosen = random.choice(os.listdir(PATH))
    fpath = PATH + chosen
    os.system(f"termux-wallpaper -f '{fpath}' -l")
    next_wait_time = random.randint(1200, 7200)
    time.sleep(next_wait_time)
