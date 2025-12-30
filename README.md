# ボーリングランダムスコア表示
[![test](https://github.com/HAR6910/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/HAR6910/mypkg/actions)

## パッケージ概要
本パッケージは、ROS 2（Humble）を用いた Python 製通信パッケージです。  
基本的なpublish / subscribe 通信（talker / listener) と、  
ボウリングのスコア処理を行うノードを実装しています。

---

## ノードの説明

### talker.py
- 役割：文字列メッセージを一定周期で publish するノード
- ノード名：`talker`
- パブリッシュするトピック：`/chatter`
- メッセージ型：`std_msgs/String`

---

### listener.py
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

## 実行方法

### 1.同時に起動させる場合

```
＄ros2 launch mypkg bowling_launch.py
```

### 2.別々に起動させる場合
- 端末１でtalkerの起動
```
$ ros2 run mypkg talker
```

上記のようにtalkerを起動するとその回で倒したピンの数が配信されます。

- 端末２でlistenerの起動
```
$ ros2 run mypkg listener
```

上記のようにlistenerを起動するとtalkerに応じて合計スコアが常に更新され、配信します。

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
