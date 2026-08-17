# WanVaceToVideo

WanVaceToVideo ノードは、動画生成モデル用のビデオ条件付けデータを処理します。ポジティブ条件付け入力とネガティブ条件付け入力、およびビデオ制御データを受け取り、動画生成用の潜在表現を準備します。このノードは、ビデオのアップスケーリング、マスキング、VAE エンコーディングを処理して、動画モデルに適した条件付け構造を作成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | 生成をガイドするためのポジティブ条件付け入力です。 | CONDITIONING | はい | - |
| `negative` | 生成をガイドするためのネガティブ条件付け入力です。 | CONDITIONING | はい | - |
| `vae` | 画像とビデオフレームのエンコーディングに使用される VAE モデルです。 | VAE | はい | - |
| `width` | 出力ビデオの幅（ピクセル単位）です（デフォルト: 832、ステップ: 16）。 | INT | はい | 16 to MAX_RESOLUTION |
| `height` | 出力ビデオの高さ（ピクセル単位）です（デフォルト: 480、ステップ: 16）。 | INT | はい | 16 to MAX_RESOLUTION |
| `length` | ビデオのフレーム数です（デフォルト: 81、ステップ: 4）。 | INT | はい | 1 to MAX_RESOLUTION |
| `batch_size` | 同時に生成するビデオの数です（デフォルト: 1）。 | INT | はい | 1 to 4096 |
| `strength` | VACE 制御の条件強度です（デフォルト: 1.0、ステップ: 0.01）。これは LoRA 強度ではありません。LoRA の重みは別の LoRA ノードを通じて適用されます。 | FLOAT | はい | 0.0 to 1000.0 |
| `control_video` | 制御条件付け用のオプションの入力ビデオです。指定しない場合は、ニュートラルグレーのビデオが自動的に作成されます。指定した場合は、`width` × `height` にアップスケールされ、最初の `length` フレームに制限されます。フレーム数が不足している場合は、不足しているフレームがニュートラルグレーで埋められます。 | IMAGE | いいえ | - |
| `control_masks` | ビデオのどの部分を変更するかを制御するためのオプションのマスクです。指定しない場合は、全面白のマスクが使用されます。指定した場合は、マスクが `width` × `height` にアップスケールされ、`length` フレームに制限され、フレーム数が不足している場合は白で埋められます。 | MASK | いいえ | - |
| `reference_image` | 追加の条件付け用のオプションの参照画像です。指定した場合は、`width` × `height` にアップスケールされ、VAE によってエンコードされ、潜在シーケンスの先頭に追加されます。 | IMAGE | いいえ | - |

**注記:** `control_video` を指定すると、指定された `width` と `height` にアップスケールされます。`control_masks` を指定すると、同じ寸法にアップスケールされます。`reference_image` を指定すると、VAE を通じてエンコードされ、潜在シーケンスの先頭に追加されます。`length` パラメータはフレーム数を決定し、潜在長は `((length - 1) // 4) + 1` として計算されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | ビデオ制御データ（vace_frames、vace_mask、vace_strength）が適用されたポジティブ条件付けです。 | CONDITIONING |
| `negative` | ビデオ制御データ（vace_frames、vace_mask、vace_strength）が適用されたネガティブ条件付けです。 | CONDITIONING |
| `latent` | 動画生成用の空の潜在テンソルです。形状は [batch_size, 16, latent_length, height/8, width/8] です。 | LATENT |
| `trim_latent` | 参照画像を使用する場合にトリミングする潜在フレーム数です（参照画像が指定されていない場合は 0 です）。 | INT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
