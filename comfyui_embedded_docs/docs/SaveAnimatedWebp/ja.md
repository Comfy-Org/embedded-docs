
このノードは、画像のシーケンスをアニメーションWEBPファイルとして保存するために設計されています。個々のフレームを統合して一貫したアニメーションを作成し、指定されたメタデータを適用し、品質と圧縮設定に基づいて出力を最適化します。

## 入力

| フィールド          | Data Type | 説明                                                                         |
|-------------------|-------------|-------------------------------------------------------------------------------------|
| `images`          | `IMAGE`     | アニメーションWEBPのフレームとして保存される画像のリスト。このパラメータはアニメーションの視覚コンテンツを定義するために不可欠です。 |
| `filename_prefix` | `STRING`    | 出力ファイルの基本名を指定し、カウンターと'.webp'拡張子が付加されます。このパラメータは保存されたファイルを識別し整理するために重要です。 |
| `fps`             | `FLOAT`     | アニメーションのフレーム毎秒数を指定し、再生速度に影響を与えます。 |
| `lossless`        | `BOOLEAN`   | ロスレス圧縮を使用するかどうかを示すブール値で、アニメーションのファイルサイズと品質に影響を与えます。 |
| `quality`         | `INT`       | 圧縮品質レベルを0から100の間で設定する値で、高い値ほど画像品質が良くなりますが、ファイルサイズも大きくなります。 |
| `method`          | COMBO[STRING] | 使用する圧縮方法を指定し、エンコード速度とファイルサイズに影響を与える可能性があります。 |

## 出力

| フィールド | Data Type | 説明                                                                       |
|-------|-------------|-----------------------------------------------------------------------------------|
| `ui`  | N/A         | 保存されたアニメーションWEBP画像とそのメタデータを表示し、アニメーションが有効かどうかを示すUIコンポーネントを提供します。 |
