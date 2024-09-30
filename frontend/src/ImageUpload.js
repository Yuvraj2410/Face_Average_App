import React, { useState } from 'react';
import axios from 'axios';
import './ImageUpload.css';

const ImageUpload = () => {
    const [imageInputs, setImageInputs] = useState([0]); // Array to hold the state of file inputs
    const [images, setImages] = useState([]);
    const [averagedImage, setAveragedImage] = useState(null);
    const [loading, setLoading] = useState(false);

    // Function to handle image selection
    const handleImageChange = (event, index) => {
        const selectedFile = event.target.files[0];
        const newImages = [...images];
        newImages[index] = selectedFile;
        setImages(newImages);
    };

    // Function to handle form submission
    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        
        images.forEach((image) => {
            formData.append('files', image);
        });

        setLoading(true);

        try {
            const response = await axios.post('http://localhost:8000/upload_images/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log('Response:', response.data); // Check response for debugging
            const base64Image = `data:image/jpeg;base64,${response.data.averaged_image}`; // Prefix with data type
        setAveragedImage(base64Image); // Update the averaged image state
        } catch (error) {
            if (error.response) {
                // The request was made and the server responded with a status code
                console.error('Error uploading images:', error.response.data);
            } else if (error.request) {
                // The request was made but no response was received
                console.error('No response received:', error.request);
            } else {
                // Something happened in setting up the request that triggered an Error
                console.error('Error', error.message);
                alert('An unexpected error occurred. Please try again.');
            }
        } finally {
            setLoading(false);
        }
    };

    // Function to add a new file input
    const addImageInput = () => {
        setImageInputs([...imageInputs, imageInputs.length]); // Adds a new input
    };

    // Function to remove a file input
    const removeImageInput = (index) => {
        const newInputs = imageInputs.filter((_, i) => i !== index);
        const newImages = images.filter((_, i) => i !== index); // Remove corresponding image
        setImageInputs(newInputs);
        setImages(newImages);
    };

    return (
        <div>
            <h1>Image Upload</h1>
            <form onSubmit={handleSubmit}>
                {imageInputs.map((input, index) => (
                    <div key={index} style={{ marginBottom: '10px', display: 'flex', alignItems: 'center' }}>
                        <input
                            type="file"
                            onChange={(event) => handleImageChange(event, index)}
                            style={{ marginRight: '10px' }}
                        />
                        <button type="button" onClick={() => removeImageInput(index)}>-</button>
                    </div>
                ))}
                <button type="button" onClick={addImageInput}>+</button>
                <button type="submit" style={{ marginLeft: '10px' }} disabled={loading}>{loading ? 'Uploading...' : 'Upload'}</button>
            </form>
            {averagedImage && <img src={averagedImage} alt="Averaged" style={{ maxWidth: '100%', height: 'auto' }} />}
        </div>
    );
};

export default ImageUpload;
