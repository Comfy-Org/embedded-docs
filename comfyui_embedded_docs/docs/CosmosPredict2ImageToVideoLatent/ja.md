# CosmosPredict2ImageToVideoLatent

CosmosPredict2ImageToVideoLatent ノードは、動画生成用に、画像から動画の潜在表現を作成します。空白の動画潜在表現を生成したり、開始画像と終了画像を組み込んで、指定した寸法と長さの動画シーケンスを作成することができます。このノードは、動画処理に適した潜在空間フォーマットへの画像のエンコードを処理します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `vae` | 画像を潜在空間にエンコードするために使用される VAE モデル | VAE | はい | - |
| `width` | 出力動画の幅（ピクセル単位）（デフォルト: 848、16 で割り切れる必要があります） | INT | はい | 16 〜 MAX_RESOLUTION（ステップ 16） |
| `height` | 出力動画の高さ（ピクセル単位）（デフォルト: 480、16 で割り切れる必要があります） | INT | はい | 16 〜 MAX_RESOLUTION（ステップ 16） |
| `length` | 動画シーケンスのフレーム数（デフォルト: 93） | INT | はい | 1 〜 MAX_RESOLUTION（ステップ 4） |
| `batch_size` | 生成する動画シーケンスの数（デフォルト: 1） | INT | はい | 1 〜 4096 |
| `start_image` | 動画シーケンスの開始画像（オプション） | IMAGE | いいえ | - |
| `end_image` | 動画シーケンスの終了画像（オプション） | IMAGE | いいえ | - |

**注記:** `start_image` と `end_image` の両方が指定されていない場合、ノードは空白の動画潜在表現を生成します。画像が指定された場合、それらの画像はエンコードされ、適切なマスキングとともに動画シーケンスの先頭および/または末尾に配置されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `samples` | エンコードされた動画シーケンスを含む、生成された動画の潜在表現 | LATENT |
| `noise_mask` | 生成中に潜在表現のどの部分を保持すべきかを示すマスク | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/ja.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
