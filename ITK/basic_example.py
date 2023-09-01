#!/usr/bin/env python3

import itk
import sys
import matplotlib.pyplot as plt

input_filename = sys.argv[1]
output_filename = sys.argv[2]

image = itk.imread(input_filename, itk.US) # itk.US: unsigned short, pixel type modification to fit with median filter from ITK

# Median filter
median = itk.median_image_filter(image, radius=2) # radius: size of the median filter

# Plotting
plt.figure()
plt.subplot(1,2,1)
plt.imshow(image, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(median, cmap='gray')
plt.show()

# Save image
itk.imwrite(median, output_filename)