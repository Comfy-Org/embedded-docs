# オプティカルフローモデルの読み込み

## 概要

`models/optical_flow/` フォルダからオプティカルフローモデルを読み込みます。現在、サポートされているのは torchvision の RAFT-large 形式のみで、これは VOIDWarpedNoise ノードで使用されるモデルです。ComfyUI はオプティカルフローの重みを自動的にダウンロードしません。チェックポイントファイルを手動で `models/optical_flow/` ディレクトリに配置する必要があります。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model_name` | 読み込むオプティカルフローモデル。ファイルは `optical_flow` フォルダに配置する必要があります。現在、torchvision の `raft_large.pth` のみがサポートされています。 | COMBO | はい | `models/optical_flow/` フォルダ内のファイル一覧 |

選択されたファイルは torchvision の RAFT-large チェックポイントである必要があります。このノードは、ファイルに期待される RAFT キー（`feature_encoder.*`、`context_encoder.*`、`update_block.*`）が含まれているかを確認し、形式が認識されない場合は ValueError を発生させます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `OPTICAL_FLOW` | 読み込まれたオプティカルフローモデル。他のノードで使用できるよう ModelPatcher にラップされています。 | OPTICAL_FLOW |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/ja.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
