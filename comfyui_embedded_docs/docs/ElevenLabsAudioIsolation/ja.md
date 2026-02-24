> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/ja.md)

ElevenLabs Voice Isolation ノードは、オーディオファイルから背景ノイズを除去し、ボーカルやスピーチを分離します。オーディオを ElevenLabs API に送信して処理し、クリーンなオーディオを返します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | はい | | 背景ノイズ除去のために処理するオーディオ。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 背景ノイズが除去された処理済みオーディオ。 |
