import numpy as np
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# カメラの校正パラメータ
fx_correct = 1388.6240
cu_correct = 948.026
fy_correct = 1388.6240
cv_correct = 524.3762
FT = 782730

connections = [
    # (0, 1), (0, 2), (1, 3), (2, 4),  # 頭
    (5, 6), (5, 7), (7, 9), (6, 8), (8, 10),  # 腕
    (5, 11), (6, 12), (11, 12),  # 胴体
    (11, 13), (13, 15), (12, 14), (14, 16)   # 脚
]

# JSONファイルを読み込む
input_file = "1021/keypoints_output_video.json"
with open(input_file, 'r') as f:
    all_data = json.load(f)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def plot_skeleton_3d(ax, frame_data):
    u1_right = np.array(frame_data["u1_right"])
    v1_right = np.array(frame_data["v1_right"])
    u2_left = np.array(frame_data["u2_left"])
    v2_left = np.array(frame_data["v2_left"])
    c_right = np.array(frame_data["c_right"])
    c_left = np.array(frame_data["c_left"])

    valid_indices = (u1_right != 0) & (v1_right != 0) & (u2_left != 0) & (v2_left != 0) & (c_right >= 0.8) & (c_left != 0.8)

    # すべてのインデックス上の要素に対応するデータを準備
    X_calib_ver2, Y_calib_ver2, Z_calib = np.zeros_like(u1_right), np.zeros_like(v1_right), np.zeros_like(u1_right)

    # 有効なインデックスに対応するデータを計算
    d = np.abs(u1_right[valid_indices] - u2_left[valid_indices])
    Z_calib_valid = FT / np.where(d != 0, d, np.inf)
    X_calib_ver2_valid = (u2_left[valid_indices] - cu_correct) * Z_calib_valid / fx_correct
    Y_calib_ver2_valid = (v2_left[valid_indices] - cv_correct) * Z_calib_valid / fy_correct

    # 全データに戻った結果を代入
    X_calib_ver2[valid_indices] = X_calib_ver2_valid
    Y_calib_ver2[valid_indices] = Y_calib_ver2_valid
    Z_calib[valid_indices] = Z_calib_valid

    # プロットをクリア
    ax.cla()

    # 有効なインデックスを再計算（X_calib_ver2、Y_calib_ver2、Z_calibが0でないもの）
    valid_indices = (X_calib_ver2 != 0) & (Y_calib_ver2 != 0) & (Z_calib != 0) & (c_right >= 0.8) & (c_left != 0.8)

    # 骨格点をプロット
    ax.scatter(X_calib_ver2[valid_indices] / 10, -(Y_calib_ver2[valid_indices] / 10), Z_calib[valid_indices] / 10, c='b', marker='o')

    for idx in range(len(X_calib_ver2)):
        if valid_indices[idx]:
            ax.text(X_calib_ver2[idx] / 10, -(Y_calib_ver2[idx] / 10), Z_calib[idx] / 10, str(idx))

    # スケルトンの接続線を描画（存在するデータのみ）
    for connection in connections:
        start, end = connection
        # データが有効な条件下で、スケルトン描画（valid_indices[start]を適用）
        if start < len(valid_indices) and end < len(valid_indices):
            if valid_indices[start] and valid_indices[end]:
                ax.plot([X_calib_ver2[start] / 10, X_calib_ver2[end] / 10],
                        [-(Y_calib_ver2[start] / 10), -(Y_calib_ver2[end] / 10)],
                        [Z_calib[start] / 10, Z_calib[end] / 10], 'gray')

    # ラベルとタイトルを設定
    ax.set_xlabel('X (cm)')
    ax.set_ylabel('Y (cm)')
    ax.set_zlabel('Z (cm)')
    ax.set_title('3D Skeleton Points')
    ax.set_zlim(200, 300)
    ax.set_zticks(np.arange(200, 300, 20))
    ax.set_xlim(-20, 140)
    ax.set_xticks(np.arange(-20, 140, 20))
    ax.set_ylim(-60, 100)
    ax.set_yticks(np.arange(-60, 100, 20))

def update(frame_number):
    frame_data = all_data[frame_number]
    plot_skeleton_3d(ax, frame_data)

# アニメーションを作成
ani = FuncAnimation(fig, update, frames=len(all_data), interval=150)
plt.show()