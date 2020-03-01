import cv2
import numpy as np
import random as rng

def bounding_boxes(contours,img) :   
    minRect = [None]*len(contours)
    minEllipse = [None]*len(contours)
    angles = dict()
    for i, c in enumerate(contours):
        minRect[i] = cv2.minAreaRect(c)
        if c.shape[0] > 5:
            minEllipse[i] = cv2.fitEllipse(c)
            angles[minEllipse[i]] = minEllipse[i][2]
    drawing_ellipse = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    drawing_rectangle = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    #drawing_ellipse = find_points(minRect,minEllipse,drawing_ellipse)

    for i, c in enumerate(contours):
        if cv2.contourArea(c) < 3:
            continue
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        #cv2.drawContours(drawing, contours, i, color)
        # ellipse
        if c.shape[0] > 5 and minRect[i][1][0]+10 < minRect[i][1][1]:
            cv2.ellipse(drawing_ellipse, minEllipse[i], color, 2)
        # rotated rectangle
        box = cv2.boxPoints(minRect[i])
        box = np.intp(box) #np.intp: Integer used for indexing (same as C ssize_t; normally either int32 or int64)
        cv2.drawContours(drawing_rectangle, [box], 0, color)
    cv2.imshow('Contours', drawing_ellipse)
    cv2.imshow('contours', drawing_rectangle)

def find_points(minRect, minEllipse, drawing):
    minEllipse_1 = list()
    color = (23,34,12)
    for j, i in enumerate(minRect):
        print(i)
        if i is None:
            continue
        if i[1][0] > i[1][1]:
            print(i)
            cv2.ellipse(drawing, minEllipse[j], color, 2)
    #cv2.line(drawing,(int(x1),int(y1)),(0,0),(255,13,22),2)
    return drawing
    
def find_ellipse():
    pass

 
if __name__ == "__main__":
    frame = cv2.imread("img1.jpg")
    img = frame[:]

    scale_percent = 200 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
     

    img = np.zeros(resized.shape,dtype=np.uint8)
    img.fill(0) # or img[:] = 255

    dst = cv2.GaussianBlur(resized,(5,5),cv2.BORDER_DEFAULT)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    gray_filtered = cv2.bilateralFilter(gray, 7, 50, 50)
    ret3,th31 = cv2.threshold(gray_filtered,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    edges_high_thresh = cv2.Canny(th31, 50, 150)
    _,contours, hierarchy = cv2.findContours(edges_high_thresh,cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) 
    bounding_boxes(contours, edges_high_thresh)
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        #cv2.rectangle(og_image,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.drawContours(img, c, -1, (255,255,255), 1)
    cv2.imshow('Frame', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


















    
