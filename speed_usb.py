import numpy as np
import time
import datetime
import cv2
sumy=100000
sumz=100000
sumx=0
suma=0
tsum1=0
tsum2=0
found=False
found1=False
speed='1'
fz=0
fz1=1
distanz=20   ## distanz between the gates in meter
l1=True
l2=False
zaehl=False
cap = cv2.VideoCapture(0)   ## 
m=datetime.datetime.now()
ret, frame = cap.read()
gray=frame
fz=fz+1

def diff(a, b):
    if fz < 3:
       return False
    c=a+0.05*a    ## maybe change if the differenz between the color sum failed
    if b >= c:
      return True
    d=a-0.05*a   ##
    #print d
    if b <= d:
      return True
    return False
def fill():
    y=173          ## left gate lines
    y1=174        ##  horitontal linesposition
    y2=175        ##  take 3 lines
    x1=160        ##    vertikal line lenght starts
##############
    z=561           ## right gate lines
    z1=562          ##
    z2=563          ##
    x2=262         ##   right gate vertikal lenght starts
    while True:
       gray[x1,y] = [0,255,0]
       gray[x1,y1] = [0,255,0]
       gray[x1,y2] = [0,255,0]
       x1=x1+1
       if x1 >=250:         ## vertikal line finished
         break
    while True:
       gray[x2,z] = [0,0,255]
       gray[x2,z1] = [0,0,255]
       gray[x2,z2] = [0,0,255]
       x2=x2+1
       if x2 >=345:          ##
         break

def lese():   ## check left gate
  global sumz,tsum1,tsum2,sumy,suma
  global a,b,found,found1,l1,l2,zaehl,fz1
  sum1=0
  sum2=0
  sum0=0
  y1=178    ## horizontal line to control
  x=160      ## vertikal line to control start
  while True:
      px = gray[x,y1]
      sum0=sum0+px[0]
      sum1=sum1+px[1]
      sum2=sum2+px[2]
      suma=sum0+sum1+sum2 
      x=x+1
      if x >=250:    ## vertikal line to control ends
         break
  if diff(sumz,suma):
    if zaehl:
      sumz=suma
    else:  
      a=datetime.datetime.now()
      found=True
      l2=False
      fz1=fz
      zaehl=True
      print 'lese'+str(a)   ## show for control
  else:  
      sumz=suma
   
def lese1():   ## check right gate
  global a,b,l2,l1,found1,found,sumy,sumx,zaehl,tsum1,tsum2,sumz
  sum1=0
  sum2=0
  sum0=0
  y1=549             ##  horizontal
  x=202               ##   vertikal
  while True:
      px = gray[x,y1]
      sum0=sum0+px[0]
      sum1=sum1+px[1]
      sum2=sum2+px[2]
      sumx=sum0+sum1+sum2 
      x=x+1
      if x >=395:
         break
  if diff(sumy,sumx):
     if zaehl:
       sumy=sumx
     else:  
        b = datetime.datetime.now()
        l2=True
        l1=False
        print 'lese1'+str(b)
  else:  
       sumy=sumx
## initialize the gates  
lese()
lese1()
ret, frame = cap.read()
gray=frame
fz=fz+1
lese()
lese1()
l1=True
#####################
while(True):
    ret, frame = cap.read()
    gray=frame
    fz=fz+1
    #print fz
    if zaehl:
      if fz >= fz1 + 50:   ## frame until  gate 1 and gate 2 are free
	lese1()
        lese()
        l1=True
        l2=False
        zaehl=False
        gray=frame
    fill()
    if l1:
       lese1()
    if l2:
      lese()
    if found:
       c=a-b
       msec=c.total_seconds()
       xsec=str(msec)+'\n'
       #print msec
       speed= str((distanz / msec *3600/1000))+" km/h"
       found=False
       font = cv2.FONT_HERSHEY_SIMPLEX
       cv2.putText(gray,speed,(180,540), font, 1,(255,255,255),2)
       cv2.imshow('Video',gray)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(gray,speed,(180,540), font, 1,(255,255,255),2)
    cv2.imshow('Video',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
