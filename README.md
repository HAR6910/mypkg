# ボーリングランダムスコア表示
[![test](https://github.com/HAR6910/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/HAR6910/mypkg/actions)

## パッケージ概要
本パッケージは、ROS 2（Humble）を用いた Python 製通信パッケージです。  
基本的なpublish / subscribe 通信（talker / listener) と、  
ボウリングのスコア処理を行うノードを実装しています。

---

## ノードの説明

### talker
- 役割：文字列メッセージを一定周期で publish するノード
- ノード名：`talker`
- パブリッシュするトピック：`/chatter`
- メッセージ型：`std_msgs/String`

---

### listener
- 役割：`/chatter` トピックを subscribe し、受信内容を表示するノード
- ノード名：`listener`
- サブスクライブするトピック：`/chatter`
- 表示例:以下のように「４ラウンド目までの合計スコア:31」という表示になります。

```
[INFO] [1767100260.003995083] [bowling_listener]: Current Frame: 4 | Total Score: 31
```

---

## トピックの説明

### /chatter
- 型：`std_msgs/String`
- 内容：各ラウンドの各回におけるスコア

---

## 動作確認

```
$ ros2 launch mypkg bowling_launch.py
[INFO] [launch]: All log files can be found below /home/har6910/.ros/log/2026-01-05-16-05-35-356891-HAR-1152
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [listener-1]: process started with pid [1160]
[INFO] [talker-2]: process started with pid [1163]
[listener-1] [INFO] [1767596736.211855222] [bowling_listener]: Bowling listener started
[talker-2] [INFO] [1767596736.211940173] [bowling_talker]: Bowling talker started
[talker-2] [INFO] [1767596737.195359846] [bowling_talker]: Frame 1 Roll 1: 8
[listener-1] [INFO] [1767596737.196651398] [bowling_listener]: Current Frame: 1 | Total Score: 0
[talker-2] [INFO] [1767596738.195070837] [bowling_talker]: Frame 1 Roll 2: 0
[listener-1] [INFO] [1767596738.195663181] [bowling_listener]: Current Frame: 1 | Total Score: 8
[talker-2] [INFO] [1767596739.196072791] [bowling_talker]: Frame 2 Roll 1: 2
[listener-1] [INFO] [1767596739.197601118] [bowling_listener]: Current Frame: 2 | Total Score: 8
[talker-2] [INFO] [1767596740.196811215] [bowling_talker]: Frame 2 Roll 2: 3
```
表記が長いため、上記のように略させていただきます。

---

## 必要なソフトウェア
### 本パッケージの実行には、以下の動作環境が必要です。
- OS: Ubuntu 22.04.3 LTS
- ROS2 Humble Hawksbill
- Python 3.10

---

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
- ©2025 Sho Harukawa

---

## 参考文献
- [コードの変数や関数・ロジックを管理する② -関数の使用と管理について-](https://note.com/bunsekiya_tech/n/n1b713f661cd4)
- [わかりやすく解説！コールバック関数の理解とその使い方](https://qiita.com/nakajima417/items/4d0c2d46ff82351549e6)
