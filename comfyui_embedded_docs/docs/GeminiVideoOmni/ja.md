# Google Gemini Omni（動画）

GoogleのGemini Omni Flashモデルを使い、テキストプロンプトから音声付き動画を生成します。参照画像や動画を指定して、結果をガイドまたは編集することも可能です。希望する長さ（3～10秒）やアスペクト比（16:9または9:16）はプロンプト内で直接指定してください。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | 動画生成に使用するGeminiビデオモデル。 | MODEL | Yes | "Omni Flash" |
| `seed` | seedはノードの再実行を制御します。seedに関わらず結果は非決定的です。 | INT | Yes | 0 to 2147483647 |
| `prompt` | The text prompt describing the video to generate. Must be at least one non-whitespace character after stripping leading/trailing whitespace. | STRING | Yes | Minimum 1 character after stripping whitespace |
| `images` | Optional reference images to guide the video generation. Maximum of 14 images total. | IMAGE | No | Multiple images allowed (max 14) |
| `videos` | Optional reference videos to guide or edit the video generation. Maximum of 3 videos, each up to 10 seconds. | VIDEO | No | Multiple videos allowed (max 3, each max 10s) |
| `temperature` | Controls randomness in generation (default: 1.0). | FLOAT | No | 0.0 to 2.0 |
| `top_p` | Nucleus sampling parameter (default: 0.95). | FLOAT | No | 0.0 to 1.0 |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `VIDEO` | The generated video with audio from the Gemini model. | VIDEO |
| `STRING` | Any text response from the model, such as reasoning or explanations. | STRING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/ja.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
