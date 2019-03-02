#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2
import matplotlib.pyplot as plt
import numpy
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:



im = cv2.imread('frontpage.jpg')
im.convertTo(im, CV_8UC1, 255.0);
plt.figure(figsize=(10,10))
plt.imshow(im)
img_gray = cv2.imread('frontpage.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img_gray)
# In[ ]:





# In[3]:


_, binary_thresh = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)
fig = plt.figure(figsize=(15, 15))
fig.add_subplot(1, 2, 1)
plt.imshow(im)
fig.add_subplot(1, 2, 2)
plt.imshow(binary_thresh)


# In[ ]:


'''lines = cv2.HoughLinesP(binary_thresh, 1, numpy.pi/180, 100, minLineLength= 600/2.0, maxLineGap=20)'''
'''lines = cv2.HoughLinesP(im, rho = 1,theta = 1*np.pi/180,threshold = 100,minLineLength = 100,maxLineGap = 50)  '''     

#lines = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


# In[ ]:

#new part here as bellow
minLineLength = 300
maxLineGap = 20
lines = cv2.HoughLinesP(binary_thresh, 1, numpy.pi/180, 100, minLineLength, maxLineGap)
angle = 0
for line in lines:
    x1, y1, x2, y2 = line[0]
    r = numpy.arctan2(y2 - y1, x2 - x1)
    angle += numpy.arctan2(y2 - y1, x2 - x1)
avg_radian = angle / len(lines)
avg_angle = avg_radian * 180 / numpy.pi
print("Average angle in degrees :" +str(avg_angle))
#####

lines = cv2.HoughLinesP(binary_thresh, 1, numpy.pi/180, 100, minLineLength = 600/2.0, maxLineGap=20)
angle = 0
for line in lines:
    x1, y1, x2, y2 = line[0]
    r = numpy.arctan2(y2 - y1, x2 - x1)
    angle += numpy.arctan2(y2 - y1, x2 - x1)
avg_radian = angle / len(lines)
avg_angle = avg_radian * 180 / numpy.pi
#print"Average angle is %f degrees" % avg_angle


# In[ ]:


img_blur = cv2.medianBlur(im,5)
img_thresh_Gaussian = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

plt.subplot(1,1,1),plt.imshow(img_thresh_Gaussian, cmap = 'gray')
plt.title("Image"), plt.xticks([]), plt.yticks([])
plt.show()


# In[38]:


img = cv2.imread('frontpage.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, binary_thresh = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY_INV)
edges = cv2.Canny(binary_thresh,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 50
lines = cv2.HoughLinesP(edges,1,numpy.pi/180, 100, minLineLength, maxLineGap)
#for x1,y1,x2,y2 in lines[0]:
#    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
angle = 0
for line in lines:
    x1, y1, x2, y2 = line[0]
    r = numpy.arctan2(y2 - y1, x2 - x1)
    angle += numpy.arctan2(y2 - y1, x2 - x1)
avg_radian = angle / len(lines)
avg_angle = avg_radian * 180 / numpy.pi
#cv2.imwrite('frontpage.jpg',img)
print("Average angle is degrees"+ str(avg_angle))


# In[34]:


plt.imshow(gray)


# In[ ]:


lines = cv2.HoughLinesP(edges,1, numpy.pi/180, 100, minLineLength=100, maxLineGap=50 )


# In[ ]:





# In[ ]:





# In[21]:


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilate = cv2.morphologyEx(binary_thresh, cv2.MORPH_DILATE, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5))
connected = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel, iterations=2)
fig = plt.figure(figsize=(30, 30))
#fig.add_subplot(1, 3, 1)
#plt.imshow(binary_thresh)
#fig.add_subplot(1, 3, 2)
#plt.imshow(dilate)
#fig.add_subplot(1, 3, 3)
plt.imshow(connected)


# In[33]:


contours,hierarchy=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
boxes=map(lambda c:cv2.boundingRect(c),contours)
filtered=filter(lambda b:b[2]>20 and b[3]>25,boxes)
plt.figure(figsize=(20, 20))
plt.imshow(edges)


# In[ ]:



