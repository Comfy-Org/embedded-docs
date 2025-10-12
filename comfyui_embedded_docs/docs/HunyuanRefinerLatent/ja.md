> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/ja.md)

HunyuanRefinerLatentノードは、条件付けと潜在入力を処理して精緻化操作を行うノードです。潜在画像データを組み込みながら、ポジティブ条件付けとネガティブ条件付けの両方にノイズ拡張を適用し、さらなる処理のために特定の次元を持つ新しい潜在出力を生成します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | はい | - | 処理対象のポジティブ条件付け入力 |
| `negative` | CONDITIONING | はい | - | 処理対象のネガティブ条件付け入力 |
| `latent` | LATENT | はい | - | 潜在表現入力 |
| `noise_augmentation` | FLOAT | はい | 0.0 - 1.0 | 適用するノイズ拡張の量（デフォルト: 0.10） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | ノイズ拡張と潜在画像連結が適用された処理済みポジティブ条件付け |
| `negative` | CONDITIONING | ノイズ拡張と潜在画像連結が適用された処理済みネガティブ条件付け |
| `latent` | LATENT | [バッチサイズ, 32, 高さ, 幅, チャンネル] の次元を持つ新しい潜在出力 |
