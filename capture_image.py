import cv2
import os
import numpy as np
from facenet_pytorch import MTCNN
from PIL import Image

# Initialize MTCNN for face detection
mtcnn = MTCNN(keep_all=False, device='cpu')

# Create dataset directories
os.makedirs("dataset/authorized", exist_ok=True)
os.makedirs("dataset/unauthorized", exist_ok=True)

# Function to capture images while the spacebar is held down
def capture_images(user_name="unknown", user_type="unauthorized"):
    cap = cv2.VideoCapture(0)
    count = 0
    max_images = 1500  # Maximum images per session
    img_size = (250, 250)  # Target size for face images

    if user_type == "authorized":
        save_path = os.path.join("dataset/authorized", user_name)
        os.makedirs(save_path, exist_ok=True)
    else:
        save_path = "dataset/unauthorized"  # All unauthorized images go here

    print(f"[INFO] Hold SPACEBAR to capture images for {user_name} ({user_type}).")
    print("[INFO] Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect faces
        boxes, _ = mtcnn.detect(frame)

        # Display the webcam feed
        cv2.imshow("Capturing Faces", frame)

        key = cv2.waitKey(1) & 0xFF
        
        # Continuously capture images while SPACEBAR is held down
        if key == ord(' '):  
            if boxes is not None:
                for (x, y, x2, y2) in boxes:
                    face = frame[int(y):int(y2), int(x):int(x2)]
                    if face.size > 0:
                        # Convert face to PIL image, resize to 250x250, and save
                        face_resized = Image.fromarray(cv2.cvtColor(face, cv2.COLOR_BGR2RGB)).resize(img_size)
                        img_path = os.path.join(save_path, f"face_{count}.jpg")
                        face_resized.save(img_path)
                        count += 1
                        print(f"[INFO] Captured: {img_path}")

                        if count >= max_images:
                            print(f"[INFO] {max_images} images captured. Exiting...")
                            cap.release()
                            cv2.destroyAllWindows()
                            return
        
        # Quit if 'q' is pressed
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"[INFO] {count} images saved in {save_path}")

# Capture authorized images
user_type = input("Enter type (authorized/unauthorized): ").strip().lower()
if user_type == "authorized":
    user_name = input("Enter authorized person's name: ").strip()
else:
    user_name = "unknown"  # Unauthorized images are stored directly

capture_images(user_name, user_type)
