# HunyuanRefinerLatent

HunyuanRefinerLatent ノードは、リファインメント処理のための conditioning および latent 入力を処理します。ポジティブおよびネガティブの conditioning の両方にノイズ拡張を適用し、latent 画像データを組み込み、その後の処理のために特定の次元を持つ新しい latent 出力を生成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | 処理対象となるポジティブな conditioning 入力です。 | CONDITIONING | はい | - |
| `negative` | 処理対象となるネガティブな conditioning 入力です。 | CONDITIONING | はい | - |
| `latent` | 潜在表現の入力です。 | LATENT | はい | - |
| `noise_augmentation` | 適用するノイズ拡張の量です（デフォルト: 0.10、ステップ: 0.01、詳細設定パラメータ）。 | FLOAT | はい | 0.0 - 1.0 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | ノイズ拡張と latent 画像の連結が適用された、処理済みのポジティブ conditioning です。 | CONDITIONING |
| `negative` | ノイズ拡張と latent 画像の連結が適用された、処理済みのネガティブ conditioning です。 | CONDITIONING |
| `latent` | 入力 `latent` と同じバッチサイズと同じ最後の3つの次元サイズを持ち、チャンネル数が32である新しいゼロ埋め latent です。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/ja.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
