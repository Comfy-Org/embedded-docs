# スイッチ

Switch ノードは、ブール条件に基づいて2つの可能な入力から1つを選択します。`switch` が有効な場合は `on_true` 入力を出力し、`switch` が無効な場合は `on_false` 入力を出力します。これにより、条件付きロジックを作成し、ワークフロー内で異なるデータパスを選択できます。このノードは現在、実験的としてマークされています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `switch` | どの入力を通過させるかを決定するブール条件です。有効（true）の場合、`on_true` 入力が選択されます。無効（false）の場合、`on_false` 入力が選択されます。 | BOOLEAN | はい |  |
| `on_false` | `switch` が無効（false）のときに出力へ渡されるデータです。この入力は、`switch` が false の場合にのみ必要です。 | MATCH_TYPE | いいえ |  |
| `on_true` | `switch` が有効（true）のときに出力へ渡されるデータです。この入力は、`switch` が true の場合にのみ必要です。 | MATCH_TYPE | いいえ |  |

**入力要件に関する注記:** `on_false` および `on_true` 入力は条件付きで必要です。ノードは、`switch` が true の場合にのみ `on_true` 入力を要求し、`switch` が false の場合にのみ `on_false` 入力を要求します。両方の入力は同じデータ型でなければなりません。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `output` | 選択されたデータです。`switch` が true の場合は `on_true` 入力の値、false の場合は `on_false` 入力の値になります。 | MATCH_TYPE |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/ja.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
