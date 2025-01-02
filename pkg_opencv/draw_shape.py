import cv2 as cv
import numpy as np

def _draw_line():
    img = np.zeros((512, 512, 3), np.uint8)
    cv.line(img, (0, 0), (512, 512), (128, 252, 192), thickness = 5)
    cv.imshow('line', img)
    
    key = cv.waitKey(0)
    if key == ord('q'):
        print('->exit + + + + +')
        cv.destroyAllWindows();

if __name__=='__main__':
    _draw_line()