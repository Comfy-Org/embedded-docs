> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/ja.md)

PairConditioningCombineノードは、2組のコンディショニングデータ（ポジティブとネガティブ）を1組に結合します。2つの別々のコンディショニングペアを入力として受け取り、ComfyUIの内部コンディショニング結合ロジックを使用してそれらをマージします。このノードは実験的であり、主に高度なコンディショニング操作ワークフローで使用されます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive_A` | CONDITIONING | はい | - | 1つ目のポジティブコンディショニング入力 |
| `negative_A` | CONDITIONING | はい | - | 1つ目のネガティブコンディショニング入力 |
| `positive_B` | CONDITIONING | はい | - | 2つ目のポジティブコンディショニング入力 |
| `negative_B` | CONDITIONING | はい | - | 2つ目のネガティブコンディショニング入力 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 結合されたポジティブコンディショニング出力 |
| `negative` | CONDITIONING | 結合されたネガティブコンディショニング出力 |