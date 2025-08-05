import cv2
import matplotlib.pyplot as plt
img = cv2.imread("MARCUS RASHFROD.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w, _ = img.shape

cv2.rectangle(img, (20, 20), (170, 170), (0, 255, 255), 3)
cv2.rectangle(img, (w-220, h-170), (w-20, h-20), (255, 0 ,255), 3)

center1 = (95, 95)
center2 = (w-120, h-95)
cv2.circle(img, center1, 15, (0, 255, 0), -1)
cv2.circle(img, center2, 15, (0, 0, 255), -1)

cv2.line(img, center1, center2, (0,255, 0), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Region 1", (20, 15), font, 0.6, (0, 255, 255), 2)
cv2.putText(img, "Region 2", (w-220, h-180), font, 0.6, (255, 0, 255), 2)
cv2.putText(img, "Center 1", (55, 135), font, 0.6, (0, 255, 0), 2)
cv2.putText(img, "Center 2", (center2[0]-40, center2[1]+40), font, 0.6, (0, 0, 255), 2)

cv2.arrowedLine(img, (w-50, 20), (w-50, h-20), (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(img, (w-50, h-20), (w-50, 20), (255, 255, 0), 3, tipLength=0.05)
cv2.putText(img, f"Height: {h}px", (w-200, h//2), font, 0.7, (255, 255, 0), 2)

plt.imshow(img)
plt.axis("off")
plt.title("Annotated Image")
plt.show()