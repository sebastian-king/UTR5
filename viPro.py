import cv2
import numpy as np

image = cv2.imread("di_in_cache.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)

_, cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
candidates = []

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) > 5:
        candidates.append(approx)

mask = np.zeros_like(image)
cv2.drawContours(mask, candidates, 0, (255, 255, 255), -1)


out = np.zeros_like(image)
out[mask == 255] = image[mask == 255]

cv2.drawContours(image, candidates, -1, (0, 255, 0), 3)

ret, th = cv2.threshold(out, 80, 255, cv2.THRESH_BINARY)

try:
    cv2.imshow("mask", mask)
    cv2.imshow("woo", out)
    cv2.waitKey(0)
except:
    from matplotlib import pyplot as plt
    plt.imshow(th, cmap = 'gray')
    plt.show()
