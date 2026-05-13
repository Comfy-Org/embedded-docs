> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/ja.md)

以下が翻訳結果です。

TripoConversionNode は、Tripo API を使用して 3D モデルを異なるファイル形式に変換します。以前の Tripo 操作（モデル生成、リギング、またはリターゲティング）のタスク ID を受け取り、様々なエクスポートオプションを使用して結果のモデルを目的の形式に変換します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | はい | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | 以前の Tripo 操作（モデル生成、リギング、またはリターゲティング）のタスク ID |
| `format` | COMBO | はい | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | 変換後の 3D モデルのターゲットファイル形式 |
| `quad` | BOOLEAN | いいえ | True/False | 三角形を四角形に変換するかどうか（デフォルト：False） |
| `face_limit` | INT | いいえ | -1 ～ 2000000 | 出力モデルの最大面数。-1 は制限なし（デフォルト：-1） |
| `texture_size` | INT | いいえ | 128 ～ 4096 | 出力テクスチャのサイズ（ピクセル単位）（デフォルト：4096） |
| `texture_format` | COMBO | いいえ | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | エクスポートするテクスチャの形式（デフォルト：JPEG） |
| `force_symmetry` | BOOLEAN | いいえ | True/False | モデルに強制的に対称性を適用するかどうか（デフォルト：False） |
| `flatten_bottom` | BOOLEAN | いいえ | True/False | モデルの底面を平坦化するかどうか（デフォルト：False） |
| `flatten_bottom_threshold` | FLOAT | いいえ | 0.0 ～ 1.0 | 底面平坦化のしきい値（デフォルト：0.0） |
| `pivot_to_center_bottom` | BOOLEAN | いいえ | True/False | ピボットポイントをモデルの底面中央に移動するかどうか（デフォルト：False） |
| `scale_factor` | FLOAT | いいえ | 0.0 以上 | モデルに適用するスケール係数（デフォルト：1.0） |
| `with_animation` | BOOLEAN | いいえ | True/False | エクスポートにアニメーションデータを含めるかどうか（デフォルト：False） |
| `pack_uv` | BOOLEAN | いいえ | True/False | UV 座標をパックするかどうか（デフォルト：False） |
| `bake` | BOOLEAN | いいえ | True/False | テクスチャをベイクするかどうか（デフォルト：False） |
| `part_names` | STRING | いいえ | カンマ区切りのリスト | エクスポートに含めるパーツ名のカンマ区切りリスト（デフォルト：""） |
| `fbx_preset` | COMBO | いいえ | blender<br>mixamo<br>3dsmax | 使用する FBX エクスポートプリセット（デフォルト：blender） |
| `export_vertex_colors` | BOOLEAN | いいえ | True/False | 頂点カラーをエクスポートするかどうか（デフォルト：False） |
| `export_orientation` | COMBO | いいえ | align_image<br>default | エクスポートの向きモード（デフォルト：default） |
| `animate_in_place` | BOOLEAN | いいえ | True/False | モデルをその場でアニメーションさせるかどうか（デフォルト：False） |

**注意：** `original_model_task_id` は、以前の Tripo 操作（モデル生成、リギング、またはリターゲティング）の有効なタスク ID である必要があります。「詳細」とマークされたパラメータはオプションであり、特定のエクスポート要件がある場合にのみ設定する必要があります。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| *名前付き出力なし* | - | このノードは変換を非同期で処理し、Tripo API システムを通じて結果を返します |

---
**Source fingerprint (SHA-256):** `b11ecab98701b7153a350f5e4980ddc2f446c0a12be3402ca98a5e6de60bd7ce`
