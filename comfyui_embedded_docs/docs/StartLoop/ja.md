# StartLoop

Start Loop ノードは、ワークフロー内でループ構造を開始します。接続されたループ本体を各反復につき1回実行し、反復回数を3つの方法で数えることができます。固定回数の繰り返し（simple）、数値インデックス範囲（For）、リスト内の各項目につき1回のパス（List）です。各パスでは、現在のインデックス、先頭/末尾フラグ、および反復間で受け渡し可能なオプションの持ち越し値が公開されます。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `mode` | ループの反復モード（デフォルト: "simple"）。選択したモードによって、追加で表示されるパラメータが決まります。 | DYNAMIC_COMBO | はい | `"simple"`<br>`"For"`<br>`"List"` |
| `cache_iterations` | 以前の実行から変更されていない反復結果を再利用します。無効にすると、すべての反復を再度実行します。デフォルト: false。 | BOOLEAN | いいえ | true<br>false |
| `parent_iteration` | 外側の Start Loop の iteration_index を接続して、このループをネストします。この入力は強制入力専用です（リンクが必要です）。 | INT | いいえ | Any integer |
| `initial_iteration_value` | 最初の反復で current_iteration_value として公開される値です。 | ANY（型一致） | いいえ | Any value |

### Simple モード入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `num_iterations` | ループ本体を実行する回数。デフォルト: 4。 | INT | はい | Minimum 0 |

### For モード入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `start_iteration_index` | For ループモードを使用するときの最初の反復のインデックス。デフォルト: 0。 | INT | はい | Any integer |
| `max_iteration` | For モードにおける iteration_index の排他的な停止値。デフォルト: 4。 | INT | はい | Maximum 0xffffffffffffffff |
| `step` | For ループモードを使用するときの各反復間のインデックスステップサイズ。デフォルト: 1。 | INT | はい | Minimum 1 |

### List モード入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `list` | ループが反復処理する項目のリスト。ループ本体は項目ごとに1回実行されます。 | ANY（型一致するリスト項目） | はい | Any list |

注意:

- 現在選択されている `mode` に属するパラメータのみが表示され、使用されます。
- Simple モードでは、反復インデックスは 0 から `num_iterations` - 1 まで実行されます。For モードでは、インデックスは `start_iteration_index` から（ただし `max_iteration` は含まずに）`step` ずつ増加しながら実行されます。List モードでは、`list` 内の項目ごとに1回の反復が実行されます。
- `step` は 0 であってはなりません。値が 0 の場合はエラーになります。1 未満の値は許可されていません。
- 計算された反復回数が 0 の場合、`is_last` 出力は true として報告され、ループ本体は実行されません。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `iteration_index` | 現在のループ反復のインデックス。 | INT |
| `is_first` | ループの最初の反復中は true です。 | BOOLEAN |
| `is_last` | ループの最後の反復中は true です。 | BOOLEAN |
| `list_item` | List モードを使用しているときのリスト内の現在の項目。Simple モードと For モードでは None です。 | ANY（型一致） |
| `current_iteration_value` | 現在の反復のループ持ち越し値です。最初の反復では initial_iteration_value、その後は各反復で End Loop からの next_iteration_value になります。 | ANY（型一致） |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StartLoop/ja.md)

---
**Source fingerprint (SHA-256):** `2584af9fd623f4762f440a043679e47aeef25ad0d571cfac11506cb513dd1b98`
