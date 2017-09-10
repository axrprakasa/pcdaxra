import cv2

image = cv2.imread('D:\Media\Image\Wallpaper\subaru_impreza.jpg')
abu = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('subaru_gray.jpg', abu)
