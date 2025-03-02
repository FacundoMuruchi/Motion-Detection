# Libraries
import cv2
import os
import numpy as np

# Video Configuration
VIDEO_PATH = "sample_video_clip.mp4" # sample video
OUTPUT_DIR = "output" # output folder
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
OUTPUT_VIDEO_RAW = os.path.join(OUTPUT_DIR, "output_raw.mp4") # raw video
OUTPUT_VIDEO_DETECTED = os.path.join(OUTPUT_DIR, "output_detected.mp4") # processed video
FPS = 5
RESIZE_DIM = (1280, 720)

# Upload video
cap = cv2.VideoCapture(VIDEO_PATH) # reading video
frame_rate = int(cap.get(cv2.CAP_PROP_FPS)) # original FPS
frame_interval = max(1, frame_rate // FPS)
frame_width, frame_height = RESIZE_DIM

# Output Video Configuration
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out_raw = cv2.VideoWriter(OUTPUT_VIDEO_RAW, fourcc, FPS, (frame_width, frame_height))
out_detected = cv2.VideoWriter(OUTPUT_VIDEO_DETECTED, fourcc, FPS, (frame_width, frame_height))

# Processing Video
ret, prev_frame = cap.read()
prev_frame = cv2.resize(prev_frame, RESIZE_DIM)
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    if frame_count % frame_interval == 0:
        frame_resized = cv2.resize(frame, RESIZE_DIM)
        gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
        
        # Motion Detection
        frame_diff = cv2.absdiff(prev_gray, gray)
        blurred = cv2.GaussianBlur(frame_diff, (5, 5), 0)
        _, thresh = cv2.threshold(blurred, 15, 255, cv2.THRESH_BINARY)
        
        # Bounding Boxes
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frame_with_contours = frame_resized.copy()
        
        for contour in contours:
            if cv2.contourArea(contour) > 2000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame_with_contours, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Writing Videos
        out_raw.write(frame_resized)  # raw video
        out_detected.write(frame_with_contours)  # processed video
        
        # Update Previous Frame
        prev_gray = gray.copy()
    
    frame_count += 1

# Closing and Cleaning
cap.release()
out_raw.release()
out_detected.release()
cv2.destroyAllWindows()

print("Videos saved as", OUTPUT_VIDEO_RAW, "and", OUTPUT_VIDEO_DETECTED)