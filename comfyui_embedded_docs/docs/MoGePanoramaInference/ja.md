# MoGeパノラマ推論

このノードは、正距円筒図法のパノラマ画像に対して深度推定を実行します。パノラマを12個の透視ビューに分割し、各ビューでMoGe深度推定モデルを実行してから、結果を元のパノラマに対する単一の完全な深度マップにマージします。

## 入力

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `moge_model` | 推論に使用するMoGeモデル。 | MOGE_MODEL | Yes |  |
| `image` | 正距円筒図法のパノラマ画像（任意のアスペクト比）。単一画像のみ受け付けます。 | IMAGE | Yes |  |
| `resolution_level` | ビューごとの詳細度（0 = 最速、9 = 最も詳細）。デフォルト: 9。 | INT | Yes | 0 to 9 |
| `split_resolution` | 各透視分割の解像度。デフォルト: 512。 | INT | Yes | 256 to 1024 |
| `merge_resolution` | マージされた正距円筒距離マップの長辺の解像度。デフォルト: 1920。 | INT | Yes | 256 to 8192 |
| `batch_size` | 推論バッチあたりのビュー数（合計12分割）。デフォルト: 4。 | INT | Yes | 1 to 12 |

注: このノードは単一画像のみ受け付けます。画像のバッチを渡すとエラーが発生します。パノラマは常に12個の透視ビューに分割されます。`batch_size` は、そのうち何ビューを推論バッチごとに処理するかを制御するだけです。

## 出力

| Output Name | Description | Data Type |
| --- | --- | --- |
| `moge_geometry` | 推定されたジオメトリを含む辞書: `points`（3Dポイントクラウド）、`depth`（深度マップ）、`mask`（有効領域マスク）、`image`（入力画像）。 | MOGE_GEOMETRY |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/ja.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
