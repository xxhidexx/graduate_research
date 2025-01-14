# Graduation-research

##　概要
単眼カメラで撮影された動画を入力とし、3次元姿勢推定モデルGASTを用いて、3次元骨格座標を推定する。

## プログラムの仕様

### gen_skes.py
単眼カメラで撮影された動画を入力とし、3次元骨格座標を推定するプログラムです。
実行時オプション引数を指定することで、アニメーションを出力したり、骨格座標をnpzファイルに保存することができます。

### skelton_visual_camera.py
gen_skes.pyで出力されたnpzファイルを読み込み、カメラ座標系に変換し、cm単位に変換し、それぞれのフレームでの骨格座標を結ぶ線を描画し、アニメーションを出力するプログラムです。


## プログラムの使い方

### gen_skes.pyの使い方
```python calculate_coordinates.py
```
キャリブレーションを行う際に使用し、画像内の任意の点をクリックすると、その画像内の座標を取得することができます。

### rec_video.pyの使い方
```
python rec_video.py
```
実行すると、2台のカメラで動画が撮影され、保存されます。


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
