import cv2
import matplotlib.pyplot as plt

# Load grayscale image
image = cv2.imread('test1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)

# Display original vs equalized image
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Histogram Equalized")
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.show()

# Optionally save result
cv2.imwrite('equalized_image.jpg', equalized_image)
