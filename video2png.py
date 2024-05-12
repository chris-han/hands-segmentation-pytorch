import cv2
import os

def rotate_video_and_extract_frames(video_path):
    # Check if the directory for frames exists, if not, create it
    parts = video_path.split('_', 2)
    frames_dir = parts[0] + '_' + parts[1] + '_frames'
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Check if video opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        return
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Rotate the frame
        frame_rotated = cv2.rotate(frame, cv2.ROTATE_180)
        
        # Save the frame
        frame_path = os.path.join(frames_dir, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_path, frame_rotated)
        
        frame_count += 1
    
    cap.release()
    print(f"Extracted and rotated {frame_count} frames from {video_path}")

# Assuming data_set is a directory containing multiple video files
import glob

video_files = glob.glob('data_set/*.mp4')

for video_path in video_files:
    rotate_video_and_extract_frames(video_path)