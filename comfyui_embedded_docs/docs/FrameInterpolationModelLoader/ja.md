# フレーム補間モデルを読み込む

## 概要

このノードは、フレーム補間モデルをファイルから読み込み、ワークフローで使用できるように準備します。モデルタイプ（FILM または RIFE）を自動的に検出し、お使いのハードウェアで最適なパフォーマンスが得られるようにモデルを構成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model_name` | 読み込むフレーム補間モデルを選択します。モデルは `frame_interpolation` フォルダに配置する必要があります。 | COMBO | Yes | `frame_interpolation` フォルダ内のモデルファイルのリスト |

注：選択したファイルが認識可能な FILM または RIFE フレーム補間モデルでない場合、ノードはエラーを発生させます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | 読み込まれ、構成されたフレーム補間モデルです。他のノードで使用する準備ができています。 | INTERP_MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/ja.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
