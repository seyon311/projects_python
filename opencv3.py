import cv2

img = cv2.imread("example.jpg")
img = cv2.resize(img, (800, 600))
h, w = img.shape[:2]

cv2.rectangle(img, (50, 50), (w - 50, h - 50), (255, 0, 0), 2)

start_w = (50, h - 30)
end_w = (w - 50, h - 30)

cv2.arrowedLine(img, start_w, end_w, (0, 0, 255), 3, tipLength=0.05)
cv2.arrowedLine(img, end_w, start_w, (0, 0, 255), 3, tipLength=0.05)

cv2.putText(img, f"Width: {w-100}px", (w//2 - 100, h - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

start_h = (w - 30, 50)
end_h = (w - 30, h - 50)

cv2.arrowedLine(img, start_h, end_h, (0, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(img, end_h, start_h, (0, 255, 0), 3, tipLength=0.05)

cv2.putText(img, f"Height: {h-100}px", (w - 200, h//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Annotated Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()