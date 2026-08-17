# HunyuanVideo15ImageToVideo

HunyuanVideo15ImageToVideo ノードは、HunyuanVideo 1.5 モデルに基づくビデオ生成用の条件付け（conditioning）と潜在空間データを準備します。ビデオシーケンスの初期潜在表現を作成し、必要に応じて開始画像またはCLIPビジョン出力を統合して生成プロセスをガイドできます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | ビデオに含める内容を記述するポジティブ条件付けプロンプト。 | CONDITIONING | はい | - |
| `negative` | ビデオで避けるべき内容を記述するネガティブ条件付けプロンプト。 | CONDITIONING | はい | - |
| `vae` | 開始画像を潜在空間にエンコードするために使用されるVAE（Variational Autoencoder）モデル。 | VAE | はい | - |
| `width` | 出力ビデオフレームの幅（ピクセル単位）。16で割り切れる必要があります。（デフォルト：848） | INT | はい | 16 to MAX_RESOLUTION, step: 16 |
| `height` | 出力ビデオフレームの高さ（ピクセル単位）。16で割り切れる必要があります。（デフォルト：480） | INT | はい | 16 to MAX_RESOLUTION, step: 16 |
| `length` | ビデオシーケンスの総フレーム数。値は4ステップずつ増加します。（デフォルト：33） | INT | はい | 1 to MAX_RESOLUTION, step: 4 |
| `batch_size` | 1回のバッチで生成するビデオシーケンスの数。（デフォルト：1） | INT | はい | 1 to 4096 |
| `start_image` | ビデオ生成を初期化するためのオプションの開始画像。指定すると、エンコードされて最初のフレームの条件付けに使用されます。画像の最初の`length`フレームのみが使用されます。 | IMAGE | いいえ | - |
| `clip_vision_output` | 生成に追加の視覚的条件付けを提供するためのオプションのCLIPビジョン埋め込み。 | CLIP_VISION_OUTPUT | いいえ | - |

**注：** `start_image` が指定された場合、バイリニア補間を使用して指定された `width` と `height` に自動的にリサイズされ、その RGB チャンネルのみが使用されます。画像バッチの最初の `length` フレームが使用されます。その後、エンコードされた画像は、対応する `concat_mask` を持つ `concat_latent_image` として `positive` と `negative` の両方の条件付けに追加されます。マスクは、開始画像でカバーされるフレームでは 0.0 に、残りのフレームでは 1.0 に設定されます。`clip_vision_output` が指定された場合、それも `positive` と `negative` の両方の条件付けに追加されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | 変更されたポジティブ条件付け。エンコードされた開始画像またはCLIPビジョン出力が含まれる場合があります。 | CONDITIONING |
| `negative` | 変更されたネガティブ条件付け。エンコードされた開始画像またはCLIPビジョン出力が含まれる場合があります。 | CONDITIONING |
| `latent` | 指定されたバッチサイズ、ビデオ長、幅、高さに合わせて構成された次元を持つ空の潜在テンソル。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
