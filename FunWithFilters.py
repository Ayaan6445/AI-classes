import cv2

image = cv2.imread("MARCUS RASHFROD.jpg")

original = image.copy()

def apply_filter(key, img):
    if key == ord("o"):
        return original
    elif key == ord("s"):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, 3)
        sobely = cv2.Sobel(gray, cv2.CV64F, 0, 1, 3)
        sobel = cv2.magnitude(sobelx, sobely)
        return cv2.convertScaleAbs(sobel)
    elif key == ord("c"):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 100, 200)
    elif key == ord("a"):
        return cv2.GaussianBlur(img, (7, 7), 0)
    elif key == ord("m"):
        return cv2.medianBlur(img, 5)
    elif key == ord("r"):
        tinted = img.copy()
        tinted[:, :, 0] = 0
        tinted[:, :, 1] = 0
        return tinted
    elif key == ord("g"):
        tinted = img.copy()
        tinted[:, :, 0] = 0
        tinted[:, :, 2] = 0
        return tinted
    elif key == ord("b"):
        tinted = img.copy()
        tinted[:, :, 1] = 0
        tinted[:, :, 2] = 0
        return tinted
    elif key == ord("R"):
        img_copy = img.copy()
        img_copy[:, :, 2] = cv2.add(img_copy[:, :, 2], 50)
        return img_copy
    elif key == ord("G"):
        img_copy = img.copy()
        img_copy[:, :, 1] = cv2.add(img_copy[:, :, 1], 50)
        return img_copy
    elif key == ord("B"):
        img_copy = img.copy()
        img_copy[:, :, 0] = cv2.add(img_copy[:, :, 0], 50)
        return img_copy
    else:
        return img
    
cv2.namedWindow("Interactive Filters")
while True:
    cv2.imshow("Interactive Filters", image)
    key = cv2.waitKey(0) & 0xFF

    if key == ord("q"):
        break
    else:
        image = apply_filter(key, original)
cv2.destroyAllWindows()