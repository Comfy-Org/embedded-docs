> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/ja.md)

## 概要
GoogleのVeo 3 APIを使用して、テキストプロンプトから動画を生成します。このノードは高速版や軽量版を含む複数のVeo 3モデルをサポートしており、動画の解像度、長さ、音声生成を指定できます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | はい | - | 動画のテキストによる説明（デフォルト: ""） |
| `aspect_ratio` | COMBO | はい | "16:9"<br>"9:16" | 出力動画のアスペクト比（デフォルト: "16:9"） |
| `resolution` | COMBO | いいえ | "720p"<br>"1080p"<br>"4k" | 出力動画の解像度。veo-3.1-liteおよびveo-3.0モデルでは4Kは利用できません。（デフォルト: "720p"） |
| `negative_prompt` | STRING | いいえ | - | 動画で避けたい内容を指定するネガティブテキストプロンプト（デフォルト: ""） |
| `duration_seconds` | INT | いいえ | 4-8 | 出力動画の長さ（秒）。2秒単位で指定します（デフォルト: 8） |
| `enhance_prompt` | BOOLEAN | いいえ | - | このパラメータは非推奨であり、無視されます。（デフォルト: True） |
| `person_generation` | COMBO | いいえ | "ALLOW"<br>"BLOCK" | 動画内に人物を生成することを許可するかどうか（デフォルト: "ALLOW"） |
| `seed` | INT | いいえ | 0-4294967295 | 動画生成のシード値（0はランダム）（デフォルト: 0） |
| `image` | IMAGE | いいえ | - | 動画生成をガイドするオプションの参照画像 |
| `model` | COMBO | いいえ | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite"<br>"veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | 動画生成に使用するVeo 3モデル（デフォルト: "veo-3.0-generate-001"） |
| `generate_audio` | BOOLEAN | いいえ | - | 動画の音声を生成します。すべてのVeo 3モデルでサポートされています。（デフォルト: False） |

**注意:** `enhance_prompt`パラメータは非推奨であり、その値は無視されます。ノードは常に内部でプロンプトを拡張します。また、`resolution`パラメータはveo-3.1モデル使用時のみ適用され、veo-3.0モデルでは無視されます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成された動画ファイル |

---
**Source fingerprint (SHA-256):** `36ea9d3f0ea717eb7b8146ca35dfdfbe538fbbf164541ee1d1b19b660543e375`
