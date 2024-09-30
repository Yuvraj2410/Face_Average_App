from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
import numpy as np
import cv2
from dlib_face_features import detect_landmarks
from faceAverage import average_face
from io import BytesIO
from PIL import Image
from typing import List
import traceback
import base64
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload_images/")
async def upload_images(files: List[UploadFile] = File(...)):
    try:
        images = []
        all_landmarks = []
        print(f'Received {len(files)} files.')
        for file in files:
            contents = await file.read()
            print(f"Processing file: {file.filename}")
            
            # Process each image
            landmarks = detect_landmarks(contents)
            if not landmarks:
                raise HTTPException(status_code=400, detail=f"Could not detect landmarks in {file.filename}")
            
            image = np.array(Image.open(BytesIO(contents)))
            print(f"Image shape: {image.shape}")
            
            all_landmarks.append(landmarks)
            images.append(image)

        # Compute the average face
        average_face_image = average_face(images, all_landmarks)
        print("Average face computed successfully")

        average_face_image = cv2.cvtColor(average_face_image, cv2.COLOR_BGR2RGB)

        # Convert the image back to a byte format for the response
        _, encoded_image = cv2.imencode('.jpg', average_face_image)
        print("Image encoding successful")

        encoded_image = encoded_image.tobytes()
        # image_bytes = BytesIO(encoded_image.tobytes())

        # # Return the image as a StreamingResponse
        # return StreamingResponse(image_bytes, media_type="image/jpeg")

        jpg_as_text = base64.b64encode(encoded_image).decode('utf-8')  # Convert to base64 string
    
        return JSONResponse(content={"averaged_image": jpg_as_text})

    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))