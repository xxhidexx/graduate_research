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

* アニメーションを出力する場合
    * 1人の骨格座標を推定する場合
    ```
    python gen_skes.py -v baseball.mp4 -np 1 --animation
    ```

    * 2人の骨格座標を推定する場合
    ```
    python gen_skes.py -v baseball.mp4 -np 2 --animation
    ```


* 骨格座標をnpzファイルに保存する場合
```
    python gen_skes.py -v baseball.mp4 -np 1
```

### skelton_visual_camera.pyの使い方
```
python skelton_visual_camera.py
```
実行すると、カメラ座標系の3次元骨格座標(cm単位)を結ぶ線を描画し、アニメーションを表示し、骨格座標はnpzファイルで出力する


## 開発者

* 作成者：上野瑛博
* 所属：関西学院大学工学部情報工学課程
* E-mail：guv80359@kwansei.ac.jp
