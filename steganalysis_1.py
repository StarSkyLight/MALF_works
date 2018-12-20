from PIL import Image
import numpy as np


def discover():
    temp1 = input("Please input the name of the stego image:")
    stego_image = str(temp1)

    img = np.array(Image.open(stego_image))

    temp = input("Please input the number of bits:")
    num = int(temp) * 2

    rows, columns, channels = img.shape

    list_bits = np.zeros((rows * columns * channels,), dtype=np.int)

    length = len(list_bits)

    x1 = 0
    y1 = 0
    z1 = 0
    index = 0
    while index < length:
        list_bits[index] = img[x1, y1, z1] - img[x1, y1, z1] // num * num
        z1 = z1 + 1
        index = index + 1
        if index < length:
            list_bits[index] = img[x1, y1, z1] - img[x1, y1, z1] // num * num
            z1 = z1 + 1
            index = index + 1
            if index < length:
                list_bits[index] = img[x1, y1, z1] - img[x1, y1, z1] // num * num
                z1 = 0
                index = index + 1
            else:
                break
        else:
            break

        if (y1 + 1) < columns:
            y1 = y1 + 1
        else:
            if (x1 + 1) < rows:
                x1 = x1 + 1
                y1 = 0
            else:
                break

    list_bytes = np.packbits(list_bits)
    list_bytes.tofile("testFile.txt")


discover()
