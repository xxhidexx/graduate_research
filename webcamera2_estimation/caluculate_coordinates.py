import cv2

# マウスイベント時に処理を行う
def click_event(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN:
    print(f'Image coordinates: ({x}, {y})')
    with open('1207/coordinates_right_calib__.txt', 'a') as f:
      f.write(f'Image coordinates: ({x}, {y})\n')
    

# 画像を読み込む
img = cv2.imread('1207/camera_0.jpg', 1)

# ウィンドウを作成し、マウスイベントをバインドする
cv2.namedWindow('image')
cv2.setMouseCallback('image', click_event)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESCキー押下で終了
        break
cv2.destroyAllWindows()