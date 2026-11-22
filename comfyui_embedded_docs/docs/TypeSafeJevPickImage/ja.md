# TypeSafe Jev (Pick Image)

TypeSafe Jev (Pick Image) ノードは、バッチから 1 枚の画像を選択します。選択した画像を保持するには、同じ画像バッチを `index` とともに Get Image from Batch に接続するか、選択が十分に良いかどうかを判断するために `confidence` を読み取ります。これは API ノードです。Comfy のサーバー上で実行され、クレジット付きの Comfy.org アカウントが必要です。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | 使用する Jev モデルです。現在利用可能なモデルは 1 つだけです: `jev-1.14.0`。 | COMBO | はい | `"jev-1.14.0"` |
| `question` | どの画像を選択するかです。`text` にプロンプトを接続すると、それに最も一致する画像を選択します（デフォルト: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`）。 | STRING | はい | 1～1000 文字 |
| `images` | 選択対象の画像です。バッチ化された入力は画像ごとに 1 回として数えられるため、バッチ内のすべての画像が候補になります。アップロード前に、各画像の長辺はバッチサイズに応じて上限が設定されます。最大 4 枚の場合は 1568 px、最大 8 枚の場合は 1024 px、最大 16 枚の場合は 768 px、最大 32 枚の場合は 512 px です。そのため、バッチが大きいほど各画像の詳細は少なくなります。 | IMAGE | はい | 2～32 枚の画像 |
| `text` | `question` が対象とするテキストです。たとえば、画像の生成元となったプロンプトなどです。 | STRING | いいえ | 0～3000 文字 |

**注意:**

- 接続された画像が 2 枚未満、または 32 枚を超える場合、ノードはエラーを発生します。
- `index` は 0 から数えます。これは Get Image from Batch が想定する位置です。
- 課金はトークン単位です。ノード上の価格バッジには、100 万トークンあたりの概算レートが表示されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `index` | バッチ内で選択された画像の位置です。0 から始まります。 | INT |
| `confidence` | Jev がどれだけ確信しているかです。0（明確な勝者なし）から 1（確実）までの値です。 | FLOAT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/ja.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
