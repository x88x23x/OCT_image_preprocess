import cv2

# 加载灰度图像
gray_image = cv2.imread('1_0001.png', cv2.IMREAD_GRAYSCALE)

# 对灰度图像进行直方图均衡化处理
equalized_image = cv2.equalizeHist(gray_image)

# 显示原始灰度图像和直方图均衡化后的图像
cv2.imshow('gray image', gray_image)
cv2.imshow('equalized image', equalized_image)
cv2.waitKey(0)
