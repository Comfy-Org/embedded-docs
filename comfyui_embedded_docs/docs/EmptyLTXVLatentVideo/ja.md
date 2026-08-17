# 空のLTXV潜在ビデオ

`EmptyLTXVLatentVideo` ノードは、ビデオ生成用の空の潜在テンソルを作成します。指定された幅・高さ・長さ・バッチサイズに基づいて、ゼロで埋められた潜在表現を生成し、LTXV ビデオワークフローで開始点として使用できる状態にします。この潜在表現はビデオを圧縮形式で格納します。空間次元は32で除算され、フレーム数は8分の1に削減されます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `width` | 潜在ビデオの幅（ピクセル単位）（デフォルト: 768、ステップ: 32） | INT | はい | 64 to MAX_RESOLUTION |
| `height` | 潜在ビデオの高さ（ピクセル単位）（デフォルト: 512、ステップ: 32） | INT | はい | 64 to MAX_RESOLUTION |
| `length` | 潜在ビデオのフレーム数（デフォルト: 97、ステップ: 8） | INT | はい | 1 to MAX_RESOLUTION |
| `batch_size` | 1回のバッチで生成する潜在ビデオの数（デフォルト: 1） | INT | いいえ | 1 to 4096 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `samples` | ゼロで満たされた、生成された空の潜在テンソル。この潜在表現には、幅と高さに適用される空間的ダウンスケールを表す `downscale_ratio_spacial` 値（32）も含まれています。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/ja.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
