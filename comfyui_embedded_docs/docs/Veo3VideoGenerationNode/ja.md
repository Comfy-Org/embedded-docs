> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/ja.md)

GoogleのVeo 3 APIを使用してテキストプロンプトから動画を生成します。このノードは、veo-3.0-generate-001とveo-3.0-fast-generate-001の2つのVeo 3モデルをサポートしています。ベースのVeoノードを拡張し、音声生成と固定8秒間の長さといったVeo 3固有の機能を含んでいます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | はい | - | 動画のテキストによる説明（デフォルト: ""） |
| `aspect_ratio` | COMBO | はい | "16:9"<br>"9:16" | 出力動画のアスペクト比（デフォルト: "16:9"） |
| `negative_prompt` | STRING | いいえ | - | 動画内で避けるべき内容を指示する否定的なテキストプロンプト（デフォルト: ""） |
| `duration_seconds` | INT | いいえ | 8-8 | 出力動画の長さ（秒）。Veo 3は8秒のみサポートしています（デフォルト: 8） |
| `enhance_prompt` | BOOLEAN | いいえ | - | AI支援でプロンプトを強化するかどうか（デフォルト: True） |
| `person_generation` | COMBO | いいえ | "ALLOW"<br>"BLOCK" | 動画内での人物生成を許可するかどうか（デフォルト: "ALLOW"） |
| `seed` | INT | いいえ | 0-4294967295 | 動画生成のシード（0でランダム）（デフォルト: 0） |
| `image` | IMAGE | いいえ | - | 動画生成をガイドするためのオプションの参照画像 |
| `model` | COMBO | いいえ | "veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | 動画生成に使用するVeo 3モデル（デフォルト: "veo-3.0-generate-001"） |
| `generate_audio` | BOOLEAN | いいえ | - | 動画の音声を生成します。すべてのVeo 3モデルでサポートされています（デフォルト: False） |

**注意:** `duration_seconds`パラメータは、すべてのVeo 3モデルで8秒に固定されており、変更できません。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成された動画ファイル |