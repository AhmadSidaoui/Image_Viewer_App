# Image Viewer and Segmentation App

## Introduction
This is a simple image viewer application with additional features such as extracting metadata and image segmentation. The application is built using the Tkinter library in Python and leverages popular image processing libraries like OpenCV and NumPy for segmentation.

## Features
1. **Image Viewing**: Browse through a folder containing images and view them in the application.
2. **Metadata Extraction**: Extract and display metadata information from the selected image.
3. **Image Segmentation**: Perform image segmentation using K-means clustering. Adjust the number of clusters for different segmentation results.

## Dependencies
- Python 3.x
- Tkinter
- PIL (Pillow)
- NumPy
- OpenCV
- Matplotlib

## How to Use
1. Run the application by executing the provided Python script (`image_viewer_app.py`).
2. Click the "open" button to select a folder containing images.
3. Use the "<" and ">" buttons to navigate between images in the folder.
4. Click the "meta" button to extract and display metadata for the current image.
5. Adjust the "Cluster Number" spinbox to set the number of clusters for image segmentation.
6. Click the "Segment Image" button to perform image segmentation using K-means clustering.

## Important Notes
- Supported image formats: JPG, JPEG, PNG.
- The application automatically resizes images for better display.
- Image segmentation results are displayed in the same window.

## Acknowledgments
- This application uses the K-means clustering algorithm for image segmentation.

## Author
Ahmad Sidaoui

Feel free to contribute, report issues, or suggest improvements!
