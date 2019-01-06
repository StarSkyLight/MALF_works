"""This file is for i of Question 1.

It is a method that hide the text in the image.
"""


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def hide():
    # input of the cover image
    temp1 = input("Please input the name of the cover image:")
    cover_image = str(temp1)

    # input of the text file
    temp2 = input("Please input the name of the text file which you want to hide:")
    text_file = str(temp2)

    img = np.array(Image.open(cover_image))

    file = open(text_file, "r")

    rows, columns, channels = img.shape

    counter = 0

    x = 1
    y = 0
    z = 0
    while True:
        # read a byte of the file
        temp = file.read(1)
        # If it is the end of the file, stop the loop
        if temp == '':
            break

        counter = counter + 1

        temp_int = ord(temp)

        temp_4 = temp_int // 4
        temp_16 = temp_int // 16

        # get the last 2 bits of the char
        r = temp_int - (temp_4 * 4)
        # get the middle 2 bits of the char
        g = temp_4 - (temp_16 * 4)
        # get the highest 3 bits of the char
        b = temp_16

        # add the last 2 bits of the char on the red channel
        img[x, y, z] = img[x, y, z] // 4 * 4 + r
        z = z + 1
        # add the middle 2 bits of the char on the green channel
        img[x, y, z] = img[x, y, z] // 4 * 4 + g
        z = z + 1
        # add the highest 3 bits of the char on the blue channel
        img[x, y, z] = img[x, y, z] // 8 * 8 + b
        z = 0

        # move to next pixel
        if (y + 1) < columns:
            y = y + 1
        else:
            if (x + 1) < rows:
                x = x + 1
                y = 0
            else:
                print('You need a larger image!')
                return

    # calculate the number of bits that are changed and stores in the image
    counter1 = counter
    x1 = 0
    y1 = 0
    z1 = 0
    while y1 < columns:
        for z1 in range(0, 3):
            img[x1, y1, z1] = img[x1, y1, z1] // 4 * 4 + (counter1 % 4)
            counter1 = counter1 // 4
        y1 = y1 + 1

    file.close()

    # show the image
    plt.figure("hide_information")
    plt.imshow(img)
    plt.axis('off')

    fig = plt.gcf()
    fig.set_size_inches(2.2 / 0.72, 2.2 / 0.72)

    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)

    # save the image
    plt.savefig("stego_image.png", transparent=True, dpi=72, pad_inches=0)
    plt.show()


hide()
