# モデルを保存

ModelSaveノードは、トレーニング済みまたは変更されたモデルをコンピュータのストレージに保存します。モデルを入力として受け取り、指定したファイル名プレフィックスを使用して、出力フォルダ内のsafetensorsチェックポイントファイルに書き込みます。ワークフローのプロンプトとメタデータ情報は、利用可能な場合に保存ファイルに埋め込まれます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | ディスクに保存するモデル | MODEL | はい | - |
| `filename_prefix` | 保存するモデルファイルのファイル名とパスプレフィックス（デフォルト："diffusion_models/ComfyUI"）。保存時にカウンタが名前に追加されます（例：`ComfyUI_00000_.safetensors`）。 | STRING | はい | - |
| `prompt` | ワークフローのプロンプト情報（自動的に提供されます） | PROMPT | いいえ | - |
| `extra_pnginfo` | 追加のワークフローメタデータ（自動的に提供されます） | EXTRA_PNGINFO | いいえ | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| *None* | このノードは出力値を返しません | - |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/ja.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
