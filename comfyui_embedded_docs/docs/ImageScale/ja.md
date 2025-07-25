ImageScaleノードは、特定の寸法に画像をリサイズするために設計されており、さまざまなアップスケール方法を提供し、リサイズされた画像をクロップする機能も備えています。画像のアップスケールとクロップの複雑さを抽象化し、ユーザー定義のパラメータに基づいて画像の寸法を変更するための簡単なインターフェースを提供します。

## 入力

| パラメータ       | Data Type | 説明                                                                           |
|-----------------|-------------|---------------------------------------------------------------------------------------|
| `image`         | `IMAGE`     | アップスケールされる入力画像。このパラメータはノードの操作の中心であり、リサイズ変換が適用される主要なデータとして機能します。出力画像の品質と寸法は、元の画像の特性に直接影響されます。 |
| `upscale_method`| COMBO[STRING] | 画像のアップスケールに使用される方法を指定します。方法の選択は、アップスケールされた画像の品質と特性に影響を与え、リサイズされた出力における視覚的忠実度と潜在的なアーティファクトに影響を与える可能性があります。 |
| `width`         | `INT`       | アップスケールされた画像の目標幅。このパラメータは出力画像の寸法に直接影響を与え、リサイズ操作の水平スケールを決定します。 |
| `height`        | `INT`       | アップスケールされた画像の目標高さ。このパラメータは出力画像の寸法に直接影響を与え、リサイズ操作の垂直スケールを決定します。 |
| `crop`          | COMBO[STRING] | アップスケールされた画像をクロップするかどうか、またどのようにクロップするかを決定します。クロップを無効にするオプションや中央クロップのオプションを提供します。これにより、指定された寸法に合わせるためにエッジを削除することで、画像の最終的な構成に影響を与えます。 |

## 出力

| パラメータ | データ型 | 説明 |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | アップスケールされ（オプションでクロップされた）画像で、さらなる処理や視覚化の準備が整っています。 |
