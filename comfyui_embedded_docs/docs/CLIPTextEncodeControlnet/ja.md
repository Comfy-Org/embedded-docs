# CLIPテキストエンコードコントロールネット

CLIPTextEncodeControlnet ノードは、CLIPモデルを使用してテキスト入力を処理し、既存のconditioningデータと組み合わせて、controlnetアプリケーション向けの拡張されたconditioning出力を生成します。入力テキストをトークン化し、CLIPモデルを通じてエンコードし、得られた埋め込みをクロスアテンションcontrolnetパラメータとして提供されたconditioningデータに追加します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip` | テキストのトークン化とエンコードに使用されるCLIPモデル | CLIP | はい | - |
| `conditioning` | controlnetパラメータで拡張される既存のconditioningデータ | CONDITIONING | はい | - |
| `text` | CLIPモデルで処理されるテキスト入力。複数行テキストと動的プロンプトに対応 | STRING | はい | - |

**注記:** このノードは、正しく機能するために3つの入力（`clip`、`conditioning`、`text`）すべてを必要とします。`text` 入力は動的プロンプトと複数行テキストに対応しており、柔軟なテキスト処理が可能です。このノードは実験的としてマークされています。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `CONDITIONING` | CLIPテキストエンコードから導出されたcontrolnetクロスアテンションパラメータ（`cross_attn_controlnet` および `pooled_output_controlnet`）が追加された、拡張済みconditioningデータ | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/ja.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
