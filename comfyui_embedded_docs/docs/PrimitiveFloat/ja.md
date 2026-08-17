# 浮動小数点数

PrimitiveFloat ノードは、ワークフローで使用できる浮動小数点数値を作成します。単一の数値入力を受け取り、その同じ値を出力することで、ComfyUI パイプライン内の異なるノード間で浮動小数点数値を定義して渡すことができます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `value` | 出力する浮動小数点数値（デフォルト: 0.0） | FLOAT | はい | -sys.maxsize to sys.maxsize (step: 0.1) |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `output` | 入力された浮動小数点数値 | FLOAT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/ja.md)

---
**Source fingerprint (SHA-256):** `df57e5900e972e17da365fbbdb7b7db777dda6f9f938e1074f1a89451d4b7c73`
