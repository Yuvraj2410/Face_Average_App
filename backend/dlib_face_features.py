import cv2
import dlib
import numpy as np
from io import BytesIO
from PIL import Image

# Load the pre-trained face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('D:\code\Data_Science\Data_Science_Project\Face_Average\shape_predictor_68_face_landmarks.dat\shape_predictor_68_face_landmarks.dat')

def detect_landmarks(image_file, scale_factor=0.5):   
    try:
        # Load the image from the in-memory file
        image = np.array(Image.open(BytesIO(image_file)))
        print(f"Image shape: {image.shape}")
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = detector(gray)

        # Initialize a list to store landmarks
        landmark_points = []

        # Loop over each detected face
        for face in faces:
            # Get the landmarks
            landmarks = predictor(gray, face)

            # Collect landmarks in a list
            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                landmark_points.append((x, y))

        return landmark_points
    except Exception as e:
        print(f"Error in detect_landmarks: {e}")
        return []