# Google Gemini Decision (Score)

接続したテキスト、画像、オーディオ、または動画を 1～10 で評価し、スコアと、設定したしきい値で切り替わるブール値を取得します。出力のフィルタリングや並べ替えに使用できます。たとえば、スコアが少なくとも 7 の画像だけを残し、`result` を If/Else Switch ノードに接続して処理を分岐できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | 使用するモデル（デフォルト：`"gemini-decision-1"`）。 | COMBO | はい | `"gemini-decision-1"` |
| `question` | 何を評価するか。1 と 10 が何を意味するかを記述します（デフォルト："Rate the technical quality of the image from 1 (worst) to 10 (best)."）。 | STRING | はい | 1～5000 文字 |
| `threshold` | スコアがこの値以上の場合、`result` は true になります。きれいでシャープな画像は約 7～8、ひどく損傷した画像は約 3～5 のスコアになります（デフォルト：6.0）。 | FLOAT | はい | 1.0～10.0（ステップ 0.1） |
| `images` | 評価する画像。拡張可能なスロット（`image_1` ... `image_16`）全体で最大 16 枚までです。バッチ化された画像は画像 1 枚につき 1 回としてカウントされます。 | IMAGE | いいえ | 最大 16 枚の画像 |
| `audio` | 評価するオーディオクリップ。 | AUDIO | いいえ | - |
| `video` | 評価する動画クリップ。 | VIDEO | いいえ | - |
| `text` | 質問の対象となるテキスト。プロンプトや LLM の応答などで、最大 20000 文字です。 | STRING | いいえ | 最大 20000 文字 |

`text`、`images`、`audio`、`video` のうち少なくとも 1 つを接続してください。評価対象がない場合、ノードはエラーを発生します。画像が複数ある場合は、質問内で `image_1`、`image_2` などの名前を付けてください。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `result` | スコアが `threshold` 以上の場合に true、それ以外の場合は false です。 | BOOLEAN |
| `score` | 1～10 の評価スコアです。 | FLOAT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/ja.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`
