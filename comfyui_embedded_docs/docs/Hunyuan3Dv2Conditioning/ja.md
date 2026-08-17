# Hunyuan3Dv2Conditioning

Hunyuan3Dv2Conditioning ノードは、CLIP vision 出力を処理して 3D モデル用の conditioning データを生成します。ビジョン出力から最後の隠れ状態の埋め込みを抽出し、ポジティブとネガティブの conditioning ペアを作成します。ポジティブ conditioning は実際の埋め込みを使用し、ネガティブ conditioning は同じ形状のゼロ値の埋め込みを使用します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip_vision_output` | 視覚埋め込みを含む CLIP vision モデルの出力 | CLIP_VISION_OUTPUT | はい | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | CLIP vision 埋め込みを含むポジティブ conditioning データ | CONDITIONING |
| `negative` | ポジティブ埋め込みと同じ形状のゼロ値埋め込みを含むネガティブ conditioning データ | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/ja.md)

---
**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`
