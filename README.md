# 概要
1秒間に1だけ増加させた値を2倍、4倍にして出力するプログラムです

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
もとのノードから変更した点は以下のようになります  
  
https://github.com/HayatoSakurai/mypkg/blob/main/scripts/twice.py  
上記リンクのtwice.pyにおいて変更点は以下になります  
10行目:rospy.loginfo(n)を追加  
16行目:10を1に変更  
  
https://github.com/HayatoSakurai/mypkg/blob/main/scripts/fourth.py  
fourth.pyは講義内のtwice.pyをもとに一部変更したノードとなっています  
上記リンクのfourth.pyにおいて変更点は以下になります  
10行目:rospy.loginfo(n)を追加  
13行目:twiceをfourthに変更  
14行目:count_upをtwiceに変更  
15行目:twiceをfourthに変更  
16行目:10を1に変更

#  ライセンス
BSD 3-Clause "New" or "Revised" License
