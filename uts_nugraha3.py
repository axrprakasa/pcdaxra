import cv2

image = cv2.imread('D:\Media\Image\Wallpaper\subaru_impreza.jpg')
cv2.normalize(image, image, alpha=15, beta=175, norm_type=cv2.NORM_MINMAX)
cv2.imwrite('subaru_imprezaaa.jpg', image)
