# AutogrowPrefixTestNode

The AutogrowPrefixTestNode は、自動拡張入力機能をテストするためのロジックノードです。動的な数の float 入力を受け取り、それらの値をカンマ区切りの文字列に結合して出力します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `autogrow` | float 値を受け取る動的入力グループです。このグループは 1 ～ 10 個の float 入力を保持でき、ノードは指定されたすべての値を処理します。 | FLOAT | はい | 1 ～ 10 個の入力 |

**注:** `autogrow` 入力は特別な動的入力であり、最大 10 個まで float 入力を追加できます。最小は 1 個です。このノードの `min` と `max` の値は、個々の float の値の範囲ではなく、グループ内で許可される入力数を定義します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `output` | すべての入力 float 値をカンマで区切って連結した単一の文字列。 | STRING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/ja.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
