> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/ja.md)

TripoのAPIを使用して、単一の画像に基づいて3Dモデルを同期的に生成します。このノードは入力画像を受け取り、テクスチャ、品質、モデルプロパティに関する様々なカスタマイズオプションを使用して3Dモデルに変換します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | はい | - | 3Dモデルの生成に使用する入力画像 |
| `model_version` | COMBO | いいえ | 複数のオプションが利用可能 | 生成に使用するTripoモデルのバージョン |
| `style` | COMBO | いいえ | 複数のオプションが利用可能 | 生成されるモデルのスタイル設定（デフォルト: "None"） |
| `texture` | BOOLEAN | いいえ | - | モデルにテクスチャを生成するかどうか（デフォルト: True） |
| `pbr` | BOOLEAN | いいえ | - | 物理ベースレンダリングを使用するかどうか（デフォルト: True） |
| `model_seed` | INT | いいえ | - | モデル生成用の乱数シード（デフォルト: 42） |
| `orientation` | COMBO | いいえ | 複数のオプションが利用可能 | 生成されるモデルの向き設定 |
| `texture_seed` | INT | いいえ | - | テクスチャ生成用の乱数シード（デフォルト: 42） |
| `texture_quality` | COMBO | いいえ | "standard"<br>"detailed" | テクスチャ生成の品質レベル（デフォルト: "standard"） |
| `texture_alignment` | COMBO | いいえ | "original_image"<br>"geometry" | テクスチャマッピングの配置方法（デフォルト: "original_image"） |
| `face_limit` | INT | いいえ | -1 から 500000 | 生成されるモデルの最大面数、-1は制限なし（デフォルト: -1） |
| `quad` | BOOLEAN | いいえ | - | 三角形の代わりに四角形の面を使用するかどうか（デフォルト: False） |

**注意:** `image`パラメータは必須であり、ノードが機能するために提供する必要があります。画像が提供されない場合、ノードはRuntimeErrorを発生させます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成された3Dモデルファイル |
| `model task_id` | MODEL_TASK_ID | モデル生成プロセスを追跡するためのタスクID |
