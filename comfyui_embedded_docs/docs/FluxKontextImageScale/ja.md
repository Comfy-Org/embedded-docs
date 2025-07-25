このノードは、入力画像のアスペクト比に基づいて、Lanczosアルゴリズムを使用してFlux Kontextモデルのトレーニング時に使用された最適なサイズに画像をスケーリングします。大きなサイズの画像を入力すると、モデルの出力品質が低下したり、出力に複数の被写体が表示されるなどの問題が発生する可能性があるため、このノードは特に有用です。

## 入力

| パラメータ名 | データ型 | 入力タイプ | デフォルト値 | 値の範囲 | 説明 |
|------------|----------|------------|--------------|----------|------|
| `image` | IMAGE | 必須 | - | - | リサイズする入力画像 |

## 出力

| 出力名 | データ型 | 説明 |
|--------|----------|------|
| `image` | IMAGE | リサイズされた画像 |

## プリセットサイズリスト

以下は、モデルトレーニング時に使用された標準サイズのリストです。ノードは入力画像のアスペクト比に最も近いサイズを選択します：

| 幅 | 高さ | アスペクト比 |
|----|------|------------|
| 672  | 1568 | 0.429    |
| 688  | 1504 | 0.457    |
| 720  | 1456 | 0.494    |
| 752  | 1392 | 0.540    |
| 800  | 1328 | 0.603    |
| 832  | 1248 | 0.667    |
| 880  | 1184 | 0.743    |
| 944  | 1104 | 0.855    |
| 1024 | 1024 | 1.000    |
| 1104 | 944  | 1.170    |
| 1184 | 880  | 1.345    |
| 1248 | 832  | 1.500    |
| 1328 | 800  | 1.660    |
| 1392 | 752  | 1.851    |
| 1456 | 720  | 2.022    |
| 1504 | 688  | 2.186    |
| 1568 | 672  | 2.333    |
