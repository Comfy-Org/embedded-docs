> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/ja.md)

Switchノードは、ブール条件に基づいて2つの入力のいずれかを選択します。`switch`が有効な場合は`on_true`入力を、`switch`が無効な場合は`on_false`入力を出力します。これにより、ワークフロー内で条件付きロジックを作成し、異なるデータパスを選択することが可能になります。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | はい | | どの入力を通過させるかを決定するブール条件です。有効（true）の場合、`on_true`入力が選択されます。無効（false）の場合、`on_false`入力が選択されます。 |
| `on_false` | MATCH_TYPE | いいえ | | `switch`が無効（false）の場合に出力に渡されるデータです。この入力は`switch`がfalseの場合にのみ必要です。 |
| `on_true` | MATCH_TYPE | いいえ | | `switch`が有効（true）の場合に出力に渡されるデータです。この入力は`switch`がtrueの場合にのみ必要です。 |

**入力要件に関する注意:** `on_false`および`on_true`入力は条件付きで必須です。ノードは、`switch`がtrueの場合にのみ`on_true`入力を、`switch`がfalseの場合にのみ`on_false`入力を要求します。両方の入力は同じデータ型である必要があります。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | 選択されたデータです。`switch`がtrueの場合は`on_true`入力の値、`switch`がfalseの場合は`on_false`入力の値が出力されます。 |
