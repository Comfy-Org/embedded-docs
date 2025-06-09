`チェックポイントを保存`ノードは、完全なStable Diffusionモデル（UNet、CLIP、VAEコンポーネントを含む）を**.safetensors**形式のチェックポイントファイルとして保存するために設計されています。

このノードは主にモデル結合ワークフローで使用されます。`ModelMergeSimple`や`ModelMergeBlocks`などのノードを通じて新しい結合モデルを作成した後、このノードを使用して結果を再利用可能なチェックポイントファイルとして保存できます。

## 入力パラメータ

| パラメータ名 | データ型 | 説明 |
|------------|---------|------|
| `モデル` | MODEL | 保存する主要なモデルを表します。将来の復元や分析のためにモデルの現在の状態をキャプチャするのに不可欠です。 |
| `clip` | CLIP | 主要なモデルに関連付けられたCLIPモデルのパラメータで、主要なモデルと一緒にその状態を保存できます。 |
| `vae` | VAE | 変分オートエンコーダー（VAE）モデルのパラメータで、主要なモデルとCLIPと一緒にその状態を将来の使用や分析のために保存できます。 |
| `ファイル名プレフィックス` | STRING | 保存するチェックポイントのファイル名プレフィックスを指定します。 |

さらに、このノードにはメタデータ用の2つの隠れた入力があります：

**prompt (PROMPT)**: ワークフローのプロンプト情報
**extra_pnginfo (EXTRA_PNGINFO)**: 追加のPNG情報

## 出力

このノードはチェックポイントファイルを出力し、対応する出力ファイルパスは`output/checkpoints/`ディレクトリです。

## アーキテクチャの互換性

- 現在完全にサポートされているもの：SDXL、SD3、SVDなどの主要なアーキテクチャ、[ソースコード](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)を参照
- 基本サポート：その他のアーキテクチャは保存可能ですが、標準化されたメタデータ情報なし

## 関連リンク

関連ソースコード：[nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)
