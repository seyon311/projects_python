import cv2
from deepface import DeepFace

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:

    # Capture frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Process every detected face
    for (x, y, w, h) in faces:

        # Draw rectangle around face
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        # Crop face
        face = frame[y:y + h, x:x + w]

        try:
            # Detect emotion
# Crop face
            face = frame[y:y + h, x:x + w]

            # Ensure it's a proper numpy array
            import numpy as np
            face = np.array(face)

            # Skip empty or invalid crops
            if face is None or face.size == 0:
                continue
            print("FACE TYPE:", type(face), "SHAPE:", getattr(face, "shape", None))

            result = DeepFace.analyze(
                face,
                actions=["emotion"],
                enforce_detection=False
            )

            # Handle dict or list formats
            if isinstance(result, list):
                emotion = result[0]["dominant_emotion"]
            else:
                emotion = result["dominant_emotion"]



            # Display emotion
            cv2.putText(
                frame,
                "Emotion: " + emotion,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        except Exception as e:
            print("Emotion detection error:", e)

    # Show result
    cv2.imshow(
        "Real-Time Face and Emotion Detection",
        frame
    )

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera
cap.release()
cv2.destroyAllWindows()

# IT IS NOT WORKING FOR SOME REASON