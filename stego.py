from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def hide():
    img = np.array(Image.open('Lena.png'))

    file = open("verySecretTextFile.txt", "r")

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

        r = temp_int - (temp_4 * 4)
        g = temp_4 - (temp_16 * 4)
        b = temp_16

        img[x, y, z] = img[x, y, z] // 4 * 4 + r
        z = z + 1
        img[x, y, z] = img[x, y, z] // 4 * 4 + g
        z = z + 1
        img[x, y, z] = img[x, y, z] // 8 * 8 + b
        z = 0

        if (y + 1) < columns:
            y = y + 1
        else:
            if (x + 1) < rows:
                x = x + 1
                y = 0
            else:
                print('You need a larger image!')
                return

    counter1 = counter
    x1 = 0
    y1 = 0
    z1 = 0
    while y1 < columns:
        for z1 in range(0, 3):
            print(counter1 % 4)
            img[x1, y1, z1] = img[x1, y1, z1] // 4 * 4 + (counter1 % 4)
            counter1 = counter1 // 4
        y1 = y1 + 1

    file.close()

    # print(counter)
    # print(counter1)

    plt.figure("hide_information")
    plt.imshow(img)
    plt.axis('off')

    fig = plt.gcf()
    fig.set_size_inches(2.2 / 0.72, 2.2 / 0.72)

    # plt.gca().xaxis.set_major_locator(plt.NullLocator())
    # plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)

    plt.savefig("stego_image.png", transparent=True, dpi=72, pad_inches=0)
    plt.show()


hide()
