import cv2
import numpy as np
import os,sys
import imutils

# you will need imutils to be downloaded

path = "C:\Users\Sean\PycharmProjects\Processing_Region5"

#file_name = os.path.join(path, "di_in_cache.jpeg")
#for f in

#image = Image
#image = cv2.LoadImage("C:/Users/Sean\PycharmProjects/Processing_Region5/di_in_cache.jpeg",  cv2.COLOR_BGR2GRAY )
image = cv2.imread("C:/Users/Sean/PycharmProjects/Processing_Region5/di_in_cache.jpg")

height, width, channels = image.shape


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gb", gray_image)
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
edged = cv2.Canny(gray_image, 30, 200)

#cv2.imshow("g", edged)
_ , cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]



candidates = []

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) > 2:
        candidates.append(approx)

mask = np.zeros_like(gray_image)
cv2.drawContours(mask, candidates, 0, (255, 255, 255), -1)

(_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]



cv2.imshow("mask", mask)
#cv2.waitKey(0)

_, cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#print(len(cnts) - 1)  # -1 because the die itself counts
#cnts = cnts[0] if imutils.is_cv2() else cnts[1]
c = max(cnts, key=cv2.contourArea)

extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

LeftSpot = tuple([] , [])
NorthSpot = tuple([] [])
RightSpot = tuple([] [])
SouthSpot = tuple([] [])


#cv2.drawContours(mask, [c], -1, (0, 255, 255), 2)
#cv2.circle(mask, extLeft, 8, (0, 0, 255), -1)
#cv2.circle(mask, extRight, 8, (0, 255, 0), -1)
#cv2.circle(mask, extTop, 8, (255, 0, 0), -1)
#cv2.circle(mask, extBot, 8, (255, 255, 0), -1)

# show the output image
cv2.imshow("Image", mask)
cv2.waitKey(0)

#Try to shorten the array by cutting any black square of at least 40*40 pixels

''
