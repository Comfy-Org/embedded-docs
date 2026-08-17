# Empty HunyuanVideo 1.5 Latent

このノードは、HunyuanVideo 1.5 モデルで使用するために特別にフォーマットされた空の潜在テンソルを作成します。モデルの潜在空間に適したチャンネル数と空間次元を持つゼロのテンソルを割り当てることで、ビデオ生成用の空白の開始点を生成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `width` | ビデオフレームの幅（ピクセル単位）。 | INT | Yes | - |
| `height` | ビデオフレームの高さ（ピクセル単位）。 | INT | Yes | - |
| `length` | ビデオシーケンスのフレーム数。 | INT | Yes | - |
| `batch_size` | バッチで生成するビデオサンプルの数（デフォルト：1）。 | INT | No | - |

**注：** 生成された潜在テンソルの空間次元は、入力の `width` と `height` を 16 で割ることで計算されます。時間次元（フレーム数）は `((length - 1) // 4) + 1` として計算されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `samples` | HunyuanVideo 1.5 モデルに適した次元を持つ空の潜在テンソル。テンソルの形状は `[batch_size, 32, frames, height//16, width//16]` です。出力には `downscale_ratio_spacial` 値 16 も含まれます。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/ja.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`
