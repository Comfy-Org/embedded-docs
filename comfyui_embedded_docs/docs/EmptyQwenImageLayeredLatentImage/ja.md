> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/ja.md)

## 概要 Empty Qwen Image Layered Latentノードは、Qwen画像モデルで使用するための空の多層潜在表現を作成します。指定されたレイヤー数、バッチサイズ、および空間次元で構成された、ゼロで満たされたテンソルを生成します。この空の潜在表現は、その後の画像生成や操作ワークフローの開始点として機能します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|----------|------|------|------|
| `width` | INT | はい | 16～MAX_RESOLUTION | 作成する潜在画像の幅です。値は16で割り切れる必要があります。（デフォルト：640） |
| `height` | INT | はい | 16～MAX_RESOLUTION | 作成する潜在画像の高さです。値は16で割り切れる必要があります。（デフォルト：640） |
| `layers` | INT | はい | 0～MAX_RESOLUTION | 潜在構造に追加する追加レイヤーの数です。これにより潜在表現の深さが定義されます。（デフォルト：3） |
| `batch_size` | INT | いいえ | 1～4096 | バッチ内で生成する潜在サンプルの数です。（デフォルト：1） |

**注記：** `width` および `height` パラメータは、出力される潜在テンソルの空間次元を決定するために内部的に8で除算されます。

## 出力

| 出力名 | データ型 | 説明 |
|--------|----------|------|
| `samples` | LATENT | ゼロで満たされた潜在テンソルです。その形状は `[batch_size, 16, layers + 1, height // 8, width // 8]` となります。 |

---
**Source fingerprint (SHA-256):** `99497e3e4a67bf7b3f650573e7b8eb2d7fad6be5819b7ebbbb8736291dc44e0c`
