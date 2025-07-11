
LatentCompositeノードは、2つの潜在表現を1つの出力にブレンドまたはマージするように設計されています。このプロセスは、入力された潜在の特性を制御された方法で組み合わせることによって、合成画像や特徴を作成するために不可欠です。

## 入力

| パラメータ    | Data Type | 説明 |
|--------------|-------------|-------------|
| `samples_to` | `LATENT`    | 'samples_from'が合成される'samples_to'の潜在表現です。合成操作のベースとして機能します。 |
| `samples_from` | `LATENT` | 'samples_to'に合成される'samples_from'の潜在表現です。最終的な合成出力にその特徴や特性を提供します。 |
| `x`          | `INT`      | 'samples_from'の潜在が'samples_to'に配置されるx座標（水平位置）です。合成の水平位置を決定します。 |
| `y`          | `INT`      | 'samples_from'の潜在が'samples_to'に配置されるy座標（垂直位置）です。合成の垂直位置を決定します。 |
| `feather`    | `INT`      | 'samples_from'の潜在を合成前に'samples_to'に合わせてリサイズするかどうかを示すブール値です。これにより、合成結果のスケールと比率に影響を与えることができます。 |

## 出力

| パラメータ | データ型 | 説明 |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | 出力は、指定された座標とリサイズオプションに基づいて、'samples_to'と'samples_from'の両方の特徴をブレンドした合成潜在表現です。 |
