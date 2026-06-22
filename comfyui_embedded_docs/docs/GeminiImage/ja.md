# GeminiImage

以下が翻訳結果です。

GeminiImageノードは、GoogleのGemini AIモデルからテキストと画像の応答を生成します。テキストプロンプト、画像、ファイルを含むマルチモーダル入力を提供することで、一貫性のあるテキストと画像の出力を作成できます。このノードは、最新のGeminiモデルとのすべてのAPI通信と応答解析を処理します。

## 入力

| パラメータ | 説明 | データ型 | 入力タイプ | デフォルト値 | 範囲 |
| --- | --- | --- | --- | --- | --- |
| `prompt` | 生成のためのテキストプロンプト | STRING | 必須 | "" | - |
| `model` | 応答生成に使用するGeminiモデル。 | COMBO | 必須 | gemini_2_5_flash_image_preview | `gemini_2_5_flash_image_preview`<br>`gemini_2_5_pro_exp_03_25`<br>`gemini_2_0_flash_exp_image_generation` |
| `seed` | シード値を特定の値に固定すると、モデルは繰り返しリクエストに対して同じ応答を提供するよう最善を尽くします。決定論的な出力は保証されません。また、temperatureなどのモデルやパラメータ設定を変更すると、同じシード値を使用しても応答にばらつきが生じる可能性があります。デフォルトでは、ランダムなシード値が使用されます。 | INT | 必須 | 42 | 0 ～ 18446744073709551615 |
| `images` | モデルのコンテキストとして使用するオプションの画像。複数の画像を含めるには、Batch Imagesノードを使用できます。 | IMAGE | オプション | None | - |
| `files` | モデルのコンテキストとして使用するオプションのファイル。Gemini Generate Content Input Filesノードからの入力を受け付けます。 | GEMINI_INPUT_FILES | オプション | None | - |

**注記:** このノードには、システムによって自動的に処理され、ユーザー入力が不要な隠しパラメータ（`auth_token`、`comfy_api_key`、`unique_id`）が含まれています。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `IMAGE` | Geminiモデルから生成された画像応答 | IMAGE |
| `STRING` | Geminiモデルから生成されたテキスト応答 | STRING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage/ja.md)

---
**Source fingerprint (SHA-256):** `bf55ec4f5a869a6bc5a15366f55f86ad25f9498c14056acc80951d3637bf08f2`
