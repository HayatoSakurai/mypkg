# 概要
1秒間に1だけ増加させた値を2倍、4倍にして出力するプログラムです。

# 環境
ubuntu20.04  
ROS noetic

# 使用機器
Raspberry Pi 4

# インストール
```
$ roscore &
$ cd ~/catkin_ws/src  
$ git clone https://github.com/HayatoSakurai/mypkg.git  
$ ( cd ~/catkin_ws/ && catkin_make )  
$ source ~/.bashrc  
```
# 実行
1. パーミッションを設定する
```
$ cd ~/catkin_ws/src/mypkg/scripts
$ chmod +x count.py
$ chmod +x twice.py
$ chmod +x fourth.py
```
2. 端末を三つ用意する  
3. 一つ目の端末で以下を実行する  
```
$ rosrun mypkg count.py
```
4. 二つ目の端末で以下を実行する  
```
$ rosrun mypkg twice.py
```
5. 三つ目の端末で以下を実行する
```
$ rosrun mypkg fourth.py
```

# 実行結果
https://www.youtube.com/watch?v=zd7U8Zup3Io

# 製作者
https://github.com/ryuichiueda  
https://github.com/HayatoSakurai  
  
ノードは上田教授が作成したものをもとに作成しています

# 変更点
元のノードから変更した点は以下のようになります  
