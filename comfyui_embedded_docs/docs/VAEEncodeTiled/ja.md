# VAEエンコード（タイル）

VAEEncodeTiled ノードは、画像を小さなタイルに分割し、Variational Autoencoder（VAE）を使用してエンコードすることで画像を処理します。このタイル方式により、メモリ制限を超える可能性のある大きな画像を扱うことができます。このノードは画像用と動画用の両方のVAEをサポートしており、空間次元と時間次元にそれぞれタイル制御を備えています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `pixels` | エンコードする入力画像データです | IMAGE | はい | - |
| `vae` | エンコードに使用するVariational Autoencoder（VAE）モデルです | VAE | はい | - |
| `tile_size` | 空間処理の各タイルのサイズです（デフォルト: 512） | INT | はい | 64-4096 (step: 64) |
| `overlap` | 隣接するタイル間のオーバーラップ量です（デフォルト: 64） | INT | はい | 0-4096 (step: 32) |
| `temporal_size` | 動画用VAEでのみ使用されます。一度にエンコードするフレーム数です（デフォルト: 64） | INT | はい | 8-4096 (step: 4) |
| `temporal_overlap` | 動画用VAEでのみ使用されます。オーバーラップするフレーム数です（デフォルト: 8） | INT | はい | 4-4096 (step: 4) |

**注記:** `temporal_size` と `temporal_overlap` のパラメータは、動画用VAEを使用する場合にのみ関連し、標準の画像用VAEには影響しません。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `LATENT` | 入力画像のエンコードされた潜在表現です | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/ja.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
