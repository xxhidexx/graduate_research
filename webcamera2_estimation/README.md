# Graduation-research

2台の単眼カメラとYOLOを用いて、3次元骨格座標を推定する

## プログラムの仕様

### take_image.py

接続された2台のカメラで同時に写真を撮影し、それぞれの画像を保存するプログラムです。

### caluculate_coordinates.py

撮影した画像を読み込み、画像内の任意の点をクリックすると、その点の2次元座標を取得し、テキストファイルに出力するプログラムです。

### rec_video.py

接続された2台のカメラで動画を撮影し、保存するプログラムです。

### get_skelton_video.py

2台のカメラで撮影した動画を読み込み、それぞれからYOLOを用いて骨格座標を取得し、骨格座標JSONファイルを出力するプログラムです。

### estimation_yolo_video.py

get_skelton_video.pyで出力した骨格座標JSONファイルを読み込み、それぞれのフレームでの骨格座標を結ぶ線を描画し、アニメーションを出力するプログラムです。

## 必要なパッケージのインストール法

```
pip install -r requirements.txt
```

## キャリブレーションの方法

2台の単眼カメラから撮影されたそれぞれの画像内の2点の実際の3次元座標と2次元座標を計測し，その値を用いてキャリブレーションを行い，必要なパラメータを求める。用いるプログラムはtake_image.pyとcaluculate_coordinates.pyの2つである。

## プログラムの使い方

### take_image.pyの使い方

* PCに接続された2台の単眼カメラで同時に写真を撮影し、それぞれの画像を保存します。

```
python take_image.py
```

### caluculate_coordinates.pyの使い方

* 画像を読み込み，画像内の3次元座標が既知の点をクリックすると，その点の2次元座標を取得し，テキストファイルに出力します。
* 画像をクリックするごとに2次元座標がテキストファイルに出力され、ESCキーを押すと終了します。
  ここで得られた2次元座標と3次元座標を用いて連立方程式を解き，必要なパラメータを求めます。

```
python caluculate_coordinates.py
```

### rec_video.pyの使い方

* プログラム実行前に、PCに2台の単眼カメラを接続し(必要に応じてUSB-Cハブ等を用いる)、2台のカメラの向きが平行になるように設置してください。

```
python rec_video.py
```

実行すると、2台のカメラで動画が撮影され、保存されます。

### get_skelton_video.pyの使い方

```
python get_skelton_video.py
```

rec_video.pyで出力された動画を読み込み、それぞれのフレームからYOLOを用いて骨格座標を取得し、骨格座標JSONファイルを出力します。

### estimation_yolo_video.pyの使い方

三角測量に用いるパラメーターがfx_correct, cu_correct, fy_correct, cv_correct, FTの４つあり、キャリブレーションで求めた値を設定してください。

```
python estimation_yolo_video.py
```

get_skelton_video.pyで出力した骨格座標JSONファイルを読み込み、三角測量を適用することで3次元骨格座標を推定し、それぞれのフレームでの3次元骨格座標を結ぶ線を描画し、アニメーションを出力します。

## 開発者

* 作成者：上野瑛博
* 所属：関西学院大学工学部情報工学課程
* E-mail：guv80359@kwansei.ac.jp
