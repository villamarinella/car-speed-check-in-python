import numpy as np
import time
import datetime
import cv2
import sys
#from speed_lib import *
from lr_lib import *
datei = sys.argv[1]
ende=False
sumy=0
sumz=0
found=False
speed='1'
speed1=""
gray=""
fz=0
fz1=1
fzx=0
distanz=40  ## distanz between the gates in meter
l1=False
l2=True
kreisrot=False
kreisgruen=False
## open file 
cap = cv2.VideoCapture(datei)
## open network stream
#cap = cv2.VideoCapture(0)   
#cap.open('http://192.168.1.134:8080/stream/video.mjpeg')
fourcc = cv2.cv.CV_FOURCC(*'XVID')
#font = cv2.FONT_HERSHEY_SIMPLEX
font=cv2.FONT_ITALIC
##########
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1280,720))

while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #cv2.imshow('Video',frame)
  fz=fz+1
  #print fz
  if fz >= 10:
    break
sumy=init_gater(gray)
sumz=init_gatel(gray)
print sumy,sumz
#time.sleep(10)
def lese():   ## check left gate
  global gltime,found,l1,l2,sumz,fzx,kreisrot,kreisgruen,fz1,ende
  if ende:
    return
  lyl=374  ## horizontal line to control
  lxl=340    ## vertikal line to control start
  suma=0
  while True:
      px = gray[lyl,lxl]
      suma=suma+px 
      lxl=lxl+1
      if lxl >=430: 
          break
  #print str(fz)+" "+str(suma)+" "+str(sumz)
  #wert=suma*100/sumz
  #print sumz,suma,wert
  if diff(sumz,suma,fz):
       gltime=datetime.datetime.now()
       l2=False
       l1=True
       fzx=1
       kreisgruen=True
       wert=suma*100/sumz
       print 'lese  '+str(gltime)   ## show for control
       print sumz,suma,wert
       speed1=""
       fz1=fz
       return
       #time.sleep(10)
  else:  
      #print sumz,suma,99
      sumz=suma
####################
def lese1():   ## check right gate
  global l2,l1,sumy,grtime,fzx,speed1,kreisrot,kreisgruen,fz1,found,ende
  if ende:
    return
  
  ryr=913           ##  horizonta
  rxr=510              ##   vertikal
  sumx=0
  while True:
      rpx = gray[rxr,ryr]
      sumx=sumx+rpx 
      rxr=rxr+1
      if rxr >=580:
         break  
  fzx=fzx+1
  if fzx >= 100:
     l2=True
     l1=False
     print 'abbruch lese1'
     return       
  if diff(sumy,sumx,fz):
     grtime= datetime.datetime.now()
     found=True
     ende=True
     fz1=fz
     l2=True
     l1=False
     kreisrot=True
     fz1=fz
     print 'lese1  '+str(grtime)
     wert=sumx*100/sumy
     print sumy,sumx,wert 
     return
  else:  
     sumy=sumx
     #print sumy,sumx
#####################
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fz=fz+1
    if l1:
       lese1()
    if l2: 
      lese()
    if found:
       messtime=grtime-gltime
       msec=messtime.total_seconds()
       xsec=str(msec)+'\n'
       speed= (distanz / msec *3600/1000)
       speed=("%.2f" % speed)
       speed1=str(speed)+" Km/h"
       print xsec + "  " + speed1
       found=False
       if fz >= fz1+100:
	 kreisrot=False
         kreisgruen=False
    fill1(frame,speed1,font,kreisrot,kreisgruen)
    if fz >= fz1+60:
	 kreisrot=False
         kreisgruen=False
    cv2.imshow('Video',frame)
    #out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    #if fz >= 12000:
        break
cap.release()
cv2.destroyAllWindows()
#out.release()
