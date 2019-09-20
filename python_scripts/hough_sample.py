import cv2
import numpy as np

def pick_up_blue_ball():
    cap = cv2.VideoCapture(0)

    while True:
        ret,img = cap.read()
        size = (640,480)
        cimg1 = img

        # Convert to hsv
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([150, 255, 255])
        img_mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        img_color_blue = cv2.bitwise_and(img, img, mask=img_mask_blue)

        # Hough_tranceration
        img = img[:,::-1]
        img_color_blue = cv2.resize(img_color_blue, size)
        img_color_blue = cv2.GaussianBlur(img_color_blue, (33,33), 1)

        cimg2 = img_color_blue

        img_color_blue = cv2.cvtColor(img_color_blue, cv2.COLOR_RGB2GRAY)
        circles = cv2.HoughCircles(img_color_blue,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=10,maxRadius=120)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                #draw the outer circle
                cv2.circle(cimg1,(i[0],i[1]),i[2],(0,255,0),2)
                #draw the center of the circle
                cv2.circle(cimg1,(i[0],i[1]),2,(0,0,255),3)

        cv2.imshow('orizin',cimg1)
        cv2.imshow('blue',cimg2)
        k = cv2.waitKey(10)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    pick_up_blue_ball()
