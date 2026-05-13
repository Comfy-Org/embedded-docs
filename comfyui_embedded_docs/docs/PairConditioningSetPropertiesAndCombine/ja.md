> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/ja.md)

以下は、指定された英語ドキュメントを日本語に翻訳したものです。

---

PairConditioningSetPropertiesAndCombine ノードは、既存のポジティブおよびネガティブな conditioning 入力に新しい conditioning データを適用することで、conditioning ペアを変更および結合します。適用する conditioning の強度を調整したり、conditioning 領域の設定方法を制御したりできます。このノードは、複数の conditioning ソースをブレンドする必要がある高度な conditioning 操作ワークフローに特に役立ちます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | はい | - | 元のポジティブ conditioning 入力 |
| `negative` | CONDITIONING | はい | - | 元のネガティブ conditioning 入力 |
| `positive_NEW` | CONDITIONING | はい | - | 適用する新しいポジティブ conditioning |
| `negative_NEW` | CONDITIONING | はい | - | 適用する新しいネガティブ conditioning |
| `strength` | FLOAT | はい | 0.0 ～ 10.0 | 新しい conditioning を適用する際の強度係数（デフォルト：1.0） |
| `set_cond_area` | STRING | はい | "default"<br>"mask bounds" | conditioning 領域の適用方法を制御します（デフォルト："default"） |
| `mask` | MASK | いいえ | - | conditioning の適用領域を制限するオプションのマスク |
| `hooks` | HOOKS | いいえ | - | 高度な制御のためのオプションのフックグループ |
| `timesteps` | TIMESTEPS_RANGE | いいえ | - | オプションのタイムステップ範囲指定 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 結合されたポジティブ conditioning の出力 |
| `negative` | CONDITIONING | 結合されたネガティブ conditioning の出力 |

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
