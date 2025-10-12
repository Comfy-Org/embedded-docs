> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/ja.md)

StableCascade_StageB_Conditioningノードは、既存の条件付け情報とStage Cからの事前潜在表現を組み合わせることで、Stable Cascade Stage Bの生成用の条件付けデータを準備します。このノードは、Stage Cの潜在サンプルを含むように条件付けデータを修正し、生成プロセスがより一貫性のある出力を得るために事前情報を活用できるようにします。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `コンディショニング` | CONDITIONING | はい | - | Stage Cの事前情報で修正される条件付けデータ |
| `ステージc` | LATENT | はい | - | 条件付け用の事前サンプルを含むStage Cからの潜在表現 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Stage Cの事前情報が統合された修正済み条件付けデータ |