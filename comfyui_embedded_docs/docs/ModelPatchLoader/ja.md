# モデルパッチローダー

以下に、英語ドキュメントを日本語に翻訳しました。

---

ModelPatchLoader ノードは、`model_patches` フォルダから特殊なモデルパッチを読み込みます。パッチファイルの種類を自動的に検出し、適切なモデルアーキテクチャをロードした後、ワークフローで使用できるように `ModelPatcher` にラップします。このノードは、controlnet ブロック、feature embedder モデル、その他の特殊なアーキテクチャを含む、さまざまなパッチタイプをサポートしています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `name` | `model_patches` ディレクトリからロードするモデルパッチのファイル名です。 | STRING | はい | `model_patches` フォルダにある利用可能なすべてのモデルパッチファイル |

注: このノードは ComfyUI では実験的としてマークされています。パッチタイプはファイルの内容から自動的に検出されるため、このノード単体で複数の種類のパッチを処理できます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `MODEL_PATCH` | ワークフローで使用できるように `ModelPatcher` にラップされた、ロード済みのモデルパッチです。 | MODEL_PATCH |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/ja.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`
