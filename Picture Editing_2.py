#  Rotating and Adjusting Brightness
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('Image_2.webp')  # Load the image
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# Rotate the image by 45 degrees around its center
(h,w)= rgb_image.shape[:2]
center = (w//2, h//2)  # Center of the image
M = cv2.getRotationMatrix2D(center, 45, 1.0)    # rotate by 45 degrees    
rotated = cv2.warpAffine(image, M, (w, h))  # Rotate the image

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)  # Convert rotated image to RGB
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

# Increase brightness by adding 50 to all pixel values
# Use cv2.add to avoid negative values or overflow
brightness_matrix = np.ones(rgb_image.shape, dtype="uint8") * 50
brighter= cv2.add(image, brightness_matrix)  # Increase brightness

brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)  # Convert to RGB
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()