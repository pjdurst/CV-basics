
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#def print_checkerboard(size):
#    for row in range(size):
 #       for col in range(size):
  #          # Print '#' for black squares and ' ' for white squares
   #         if (row + col) % 2 == 0:
    #            print('1', end=' ')
     #       else:
      #          print('0', end=' ')
       # print()

# Specify the size of the checkerboard
#board_size = 12
#print_checkerboard(board_size)

# Define the size of the checkerboard
size = 16

# Create the checkerboard pattern
checkerboard = np.indices((size, size)).sum(axis=0) % 2

# Plot the checkerboard
#plt.imshow(checkerboard, cmap='gray', interpolation='nearest')
#plt.axis('off')  # Turn off the axis
#plt.show()

# Create a 3D array for the checkerboard (size x size x 3 for RGB channels)
checkerboard = np.zeros((size, size, 3))

# Fill the checkerboard with two colors (black and red)
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            checkerboard[i, j] = [255, 255, 2555]  
        else:
            checkerboard[i, j] = [0, 0, 0] 

# Plot the checkerboard
#plt.imshow(checkerboard, interpolation='nearest')
#plt.axis('off')  # Turn off the axis
#plt.show()



# Load the image
image_path = 'RIT.jpg'  # Replace with the path to your image
image = Image.open(image_path)


# Display the image
plt.imshow(image)
plt.axis('off')  # Hide the axis
plt.show()

# Convert the image to grayscale
grayscale_image = image.convert("L")

# Display the grayscale image
plt.imshow(grayscale_image, cmap='gray')
plt.axis('off')  # Hide the axis
plt.show()

# Convert the image to a NumPy array
pixel_array = np.array(image)

# Display the pixel array
print(pixel_array)