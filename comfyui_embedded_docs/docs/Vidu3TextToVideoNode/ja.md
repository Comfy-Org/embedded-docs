# Vidu Q3 テキストから動画生成

Vidu Q3 Text-to-Video Generation ノードは、テキストによる説明からビデオを生成します。このノードは Vidu Q3 Pro または Q3 Turbo モデルを使用して、プロンプトに基づいてビデオコンテンツを生成し、ビデオの長さ、解像度、アスペクト比、オーディオの有無を制御できます。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | ビデオ生成に使用するモデル。モデルを選択すると、アスペクト比、解像度、長さ、オーディオに関する追加の設定パラメータが表示されます。 | COMBO | はい | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `prompt` | ビデオ生成のためのテキストによる説明。最大長は2000文字です。 | STRING | はい | N/A |
| `seed` | 生成のランダム性を制御するシード値（デフォルト: 1）。 | INT | はい | 0 から 2147483647 |

### viduq3-pro および viduq3-turbo の入力

以下の設定パラメータは、`viduq3-pro` モデルと `viduq3-turbo` モデルで共通です。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model.aspect_ratio` | 出力ビデオのアスペクト比。 | COMBO | はい | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `model.resolution` | 出力ビデオの解像度。 | COMBO | はい | `"720p"`<br>`"1080p"` |
| `model.duration` | 出力ビデオの長さ（秒単位）（デフォルト: 5）。 | INT | はい | 1 から 16 |
| `model.audio` | 有効にすると、音声付きのビデオ（会話や効果音を含む）を出力します（デフォルト: False）。 | BOOLEAN | はい | True/False |

**注意:** `aspect_ratio`、`resolution`、`duration`、`audio` の各パラメータは、`model` を選択すると必須になります。これらはモデルの設定の一部だからです。`prompt` は空にできず、2000文字を超えることはできません。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `video` | 生成されたビデオファイル。 | VIDEO |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/ja.md)

---
**Source fingerprint (SHA-256):** `89c23454375a43cdfaf46c9e0e55a8a8166d02ada47ca2e237bd9f73fa4d78db`
