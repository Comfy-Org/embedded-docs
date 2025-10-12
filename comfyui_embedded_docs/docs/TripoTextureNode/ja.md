> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/ja.md)

TripoTextureNodeは、Tripo APIを使用してテクスチャ付きの3Dモデルを生成します。モデルのタスクIDを受け取り、PBRマテリアル、テクスチャ品質設定、アライメント方法など様々なオプションを含むテクスチャ生成を適用します。このノードはTripo APIと通信してテクスチャ生成リクエストを処理し、結果のモデルファイルとタスクIDを返します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | はい | - | テクスチャを適用するモデルのタスクID |
| `texture` | BOOLEAN | いいえ | - | テクスチャを生成するかどうか（デフォルト: True） |
| `pbr` | BOOLEAN | いいえ | - | PBR（物理ベースレンダリング）マテリアルを生成するかどうか（デフォルト: True） |
| `texture_seed` | INT | いいえ | - | テクスチャ生成用のランダムシード（デフォルト: 42） |
| `texture_quality` | COMBO | いいえ | "standard"<br>"detailed" | テクスチャ生成の品質レベル（デフォルト: "standard"） |
| `texture_alignment` | COMBO | いいえ | "original_image"<br>"geometry" | テクスチャのアライメント方法（デフォルト: "original_image"） |

*注: このノードは認証トークンとAPIキーを必要としますが、これらはシステムによって自動的に処理されます。*

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model_file` | STRING | テクスチャが適用された生成済みモデルファイル |
| `model task_id` | MODEL_TASK_ID | テクスチャ生成プロセスを追跡するためのタスクID |
