
LatentCropノードは、画像の潜在表現に対してクロップ操作を行うように設計されています。クロップの寸法と位置を指定することで、潜在空間のターゲットを絞った修正が可能です。

## 入力

| パラメータ | データ型 | 説明 |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | 'samples'パラメータはクロップされる潜在表現を表します。これはクロップ操作が行われるデータを定義するために重要です。 |
| `width`   | `INT`       | クロップ領域の幅を指定します。これは出力される潜在表現の寸法に直接影響します。 |
| `height`  | `INT`       | クロップ領域の高さを指定し、結果として得られるクロップされた潜在表現のサイズに影響を与えます。 |
| `x`       | `INT`       | クロップ領域の開始x座標を決定し、元の潜在表現内でのクロップの位置に影響を与えます。 |
| `y`       | `INT`       | クロップ領域の開始y座標を決定し、元の潜在表現内でのクロップの位置を設定します。 |

## 出力

| パラメータ | データ型 | 説明 |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | 出力は指定されたクロップが適用された修正済みの潜在表現です。 |
