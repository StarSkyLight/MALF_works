from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# img=np.array(Image.open('test.jpg')) #打开图像并转化为数字矩阵

#随机生成5000个椒盐
# rows,cols,dims=img.shape
# for i in range(5000):
#     x=np.random.randint(0,rows)
#     y=np.random.randint(0,cols)
#     img[x,y,:]=255
#
# plt.figure("cat_salt")
# plt.imshow(img)
# plt.axis('off')
# plt.show()

# img = Image.open('Lena.png')
# rgb_img = img.convert('RGB')
# r, g, b = rgb_img.getpixel((1, 1))
# print(r)
# print(g)
# print(b)
#
#
# img_ch = np.array(img)
# # img_ch[1, 1, 0] = 0
# print(img_ch[1, 1, 0])
# print(img_ch[1, 1, 1])
# print(img_ch[1, 1, 2])
#
# rows, cols, dims = img_ch.shape

# print(rows)
# print(cols)
# print(dims)

# print(img.info)

# file = open("verySecretTextFile.txt", "r")
# temp = file.read(1)
# temp_int = ord(temp)
#
# temp_4 = temp_int // 4
# temp_16 = temp_int // 16
#
# r = temp_int - (temp_4 * 4)
# g = temp_4 - (temp_16 * 4)
# b = temp_16
# print(r)
# print(g)
# print(b)
# # chr()
# file.close()

# file = open("verySecretTextFile.txt", "rb")
# temp = file.read(1)
# Bytes = np.fromfile("verySecretTextFile.txt", dtype ="uint8")
# Bits = np.unpackbits(Bytes)
# Bytes.tofile("test.txt")

int1 = 124
bin1 = bin(int1)
str1 = str(bin1)
print(str1)
print(str1[3] == str(0))
