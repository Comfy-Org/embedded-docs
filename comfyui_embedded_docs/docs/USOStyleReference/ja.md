> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/ja.md)

USOStyleReference ノードは、CLIPビジョン出力からエンコードされた画像特徴量を使用して、モデルにスタイル参照パッチを適用します。視覚入力から抽出されたスタイル情報を組み込むことで、入力モデルの修正バージョンを作成し、スタイル転送や参照ベースの生成機能を実現します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | はい | - | スタイル参照パッチを適用するベースモデル |
| `model_patch` | MODEL_PATCH | はい | - | スタイル参照情報を含むモデルパッチ |
| `clip_vision_output` | CLIP_VISION_OUTPUT | はい | - | CLIPビジョン処理から抽出されたエンコード済み視覚特徴量 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model` | MODEL | スタイル参照パッチが適用された修正済みモデル |

---
**Source fingerprint (SHA-256):** `fd800fb927677da29e148bfa1b287efed82895860ce4b0241d662579d2c07ff4`
