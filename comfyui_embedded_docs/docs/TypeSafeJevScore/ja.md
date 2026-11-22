# TypeSafe Jev (Score)

TypeSafe Jev (Score) ノードは、接続されたテキスト、画像、またはその両方を 1～10 で評価し、その評価をしきい値と比較します。`result` を If/Else Switch ノードに接続してスコアに基づいて処理するか、`score` を読み取って生の評価値を使用できます。これは API ノードであり、Comfy.org アカウントと API キーが必要です。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | 使用する Jev モデルです。現在利用できるモデルは `jev-1.14.0` のみです。 | COMBO | はい | `"jev-1.14.0"` |
| `question` | 1～10 の尺度で何を評価するかを指定します。デフォルト（`Rate the technical quality of the image from 1 (worst) to 10 (best).`）のように、1 と 10 が何を意味するかを記述してください。 | STRING | はい | 1～1000 文字 |
| `threshold` | スコアがこの値以上の場合に `result` が true になります（デフォルト: 5.0）。 | FLOAT | はい | 1.0～10.0（ステップ 0.1） |
| `images` | 質問の対象となる画像です。合計で最大 32 枚の画像を指定できます。バッチ入力は画像ごとに 1 枚としてカウントされ、4 枚を超える画像はより小さいサイズで送信されます。 | AUTOGROW | いいえ | 0～32 枚の画像 |
| `text` | 質問の対象となるテキストです。プロンプトや LLM の応答などが該当します。 | STRING | いいえ | 0～3000 文字 |

**注記：**

- テキストまたは少なくとも 1 枚の画像を接続してください。両方が空の場合、ノードはエラーを発生させます。
- スコアは 1～10 で報告され、スコアが `threshold` 以上の場合に `result` が true になります。
- 課金はトークンベースです。ノード上の価格バッジには、100 万トークンあたりの概算レートが表示されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `result` | `score` が `threshold` 以上の場合に true になります。 | BOOLEAN |
| `score` | 1（最低）から 10（最高）までの評価です。 | FLOAT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/ja.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
