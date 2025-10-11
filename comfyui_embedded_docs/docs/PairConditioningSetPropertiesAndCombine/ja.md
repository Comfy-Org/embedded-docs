> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/ja.md)

PairConditioningSetPropertiesAndCombineノードは、既存のポジティブおよびネガティブなコンディショニング入力に対して新しいコンディショニングデータを適用することで、コンディショニングペアを修正および結合します。適用するコンディショニングの強度を調整したり、コンディショニング領域の設定方法を制御したりすることができます。このノードは、複数のコンディショニングソースをブレンドする必要がある高度なコンディショニング操作ワークフローで特に有用です。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | はい | - | 元のポジティブなコンディショニング入力 |
| `negative` | CONDITIONING | はい | - | 元のネガティブなコンディショニング入力 |
| `positive_NEW` | CONDITIONING | はい | - | 適用する新しいポジティブなコンディショニング |
| `negative_NEW` | CONDITIONING | はい | - | 適用する新しいネガティブなコンディショニング |
| `strength` | FLOAT | はい | 0.0 ～ 10.0 | 新しいコンディショニングを適用する際の強度係数（デフォルト: 1.0） |
| `set_cond_area` | STRING | はい | "default"<br>"mask bounds" | コンディショニング領域の適用方法を制御します |
| `mask` | MASK | いいえ | - | コンディショニング適用領域を制限するオプションのマスク |
| `hooks` | HOOKS | いいえ | - | 高度な制御のためのオプションのフックグループ |
| `timesteps` | TIMESTEPS_RANGE | いいえ | - | オプションのタイムステップ範囲指定 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 結合されたポジティブなコンディショニング出力 |
| `negative` | CONDITIONING | 結合されたネガティブなコンディショニング出力 |