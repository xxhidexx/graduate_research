# Graduation-research

## プログラムの仕様

### rec_video.py
接続された2台のカメラで動画を撮影し、保存するプログラムです。

### get_skelton_video.py
2台のカメラで撮影した動画を読み込み、それぞれからYOLOを用いて骨格座標を取得し、骨格座標JSONファイルを出力するプログラムです。

### estimation_yolo_video.py
get_skelton_video.pyで出力した骨格座標JSONファイルを読み込み、それぞれのフレームでの骨格座標を結ぶ線を描画し、アニメーションを出力するプログラムです。

### rec_video.pyの使い方
```
python rec_video.py
```
実行すると、2台のカメラで動画が撮影され、保存されます。

## プログラムの使い方

### get_skelton_video.pyの使い方
```
python get_skelton_video.py
```

### estimation_yolo_video.pyの使い方
```
python estimation_yolo_video.py
```

## 開発者

* 作成者：上野瑛博
* 所属：関西学院大学工学部情報工学課程
* E-mail：guv80359@kwansei.ac.jp
