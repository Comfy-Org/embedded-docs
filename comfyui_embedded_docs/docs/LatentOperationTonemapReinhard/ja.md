# 潜在操作トーンマップライナード

LatentOperationTonemapReinhard は、潜在ベクトルに Reinhard トーンマッピングを適用します。この技術は潜在ベクトルを正規化し、大きさの平均と標準偏差に基づく統計的手法を用いてその大きさを調整します。強度は `multiplier` パラメータによって制御されます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `multiplier` | トーンマッピング効果の強度を制御します（デフォルト: 1.0） | FLOAT | はい | 0.0 to 100.0 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `operation` | 潜在ベクトルに適用可能なトーンマッピング操作を返します | LATENT_OPERATION |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/ja.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
