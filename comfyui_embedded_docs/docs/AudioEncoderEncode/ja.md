# オーディオエンコーダーエンコード

AudioEncoderEncode ノードは、オーディオエンコーダーモデルを使用して音声データをエンコードし、処理します。音声入力を取得し、条件付けパイプラインでさらに処理できるエンコードされた表現に変換します。このノードは、生のオーディオ波形を、オーディオベースの機械学習アプリケーションに適した形式に変換します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `audio_encoder` | 音声入力を処理するために使用されるオーディオエンコーダーモデル | AUDIO_ENCODER | はい | - |
| `audio` | 波形とサンプルレート情報を含む音声データ | AUDIO | はい | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `output` | オーディオエンコーダーによって生成されたエンコード済み音声表現 | AUDIO_ENCODER_OUTPUT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/ja.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
