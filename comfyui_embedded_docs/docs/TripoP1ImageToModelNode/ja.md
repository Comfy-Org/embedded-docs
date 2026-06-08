以下が翻訳結果です。

## 概要

このノードは、Tripo P1 APIを使用して、1枚の2D画像を3Dモデルに変換します。低ポリゴンでゲームにすぐに使用できるメッシュの生成に最適化されています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `image` | 3Dモデルに変換する入力画像です。 | IMAGE | はい | - |
| `output_mode` | 出力モードと品質設定を指定する辞書です。このパラメータは、生成されるモデルの種類とテクスチャ品質を制御します。利用可能なオプションは、`_build_p1_output_mode` ヘルパー関数によって定義され、`texture_quality`（例："standard"、"high"、"ultra"）や `image_alignment` の設定が含まれます。 | DICT | はい | 説明を参照 |
| `enable_image_autofix` | 生成品質を向上させるため、入力画像を前処理します。（デフォルト：False） | BOOLEAN | いいえ | True<br>False |
| `face_limit` | 生成されるメッシュの面の数を制限します。-1 を指定すると制限なしになります。（デフォルト：-1） | INT | いいえ | - |
| `model_seed` | 再現可能なモデル生成のためのシード値です。指定しない場合はランダムなシードが使用されます。（デフォルト：None） | INT | いいえ | - |
| `auto_size` | 生成されるモデルの最適なサイズを自動的に決定します。（デフォルト：False） | BOOLEAN | いいえ | True<br>False |
| `export_uv` | モデルとともにUV座標をエクスポートします。（デフォルト：True） | BOOLEAN | いいえ | True<br>False |
| `compress_geometry` | ジオメトリデータを圧縮してファイルサイズを削減します。（デフォルト：False） | BOOLEAN | いいえ | True<br>False |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model_file` | 生成された3Dモデルのファイルパスです。この出力は後方互換性のためにのみ提供されています。 | STRING |
| `model task_id` | モデル生成リクエストの一意のタスクIDです。 | MODEL_TASK_ID |
| `GLB` | GLB形式で生成された3Dモデルです。 | FILE3DGLB |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/ja.md)

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
