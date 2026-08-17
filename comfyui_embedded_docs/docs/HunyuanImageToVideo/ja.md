# HunyuanImageToVideo

HunyuanImageToVideo ノードは、Hunyuan ビデオモデルを使用して画像をビデオ潜在表現に変換します。このノードは、条件付け入力とオプションの開始画像を受け取り、ビデオ生成モデルでさらに処理できるビデオ潜在変数を生成します。また、開始画像がビデオ生成プロセスに与える影響を制御するためのさまざまなガイダンスタイプをサポートしています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | ビデオ生成をガイドするためのポジティブ条件付け入力 | CONDITIONING | はい | - |
| `vae` | 画像を潜在空間にエンコードするために使用される VAE モデル | VAE | はい | - |
| `width` | 出力ビデオの幅（ピクセル単位）（デフォルト: 848、ステップ: 16） | INT | はい | 16 から MAX_RESOLUTION |
| `height` | 出力ビデオの高さ（ピクセル単位）（デフォルト: 480、ステップ: 16） | INT | はい | 16 から MAX_RESOLUTION |
| `length` | 出力ビデオのフレーム数（デフォルト: 53、ステップ: 4） | INT | はい | 1 から MAX_RESOLUTION |
| `batch_size` | 同時に生成するビデオの数（デフォルト: 1） | INT | はい | 1 から 4096 |
| `guidance_type` | 開始画像をビデオ生成に組み込む方法（デフォルト: "v1 (concat)"） | COMBO | はい | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `start_image` | ビデオ生成を初期化するためのオプションの開始画像 | IMAGE | いいえ | - |

**注:** `start_image` が指定された場合、ノードは選択された `guidance_type` に基づいて異なるガイダンスメソッドを使用します。

- "v1 (concat)": 画像潜在変数とビデオ潜在変数を連結し、画像をビデオにブレンドするためのマスクを適用します。
- "v2 (replace)": 初期ビデオフレームを画像潜在変数で置き換え、ノイズマスクを適用します。
- "custom": 画像をガイダンス用の参照潜在変数として使用します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | `start_image` が指定された場合に画像ガイダンスが適用された修正済みポジティブ条件付け | CONDITIONING |
| `latent` | ビデオ生成モデルによるさらなる処理の準備が整ったビデオ潜在表現 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`
