from PIL import Image
import numpy as np


def discover():
    # temp1 = input("Please input the name of the stego image:")
    # stego_image = str(temp1)
    stego_image = "stego_image.png"
    ste_img = np.array(Image.open(stego_image))

    # temp2 = input("Please input the name of the cover image:")
    # cover_image = str(temp2)
    cover_image = "Lena.png"
    cov_img = np.array(Image.open(cover_image))

    rows, columns, channels = ste_img.shape
    rows2, columns2, channels2 = cov_img.shape

    collect_bits = np.zeros((rows * columns * channels * 8,), dtype=np.int)

    length = rows * columns * channels

    x1 = 0
    y1 = 0
    z1 = 0
    index = 0
    i = 0
    while i < 3:
        for z1 in range(0, 3):
            binary_ste = bin(ste_img[x1, y1, z1])
            print(binary_ste)
            if (x1 > rows2) or (y1 > columns2):
                for k in range(3, len(binary_ste)):
                    collect_bits[index] = int(binary_ste[k])
                    index = index + 1
            else:
                binary_cov = bin(cov_img[x1, y1, z1])
                print(binary_cov)

                for j in range(3, len(binary_ste)):
                    if binary_ste[j] != binary_cov[j]:
                        collect_bits[index] = int(binary_ste[j])
                        index = index + 1

        if (y1 + 1) < columns:
            y1 = y1 + 1
        else:
            if (x1 + 1) < rows:
                x1 = x1 + 1
                y1 = 0
            else:
                break

        i = i + 1
    print(collect_bits[0:8])
    list_bytes = np.packbits(collect_bits)
    list_bytes.tofile("test2File.txt")


discover()
