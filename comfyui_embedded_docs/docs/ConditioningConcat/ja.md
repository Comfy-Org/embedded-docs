> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/ja.md)

ConditioningConcat ノードは、コンディショニングベクトルを連結するために設計されており、具体的には `conditioning_from` ベクトルを `conditioning_to` ベクトルにマージします。この操作は、2つのソースからのコンディショニング情報を1つの統合された表現に結合する必要があるシナリオにおいて基本となる処理です。

## 入力

| パラメータ            | Comfy dtype        | 説明 |
|-----------------------|--------------------|------|
| `conditioning_to`     | `CONDITIONING`     | `conditioning_from` ベクトルが連結される、主要なコンディショニングベクトルのセットを表します。連結処理のベースとして機能します。 |
| `conditioning_from`   | `CONDITIONING`     | `conditioning_to` ベクトルに連結されるコンディショニングベクトルで構成されます。このパラメータにより、既存のセットに追加のコンディショニング情報を統合できます。 |

## 出力

| パラメータ            | Comfy dtype        | 説明 |
|-----------------------|--------------------|------|
| `conditioning`        | `CONDITIONING`     | `conditioning_from` ベクトルを `conditioning_to` ベクトルに連結した結果として得られる、統合されたコンディショニングベクトルのセットです。 |