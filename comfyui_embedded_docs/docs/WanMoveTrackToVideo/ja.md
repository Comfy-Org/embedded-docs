# WanMoveTrackToVideo

WanMoveTrackToVideo ノードは、ビデオ生成用のコンディショニングデータと潜在データを準備します。VAE を使用して開始画像シーケンスを潜在空間にエンコードし、オプションでモーショントラッキング情報を組み込んで、生成されたビデオ内のオブジェクトの動きをガイドできます。このノードは、変更されたポジティブおよびネガティブコンディショニングと、ビデオ生成モデルで使用できる空の潜在テンソルを出力します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | 変更されるポジティブコンディショニング入力です。 | CONDITIONING | はい | - |
| `negative` | 変更されるネガティブコンディショニング入力です。 | CONDITIONING | はい | - |
| `vae` | 開始画像を潜在空間にエンコードするために使用される VAE モデルです。 | VAE | はい | - |
| `tracks` | オブジェクトのパスを含むオプションのモーショントラッキングデータです。 | TRACKS | いいえ | - |
| `strength` | トラックコンディショニングの強さです。`tracks` が提供され、値が 0.0 より大きい場合にのみ効果があります。（デフォルト: 1.0） | FLOAT | はい | 0.0 - 100.0 |
| `width` | 出力ビデオの幅です。16 の倍数で設定します。（デフォルト: 832） | INT | はい | 16 - MAX_RESOLUTION |
| `height` | 出力ビデオの高さです。16 の倍数で設定します。（デフォルト: 480） | INT | はい | 16 - MAX_RESOLUTION |
| `length` | ビデオシーケンスのフレーム数です。4 の倍数で設定します。（デフォルト: 81） | INT | はい | 1 - MAX_RESOLUTION |
| `batch_size` | 潜在出力のバッチサイズです。（デフォルト: 1） | INT | はい | 1 - 4096 |
| `start_image` | VAE でエンコードする開始画像または画像シーケンスです。 | IMAGE | はい | - |
| `clip_vision_output` | コンディショニングに追加するオプションの CLIP ビジョンモデル出力です。 | CLIP_VISION_OUTPUT | いいえ | - |

注：トラックベースのモーションは、`tracks` が提供され、`strength` が 0.0 より大きい場合にのみ適用されます。それ以外の場合、コンディショニングは変更されていないエンコード済みの開始画像を受け取ります。`start_image` は、コンディショニング用の潜在画像とマスクを作成するために使用されます。利用できない場合は、ノードはコンディショニングをそのまま通過させ、空の潜在を出力します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | 変更されたポジティブコンディショニングです。`concat_latent_image`、`concat_mask`、`clip_vision_output` を含む可能性があります。 | CONDITIONING |
| `negative` | 変更されたネガティブコンディショニングです。`concat_latent_image`、`concat_mask`、`clip_vision_output` を含む可能性があります。 | CONDITIONING |
| `latent` | `batch_size`、`length`、`height`、`width` の入力によって形状が決まる空の潜在テンソルです。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
