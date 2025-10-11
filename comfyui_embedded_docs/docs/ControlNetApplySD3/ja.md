> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/ja.md)

このノードは、Stable Diffusion 3のコンディショニングにControlNetのガイダンスを適用します。ポジティブおよびネガティブなコンディショニング入力と、ControlNetモデルおよび画像を受け取り、調整可能な強度とタイミングパラメータで制御ガイダンスを適用し、生成プロセスに影響を与えます。

**注記:** このノードは非推奨としてマークされており、将来のバージョンで削除される可能性があります。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | はい | - | ControlNetガイダンスを適用するポジティブなコンディショニング |
| `negative` | CONDITIONING | はい | - | ControlNetガイダンスを適用するネガティブなコンディショニング |
| `control_net` | CONTROL_NET | はい | - | ガイダンスに使用するControlNetモデル |
| `vae` | VAE | はい | - | プロセスで使用されるVAEモデル |
| `image` | IMAGE | はい | - | ControlNetがガイダンスとして使用する入力画像 |
| `strength` | FLOAT | はい | 0.0 - 10.0 | ControlNet効果の強度（デフォルト: 1.0） |
| `start_percent` | FLOAT | はい | 0.0 - 1.0 | ControlNetの適用が開始される生成プロセス内の開始点（デフォルト: 0.0） |
| `end_percent` | FLOAT | はい | 0.0 - 1.0 | ControlNetの適用が停止する生成プロセス内の終了点（デフォルト: 1.0） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | ControlNetガイダンスが適用された修正済みポジティブコンディショニング |
| `negative` | CONDITIONING | ControlNetガイダンスが適用された修正済みネガティブコンディショニング |