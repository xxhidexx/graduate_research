import cv2

# マウスイベント時に処理を行う
def click_event(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN:
    print(f'Image coordinates: ({x}, {y})')
    with open('0819_another/coordinates_right_calib.txt', 'a') as f:
      f.write(f'Image coordinates: ({x}, {y})\n')
    cv2.destroyAllWindows()

# 画像を読み込む
img = cv2.imread('0819_another/camera_0.jpg', 1)

# ウィンドウを作成し、マウスイベントをバインドする
cv2.namedWindow('image')
cv2.setMouseCallback('image', click_event)

# 画像を表示する
cv2.imshow('image', img)

# ユーザーが何かキーを押すまで待つ
cv2.waitKey(0)

# すべてのウィンドウを閉じる
cv2.destroyAllWindows()