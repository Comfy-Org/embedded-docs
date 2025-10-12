> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/ja.md)

Kling Virtual Try Onノード。人物画像と衣服画像を入力して、人物に衣服を試着させます。複数の衣服アイテムの画像を1つの画像に白背景で統合することができます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `人物画像` | IMAGE | はい | - | 衣服を試着する人物画像 |
| `服画像` | IMAGE | はい | - | 人物に試着する衣服画像 |
| `モデル名` | STRING | はい | `"kolors-virtual-try-on-v1"` | 使用する仮想試着モデル（デフォルト: "kolors-virtual-try-on-v1"） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | IMAGE | 衣服を試着した結果の人物画像 |