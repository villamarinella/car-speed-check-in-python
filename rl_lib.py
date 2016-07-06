import numpy as np
import time
import datetime
import cv2

def diff(a, b,fz):
    if fz < 3:
       return False
    c=a+0.08*a    ## maybe change if the differenz between the color sum failed
    if b >= c:
      return True
    d=a-0.08*a   ##
    #print d
    if b <= d:
      return True
    return False

def fill1(frame,speed1,font,kreisrot,kreisgruen):
  pt1=(700,22)
  pt2=(1250,295)
  color=(255,255,255) ##weiss
  color1=(0,0,0)  ## schwarz
  color2=(0,0,255)  ## rot
  color3=(0,255,0)
  y=285       ## left gate lines
  y1=286        ##  horitontal linesposition
  y2=287        ##  take 3 lines
  x1=200    ##    vertikal line lenght starts
##############
  z=885       ## right gate lines
  z1=886          ##
  z2=887         ##
  x2=490       ##   right gate vertikal lenght starts
  while True:
      frame[y,x1] = [0,255,0]
      frame[y1,x1] = [0,255,0]
      frame[y2,x1] = [0,255,0]
      x1=x1+1
      if x1 >=420:         ## vertikal line finished
        break
  while True:
      frame[x2,z] = [0,0,255]
      frame[x2,z1] = [0,0,255]
      frame[x2,z2] = [0,0,255]
      x2=x2+1
      if x2 >=640:          ##
        break
  cv2.rectangle(frame, pt1, pt2, color, thickness=cv2.cv.CV_FILLED)
  cv2.putText(frame,'Distance about 110 meter',(720,80), font, 1,color1,2)
  cv2.putText(frame,'Raspicam with  10x zoomlens',(720,130), font, 1,color1,2)
  cv2.putText(frame,speed1,(720,200), font, 1,color2,2)
  if kreisrot: 
            cv2.circle(frame, (884,489), 20, color2, thickness=-1, lineType=8, shift=0)
  if kreisgruen: 
            cv2.circle(frame, (426,282), 20, color3, thickness=-1, lineType=8, shift=0)    
            

def init_gater(gray):
  global sumy
  yr=913          
  xr=510
  sumx=0
  while True:
      pxr = gray[xr,yr]
      sumx=sumx+pxr 
      xr=xr+1
      if xr >=580:
	sumy=sumx
        break
  #print sumy,sumx    
  return (sumy)

def init_gatel(gray):
  global sumz
  suma=0
  yl=288
  xl=260     
  while True:
    pxl = gray[yl,xl]
    suma=suma+pxl 
    #time.sleep(1)
    xl=xl+1
    if xl >=370:    ## vertikal line to control ends
       sumz=suma 
       #print suma,sumz
       break
  return(sumz)
  #time.sleep(10)
       
       
       
       
       
       