
VAEDecodeノードは、指定されたVariational Autoencoder（VAE）を使用して潜在表現を画像にデコードするために設計されています。これは、圧縮データ表現から画像を生成し、潜在空間エンコーディングからの画像再構築を促進します。

## 入力

| パラメータ | データ型 | 説明 |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | 'samples'パラメータは、画像にデコードされる潜在表現を表します。これは、画像が再構築される圧縮データを提供するため、デコードプロセスにおいて重要です。 |
| `vae`     | VAE       | 'vae'パラメータは、潜在表現を画像にデコードするために使用されるVariational Autoencoderモデルを指定します。これは、デコードメカニズムと再構築された画像の品質を決定するために不可欠です。 |

## 出力

| パラメータ | データ型 | 説明 |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | 出力は、指定されたVAEモデルを使用して提供された潜在表現から再構築された画像です。 |
