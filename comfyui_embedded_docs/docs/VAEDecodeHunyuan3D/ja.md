# VAEDecodeHunyuan3D

VAEDecodeHunyuan3D ノードは、VAEデコーダーを使用して潜在表現を3Dボクセルデータに変換します。設定可能なチャンク化と解像度設定を使用して潜在サンプルをVAEモデルに通し、3Dアプリケーションに適したボリュームデータを生成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `samples` | 3Dボクセルデータにデコードする潜在表現 | LATENT | はい | - |
| `vae` | 潜在サンプルのデコードに使用するVAEモデル | VAE | はい | - |
| `num_chunks` | メモリ管理のために処理を分割するチャンク数（デフォルト：8000） | INT | はい | 1000-500000 |
| `octree_resolution` | 3Dボクセル生成に使用するオクツリー構造の解像度（デフォルト：256） | INT | はい | 16-512 |

注：`num_chunks` と `octree_resolution` は上級者向けパラメータです。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `voxels` | デコードされた潜在表現から生成された3Dボクセルデータ | VOXEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/ja.md)

---
**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`
