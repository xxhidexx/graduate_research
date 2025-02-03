import cv2
import os
import time

# カメラデバイスのインデックス
camera_indices = [0, 1] # 0: 右カメラ, 1: 左カメラ

# 画像を保存するディレクトリを作成
save_dir = "0127"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 7秒間待機
print("7秒後に撮影を開始します...")
time.sleep(1)

# 各カメラから画像をキャプチャ
for i, index in enumerate(camera_indices):
    # カメラを開く
    cap = cv2.VideoCapture(index)

    if not cap.isOpened():
        print(f"カメラ {index} を開けませんでした")
        continue

    # 画像をキャプチャする
    ret, frame = cap.read()

    if not ret:
        print(f"カメラ {index} から画像をキャプチャできませんでした")
    else:
        # 画像を保存する
        image_path = os.path.join(save_dir, f"camera_{i}.jpg")
        cv2.imwrite(image_path, frame)
        print(f"カメラ {index} から画像を保存しました: {image_path}")

    # カメラを閉じる
    cap.release()

