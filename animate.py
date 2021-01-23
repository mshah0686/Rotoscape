# import cv2
# import numpy as np

# cap = cv2.VideoCapture('Temp_Short.mp4')

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     if ret == True:
#         out.write(frame)

#         cv2.imshow('frame', gray)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()

import tkinter as tk
import PIL
import numpy as np
import FindMattes as fm
import os

# Split into seperate frames:
import cv2
vidcap = cv2.VideoCapture('Dance.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  if count % 2 == 0:
    print("creating matte")
    inputname = "frames/frame%d.jpg" % (count)
    outputname = "mattes/frame%d.jpg" % (count)
    fm.createMatte(inputname, outputname, 1080)
  count += 1

os.system("ffmpeg -r 60 -i mattes/frame%01d.jpg -vcodec mpeg4 -y movie.mp4")

