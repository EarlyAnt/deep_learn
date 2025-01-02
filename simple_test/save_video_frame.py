import cv2

# 初始化对象
# cap = cv2.VideoCapture('.\\demo.mp4')
cap = cv2.VideoCapture(0)

# 检查视频是否打开
if not cap.isOpened():
    print("视频文件打开失败")

# 读取视频
while cap.isOpened():
    # 逐帧读取
    ret, frame = cap.read()

    if ret:
        # 展示读取结果        
        image = cv2.flip(frame, 1)
        cv2.imshow('cv2', image)

        # 按 S 保存
        if cv2.waitKey(5) & 0xFF == ord('s'):
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cv2.imwrite("image.jpg", image)
            print(f"save capture frame")

        # 按 Q 退出
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
