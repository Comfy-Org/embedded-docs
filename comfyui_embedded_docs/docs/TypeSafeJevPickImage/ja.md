# TypeSafe Jev (Pick Image)

TypeSafe Jev (Pick Image) ノードは、バッチの中から 1 枚の画像を選択します。同じ画像バッチを `index` と一緒に Get Image from Batch に接続すると、選択された画像を保持できます。また、`confidence` を読み取ることで、選択が十分な品質かどうかを判断できます。これは API ノードです。Comfy のサーバー上で実行され、クレジット付きの Comfy.org アカウントが必要です。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | 使用する Jev モデル。現在利用できるモデルは 1 つのみです：`jev-1.14.0`。 | COMBO | はい | `"jev-1.14.0"` |
| `question` | どの画像を選択するか。プロンプトを `text` に接続すると、それに最も一致する画像を選択します（デフォルト：`Which image best matches the prompt in text? If there is no text, which image has the best quality?`）。 | STRING | はい | 1～1000 文字 |
| `images` | 選択対象となる画像。バッチ入力は画像ごとに 1 回カウントされるため、バッチ内のすべての画像が候補になります。すべての画像の長辺は、アップロード前のバッチサイズに応じて制限されます。最大 4 枚までは 1568 px、最大 8 枚までは 1024 px、最大 16 枚までは 768 px、最大 32 枚までは 512 px となるため、バッチが大きくなるほど各画像のディテールが低下する可能性があります。 | IMAGE | はい | 2～32 枚の画像 |
| `text` | question の対象となるテキスト。たとえば、画像の生成元となったプロンプトなどです。 | STRING | いいえ | 0～3000 文字 |

**注記：**

- 接続された画像が 2 枚未満、または 32 枚を超える場合、ノードはエラーを発生させます。
- `index` は 0 からカウントされ、これは Get Image from Batch が想定する位置です。
- 課金はトークンベースです。ノード上の価格バッジには、100 万トークンあたりのおおよその料金が表示されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `index` | バッチ内で選択された画像の位置（0 から始まります）。 | INT |
| `confidence` | Jev がどれだけ確信しているかを示す値で、0（明確な勝者なし）から 1（確実）までの範囲です。 | FLOAT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/ja.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
