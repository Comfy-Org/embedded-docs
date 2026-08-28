# Meshy：複数画像からモデルへ

このノードは、Meshy API を使用して複数の入力画像から 3D モデルを生成します。提供された画像をアップロードし、処理タスクを送信して、生成された 3D モデルファイル（GLB および FBX）と、参照用のタスク ID を返します。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | 使用する AI モデルのバージョンを指定します。 | COMBO | はい | `"latest"` |
| `should_remesh` | 生成されたメッシュを処理するかどうかを指定します。`"false"` に設定すると、未処理の三角形メッシュが返されます。`"true"` に設定すると、以下のリメッシュ設定が表示されます。 | DYNAMIC_COMBO | はい | `"true"`<br>`"false"` |
| `symmetry_mode` | 生成されたモデルに対称性を適用するかどうかを制御します。 | COMBO | はい | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | テクスチャを生成するかどうかを指定します。`"false"` に設定すると、テクスチャフェーズをスキップし、テクスチャなしのメッシュが返されます。`"true"` に設定すると、以下のテクスチャ設定が表示されます。 | DYNAMIC_COMBO | はい | `"true"`<br>`"false"` |
| `pose_mode` | 生成されたモデルのポーズモードを指定します。 | COMBO | はい | `""` (empty)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | シードはノードを再実行するかどうかを制御します。シードに関係なく、結果は非決定的です。（デフォルト: 0） | INT | はい | 0〜2147483647 |

### リメッシュ設定（`should_remesh` が `"true"` に設定されている場合に表示）

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `topology` | リメッシュ出力のターゲットとなるポリゴンタイプ。 | COMBO | いいえ | `"triangle"`<br>`"quad"` |
| `target_polycount` | リメッシュモデルのターゲットポリゴン数（デフォルト: 300000）。 | INT | いいえ | 100〜300000 |

### テクスチャ設定（`should_texture` が `"true"` に設定されている場合に表示）

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `enable_pbr` | ベースカラーに加えて PBR マップ（メタリック、ラフネス、ノーマル）を生成します。（デフォルト: False） | BOOLEAN | いいえ | True / False |
| `texture_prompt` | テクスチャ処理をガイドするテキストプロンプトを指定します。最大 600 文字です。`texture_image` とは同時に使用できません。（デフォルト: 空） | STRING | いいえ | - |
| `texture_image` | `texture_image` と `texture_prompt` は、同時に使用できるのはどちらか一方のみです。 | IMAGE | いいえ | - |

### 画像入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `images` | 拡張可能スロット: 2～4 枚の入力画像（`image_1`、`image_2`、`image_3`、`image_4`）を接続します。これらの画像は 3D モデルの生成に使用されます。 | IMAGE | はい | 2〜4 images |

**注記**

* `images` 入力には 2～4 枚の画像を指定する必要があります。
* `topology` と `target_polycount` パラメータは、`should_remesh` が `"true"` に設定されている場合にのみ有効です。
* `enable_pbr`、`texture_prompt`、`texture_image` パラメータは、`should_texture` が `"true"` に設定されている場合にのみ有効です。
* `texture_prompt` と `texture_image` は相互に排他的です。両方を同時に使用することはできません。`texture_prompt` は 600 文字以内です。
* `seed` の値は結果を決定的にするものではありません。値を変更すると、単にノードが生成タスクを再実行するだけです。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model_file` | 生成された GLB モデルのファイル名です。この出力は後方互換性のためだけに提供されます。 | STRING |
| `meshy_task_id` | Meshy API タスクの一意の識別子です。 | MESHY_TASK_ID |
| `GLB` | GLB 形式で生成された 3D モデルです。 | FILE3DGLB |
| `FBX` | FBX 形式で生成された 3D モデルです。 | FILE3DFBX |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/ja.md)

---
**Source fingerprint (SHA-256):** `c2282cad611bbbc8c0a618df6a68fcd9f6e3c29c6d08b2c96a117c29765d8a7a`
