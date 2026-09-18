import cv2
import numpy as np

# Load image
image = cv2.resize(cv2.imread("example.jpg"), (1020, 600))

if image is None:
    print("Image not found!")
    exit()

# Create window
window_name = "Image Color Filter"
cv2.namedWindow(window_name)

# Trackbar function
def nothing(x):
    pass

# Create RGB intensity sliders
cv2.createTrackbar("Red", window_name, 100, 200, nothing)
cv2.createTrackbar("Green", window_name, 100, 200, nothing)
cv2.createTrackbar("Blue", window_name, 100, 200, nothing)

print("Controls:")
print("R - Increase Red")
print("G - Increase Green")
print("B - Increase Blue")
print("r - Reset")
print("S - Save Image")
print("Q - Quit")

while True:

    # Get slider values
    red = cv2.getTrackbarPos("Red", window_name)
    green = cv2.getTrackbarPos("Green", window_name)
    blue = cv2.getTrackbarPos("Blue", window_name)

    # Convert image to float
    filtered = image.astype(np.float32)

    # OpenCV uses BGR
    filtered[:, :, 0] *= blue / 100
    filtered[:, :, 1] *= green / 100
    filtered[:, :, 2] *= red / 100

    # Keep values between 0 and 255
    filtered = np.clip(filtered, 0, 255)

    # Convert back to image format
    filtered = filtered.astype(np.uint8)

    # Show values
    cv2.putText(
        filtered,
        f"Red: {red}%",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    cv2.putText(
        filtered,
        f"Green: {green}%",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        filtered,
        f"Blue: {blue}%",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

    # Display image
    cv2.imshow(window_name, filtered)

    key = cv2.waitKey(1) & 0xFF

    # Keyboard controls
    if key == ord('R'):
        cv2.setTrackbarPos("Red", window_name, min(red + 10, 200))

    elif key == ord('G'):
        cv2.setTrackbarPos("Green", window_name, min(green + 10, 200))

    elif key == ord('B'):
        cv2.setTrackbarPos("Blue", window_name, min(blue + 10, 200))

    # Reset
    elif key == ord('r'):
        cv2.setTrackbarPos("Red", window_name, 100)
        cv2.setTrackbarPos("Green", window_name, 100)
        cv2.setTrackbarPos("Blue", window_name, 100)

    # Save
    elif key == ord('s') or key == ord('S'):
        cv2.imwrite("filtered_photo.jpg", filtered)
        print("Image saved as filtered_photo.jpg")

    # Exit
    elif key == ord('q') or key == ord('Q'):
        break