> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/ja.md)

PatchModelAddDownscale ノードは、モデル内の特定のブロックにダウンスケールおよびアップスケール処理を適用することで、Kohya Deep Shrink 機能を実装します。処理中の中間特徴量の解像度を低下させ、その後元のサイズに復元することで、品質を維持しながらパフォーマンスを向上させることができます。このノードは、モデルの実行中にこれらのスケーリング処理をいつ、どのように行うかを正確に制御できます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | はい | - | ダウンスケールパッチを適用するモデル |
| `block_number` | INT | いいえ | 1-32 | ダウンスケールを適用する特定のブロック番号（デフォルト: 3） |
| `downscale_factor` | FLOAT | いいえ | 0.1-9.0 | 特徴量をダウンスケールする倍率（デフォルト: 2.0） |
| `start_percent` | FLOAT | いいえ | 0.0-1.0 | ノイズ除去処理においてダウンスケールを開始する位置（デフォルト: 0.0） |
| `end_percent` | FLOAT | いいえ | 0.0-1.0 | ノイズ除去処理においてダウンスケールを終了する位置（デフォルト: 0.35） |
| `downscale_after_skip` | BOOLEAN | いいえ | - | スキップ接続後にダウンスケールを適用するかどうか（デフォルト: True） |
| `downscale_method` | COMBO | いいえ | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | ダウンスケール処理に使用する補間方法 |
| `upscale_method` | COMBO | いいえ | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | アップスケール処理に使用する補間方法 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model` | MODEL | ダウンスケールパッチが適用された変更後のモデル |

---
**Source fingerprint (SHA-256):** `93ece77ad2dce3c1cdd554583ae1f2e6be51a43ab072d408869dddbcc7798c40`
