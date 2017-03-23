import cv2
import numpy as np
import os,sys
#import Image`

path = "C:\Users\Sean\PycharmProjects\Processing_Region5"

#file_name = os.path.join(path, "di_in_cache.jpeg")
#for f in

#image = Image

kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])  #

kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])

kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                             [-1,2,2,2,-1],
                             [-1,2,8,2,-1],
                             [-1,2,2,2,-1],
                             [-1,-1,-1,-1,-1]]) / 8.0

#image = cv2.LoadImage("C:/Users/Sean\PycharmProjects/Processing_Region5/di_in_cache.jpeg",  cv2.COLOR_BGR2GRAY )

image = cv2.imread("C:/Users/Sean/PycharmProjects/Processing_Region5/dieLED4.jpg")

#image = cv2.imread("C:/Users/Sean/PycharmProjects/Processing_Region5/di_in_cache.jpg")



screen_res = 1280, 720
scale_width = screen_res[0] / image.shape[1]
scale_height = screen_res[1] / image.shape[0]
scale = min(scale_width, scale_height)
window_width = int(image.shape[1] * scale)
window_height = int(image.shape[0] * scale)



cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
cv2.resizeWindow('dst_rt', window_width, window_height)

cv2.namedWindow('dst_rt2', cv2.WINDOW_NORMAL)
cv2.resizeWindow('dst_rt2', window_width, window_height)


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blur = cv2.GaussianBlur(gray_image,(5,5),0)
ret2,th2 = cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


#cv2.imshow("gb", th3)
#cv2.imshow("gb", th2)

#gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)


#output_1 = cv2.filter2D(gray_image, -1, kernel_sharpen_1)
#output_2 = cv2.filter2D(output_1, -1, kernel_sharpen_3)

#blur = cv2.bilateralFilter(output_2, 9, 75, 75)
#edged = cv2.Canny(output_2, 30, 200)

#cv2.imshow("dst_rt2", th3)
#cv2.imshow("dst_rt", th2)
#cv2.waitKey(0)

_ , cnts, _ = cv2.findContours(th3.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
print(len(cnts) - 1)


# ###candidates = []
#
# for c in cnts:
#     peri = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#     if len(approx) > 2:
#         candidates.append(approx)
#
# mask = np.zeros_like(gray_image)
# cv2.drawContours(mask, candidates, 0, (255, 255, 255), -1)
#
#
#
# cv2.imshow("mask", mask)
# cv2.waitKey(0)
#
#
#
# out = np.zeros_like(gray_image)
# out[mask == 255] = gray_image[mask == 255]
#
# # cv2.imshow("woo", out)
#
# ret, filter_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
# ret, filter_maskimage = cv2.threshold(out, 150, 255, cv2.THRESH_BINARY)
#
# #gray = cv2.bilateralFilter(gray, 11, 17, 17)
# #edged = cv2.Canny(gray, 30, 200)
#
#
#
#
# dots = cv2.bilateralFilter(filter_maskimage, 11, 17, 17)
# _, cnts, _ = cv2.findContours(dots, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(len(cnts) - 1)  # -1 because the die itself counts
#
# #Try to shorten the array by cutting any black square of at least 40*40 pixels
#
# try:
#     cv2.imshow("mask", mask)
#     cv2.imshow("woo", out)
#     cv2.imshow("Dice", image)
#     cv2.imshow("Dice - gray", gray_image)
#     cv2.imshow("Dice - filtered", filter_image)
#     cv2.imshow("Dice - masked - filtered", filter_maskimage)
#     cv2.waitKey(0)
# except:
#     from matplotlib import pyplot as plt
#
#     plt.imshow(filter_maskimage, cmap='gray')
# ###    plt.show()