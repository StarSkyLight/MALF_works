from PIL import Image
import numpy as np


def recover():
    temp1 = input("Please input the name of the stego image:")
    stego_image = str(temp1)

    img = np.array(Image.open(stego_image))

    rows, columns, channels = img.shape

    counter = 0

    begin = False

    x = rows - 1
    y = columns - 1
    z = 2
    while y >= 0:
        while z >= 0:
            temp_last_num = img[x, y, z] - (img[x, y, z] // 2 * 2)
            if temp_last_num > 0:
                begin = True
            if begin:
                counter = counter * 2 + int(temp_last_num)
                # print(counter)
            z = z - 1
        z = 2
        y = y - 1

    list_bits = np.zeros((counter,), dtype=np.int)

    x1 = 0
    y1 = 0
    z1 = 0
    index = 0
    while index < counter:
        list_bits[index] = img[x1, y1, z1] - img[x1, y1, z1] // 2 * 2
        z1 = z1 + 1
        index = index + 1
        if index < counter:
            list_bits[index] = img[x1, y1, z1] - img[x1, y1, z1] // 2 * 2
            z1 = z1 + 1
            index = index + 1
            if index < counter:
                list_bits[index] = img[x1, y1, z1] - img[x1, y1, z1] // 2 * 2
                z1 = 0
                index = index + 1

        if (y1 + 1) < columns:
            y1 = y1 + 1
        else:
            if (x1 + 1) < rows:
                x1 = x1 + 1
                y1 = 0
            else:
                print('Error!')
                return

    list_bytes = np.packbits(list_bits)
    list_bytes.tofile("recoverFile.txt")


recover()
