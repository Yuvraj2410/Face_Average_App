# Average Face Generator

## Overview
This project demonstrates how to create an average face using OpenCV. The average face is generated from a set of input images, utilizing techniques such as facial landmark detection, coordinate transformation, and Delaunay triangulation.

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)


## Introduction
The average face can provide insights into beauty standards and cultural perceptions of attractiveness. This project aims to blend facial features from multiple images into a single composite image.

## Methodology
1. **Facial Feature Detection**: Using dlib, we calculate 68 facial landmarks for each input image.
2. **Coordinate Transformation**: We warp the faces to a fixed size and align the corners of the eyes for normalization.
3. **Face Alignment**: By aligning the facial features based on landmark points, we ensure accurate representation.
4. **Delaunay Triangulation**: We compute triangulations to divide the images into regions, facilitating smoother blending.
5. **Face Averaging**: We compute the average pixel intensity across the aligned images to create the final average face.

## Technologies Used
- Python
- OpenCV
- dlib
- FastAPI (backend)
- React (frontend)
- Vercel (frontend deployment)
- Render (backend deployment)

## Usage
Start the backend server:
`uvicorn main:app --reload`

Visit the frontend on Vercel to upload images and generate the average face.

frontend deployment - https://face-average-app.vercel.app/

backend deployment - https://face-average-app.onrender.com

