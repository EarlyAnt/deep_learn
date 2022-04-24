import os
import time
import cv2
import numpy as np
import mediapipe as mp
import PySimpleGUI as sg

from csv_file_util import ScvFileUtil
from socket_util import SocketClient

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def select_folder():
    sg.theme('Light Blue 2')
    
    layout = [[sg.Text('功能说明：识别所选目录中照片的姿势', text_color="blue")],
              [sg.Button('OK'), sg.Button('Exit')],
              [sg.Text('选择目录', auto_size_text=True), sg.Input(size=(40, 1)), sg.FolderBrowse(key='-Folder-', initial_folder=os.path.dirname(__file__))]
             ]
    window = sg.Window('姿势识别(指定目录)', layout, resizable=True)

    while True:
        event, values = window.read()
        print(f'Event: {event}')
        
        selected_folder = values[0]
        
        if event == 'OK':
            if (selected_folder == ""):
                sg.popup("请选择目录")
            elif (not os.path.exists(selected_folder)):
                sg.popup("目录不存在，请重新选择")
            else:
                
                file_list = sorted(os.listdir(selected_folder))
                image_files = []
                for file in file_list:
                    file_name = "{}/{}".format(selected_folder, file)
                    if file.startswith(".") or not os.path.isfile(file_name):
                        continue
                    
                    image_files.append(file_name)
                
                static_image(image_files, selected_folder)
        elif event in (None, 'Exit'):
            break
        print(str(values))
        
    window.close()
    print(f'You clicked {event}')    
    
def static_image(image_files, output_folder):
    # For static images:
    output_folder = output_folder + "/format"
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    BG_COLOR = (192, 192, 192) # gray
    pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)
    for idx, file in enumerate(image_files):
        file_name = os.path.basename(file)
        image = cv2.imread(file)
        image_height, image_width, _ = image.shape
        # Convert the BGR image to RGB before processing.
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if not results.pose_landmarks:
            continue
        
        print(
            f'Nose coordinates: ('
            f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
            f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
        )

        annotated_image = image.copy()
        # Draw segmentation on the image.
        # To improve segmentation around boundaries, consider applying a joint
        # bilateral filter to "results.segmentation_mask" with "image".
        if not results.segmentation_mask:
            continue
        
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        bg_image = np.zeros(image.shape, dtype=np.uint8)
        bg_image[:] = BG_COLOR
        annotated_image = np.where(condition, annotated_image, bg_image)
        # Draw pose landmarks on the image.
        mp_drawing.draw_landmarks(
            annotated_image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        cv2.imwrite("{}/{}".format(output_folder, file_name), annotated_image)
        # Plot pose world landmarks.
        mp_drawing.plot_landmarks(
            results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

def capture_video():
    # For webcam input:
    valid_bones = ('NOSE', 'LEFT_SHOULDER', 'RIGHT_SHOULDER', 'LEFT_ELBOW', 'RIGHT_ELBOW', 'LEFT_WRIST', 'RIGHT_WRIST', 'LEFT_HIP', 'RIGHT_HIP')
    
    file = ScvFileUtil()
    client = SocketClient()
    client.connect(server_ip_port=("192.168.0.105", 2000), keep_listen=False)
    # file.open_write("{}/data.txt".format(os.path.dirname(__file__)))
    # header = ""
    # data = ""
    combined_data = ""
    start_time = time.time()
    
    cap = cv2.VideoCapture(0)
    with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            success, image = cap.read()
            
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            width, height, _ = image.shape
            results = pose.process(image)
            
            end_time = time.time()
            diff = end_time - start_time
            if diff >= 0.05:
                print("->start_time: %s, end_time: %s, time diff: %s" % (start_time, end_time, diff))
                start_time = end_time
                
                # header = ""
                # data = ""
                combined_data = ""
                for i in range(33):
                    # # 打印模拟坐标
                    # print(f'->inner data: {mp_pose.PoseLandmark(i).name}:\n{results.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value]}')
                    # # 打印真实坐标(相对真实)
                    # print(f'->real-3D origin data: {mp_pose.PoseLandmark(i).name}:\n{results.pose_world_landmarks.landmark[mp_pose.PoseLandmark(i).value]}')
                    
                    bone_name = mp_pose.PoseLandmark(i).name
                    
                    # 计算分量坐标
                    if not results.pose_world_landmarks or not results.pose_world_landmarks.landmark or not valid_bones.__contains__(bone_name):
                        continue
                    
                    x = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark(i).value].x * width
                    y = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark(i).value].y * height
                    z = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark(i).value].z * width
                    v = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark(i).value].visibility
                    
                    # # 打印分量坐标
                    # print(f'->real-3D formatted data: {bone_name}:')
                    # print(f'x: {x}')
                    # print(f'y: {y}')
                    # print(f'z: {z}')
                    # print(f'visibility: {v}\n')
                    
                    # 拼接列标题和数据
                    # header += "{}#".format(bone_name)
                    # data += "{},{},{}#".format(x,y,z)
                    combined_data += "{},{},{},{}#".format(bone_name,x,y,z)
                
                # 去掉行尾的#号
                # header = header[:len(header)-1]
                # data = data[:len(data)-1]
                combined_data = combined_data[:len(combined_data)-1]
                    
                # # 写文件
                # file.write_header(header)
                # file.write_data(data)
                
                # 通过socket发送数据
                client.send(combined_data)
                print("->send data: {}".format(combined_data))

            # Draw the pose annotation on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                # results.pose_world_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
            
            # Flip the image horizontally for a selfie-view display.
            cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
            key = cv2.waitKey(5)
            if key == ord('q'):
                break
        cap.release()
        client.close

if __name__ == "__main__":
    # select_folder()
    capture_video()