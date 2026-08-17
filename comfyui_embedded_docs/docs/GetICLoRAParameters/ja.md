# IC-LoRAパラメータの取得

## 概要

このノードは、LoRA 読み込み済みモデルのメタデータから IC-LoRA パラメータを抽出します。safetensors のメタデータを読み取り、参照ダウンスケール係数などの値を取得し、構造化されたパラメータオブジェクトとして出力します。このオブジェクトは、特別なガイド処理が必要な場合に `LTXVAddGuide` ノードへ接続できます。メタデータが存在しない場合や参照ダウンスケール係数を読み取れない場合は、値は 1 にデフォルト設定されます。値が見つかった場合は、丸められたうえで最小値 1 にクランプされます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `iclora_model` | メタデータを抽出する対象の特定の IC-LoRA について、LoRA Loader から直接出力されたもの。 | MODEL | はい | N/A |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `iclora_parameters` | LoRA メタデータから抽出された IC-LoRA パラメータ（例：`reference_downscale_factor`）。LoRA がガイドの特別な処理を必要とする場合は、`LTXVAddGuide` に接続します。 | IC_LORA_PARAMETERS |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/ja.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
