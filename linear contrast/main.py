import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('test1.jpg', cv2.IMREAD_GRAYSCALE)


def linear_contrast_enhancement(image):
    L_min = np.min(image)
    L_max = np.max(image)
    print (f"min {L_min}, max {L_max}")
    
    # L'(i,j) = ((L(i,j) - L_min) / (L_max - L_min)) * 255
    enhanced_image = ((image - L_min) / (L_max - L_min)) * 255
    enhanced_image = np.uint8(enhanced_image)
    
    L_min = np.min(enhanced_image)
    L_max = np.max(enhanced_image)
    print (f"min {L_min}, max {L_max}")
    
    return enhanced_image


enhanced_image = linear_contrast_enhancement(image)


plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

# Enhanced Image
plt.subplot(1, 2, 2)
plt.title("Enhanced Image")
plt.imshow(enhanced_image, cmap='gray')
plt.axis('off')

plt.show()


cv2.imwrite('enhanced_image.jpg', enhanced_image)
