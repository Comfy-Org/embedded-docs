
VAESaveノードは、プロンプトや追加のPNG情報を含むVAEモデルとそのメタデータを指定された出力ディレクトリに保存するために設計されています。モデルの状態と関連情報をファイルにシリアライズする機能をカプセル化し、訓練済みモデルの保存と共有を容易にします。

## 入力

| パラメータ | データ型 | 説明 |
|-----------|-------------|-------------|
| `vae`     | VAE       | 保存されるVAEモデル。このパラメータは、シリアライズされ保存されるモデルの状態を表すため、重要です。 |
| `filename_prefix` | STRING   | モデルとそのメタデータが保存されるファイル名のプレフィックス。これにより、モデルの整理された保存と簡単な取得が可能になります。 |

## 出力

このノードには出力タイプがありません。
