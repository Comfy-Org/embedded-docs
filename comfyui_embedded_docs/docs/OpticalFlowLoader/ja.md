> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/ja.md)

## 概要

`models/optical_flow/` フォルダからオプティカルフローモデルを読み込みます。現在は、VOIDWarpedNoise ノードで使用されている torchvision の RAFT-large 形式のみをサポートしています。ComfyUI はオプティカルフローの重みを自動的にダウンロードしません。チェックポイントファイルを手動で `models/optical_flow/` ディレクトリに配置する必要があります。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|----------|------|-------|------|
| `model_name` | STRING | はい | `models/optical_flow/` フォルダ内のファイル一覧 | 読み込むオプティカルフローモデル。ファイルは `optical_flow` フォルダに配置する必要があります。現在は torchvision の `raft_large.pth` のみをサポートしています。 |

## 出力

| 出力名 | データ型 | 説明 |
|---------|----------|------|
| `OPTICAL_FLOW` | MODEL | 読み込まれたオプティカルフローモデル。他のノードで使用するために ModelPatcher でラップされています。 |