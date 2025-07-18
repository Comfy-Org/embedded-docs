
KSamplerSelectノードは、指定されたサンプラー名に基づいて特定のサンプラーを選択するように設計されています。サンプラー選択の複雑さを抽象化し、ユーザーがタスクに応じて異なるサンプリング戦略を簡単に切り替えることができます。

## 入力

| パラメータ         | Data Type | 説明                                                                                      |
|-------------------|-------------|------------------------------------------------------------------------------------------------|
| `sampler_name`    | COMBO[STRING] | 選択されるサンプラーの名前を指定します。このパラメータは、どのサンプリング戦略が使用されるかを決定し、全体的なサンプリングの動作と結果に影響を与えます。 |

## 出力

| パラメータ   | Data Type | 説明                                                                 |
|-------------|-------------|-----------------------------------------------------------------------------|
| `sampler`   | `SAMPLER`   | サンプリングタスクに使用する準備が整った選択されたサンプラーオブジェクトを返します。 |
