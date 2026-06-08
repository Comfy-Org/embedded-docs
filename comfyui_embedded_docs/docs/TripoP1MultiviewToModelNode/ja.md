以下が翻訳結果です。

## 概要

このノードは、オブジェクトまたはキャラクターの2～4枚の参照画像から3Dモデルを生成します。異なるアングル（正面、左、背面、右）からの画像を提供すると、ノードがGLB形式の3Dメッシュを作成します。正面図は必須であり、必要に応じて他の3つのビューを任意の組み合わせで追加することで、より良い結果を得ることができます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `image` | 正面図（0°）。必須です。 | IMAGE | はい | - |
| `image_left` | 左側面図（90°）、つまり被写体の左側です。 | IMAGE | いいえ | - |
| `image_back` | 背面図（180°）。 | IMAGE | いいえ | - |
| `image_right` | 右側面図（270°）、つまり被写体の右側です。 | IMAGE | いいえ | - |
| `output_mode` | 生成されるモデルの出力モードです。`"geometry"`は生のメッシュを生成し、`"textured"`は標準テクスチャを追加し、`"detailed"`は高精細なテクスチャ付きモデルを作成します（デフォルト: `"textured"`）。 | COMBO | はい | `"geometry"`<br>`"textured"`<br>`"detailed"` |
| `face_limit` | 出力メッシュの最大面数です。-1に設定すると制限なしになります（デフォルト: -1）。 | INT | いいえ | -1 ～ 100000 |
| `model_seed` | 再現可能なモデル生成のためのシード値です。0に設定するとランダムになります（デフォルト: 0）。 | INT | いいえ | 0 ～ 2147483647 |
| `auto_size` | モデルを標準的なバウンディングボックス内に収まるように自動的にサイズ調整します（デフォルト: False）。 | BOOLEAN | いいえ | True / False |
| `export_uv` | モデルとともにUV座標をエクスポートします（デフォルト: True）。 | BOOLEAN | いいえ | True / False |
| `compress_geometry` | ジオメトリデータを圧縮してファイルサイズを削減します（デフォルト: False）。 | BOOLEAN | いいえ | True / False |

**注記:** 少なくとも2枚の画像を提供する必要があります。正面図（`image`）に加えて、他のビュー（`image_left`、`image_back`、または`image_right`）のうち少なくとも1つが必要です。2枚未満の画像が提供された場合、ノードはエラーを発生させます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model_file` | 生成されたGLBモデルのファイル名です（後方互換性のため）。 | STRING |
| `model_task_id` | このモデル生成リクエストの一意のタスクIDです。 | MODEL_TASK_ID |
| `GLB` | GLB形式で生成された3Dモデルです。 | FILE3DGLB |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/ja.md)

---
**Source fingerprint (SHA-256):** `29bb87cdc5d3eef891a653c622e8876a37d6e6dc1a43e5c248b184060ead9029`
