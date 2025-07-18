
SamplerCustomノードは、さまざまなアプリケーションに対して柔軟でカスタマイズ可能なサンプリングメカニズムを提供するように設計されています。ユーザーは、特定のニーズに合わせた異なるサンプリング戦略を選択し、設定することができ、サンプリングプロセスの適応性と効率を向上させます。

## 入力

| パラメータ | データ型 | 説明 |
|-----------|--------------|-------------|
| `model`   | `MODEL`      | 'model'入力タイプは、サンプリングに使用されるモデルを指定し、サンプリングの動作と出力を決定する上で重要な役割を果たします。 |
| `add_noise` | `BOOLEAN`    | 'add_noise'入力タイプは、サンプリングプロセスにノイズを追加するかどうかを指定することができ、生成されるサンプルの多様性と特性に影響を与えます。 |
| `noise_seed` | `INT`        | 'noise_seed'入力タイプは、ノイズ生成のためのシードを提供し、ノイズを追加する際のサンプリングプロセスの再現性と一貫性を確保します。 |
| `cfg`     | `FLOAT`      | 'cfg'入力タイプは、サンプリングプロセスの設定を行い、サンプリングパラメータと動作の微調整を可能にします。 |
| `positive` | `CONDITIONING` | 'positive'入力タイプは、ポジティブな条件付け情報を表し、指定されたポジティブな属性に一致するサンプルを生成するようにサンプリングプロセスを導きます。 |
| `negative` | `CONDITIONING` | 'negative'入力タイプは、ネガティブな条件付け情報を表し、指定されたネガティブな属性を示すサンプルの生成を避けるようにサンプリングプロセスを誘導します。 |
| `sampler` | `SAMPLER`    | 'sampler'入力タイプは、使用する特定のサンプリング戦略を選択し、生成されるサンプルの性質と品質に直接影響を与えます。 |
| `sigmas`  | `SIGMAS`     | 'sigmas'入力タイプは、サンプリングプロセスで使用されるノイズレベルを定義し、サンプル空間の探索と出力の多様性に影響を与えます。 |
| `latent_image` | `LATENT` | 'latent_image'入力タイプは、サンプリングプロセスの初期潜在画像を提供し、サンプル生成の出発点として機能します。 |

## 出力

| パラメータ | データ型 | 説明 |
|-----------|--------------|-------------|
| `output`  | `LATENT`     | 'output'は、サンプリングプロセスの主要な結果を表し、生成されたサンプルを含みます。 |
| `denoised_output` | `LATENT` | 'denoised_output'は、デノイズプロセスが適用された後のサンプルを表し、生成されたサンプルの明瞭さと品質を向上させる可能性があります。 |
