import cv2

def showCapture():
    print('->open capture + + + + +')
    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('', gray)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
def saveCapture():
    print('->save video + + + + +')
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("->width: %s, height: %s" % (width, height))
    out = cv2.VideoWriter('output.mp4', fourcc, 30, (width, height))
    while (cap.isOpened()):        
        ret, frame = cap.read()
        if not ret:
            break
        
        out.write(frame)
        cv2.imshow('video', frame)
        if cv2.waitKey(1000//30) & 0xff == ord('q'):
            break
        
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    # showCapture()
    saveCapture()