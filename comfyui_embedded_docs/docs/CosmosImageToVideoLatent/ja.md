# CosmosImageToVideoLatent

CosmosImageToVideoLatent ノードは、画像から動画への生成用の動画潜在変数を作成します。このノードは空の潜在変数から始まり、必要に応じて開始画像や終了画像を動画シーケンスの最初または最後のフレームにエンコードできます。画像が提供された場合、生成中にエンコードされたフレームを固定としてマークするノイズマスクも生成されます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `vae` | 入力画像を潜在空間にエンコードするために使用される VAE モデル | VAE | Yes | - |
| `width` | 出力動画の幅（ピクセル単位）（デフォルト：1280） | INT | Yes | 16 to MAX_RESOLUTION (step 16) |
| `height` | 出力動画の高さ（ピクセル単位）（デフォルト：704） | INT | Yes | 16 to MAX_RESOLUTION (step 16) |
| `length` | 動画シーケンス内のフレーム数（デフォルト：121） | INT | Yes | 1 to MAX_RESOLUTION (step 8) |
| `batch_size` | 出力バッチで生成される動画潜在変数の数（デフォルト：1） | INT | Yes | 1 to 4096 |
| `start_image` | 動画シーケンスの先頭にエンコードする任意の画像または画像シーケンス | IMAGE | No | - |
| `end_image` | 動画シーケンスの末尾にエンコードする任意の画像または画像シーケンス | IMAGE | No | - |

**注記：** `start_image` と `end_image` のどちらも指定されない場合、ノードはノイズマスクなしの空の潜在変数を返します。少なくとも1つの画像が指定された場合、`noise_mask` が含まれます。指定された画像からエンコードされた潜在フレームのマスク値は 0（固定）となり、残りのフレームのマスク値は 1（生成対象）となります。画像はエンコード前に指定された `width` と `height` にリサイズされ、入力画像から取得されるフレーム数は、そのバッチ次元に等しく、最大で `length` です。潜在変数は16チャンネル、空間次元は `width / 8` と `height / 8`、フレーム数は `((length - 1) // 8) + 1` です。画像が指定された場合、潜在変数とそのノイズマスクは `batch_size` 回繰り返されて出力バッチを形成します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `latent` | 動画潜在変数 `samples` を含む LATENT。`start_image` または `end_image` が指定された場合、エンコードされたフレームを固定としてマークする `noise_mask` も含みます。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/ja.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
