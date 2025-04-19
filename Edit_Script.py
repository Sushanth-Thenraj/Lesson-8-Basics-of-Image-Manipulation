import cv2
import matplotlib.pyplot as plt
import numpy as np

image= cv2.imread('Image.jpg')

#Convert image from BGR to RGB
image_rgb= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.show()

#Convert image from BGR to Grayscale
gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.show()

#Save Grayscale Image
cv2.imwrite('edited_images\Grayscale_Image.jpg', gray_image)

#Wait for key press
cv2.waitKey(0)

#Crop Grayscale Image
crop_image= gray_image[100:300, 200:400]
plt.imshow(crop_image, cmap='gray')
plt.title('Cropped Image')
plt.show()

#Save Cropped Image
cv2.imwrite('edited_images\Cropped_Image.jpg', crop_image)

#Wait for key press
cv2.waitKey(0)

#Rotate Cropped Image
(h,w)= crop_image.shape[:2]
center= (w//2, h//2)
M= cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image= cv2.warpAffine(crop_image, M, (w,h))
plt.imshow(rotated_image, cmap='gray')
plt.title('Rotated Image')
plt.show()

#Save Rotated Image
cv2.imwrite('edited_images\Rotated_Image.jpg', rotated_image)

#Wait for key press
cv2.waitKey(0)

#Increase brightness of the image
brightness_matrix= np.ones(rotated_image.shape, dtype="uint8") * 50
bright_image= cv2.add(rotated_image, brightness_matrix)
plt.imshow(bright_image, cmap='gray')
plt.title('Brightened Image')
plt.show()

#Save Brightened Image
cv2.imwrite('edited_images\Brightened_Image.jpg', bright_image)

#Wait for key press
cv2.waitKey(0)

#Close all windows
cv2.destroyAllWindows()
#End of script