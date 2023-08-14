import cv2

img = cv2.imread("solar-system.jpg")
sun = "Sun"
cv2.putText(img,sun,(120,40),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
cv2.putText(img,"mercury",(140,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"venus",(210,160),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"earth",(310,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"mars",(410,160),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"jupiter",(570,40),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"saturn",(800,335),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"uranus",(980,105),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img,"neptune",(1160,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))


cv2.imshow("Solar",img)
cv2.imwrite("solar1.png",img)
cv2.waitKey(0)