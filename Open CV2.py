import cv2
image= cv2.imread("MARCUS RASHFROD.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(gray_image, (224, 224))
cv2.imshow("Processed Image", resized_image)
key=cv2.waitKey(0)
if key == ord("s"):
    cv2.imwrite("grayscale_resized_MARCUS RASHFROD.jpg", resized_image)
    print("image saved as  grayscale_resized_MARCUS RASHFROD.jpg")
else:
    print("Image not saved")
cv2.destroyAllWindows()
print(f"Processed Image DImensions: {resized_image.shape}")