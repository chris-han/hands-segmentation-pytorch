import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
import numpy as np
import cv2
def draw_contours(original_image_folder,original_image_name):
    original_image_path = Path(original_image_folder) / original_image_name
    # Construct the mask image path based on the original image path
    mask_image_path = Path(original_image_folder) / "predict" / original_image_name

    original_image = mpimg.imread(original_image_path)
    mask_image = mpimg.imread(mask_image_path)

    # Ensure the mask is binary and of type np.uint8
    mask = (mask_image > 0).astype(np.uint8) * 255

    # Convert 'original_image' to RGBA
    original_image_rgba = cv2.cvtColor(original_image, cv2.COLOR_RGB2BGRA)

    # Find contours from the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    original_image_rgb = cv2.cvtColor(original_image_rgba, cv2.COLOR_BGRA2RGB)

    # Draw contours on the RGB image
    cv2.drawContours(original_image_rgb, contours, -1, (0, 255, 0), 2)  # Green contours with thickness of 3

    return original_image_rgb
# Display the image with contours
# frame_img = draw_contours("data_set/0200A1795784_frames","frame_0000.png")
# plt.imshow(frame_img)
# plt.show()