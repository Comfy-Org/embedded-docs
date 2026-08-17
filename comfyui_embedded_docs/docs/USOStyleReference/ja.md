# USOスタイルリファレンス

USOStyleReference ノードは、参照画像から Flux モデルにスタイル情報を適用します。CLIP ビジョン出力からスタイル埋め込みを構築し、モデルのクローンをパッチして、生成中にスタイル埋め込みがテキストプロンプトのコンディショニングの前に挿入されるようにします。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | スタイル参照パッチを適用するベースモデル | MODEL | はい | - |
| `model_patch` | スタイル参照情報を含むモデルパッチ | MODEL_PATCH | はい | - |
| `clip_vision_output` | CLIP ビジョン処理から抽出されたエンコード済み視覚特徴。ノードは、レイヤー -20 と -11 の隠れ状態を、最後から2番目の隠れ状態と組み合わせてスタイル埋め込みを構築します | CLIP_VISION_OUTPUT | はい | - |

注：3つの入力はすべて必須です。このノードは実験的とマークされています。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | スタイル参照パッチが適用された修正済みモデル | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/ja.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
