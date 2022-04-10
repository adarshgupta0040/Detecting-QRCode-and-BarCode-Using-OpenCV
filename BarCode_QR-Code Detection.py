import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode


# img=cv.imread("Resources/QR_Barcode/QRcode.png")
# code=decode(img)
# print(code)


# img=cv.imread('Resources/QR_Barcode/QRcode.png')
# code=decode(img)
# for barcode in code:
#     print(barcode.data)   #output will be in b that means byte


# since the data is in byte we need to decode it

# img=cv.imread('Resources/QR_Barcode/QRcode.png')
# code=decode(img)
# for barcode in code:
#     print(barcode.data)
#     myData=barcode.data.decode("utf-8")   #convert into strings
#     print()
#     print(myData)


screen = cv.VideoCapture(1)
screen.set(3, 740)  # width
screen.set(4, 480)  # height

with open("Resources/QR_Barcode/myData.text") as f:
    myDatalist= f.read().splitlines()
print(myDatalist)


# while (True):
#     success, img = screen.read()
#     for barcode in decode(img):
#         #print(barcode.data)
#         myData = barcode.data.decode("utf-8")  # convert into strings
#         print(myData)
#         # add bounding box
#         pts=np.array([barcode.polygon],np.int32)
#         pts=pts.reshape((-1,1,2))
#         cv.polylines(img,[pts],True,(255,0,255),5)
#         pts2=barcode.rect
#         cv.putText(img,myData,(pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
#         #
#
#     cv.imshow("Result_output", img)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break


while (True):
    success, img = screen.read()
    for barcode in decode(img):
        #print(barcode.data)
        myData = barcode.data.decode("utf-8")  # convert into strings
        print(myData)
        if myData in myDatalist:
            print("Authorised")
            myOutput="Authorised"
            myColor=(7, 79, 12)

        else:
            print("Un-Authorised")
            myOutput="Un-Authorised"
            myColor=(0,0,255)

        # add bounding box
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv.polylines(img,[pts],True,myColor,5)
        pts2=barcode.rect
        cv.putText(img,myOutput,(pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)
        #

    cv.imshow("Result_output", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break