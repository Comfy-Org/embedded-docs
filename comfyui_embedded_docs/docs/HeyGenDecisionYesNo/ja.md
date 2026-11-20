# HeyGen Decision (Yes/No)

接続したテキスト、画像、音声、動画についてはい/いいえの質問を行い、ルーティングに使用できるブール値を取得します。`result` を If/Else Switch ノードに接続して 2 つのパスのどちらかを選択し、`answer` と `probability` を読むことで、回答がどれほど明確だったかを確認できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | 使用するモデル。`heygen-decision-1-turbo` は `heygen-decision-1` より高速で低コストです（デフォルト: `"heygen-decision-1"`）。 | COMBO | はい | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | 接続されている内容についてのはい/いいえの質問です。最大 5000 文字です。「はい」が実際に処理したいケースになるように質問してください（デフォルト: "Is there a person in the image?"）。 | STRING | はい | 1～5000 文字 |
| `threshold` | `result` が true になる「はい」の確率です。明確な回答は 0 または 1 に近くなります（デフォルト: 0.5）。 | FLOAT | はい | 0.01～0.99（ステップ 0.01） |
| `images` | 質問対象の画像です。バッチのすべてのフレームを数えて合計 4 枚までです。ソケット全体にわたって順番に `image_1` から `image_4` まで番号が付けられます。 | IMAGE | いいえ | 最大 4 枚の画像 |
| `audio_1` | 質問対象の音声です。最大 30 分です。 | AUDIO | いいえ | 最大 30 分 |
| `video_1` | 質問対象の動画です。最大 60 秒です。 | VIDEO | いいえ | 最大 60 秒 |
| `text` | 質問の対象となるテキストです。プロンプトや LLM の応答などで、最大 20000 文字です。 | STRING | いいえ | 最大 20000 文字 |

`text`、`images`、`audio_1`、`video_1` の少なくとも 1 つを接続し、質問内でソケット名によってそれらを参照してください。例えば「image_2 は image_1 と同じ人物を映していますか？」のように指定します。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `result` | ブール値としての回答です。「はい」の場合は true、「いいえ」の場合は false です。 | BOOLEAN |
| `answer` | 文字列 `"yes"` または `"no"` としての回答です。 | STRING |
| `probability` | 0 から 1 の間の「はい」の確率です。 | FLOAT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionYesNo/ja.md)

---
**Source fingerprint (SHA-256):** `5a6a606d5c6ef62eb3424bd54a0da3dc177da7d0acf4b5c235a62b78ad8d2df1`
