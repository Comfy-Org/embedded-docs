# EmptyHunyuanImageLatent

EmptyHunyuanImageLatent ノードは、Hunyuan 画像生成モデルで使用するための、特定の次元を持つ空の潜在テンソルを作成します。ワークフロー内の後続ノードで処理できる空白の開始点を生成します。このノードでは、潜在空間の幅、高さ、バッチサイズを指定できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `width` | 生成される潜在画像の幅（ピクセル単位）です（デフォルト: 2048、ステップ: 32）。 | INT | はい | 64 to MAX_RESOLUTION |
| `height` | 生成される潜在画像の高さ（ピクセル単位）です（デフォルト: 2048、ステップ: 32）。 | INT | はい | 64 to MAX_RESOLUTION |
| `batch_size` | バッチ内で生成する潜在サンプルの数です（デフォルト: 1）。 | INT | はい | 1 to 4096 |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `LATENT` | Hunyuan 画像処理用に指定された次元を持つ、空の潜在テンソルです。このテンソルは64チャンネルを持ち、その空間次元は、指定された幅と高さの 1/32（32分の1）です。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/ja.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
