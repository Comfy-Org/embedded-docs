> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/ja.md)

ModelPatchLoaderノードは、model_patchesフォルダから特殊なモデルパッチを読み込みます。このノードはパッチファイルのタイプを自動的に検出し、適切なモデルアーキテクチャを読み込んでから、ワークフローで使用できるようにModelPatcherでラップします。このノードは、controlnetブロックやfeature embedderモデルなど、さまざまなパッチタイプをサポートしています。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `name` | STRING | はい | model_patchesフォルダから利用可能なすべてのモデルパッチファイル | model_patchesディレクトリから読み込むモデルパッチのファイル名 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `MODEL_PATCH` | MODEL_PATCH | ワークフローで使用するためにModelPatcherでラップされた読み込まれたモデルパッチ |