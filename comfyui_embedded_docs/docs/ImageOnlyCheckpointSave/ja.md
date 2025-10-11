> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/ja.md)

ImageOnlyCheckpointSaveノードは、モデル、CLIPビジョンエンコーダー、VAEを含むチェックポイントファイルを保存します。指定されたファイル名プレフィックスでsafetensorsファイルを作成し、出力ディレクトリに保存します。このノードは、画像関連のモデルコンポーネントを単一のチェックポイントファイルにまとめて保存するために特別に設計されています。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | はい | - | チェックポイントに保存するモデル |
| `clip_vision` | CLIP_VISION | はい | - | チェックポイントに保存するCLIPビジョンエンコーダー |
| `vae` | VAE | はい | - | チェックポイントに保存するVAE（変分オートエンコーダー） |
| `filename_prefix` | STRING | はい | - | 出力ファイル名のプレフィックス（デフォルト: "checkpoints/ComfyUI"） |
| `prompt` | PROMPT | いいえ | - | ワークフロープロンプトデータ用の非表示パラメータ |
| `extra_pnginfo` | EXTRA_PNGINFO | いいえ | - | 追加のPNGメタデータ用の非表示パラメータ |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| - | - | このノードは出力を返しません |