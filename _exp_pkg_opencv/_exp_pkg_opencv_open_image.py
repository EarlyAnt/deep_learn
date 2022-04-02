import cv2
import os

print(cv2.__version__)

dir_this = os.path.dirname(__file__)
file_name = '{}/image/120002.jpg'.format(dir_this)

img = cv2.imread(file_name, 0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)

key = cv2.waitKey(0)
if key == ord('s'):
    new_file_name = 'new_image.jpg'
    print('->save image to [{}] + + + + +'.format(new_file_name))
    cv2.imwrite(new_file_name, img)
else:
    print('->exit + + + + +')
    cv2.destroyAllWindows()


