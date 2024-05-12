import cv2
import os
import numpy as np
from natsort import natsorted
from visualize_mask import draw_contours
import matplotlib.pyplot as plt

def create_masked_video(folder_name):
    # Initialize video writer with None. It will be defined later with the first frame's size.
    video_out = None
    
    # Get the list of image files in the specified folder
    image_files = natsorted([f for f in os.listdir(folder_name) if f.endswith('.png') or f.endswith('.jpg')])
    
    for image_file in image_files:
        masked_image = draw_contours(folder_name, image_file)
        if video_out is None:
            # Get the size of the first frame
            height, width = masked_image.shape[:2]
            # Define the codec and create VideoWriter object with the size of the first frame
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            video_out = cv2.VideoWriter(folder_name+'_masked.mp4', fourcc, 20.0, (width, height))
        masked_image = np.clip(masked_image * 255, 0, 255).astype('uint8')
        
        #image using RGB, video using BGR
        masked_image_bgr = cv2.cvtColor(masked_image, cv2.COLOR_RGB2BGR)
        # plt.imshow(masked_image)
        # plt.show()
        # Write the frame to the video
        video_out.write(masked_image_bgr)
    
    # Release the video writer
    if video_out is not None:
        video_out.release()

# Example usage
create_masked_video('data_set/0200A1795784_frames')