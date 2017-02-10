import cv2
import numpy as np

image = cv2.imread("di_in_cache.jpeg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
edged = cv2.Canny(gray_image, 30, 200)

_, cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
cnts = sorted(cnts, key= cv2.contourArea, reverse = True)[:5]
candidates = []

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) > 2:
        candidates.append(approx)
        
mask = np.zeros_like(gray_image)
cv2.drawContours(mask, candidates, 0, (255, 255, 255), -1)

#cv2.imshow("mask", mask)

out = np.zeros_like(gray_image)
out[mask == 255] = gray_image[mask == 255]

#cv2.imshow("woo", out)
ret,filter_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
ret,filter_maskimage = cv2.threshold(out, 150, 255, cv2.THRESH_BINARY)

try:
    cv2.imshow("mask", mask)
    cv2.imshow("woo", out)
    cv2.imshow("Dice", image)
    cv2.imshow("Dice - gray", gray_image)
    cv2.imshow("Dice - filtered", filter_image)
    cv2.imshow("Dice - masked - filtered", filter_maskimage)
    cv2.waitKey(0)
except:
    from matplotlib import pyplot as plt
    plt.imshow(filter_maskimage, cmap = 'gray')
    plt.show()
