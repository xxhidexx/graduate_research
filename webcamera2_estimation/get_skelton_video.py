from ultralytics import YOLO
import cv2
import numpy as np
import json

model = YOLO("yolov8x-pose.pt")

# 動画ファイルのパスを指定
video_right_path = "1021/output1.mp4"
video_left_path = "1021/output0.mp4"

# 動画ファイルを読み込む
cap_right = cv2.VideoCapture(video_right_path)
cap_left = cv2.VideoCapture(video_left_path)

frame_index = 0
all_data = []

while cap_right.isOpened() and cap_left.isOpened():
    ret_right, frame_right = cap_right.read()
    ret_left, frame_left = cap_left.read()

    if not ret_right or not ret_left:
        break

    # キーポイントを抽出
    results_right = model(frame_right)
    results_left = model(frame_left)

    # 結果からキーポイントを抽出する
    keypoints_right = results_right[0].keypoints
    keypoints_data_right = keypoints_right.data[0]  # Get keypoints for the first person detected

    keypoints_left = results_left[0].keypoints
    keypoints_data_left = keypoints_left.data[0]  # Get keypoints for the first person detected

    # キーポイントの(x, y, confidence)を別の変数に保存
    keypoints_xyc_right = [(kp[0].item(), kp[1].item(), kp[2].item()) for kp in keypoints_data_right]
    keypoints_xyc_left = [(kp[0].item(), kp[1].item(), kp[2].item()) for kp in keypoints_data_left]

    u1_right, v1_right, c_right = [], [], []
    u2_left, v2_left, c_left = [], [], []
    for j in range(len(keypoints_xyc_right)):
        u1_right.append(keypoints_xyc_right[j][0])
        v1_right.append(keypoints_xyc_right[j][1])
        c_right.append(keypoints_xyc_right[j][2])
        u2_left.append(keypoints_xyc_left[j][0])
        v2_left.append(keypoints_xyc_left[j][1])
        c_left.append(keypoints_xyc_left[j][2])

    # 骨格点をプロット
    for x, y, c in keypoints_xyc_right:
        cv2.circle(frame_right, (int(x), int(y)), 5, (0, 255, 255), -1)  # Yellow keypoints

    for x, y, c in keypoints_xyc_left:
        cv2.circle(frame_left, (int(x), int(y)), 5, (0, 255, 255), -1)  # Yellow keypoints

    # フレームを一時的に保存するためのパスを指定
    frame_right_path = f"1021/frame_right_{frame_index}.jpg"
    frame_left_path = f"1021/frame_left_{frame_index}.jpg"

    # フレームを一時的に保存
    cv2.imwrite(frame_right_path, frame_right)
    cv2.imwrite(frame_left_path, frame_left)

    # 変数を辞書にまとめる
    data = {
        "frame_index": frame_index,
        "u1_right": u1_right,
        "v1_right": v1_right,
        "c_right": c_right,
        "u2_left": u2_left,
        "v2_left": v2_left,
        "c_left": c_left
    }

    all_data.append(data)

    frame_index += 1

# JSONファイルとして保存
output_file = "1021/keypoints_output_video.json"
with open(output_file, 'w') as f:
    json.dump(all_data, f, indent=4)

print(f"Keypoints saved to {output_file}")

# 動画ファイルを解放
cap_right.release()
cap_left.release()
cv2.destroyAllWindows()