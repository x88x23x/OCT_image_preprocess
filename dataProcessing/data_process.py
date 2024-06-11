import cv2
import os

# 指定文件夹路径
folder_path = 'D:\OCT\Data_OCT\Term1'  # 将此路径替换为存放待处理图像的文件夹路径
gaus_path = 'D:\OCT\Data_OCT\Gaus1'  # 将此路径替换为存放高斯滤波后图像的文件夹路径
median_path = 'D:\OCT\Data_OCT\Median1'  # 将此路径替换为存放中值滤波后图像的文件夹路径

# 获取文件夹中的所有文件列表
file_list = os.listdir(folder_path)

# 遍历文件列表
for file in file_list:
    file_path = os.path.join(folder_path, file)

    # 仅处理图片文件
    if file_path.endswith('.png'):
        # 读取图片
        img = cv2.imread(file_path)

        # 对图片应用高斯滤波
        #blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
        # 对图片应用中值滤波
        blurred_img = cv2.medianBlur(img, 5)

        # 保存处理后的图片
        #output_path = os.path.join(gaus_path, file)
        output_path = os.path.join(median_path, file)
        cv2.imwrite(output_path, blurred_img)

# cv2.imshow("image",image)
# cv2.imshow("gauss",gauss)
# cv2.imshow("median",median)
# cv2.waitKey(0)