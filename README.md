Simple programm to measure the car speed between two "gates", means to lines of pixels.

The script is in python 2.7

It is running on  Ubuntu 14.04 and Raspian wheezy.

Because the Raspberry is too weak, so it only transfers the video signal via LAN to the Ubuntu machine.

As well my Ubuntu machine needs 100% CPU to run the job.

You need:

On Raspberry Pi install uv4l from here:

http://www.linux-projects.org/uv4l/installation/

prepare the system if not intalled already:

sudo apt-get install python-opencv opencv-dev python-numpy python-dev

check you must have: ls -l /dev/video0

You will find:

The video on youtube

https://youtu.be/4s2b6HW9TXM

lr.py        For cars from left to right
lr_lib.py   lr.py need it

rl.py        For cars from right to left
rl_lib.py    rl.py need it


Yes, I know, the code is terrible, but it works:-)

form follows function:-)

Stay lucky

Klaus Werner
