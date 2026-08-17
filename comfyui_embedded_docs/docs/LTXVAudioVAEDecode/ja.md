# LTXV オーディオVAEデコード

LTXV Audio VAE Decode ノードは、音声の潜在表現をオーディオ波形に変換します。このデコード処理には専用の Audio VAE モデルを使用し、特定のサンプルレートの音声出力を生成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `samples` | デコード対象の潜在表現。 | LATENT | はい | N/A |
| `audio_vae` | 潜在表現のデコードに使用する Audio VAE モデル。 | VAE | はい | N/A |

**注:** 提供された潜在表現がネストされている場合（複数の潜在表現を含む場合）、ノードはデコードにシーケンス内の最後の潜在表現を自動的に使用します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `Audio` | デコードされたオーディオ波形と、それに関連するサンプルレート。波形は入力潜在表現と同じデバイスに移動されたテンソルであり、サンプルレートは Audio VAE モデルによって決定されます。 | AUDIO |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/ja.md)

---
**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`
