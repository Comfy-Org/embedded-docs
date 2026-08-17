# WanTrackToVideo

WanTrackToVideo ノードは、モーショントラッキングデータ（ポイントトラジェクトリ）を使用して動画生成をガイドします。トラックを処理し、必要に応じて開始画像と組み合わせ、条件付けされたポジティブおよびネガティブ出力と、Wan ビデオモデル用の潜在テンソルを生成します。有効なトラックが提供されない場合、標準の画像から動画への変換にフォールバックします。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | 動画生成のためのポジティブ条件付け | CONDITIONING | 必須 | - |
| `negative` | 動画生成のためのネガティブ条件付け | CONDITIONING | 必須 | - |
| `vae` | 動画フレームのエンコードに使用される VAE モデル | VAE | 必須 | - |
| `tracks` | マルチライン文字列としての JSON 形式のトラッキングデータ（デフォルト: "[]"） | STRING | 必須 | - |
| `width` | 出力動画の幅（ピクセル単位）（デフォルト: 832、ステップ: 16） | INT | 必須 | 16 to MAX_RESOLUTION |
| `height` | 出力動画の高さ（ピクセル単位）（デフォルト: 480、ステップ: 16） | INT | 必須 | 16 to MAX_RESOLUTION |
| `length` | 出力動画のフレーム数（デフォルト: 81、ステップ: 4） | INT | 必須 | 1 to MAX_RESOLUTION |
| `batch_size` | 同時に生成する動画の数（デフォルト: 1） | INT | 必須 | 1 to 4096 |
| `temperature` | モーションパッチングのための高度な温度パラメータ（デフォルト: 220.0、ステップ: 0.1） | FLOAT | 必須 | 1.0 to 1000.0 |
| `topk` | モーションパッチングのための高度な top-k 値（デフォルト: 2） | INT | 必須 | 1 to 10 |
| `start_image` | 動画生成の最初のフレームに使用される開始画像 | IMAGE | 必須 | - |
| `clip_vision_output` | 追加の条件付けのための CLIP ビジョン出力 | CLIP_VISION_OUTPUT | 任意 | - |

**注記：**
- `tracks` 入力は、ポイントトラッキングデータを含む JSON 文字列または JSON 文字列のリストを期待します。`tracks` が空であるか解析できない場合、ノードは WanImageToVideo の動作にフォールバックします。
- `start_image` が存在する場合、`width` と `height` に合わせてリサイズされ、動画シーケンスの最初のフレームとして使用されます。
- `clip_vision_output` が提供された場合、ポジティブ条件付けとネガティブ条件付けの両方に追加されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | モーショントラックおよびオプションの画像情報が適用されたポジティブ条件付け | CONDITIONING |
| `negative` | モーショントラックおよびオプションの画像情報が適用されたネガティブ条件付け | CONDITIONING |
| `latent` | 要求された動画の寸法、長さ、バッチサイズに合わせてサイズ設定されたゼロ埋めの潜在テンソル | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
