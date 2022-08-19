import cv2
from matplotlib import pyplot as plt
import numpy as np

vidcapin = cv2.VideoCapture('input.mp4')
success,imagein = vidcapin.read()

vidcapout = cv2.VideoCapture('output.mp4')
success,imageout = vidcapout.read()

diffimg = (imagein-imageout)

allz = not np. any(diffimg)

plt.subplot(211)
plt.imshow(imagein)

plt.subplot(212)
plt.imshow(imageout)
plt.show()


print(allz)

count = 0
while count<10:
  #cv2.imwrite("inputframe%d.jpg" % count, image)     # save frame as JPEG file



  #print('Read a new frame: ', success)
  count += 1


