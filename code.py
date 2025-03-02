# Libraries
import cv2
import os
import numpy as np

# Video Configuration
VIDEO_PATH = "sample_video_clip.mp4" # sample video
OUTPUT_DIR = "output3" # output folder
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