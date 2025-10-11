> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/ja.md)

DiffusersLoaderノードは、diffusers形式から事前学習済みモデルを読み込みます。model_index.jsonファイルを含む有効なdiffusersモデルディレクトリを検索し、それらをパイプラインで使用するためのMODEL、CLIP、VAEコンポーネントとして読み込みます。このノードは非推奨のローダーカテゴリに属し、Hugging Face diffusersモデルとの互換性を提供します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model_path` | STRING | はい | 複数のオプションが利用可能<br>（diffusersフォルダから自動入力） | 読み込むdiffusersモデルディレクトリへのパス。このノードは設定されたdiffusersフォルダ内の有効なdiffusersモデルを自動的にスキャンし、利用可能なオプションを一覧表示します。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `MODEL` | MODEL | diffusers形式から読み込まれたモデルコンポーネント |
| `CLIP` | CLIP | diffusers形式から読み込まれたCLIPモデルコンポーネント |
| `VAE` | VAE | diffusers形式から読み込まれたVAE（変分オートエンコーダ）コンポーネント |