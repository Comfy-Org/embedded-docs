# HunyuanVideo15SuperResolution

HunyuanVideo15SuperResolution ノードは、動画の超解像プロセス用のコンディショニングデータを準備します。動画の潜在表現と、必要に応じて開始画像を受け取り、ノイズ増幅値とオプションのCLIPビジョンデータとともに、モデルが高解像度出力を生成するために使用できる形式にまとめます。

## 入力

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | 連結された潜在表現とノイズ増幅データで変更されるポジティブコンディショニング入力です。 | CONDITIONING | はい | N/A |
| `negative` | 連結された潜在表現とノイズ増幅データで変更されるネガティブコンディショニング入力です。 | CONDITIONING | はい | N/A |
| `vae` | オプションの `start_image` をエンコードするために使用されるVAEです。`start_image` を指定する場合に必須です。 | VAE | いいえ | N/A |
| `start_image` | 超解像プロセスをガイドするオプションの開始画像です。指定すると、アップスケールされ、`vae` でエンコードされ、コンディショニング潜在表現の先頭に配置されます。 | IMAGE | いいえ | N/A |
| `clip_vision_output` | オプションのCLIPビジョン埋め込みです。指定すると、ポジティブとネガティブの両方のコンディショニングに追加されます。 | CLIP_VISION_OUTPUT | いいえ | N/A |
| `latent` | コンディショニングに組み込まれる動画の潜在表現です。 | LATENT | はい | N/A |
| `noise_augmentation` | コンディショニングに適用するノイズ増幅の強さです（デフォルト: 0.70）。上級者向けのパラメータです。 | FLOAT | はい | 0.0 - 1.0 (step 0.01) |

**注:** `start_image` を指定する場合は、エンコードするための `vae` も接続する必要があります。`start_image` は入力 `latent` が示す寸法に合わせて自動的にアップスケールされ、最初の3つのカラーチャンネル（RGB）のみがVAEによって使用されます。

## 出力

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | 変更されたポジティブコンディショニング。連結された潜在表現、ノイズ増幅、およびオプションのCLIPビジョンデータが含まれます。 | CONDITIONING |
| `negative` | 変更されたネガティブコンディショニング。連結された潜在表現、ノイズ増幅、およびオプションのCLIPビジョンデータが含まれます。 | CONDITIONING |
| `latent` | 入力された潜在表現を、変更せずにそのまま渡します。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/ja.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
