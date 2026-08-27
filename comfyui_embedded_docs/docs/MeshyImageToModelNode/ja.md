# Meshy：画像からモデルへ

Meshy: Image to Model ノードは、Meshy API を使用して単一の入力画像から 3D モデルを生成します。画像をアップロードし、処理タスクを送信して、生成された 3D モデルファイル（GLB および FBX）を参照用のタスク ID とともに返します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | 生成に使用する AI モデルのバージョンを指定します。 | COMBO | はい | `"latest"` |
| `image` | 3D モデルに変換する入力画像です。 | IMAGE | はい | - |
| `should_remesh` | `"false"` に設定すると、未処理の三角形メッシュを返します。 | DYNAMIC_COMBO | はい | `"true"`<br>`"false"` |
| `topology` | リメッシュされたモデルの目標ポリゴントポロジーです。この入力は、`should_remesh` が `"true"` に設定されている場合にのみ使用できます。 | COMBO | いいえ* | `"triangle"`<br>`"quad"` |
| `target_polycount` | リメッシュされたモデルの目標ポリゴン数です。この入力は、`should_remesh` が `"true"` に設定されている場合にのみ使用できます。デフォルト: 300000。 | INT | いいえ* | 100 - 300000 |
| `symmetry_mode` | 生成された 3D モデルに適用する対称性を制御します。 | COMBO | はい | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | テクスチャを生成するかどうかを決定します。`"false"` に設定すると、テクスチャフェーズをスキップして、テクスチャのないメッシュを返します。 | DYNAMIC_COMBO | はい | `"true"`<br>`"false"` |
| `enable_pbr` | ベースカラーに加えて PBR マップ（メタリック、ラフネス、ノーマル）を生成します。この入力は、`should_texture` が `"true"` に設定されている場合にのみ使用できます。デフォルト: `False`。 | BOOLEAN | いいえ* | - |
| `texture_prompt` | テクスチャ処理をガイドするためのテキストプロンプトを指定します。最大 600 文字です。`texture_image` と同時に使用することはできません。この入力は、`should_texture` が `"true"` に設定されている場合にのみ使用できます。デフォルト: 空文字列。 | STRING | いいえ* | - |
| `texture_image` | `texture_image` と `texture_prompt` は、同時に使用できるのはいずれか一方のみです。この入力は、`should_texture` が `"true"` に設定されている場合にのみ使用できます。 | IMAGE | いいえ* | - |
| `pose_mode` | 生成されたモデルのポーズモードを指定します。これは上級者向けのパラメータです。 | COMBO | はい | `""`（空）<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | シードはノードを再実行するかどうかを制御します。結果はシードに関係なく非決定論的です。デフォルト: 0。 | INT | はい | 0 - 2147483647 |

**パラメータ制約に関する注意事項：**

* `topology` および `target_polycount` の入力は、`should_remesh` が `"true"` に設定されている場合にのみ使用できます。
* `enable_pbr`、`texture_prompt`、`texture_image` の入力は、`should_texture` が `"true"` に設定されている場合にのみ使用できます。
* `should_texture` が `"true"` に設定されている場合、`texture_prompt` と `texture_image` を同時に使用することはできません。両方指定すると、ノードはエラーを発生させます。
* `texture_prompt` の最大長は 600 文字です。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model_file` | 生成された GLB モデルのファイル名です。後方互換性のためだけに維持されています。 | STRING |
| `meshy_task_id` | Meshy API タスクの一意の識別子です。参照やトラブルシューティングに使用できます。 | MESHY_TASK_ID |
| `GLB` | GLB ファイル形式で生成された 3D モデルです。 | FILE3DGLB |
| `FBX` | FBX ファイル形式で生成された 3D モデルです。 | FILE3DFBX |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/ja.md)

---
**Source fingerprint (SHA-256):** `9f7abcb0db3c78715e4ba7370efe294caf186590f7ab62da8568778848fc838c`
