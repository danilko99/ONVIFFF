import cv2
import numpy

from time import sleep
from matplotlib import pyplot

import zeep
from onvif import ONVIFCamera, ONVIFService
def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue
zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

#Connection
from onvif import ONVIFCamera
mycam = ONVIFCamera('192.168.15.43', 80, 'danlvolchkov', 'WCgV9w0MJcdi')

#Open the video file
str=cv2.VideoCapture('rtsp://192.168.15.43:554')

#Creating of histogram
fig=pyplot.figure(figsize=(2, 2))
color = ('r','g','b')
ret,frame=str.read()
cv2.imshow('qwerty',frame)#displaying
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #color conversion
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #istogram calculation, hue 180 saturation 256
fig.add_subplot(2, 2, 1)  #adding of subplot
pyplot.imshow(hist,interpolation = 'nearest')#displaying

fig.add_subplot(2, 2, 2) #adding of subplot
for i,col in enumerate(color): #each value corresponds to number of pixels in that image with its corresponding pixel value RGB
      histr = cv2.calcHist([frame],[i],None,[256],[0,256])#hist is a 256x1 array, each value corresponds to number of pixels in that image with its corresponding pixel value.
      pyplot.plot(histr,color = col)
      pyplot.xlim([0,256])

#Creating media service object
media = mycam.create_media_service()
ptz = mycam.create_ptz_service()
media_profile = media.GetProfiles()[0]
image = mycam.create_imaging_service()
token = media_profile.VideoSourceConfiguration.SourceToken
SY = image.create_type('GetImagingSettings')
SY.VideoSourceToken = token
request = image.GetImagingSettings(SY)
print(request)


#Adapting of brightness
brightness=request42.Brightness
if brightness <48.0:
    while brightness < 48.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Brightness = request42.Brightness + 1.0
        brightness = brightness+1.0
if brightness > 50.0:
    while brightness > 50.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Brightness = request42.Brightness - 1.0
        brightness = brightness - 1.0


#Adapting of saturation
s42=request42.ColorSaturation

if s42 <59.0:
    while s42 <59.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.ColorSaturation = request42.ColorSaturation + 1.0
        s42 = s42+1.0
if s42 > 61.0:
    while s42 > 61.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.ColorSaturation = request42.ColorSaturation - 1.0
        s42 = s42 - 1.0

#Adapting of contrast
contr42=request42.Contrast

if contr42 <49.0:
    while contr42 <49.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Contrast = request42.Contrast + 1.0
        contr42 = contr42+1.0
if contr42 > 51.0:
    while contr42 > 51.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Contrast = request42.Contrast - 1.0
        contr42 = contr42 - 1.0

#Creating of ystogram
str=cv2.VideoCapture('rtsp://192.168.15.43:554')
ret,frame=str.read()
cv2.imshow('qwerty',frame)
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(2, 2, 3)
pyplot.imshow(hist,interpolation = 'nearest')

fig.add_subplot(2, 2, 4)
for i,col in enumerate(color): #each value corresponds to number of pixels in that image with its corresponding pixel value RGB
      histr = cv2.calcHist([frame],[i],None,[256],[0,256])#hist is a 256x1 array, each value corresponds to number of pixels in that image with its corresponding pixel value.
      pyplot.plot(histr,color = col)
      pyplot.xlim([0,256])
pyplot.show()
