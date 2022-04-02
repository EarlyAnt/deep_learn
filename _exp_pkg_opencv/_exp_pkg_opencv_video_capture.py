import cv2

def showCapture():
    print('->open capture + + + + +')
    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('', gray)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break;
        
    cap.release()
    cv2.destroyAllWindows();
    
def saveCapture():
    print('->save video + + + + +')
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 0)
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break;
        else:
            break;
        
    cap.release()
    out.release()
    cv2.destroyAllWindows();
    
if __name__ == '__main__':
    # showCapture()
    saveCapture()