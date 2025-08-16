import cv2

image = cv2.imread("Bmw M3.jpg")
image = cv2.resize(image, (500,400))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Choose a filter: sobelx, sobely, canny, laplacian, gaussian, median, exit")

while True:
    choice = input("Enter filter name").lower()

    if choice == "sobelx":
        result = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
        cv2.imshow("Sobel X", result)

    elif choice == "sobely":
        result = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
        cv2.imshow("Sobel Y", result)

    elif choice == "canny":
        result = cv2.Canny(gray, 100, 200)
        cv2.imshow("Canny", result)

    elif choice == "laplacion":
        result = cv2.Laplacian(gray, cv2.CV_64F)
        cv2.imshow("Laplacion", result)

    elif choice == "gaussian":
        result = cv2.GaussianBlur(gray, (5, 5), 0)
        cv2.imshow("Gaussian Blur", result)

    elif choice == "median":
        result = cv2.medianBlur(gray, 5)
        cv2.imshow("Median Blur", result)

    elif choice == "exit":
        print("Goodbye! Closing Windows...")
        break

    else:
        print("❌ Not a valid choice, try again!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()