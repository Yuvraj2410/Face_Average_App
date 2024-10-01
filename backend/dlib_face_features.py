import cv2
import dlib
import numpy as np
from io import BytesIO
from PIL import Image
import os 

# Load the pre-trained face detector and landmark predictor
detector = dlib.get_frontal_face_detector()

# predictor = dlib.shape_predictor('https://facefeaturedata.s3.eu-north-1.amazonaws.com/shape_predictor_68_face_landmarks.dat')
# URL of the .dat file
# model_url = 'https://facefeaturedata.s3.eu-north-1.amazonaws.com/shape_predictor_68_face_landmarks.dat'
# local_model_path = 'shape_predictor_68_face_landmarks.dat'

# # Check if the file already exists locally, if not download it
# if not os.path.exists(local_model_path):
#     print(f"Downloading {local_model_path}...")
#     urllib.request.urlretrieve(model_url, local_model_path)
#     print(f"Downloaded {local_model_path} successfully!")

# # Load the predictor from the local file
# predictor = dlib.shape_predictor(local_model_path)

# # Check if the file exists for debugging
# if not os.path.exists('shape_predictor_68_face_landmarks.dat'):
#     raise FileNotFoundError("shape_predictor_68_face_landmarks.dat not found")

# predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Update path to use the cloned repo's path
predictor = dlib.shape_predictor('eameo-faceswap-generator/shape_predictor_68_face_landmarks.dat')


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
