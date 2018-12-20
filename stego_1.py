from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def hide():
    img = np.array(Image.open('Lena.png'))

    Bytes = np.fromfile("verySecretTextFile.txt", dtype="uint8")
    Bits = np.unpackbits(Bytes)

    rows, columns, channels = img.shape

    length = len(Bits)

    counter = length
    index = 0
    x = 0
    y = 0
    z = 0
    while index < counter:

        img[x, y, z] = img[x, y, z] // 2 * 2 + Bits[index]
        z = z + 1
        index = index + 1
        if index < counter:
            img[x, y, z] = img[x, y, z] // 2 * 2 + Bits[index]
            z = z + 1
            index = index + 1
            if index < counter:
                img[x, y, z] = img[x, y, z] // 2 * 2 + Bits[index]
                z = 0
                index = index + 1

        if (y + 1) < columns:
            y = y + 1
        else:
            if (x + 1) < rows:
                x = x + 1
                y = 0
            else:
                print('You need a larger image!')
                return

    counter1 = length
    x1 = rows - 1
    y1 = 0
    z1 = 0
    while y1 < columns:
        for z1 in range(0, 3):
            img[x1, y1, z1] = img[x1, y1, z1] // 2 * 2 + (counter1 % 2)
            counter1 = counter1 // 2
        y1 = y1 + 1

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
