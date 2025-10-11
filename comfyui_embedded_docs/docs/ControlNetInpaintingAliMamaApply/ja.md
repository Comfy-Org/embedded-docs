> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/ja.md)

ControlNetInpaintingAliMamaApplyノードは、インペイント（画像修復）タスク向けにControlNetの調節を適用するノードです。ポジティブ調節とネガティブ調節をコントロール画像とマスクと組み合わせることで、生成プロセスを誘導する修正済みの調節データを作成します。入力画像とマスクを処理し、画像のどの領域を修復するかを精密に制御できるようにします。このノードは強度調整とタイミング制御をサポートしており、生成プロセスの異なる段階におけるControlNetの影響を微調整することが可能です。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | はい | - | 生成を望ましいコンテンツに向けて誘導するポジティブな調節データ |
| `negative` | CONDITIONING | はい | - | 生成を望ましくないコンテンツから遠ざけるネガティブな調節データ |
| `control_net` | CONTROL_NET | はい | - | 生成に対して追加の制御を提供するControlNetモデル |
| `vae` | VAE | はい | - | 画像のエンコードとデコードに使用されるVAE（変分オートエンコーダ） |
| `image` | IMAGE | はい | - | ControlNetの制御ガイダンスとして機能する入力画像 |
| `mask` | MASK | はい | - | 画像のどの領域を修復すべきかを定義するマスク |
| `strength` | FLOAT | はい | 0.0 ～ 10.0 | ControlNet効果の強度（デフォルト: 1.0） |
| `start_percent` | FLOAT | はい | 0.0 ～ 1.0 | 生成過程中にControlNetの影響が開始する時点（パーセンテージ）（デフォルト: 0.0） |
| `end_percent` | FLOAT | はい | 0.0 ～ 1.0 | 生成過程中にControlNetの影響が終了する時点（パーセンテージ）（デフォルト: 1.0） |

**注記:** ControlNetで `concat_mask` が有効になっている場合、マスクは反転されて画像に適用された後、ControlNetに送信される追加の連結データにマスクが含まれます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | インペイント用にControlNetが適用された修正済みのポジティブ調節データ |
| `negative` | CONDITIONING | インペイント用にControlNetが適用された修正済みのネガティブ調節データ |