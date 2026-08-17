# 空のSD3潜在画像

The EmptySD3LatentImage ノードは、Stable Diffusion 3 モデル用に特別にフォーマットされた空白の潜在画像テンソルを作成します。SD3 パイプラインが期待する正しい次元と構造を持つ、ゼロで埋められたテンソルを生成します。これは、画像生成ワークフローの開始点として一般的に使用されます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `width` | 出力潜在画像の幅（ピクセル単位）（デフォルト: 1024） | INT | はい | 16 to MAX_RESOLUTION (step: 16) |
| `height` | 出力潜在画像の高さ（ピクセル単位）（デフォルト: 1024） | INT | はい | 16 to MAX_RESOLUTION (step: 16) |
| `batch_size` | 1回のバッチで生成する潜在画像の数（デフォルト: 1） | INT | はい | 1 to 4096 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `LATENT` | SD3互換の次元を持つ空白サンプルを含む潜在テンソル。このテンソルは16チャンネルを持ち、入力の幅と高さに対して空間的に8分の1に縮小されています。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/ja.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
