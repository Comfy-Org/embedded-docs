
RescaleCFGノードは、指定された乗数に基づいてモデルの出力の条件付けおよび非条件付けスケールを調整するように設計されています。これにより、よりバランスの取れた制御された生成プロセスを目指します。モデルの出力をリスケールすることで、条件付きおよび非条件付き成分の影響を修正し、モデルの性能や出力品質を向上させる可能性があります。

## 入力

| パラメータ | データ型 | 説明 |
|-----------|-------------|-------------|
| `model`   | MODEL     | 調整される生成モデルを表します。このパラメータは、ノードがモデルの出力にリスケール関数を適用し、生成プロセスに直接影響を与えるため重要です。 |
| `multiplier` | `FLOAT` | モデルの出力に適用されるリスケールの程度を制御します。元の成分とリスケールされた成分のバランスを決定し、最終出力の特性に影響を与えます。 |

## 出力

| パラメータ | データ型 | 説明 |
|-----------|-------------|-------------|
| `model`   | MODEL     | 調整された条件付けおよび非条件付けスケールを持つ修正済みモデル。このモデルは、適用されたリスケールにより、特性が向上した出力を生成することが期待されます。 |
