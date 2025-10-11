> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/ja.md)

PatchModelAddDownscaleノードは、Kohya Deep Shrink機能を実装し、モデルの特定のブロックにダウンスケールとアップスケール操作を適用します。処理中の中間特徴量の解像度を一時的に低下させ、その後元のサイズに復元することで、品質を維持しながらパフォーマンスを向上させることができます。このノードは、モデルの実行中にこれらのスケーリング操作をいつ、どのように行うかを精密に制御することができます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | はい | - | ダウンスケールパッチを適用するモデル |
| `block_number` | INT | いいえ | 1-32 | ダウンスケールを適用する特定のブロック番号（デフォルト：3） |
| `downscale_factor` | FLOAT | いいえ | 0.1-9.0 | 特徴量をダウンスケールする係数（デフォルト：2.0） |
| `start_percent` | FLOAT | いいえ | 0.0-1.0 | ダウンスケールを開始するノイズ除去プロセス内の開始点（デフォルト：0.0） |
| `end_percent` | FLOAT | いいえ | 0.0-1.0 | ダウンスケールを終了するノイズ除去プロセス内の終了点（デフォルト：0.35） |
| `downscale_after_skip` | BOOLEAN | いいえ | - | スキップ接続の後にダウンスケールを適用するかどうか（デフォルト：True） |
| `downscale_method` | COMBO | いいえ | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | ダウンスケール操作に使用する補間方法 |
| `upscale_method` | COMBO | いいえ | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | アップスケール操作に使用する補間方法 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model` | MODEL | ダウンスケールパッチが適用された修正済みモデル |