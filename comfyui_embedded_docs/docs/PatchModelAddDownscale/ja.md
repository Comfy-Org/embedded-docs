# パッチモデル追加ダウンスケール（Kohya Deep Shrink）

The PatchModelAddDownscale ノードは、モデルの特定のブロックにダウンスケーリング操作とアップスケーリング操作を適用することで、Kohya Deep Shrink 機能を実装します。処理中の中間特徴量の解像度を低下させ、その後元のサイズに復元することで、品質を維持しながらパフォーマンスを向上させることができます。このノードは、モデルの実行中にこれらのスケーリング操作をいつ、どのように行うかを正確に制御することができます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | ダウンスケールパッチを適用するモデル | MODEL | はい | - |
| `block_number` | ダウンスケーリングが適用される特定のブロック番号（デフォルト: 3） | INT | いいえ | 1-32 |
| `downscale_factor` | 特徴量をダウンスケールする係数（デフォルト: 2.0） | FLOAT | いいえ | 0.1-9.0 |
| `start_percent` | ダウンスケーリングが開始されるデノイジングプロセスの開始点（デフォルト: 0.0） | FLOAT | いいえ | 0.0-1.0 |
| `end_percent` | ダウンスケーリングが停止されるデノイジングプロセスの終了点（デフォルト: 0.35） | FLOAT | いいえ | 0.0-1.0 |
| `downscale_after_skip` | スキップ接続の後にダウンスケーリングを適用するかどうか（デフォルト: True） | BOOLEAN | いいえ | - |
| `downscale_method` | ダウンスケーリング操作に使用される補間方法 | COMBO | いいえ | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `upscale_method` | アップスケーリング操作に使用される補間方法 | COMBO | いいえ | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | ダウンスケールパッチが適用された変更後のモデル | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/ja.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
