# Motion Detection in Football Videos

## Project Overview
This project implements a motion detection system for sports videos. It identifies and highlights areas of movement using frame differencing and contour detection.

## How to Run the Project
### **Install Dependencies**
Make sure you have Python and OpenCV installed. Run:
```bash
pip install opencv-python numpy
```

### **Run the Script**
This will process the video and generate two output videos in the `output/` folder:
- `output_raw.mp4` → Video without bounding boxes.
- `output_detected.mp4` → Video with detected movement highlighted.


## Approach Used
### **Frame Processing**
- Extracts frames at **5 FPS** and resizes them to **1280x720**.
- Converts frames to **grayscale** for efficient processing.

### **Motion Detection (Frame Differencing)**
- Computes the absolute difference between consecutive frames.
- Applies Gaussian Blur to reduce noise.
- Uses thresholding and dilation to enhance moving objects.

### **Contour Detection & Visualization**
- Identifies motion areas using `cv2.findContours()`.
- Filters small movements (`>1200 px`) to ignore noise.
- Draws bounding boxes around significant movements.


## Challenges Faced
1. **False Positives from Shadows & Noise**
   - Used dilation and a higher contour threshold to minimize false detections.
2. **Detecting Complete Players Instead of Body Parts**
   - Adjusted Gaussian Blur and minimum contour area.


## Author
Developed by Facundo Muruchi.