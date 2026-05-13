> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/ja.md)

以下が翻訳結果です。

ElevenLabs Speech to Speech ノードは、入力された音声ファイルを別の声に変換します。ElevenLabs API を使用して音声を変換し、元の音声の内容と感情的なトーンを保持します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `voice` | CUSTOM | はい | - | 変換先のターゲット音声です。Voice Selector または Instant Voice Clone から接続します。 |
| `audio` | AUDIO | はい | - | 変換する元の音声です。 |
| `stability` | FLOAT | いいえ | 0.0 - 1.0 | 音声の安定性です。値が低いほど感情の幅が広がり、値が高いほど一貫性が増しますが、単調になる可能性があります（デフォルト: 0.5）。 |
| `model` | DYNAMICCOMBO | いいえ | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` | 音声変換に使用するモデルです。各オプションは特定の音声設定（類似性ブースト、スタイル、スピーカーブーストの使用、速度）を提供します。 |
| `output_format` | COMBO | いいえ | `"mp3_44100_192"`<br>`"opus_48000_192"` | 音声の出力フォーマットです（デフォルト: "mp3_44100_192"）。 |
| `seed` | INT | いいえ | 0 - 4294967295 | 再現性のためのシード値です（デフォルト: 0）。 |
| `remove_background_noise` | BOOLEAN | いいえ | - | 音声分離を使用して、入力音声から背景ノイズを除去します（デフォルト: False）。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 指定された出力フォーマットで変換された音声ファイルです。 |

---
**Source fingerprint (SHA-256):** `118fe6e85b146d0649b104d814abb518d37f69ade2e53becac365a0ec90146fd`
