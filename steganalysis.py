"""This file is for ii of Question 1.

It is a implement of the two measures of steganalysis.
"""


from PIL import Image
import numpy as np


def discover():
    # input the name of the image
    temp1 = input("Please input the name of the image you want to test:")
    stego_image = str(temp1)
    ste_img = np.array(Image.open(stego_image))

    # input the name of reference image
    temp2 = input("Please input the name of the reference image:")
    cover_image = str(temp2)
    cov_img = np.array(Image.open(cover_image))

    rows, columns, channels = ste_img.shape
    rows2, columns2, channels2 = cov_img.shape

    collect_bits = 0
    degree = 0

    length = rows * columns * channels

    # compare the two images bit to bit and record the different bits
    x1 = 0
    y1 = 0
    z1 = 0
    index = 0
    i = 0
    while i < length:
        for z1 in range(0, channels):
            binary_ste = bin(ste_img[x1, y1, z1])
            # if the tested image is longer than reference image, record all the bits
            if (x1 > rows2) or (y1 > columns2):
                for k in range(3, len(binary_ste)):
                    collect_bits = collect_bits + 1
                    index = index + 1
                degree = degree + 255
            else:
                binary_cov = bin(cov_img[x1, y1, z1])

                for j in range(3, len(binary_ste)):
                    if binary_ste[j] != binary_cov[j]:
                        # calculate the number of different bits
                        collect_bits = collect_bits + 1
                        # calculate the degree
                        degree = degree + 2 ^ (j - 2) - 1
                        index = index + 1

        # move to next pixel
        if (y1 + 1) < columns:
            y1 = y1 + 1
        else:
            if (x1 + 1) < rows:
                x1 = x1 + 1
                y1 = 0
            else:
                break

        i = i + 1

    # print the result
    print("percentage of change : %.2f %%" % (collect_bits / length * 100))
    print("degree : %.5f %%" % (degree / (length * 255) * 100))


discover()
