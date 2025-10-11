> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/ja.md)

このノードは、オブジェクトの異なる視点を示す最大4枚の画像を処理し、TripoのAPIを使用して3Dモデルを同期的に生成します。前面画像と少なくとも1つの追加視点（左、背面、または右）が必要で、テクスチャとマテリアルのオプションを備えた完全な3Dモデルを作成します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | はい | - | オブジェクトの前面ビュー画像（必須） |
| `image_left` | IMAGE | いいえ | - | オブジェクトの左側面ビュー画像 |
| `image_back` | IMAGE | いいえ | - | オブジェクトの背面ビュー画像 |
| `image_right` | IMAGE | いいえ | - | オブジェクトの右側面ビュー画像 |
| `model_version` | COMBO | いいえ | 複数オプション利用可能 | 生成に使用するTripoモデルのバージョン |
| `orientation` | COMBO | いいえ | 複数オプション利用可能 | 3Dモデルの向き設定 |
| `texture` | BOOLEAN | いいえ | - | モデルにテクスチャを生成するかどうか（デフォルト: True） |
| `pbr` | BOOLEAN | いいえ | - | PBR（物理ベースレンダリング）マテリアルを生成するかどうか（デフォルト: True） |
| `model_seed` | INT | いいえ | - | モデル生成用の乱数シード（デフォルト: 42） |
| `texture_seed` | INT | いいえ | - | テクスチャ生成用の乱数シード（デフォルト: 42） |
| `texture_quality` | COMBO | いいえ | "standard"<br>"detailed" | テクスチャ生成の品質レベル（デフォルト: "standard"） |
| `texture_alignment` | COMBO | いいえ | "original_image"<br>"geometry" | モデルへのテクスチャ配置方法（デフォルト: "original_image"） |
| `face_limit` | INT | いいえ | -1 から 500000 | 生成モデルの最大面数、-1で制限なし（デフォルト: -1） |
| `quad` | BOOLEAN | いいえ | - | 三角形ではなく四角形ベースのジオメトリを生成するかどうか（デフォルト: False） |

**注意:** 前面画像（`image`）は常に必須です。マルチビュー処理には、少なくとも1つの追加視点画像（`image_left`、`image_back`、または`image_right`）を提供する必要があります。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成された3Dモデルのファイルパスまたは識別子 |
| `model task_id` | MODEL_TASK_ID | モデル生成プロセスを追跡するためのタスク識別子 |