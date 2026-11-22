# TypeSafe Jev (Pick Image)

TypeSafe Jev（Pick Image）ノードは、バッチから 1 枚の画像を選択します。選択した画像を保持するには `index` を Get Image from Batch に接続するか、`confidence` を読み取って選択が十分に良好かどうかを判断します。これは API ノードであり、Comfy.org アカウントと API キーが必要です。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | 使用する Jev モデルです。現在利用可能なモデルは 1 つだけです: `jev-1.14.0`。 | COMBO | はい | `"jev-1.14.0"` |
| `question` | どの画像を選択するかです。プロンプトを `text` に接続すると、最も一致する画像を選択します（デフォルト: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`）。 | STRING | はい | 1～1000 文字 |
| `images` | 選択候補となる画像です。バッチ入力は画像ごとに 1 回としてカウントされるため、バッチ内のすべての画像が候補になります。 | IMAGE | はい | 2～32 枚の画像 |
| `text` | 質問の対象となるテキストです。たとえば、画像の生成に使用したプロンプトなどです。 | STRING | いいえ | 0～3000 文字 |

**注意:**

- 接続された画像が 2 枚未満または 32 枚超の場合、ノードはエラーを発生します。
- `index` は 0 から数えます。これは Get Image from Batch が期待する位置です。
- 課金はトークンベースです。ノード上の料金バッジには、100 万トークンあたりのおおよその料金が表示されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `index` | バッチ内で選択された画像の位置です。0 から始まります。 | INT |
| `confidence` | Jev の確信度です。0（明確な勝者なし）から 1（確実）までです。 | FLOAT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/ja.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
