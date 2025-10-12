> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/ja.md)

TripoConversionNodeは、Tripo APIを使用して3Dモデルを異なるファイル形式間で変換します。前回のTripo操作で得られたタスクIDを受け取り、様々なエクスポートオプションを使用して結果のモデルを希望の形式に変換します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | はい | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | 前回のTripo操作（モデル生成、リギング、またはリターゲティング）からのタスクID |
| `format` | COMBO | はい | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | 変換後の3Dモデルのターゲットファイル形式 |
| `quad` | BOOLEAN | いいえ | True/False | 三角形を四角形に変換するかどうか（デフォルト: False） |
| `face_limit` | INT | いいえ | -1 から 500000 | 出力モデルの最大面数、-1で制限なし（デフォルト: -1） |
| `texture_size` | INT | いいえ | 128 から 4096 | 出力テクスチャのサイズ（ピクセル単位）（デフォルト: 4096） |
| `texture_format` | COMBO | いいえ | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | エクスポートするテクスチャの形式（デフォルト: JPEG） |

**注意:** `original_model_task_id`は、前回のTripo操作（モデル生成、リギング、またはリターゲティング）からの有効なタスクIDである必要があります。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| *名前付き出力なし* | - | このノードは変換を非同期で処理し、結果はTripo APIシステムを通じて返されます |
