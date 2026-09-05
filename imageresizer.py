import cv2

image = cv2.imread("example.jpg")

x1 = int(input("Enter the width of the first resized image: "))
y1 = int(input("Enter the height of the first resized image: "))

x2 = int(input("Enter the width of the second resized image: "))
y2 = int(input("Enter the height of the second resized image: "))

x3 = int(input("Enter the width of the third resized image: "))
y3 = int(input("Enter the height of the third resized image: "))

resized1 = cv2.resize(image, (x1, y1))
cv2.imshow("Resized Image 1", resized1)

resized2 = cv2.resize(image, (x2, y2))
cv2.imshow("Resized Image 2", resized2)

resized3 = cv2.resize(image, (x3, y3))
cv2.imshow("Resized Image 3", resized3)

key = cv2.waitKey(0)

if key == ord('s'): # ASCII for 's' is 83
    cv2.imwrite("resized_image1.jpg", resized1)
    cv2.imwrite("resized_image2.jpg", resized2)
    cv2.imwrite("resized_image3.jpg", resized3)
    print("Images saved as resized_image1.jpg, resized_image2.jpg, and resized_image3.jpg")

else:
    print("Images not saved.")

cv2.destroyAllWindows()
