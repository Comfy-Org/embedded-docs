
このノードは、CLIPビジョン出力を条件付けプロセスに統合するために設計されており、指定された強度とノイズ増幅パラメータに基づいてこれらの出力の影響を調整します。視覚的なコンテキストで条件付けを豊かにし、生成プロセスを強化します。

## 入力

| パラメータ              | Comfy dtype            | 説明 |
|------------------------|------------------------|-------------|
| `conditioning`         | `CONDITIONING`         | CLIPビジョン出力が追加される基本の条件付けデータで、さらなる修正の基礎として機能します。 |
| `clip_vision_output`   | `CLIP_VISION_OUTPUT`   | CLIPビジョンモデルからの出力で、条件付けに統合される視覚的なコンテキストを提供します。 |
| `strength`             | `FLOAT`                | 条件付けに対するCLIPビジョン出力の影響の強度を決定します。 |
| `noise_augmentation`   | `FLOAT`                | CLIPビジョン出力に統合する前に適用するノイズ増幅のレベルを指定します。 |

## 出力

| パラメータ             | Comfy dtype            | 説明 |
|-----------------------|------------------------|-------------|
| `conditioning`         | `CONDITIONING`         | 強度とノイズ増幅が適用されたCLIPビジョン出力を含む、豊かになった条件付けデータ。 |
