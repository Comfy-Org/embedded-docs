# EmptyCosmosLatentVideo

EmptyCosmosLatentVideo ノードは、指定された寸法で空の潜在ビデオテンソルを作成します。幅・高さ・長さ・バッチサイズのパラメータを設定可能で、ビデオ生成ワークフローの開始点として使用できる、ゼロで埋められた潜在表現を生成します。潜在変数の空間次元は、8分の1にダウンサンプリングされます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `width` | 潜在ビデオの幅（ピクセル単位）（デフォルト: 1280、16で割り切れる必要があります） | INT | はい | 16 ～ MAX_RESOLUTION |
| `height` | 潜在ビデオの高さ（ピクセル単位）（デフォルト: 704、16で割り切れる必要があります） | INT | はい | 16 ～ MAX_RESOLUTION |
| `length` | 潜在ビデオのフレーム数（デフォルト: 121、8で割り切れる必要があります） | INT | はい | 1 ～ MAX_RESOLUTION |
| `batch_size` | バッチで生成する潜在ビデオの数（デフォルト: 1） | INT | はい | 1 ～ 4096 |

潜在テンソルは16チャンネルを使用します。空間次元はピクセル寸法と比較して8で除算され（`height // 8`、`width // 8`）、フレーム数は `((length - 1) // 8) + 1` 個の潜在フレームに圧縮されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `samples` | 生成された、ゼロ値を持つ空の潜在ビデオテンソル。形状: `(batch_size, 16, ((length - 1) // 8) + 1, height // 8, width // 8)` | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/ja.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
