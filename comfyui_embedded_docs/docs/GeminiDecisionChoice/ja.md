# Google Gemini Decision (Choice)

接続したテキスト、画像、音声、動画に対して独自の選択肢から 1 つを選び、選択された選択肢、その位置、信頼度を返します。`choice` を、同じ選択肢名を入力に持つ Branch ノードに接続するか、Branch ノードが利用できない場合は `option_index` に基づいてルーティングしてください。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | 使用するモデル（デフォルト: `"gemini-decision-1"`）。 | COMBO | はい | `"gemini-decision-1"` |
| `question` | 選択肢が答える質問。最大 5000 文字（デフォルト: "What style is the image?"）。 | STRING | はい | 1～5000 文字 |
| `options` | 1 行につき 1 つの選択肢。入力されたとおりに使用され、各最大 128 文字です。どの選択肢にも当てはまらない入力向けに `other` などの選択肢を追加してください（デフォルト: `photo`、`illustration`、`3d render`、`anime`、`sketch`、`other`）。 | STRING | はい | 2～255 個の選択肢 |
| `images` | 分類する画像。拡張可能なスロット（`image_1` ... `image_16`）全体で最大 16 枚までです。バッチ化された画像は、画像ごとに 1 回として数えます。 | IMAGE | いいえ | 最大 16 枚の画像 |
| `audio` | 分類する音声クリップ。 | AUDIO | いいえ | - |
| `video` | 分類する動画クリップ。 | VIDEO | いいえ | - |
| `text` | 質問の対象となるテキスト（プロンプトや LLM の応答など）。最大 20000 文字です。 | STRING | いいえ | 最大 20000 文字 |

選択肢は 2 個以上 255 個以下にし、同じ選択肢を重複して記載しないでください。それ以外の場合、ノードはエラーを発生します。`text`、`images`、`audio`、`video` のうち少なくとも 1 つを接続し、複数の画像を使う場合は質問内で `image_1`、`image_2` などの名前を付けてください。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `choice` | `options` に書かれたとおりの、選択された選択肢。 | STRING |
| `option_index` | `options` 内での選択された選択肢の位置。0 から始まります。 | INT |
| `confidence` | 選択に対する信頼度。0～1 の範囲です。 | FLOAT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionChoice/ja.md)

---
**Source fingerprint (SHA-256):** `200c63a9197cd95ba0a21da88c5f3117014b37b0651541094a775219381afe43`
