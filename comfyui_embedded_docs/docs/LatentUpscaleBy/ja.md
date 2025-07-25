
LatentUpscaleByノードは、画像の潜在表現を拡大するために設計されています。スケールファクターと拡大方法の調整を可能にし、潜在サンプルの解像度を向上させる柔軟性を提供します。

## 入力

| パラメータ     | データ型 | 説明 |
|---------------|--------------|-------------|
| `samples`     | `LATENT`     | 拡大される画像の潜在表現です。このパラメータは、拡大プロセスを受ける入力データを決定する上で重要です。 |
| `upscale_method` | COMBO[STRING] | 潜在サンプルを拡大するために使用される方法を指定します。方法の選択は、拡大された出力の品質と特性に大きく影響を与える可能性があります。 |
| `scale_by`    | `FLOAT`      | 潜在サンプルが拡大されるファクターを決定します。このパラメータは、出力の解像度に直接影響を与え、拡大プロセスを正確に制御することを可能にします。 |

## 出力

| パラメータ | データ型 | 説明 |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | 拡大された潜在表現で、さらなる処理や生成タスクの準備が整っています。この出力は、生成された画像の解像度を向上させるため、または後続のモデル操作のために不可欠です。 |
