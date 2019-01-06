"""This file is for i of Question 1.

It is a method that recovers the text file from the stego-image.
"""


from PIL import Image
import numpy as np


def recover():
    # input the name of the stego image.
    temp1 = input("Please input the name of the stego image:")
    stego_image = str(temp1)

    # open image file
    img = np.array(Image.open(stego_image))

    file = open("recoverFile.txt", "w")

    rows, columns, channels = img.shape

    counter = 0

    begin = False

    # check every bit of the last line of the picture and get the number of bits that are changed
    x = 0
    y = columns - 1
    z = 2
    while y >= 0:
        while z >= 0:
            temp_last_num = img[x, y, z] - (img[x, y, z] // 4 * 4)
            if temp_last_num > 0:
                begin = True
            if begin:
                counter = counter * 4 + int(temp_last_num)
            z = z - 1
        z = 2
        y = y - 1

    # check every bits that are changed form the first bit of the image and get the information stored in them
    x1 = 1
    y1 = 0
    z1 = 0
    i = counter
    while i > 0:
        r = img[x1, y1, z1] - img[x1, y1, z1] // 4 * 4
        z1 = z1 + 1
        g = img[x1, y1, z1] - img[x1, y1, z1] // 4 * 4
        z1 = z1 + 1
        b = img[x1, y1, z1] - img[x1, y1, z1] // 8 * 8
        z1 = 0

        temp_int = r + (g * 4) + (b * 16)

        # transform int to char
        temp_str = chr(temp_int)

        file.write(temp_str)

        # if the bits of image less than the number that records in the image, print error information
        if (y1 + 1) < columns:
            y1 = y1 + 1
        else:
            if (x1 + 1) < rows:
                x1 = x1 + 1
                y1 = 0
            else:
                print('Error!')
                return
        i = i - 1


recover()
