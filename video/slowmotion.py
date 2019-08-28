import os
import time
print('Starting program')
time.sleep(2)

print('Recording started - 30 seconds')
os.system('raspivid -w 640 -h 480 -fps 90 -t 30000 -o vid.h264')
print('Recording complete. Please wait...')
time.sleep(2)

print('Converting video. Please wait...')
os.system('rm -f vid.mp4')
os.system('MP4Box -add vid.h264 vid.mp4')
print('Video conversion complete')
time.sleep(2)
print('Closing program')
time.sleep(2)