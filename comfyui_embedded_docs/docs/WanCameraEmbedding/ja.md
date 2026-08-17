# WanCameraEmbedding

WanCameraEmbedding ノードは、カメラのモーションパラメータに基づいて Plücker 埋め込みを使用し、カメラ軌道埋め込みを生成します。このノードは、さまざまなカメラの動きをシミュレートする一連のカメラポーズを作成し、動画生成パイプラインに適した埋め込みテンソルに変換します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `camera_pose` | シミュレートするカメラの動きのタイプ（デフォルト: "Static"） | COMBO | はい | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `width` | 出力の幅（ピクセル単位）（デフォルト: 832、ステップ: 16） | INT | はい | 16 から MAX_RESOLUTION |
| `height` | 出力の高さ（ピクセル単位）（デフォルト: 480、ステップ: 16） | INT | はい | 16 から MAX_RESOLUTION |
| `length` | カメラ軌道シーケンスの長さ（デフォルト: 81、ステップ: 4） | INT | はい | 1 から MAX_RESOLUTION |
| `speed` | カメラの動きの速度（デフォルト: 1.0、ステップ: 0.1） | FLOAT | いいえ | 0.0 から 10.0 |
| `fx` | 焦点距離 x パラメータ（デフォルト: 0.5、ステップ: 0.000000001） | FLOAT | いいえ | 0.0 から 1.0 |
| `fy` | 焦点距離 y パラメータ（デフォルト: 0.5、ステップ: 0.000000001） | FLOAT | いいえ | 0.0 から 1.0 |
| `cx` | 主点の x 座標（デフォルト: 0.5、ステップ: 0.01） | FLOAT | いいえ | 0.0 から 1.0 |
| `cy` | 主点の y 座標（デフォルト: 0.5、ステップ: 0.01） | FLOAT | いいえ | 0.0 から 1.0 |

注: `fx`、`fy`、`cx`、`cy` は上級者向けパラメータです。`length` パラメータはステップを 4 として使用します。これは、最初のカメラフレームが内部的に繰り返されるためで、実際に処理されるシーケンス長は `length + 3` となります。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `camera_embedding` | 軌道シーケンスを含む生成されたカメラ埋め込みテンソル | TENSOR |
| `width` | 処理に使用された幅の値 | INT |
| `height` | 処理に使用された高さの値 | INT |
| `length` | 処理に使用された長さの値 | INT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/ja.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`
