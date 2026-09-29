import cv2
import os

cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.putText(
        frame, f"Faces detected: {len(faces)}", (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
    )
    return frame

def webcam_mode():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Unable to open webcam.")
        return

    print("Webcam started. Press 'q' to exit.")
    while True:
        ok, frame = camera.read()
        if not ok:
            break

        frame = detect_faces(frame)
        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

def image_mode():
    path = input("Enter image path: ").strip().strip('"')

    if not os.path.isfile(path):
        print("Image not found.")
        return

    image = cv2.imread(path)
    if image is None:
        print("Unable to open image.")
        return

    image = detect_faces(image)
    cv2.imshow("Face Detection", image)
    print("Press any key in the image window to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("======================================")
print("        FACE DETECTION SYSTEM")
print("======================================")

while True:
    print("\n1. Detect faces using webcam")
    print("2. Detect faces in an image")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        webcam_mode()
    elif choice == "2":
        image_mode()
    elif choice == "3":
        print("Thank you for using the Face Detection System!")
        break
    else:
        print("Invalid choice.")
