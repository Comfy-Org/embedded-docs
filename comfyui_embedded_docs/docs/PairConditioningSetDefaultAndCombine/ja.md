> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/ja.md)

PairConditioningSetDefaultAndCombineノードは、デフォルトのコンディショニング値を設定し、入力されたコンディショニングデータと結合します。このノードは、ポジティブおよびネガティブなコンディショニング入力と、それらに対応するデフォルト値を取り込み、ComfyUIのフックシステムを通じて処理し、デフォルト値を組み込んだ最終的なコンディショニング出力を生成します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | はい | - | 処理対象の主要なポジティブコンディショニング入力 |
| `negative` | CONDITIONING | はい | - | 処理対象の主要なネガティブコンディショニング入力 |
| `positive_DEFAULT` | CONDITIONING | はい | - | フォールバックとして使用されるデフォルトのポジティブコンディショニング値 |
| `negative_DEFAULT` | CONDITIONING | はい | - | フォールバックとして使用されるデフォルトのネガティブコンディショニング値 |
| `hooks` | HOOKS | いいえ | - | カスタム処理ロジックのためのオプションのフックグループ |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | デフォルト値が組み込まれた処理済みのポジティブコンディショニング |
| `negative` | CONDITIONING | デフォルト値が組み込まれた処理済みのネガティブコンディショニング |