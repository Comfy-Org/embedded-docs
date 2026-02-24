> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/ja.md)

WanMoveTrackToVideoノードは、オプションのモーショントラッキング情報を組み込んで、ビデオ生成用のコンディショニングと潜在空間データを準備します。開始画像シーケンスを潜在表現にエンコードし、オブジェクトトラックからの位置データをブレンドして、生成されるビデオの動きをガイドすることができます。このノードは、修正されたポジティブおよびネガティブコンディショニングと、ビデオモデル用に準備された空の潜在テンソルを出力します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | はい | - | 修正されるポジティブコンディショニング入力。 |
| `negative` | CONDITIONING | はい | - | 修正されるネガティブコンディショニング入力。 |
| `vae` | VAE | はい | - | 開始画像を潜在空間にエンコードするために使用されるVAEモデル。 |
| `tracks` | TRACKS | いいえ | - | オブジェクトパスを含むオプションのモーショントラッキングデータ。 |
| `strength` | FLOAT | いいえ | 0.0 - 100.0 | トラックコンディショニングの強度。(デフォルト: 1.0) |
| `width` | INT | いいえ | 16 - MAX_RESOLUTION | 出力ビデオの幅。16で割り切れる必要があります。(デフォルト: 832) |
| `height` | INT | いいえ | 16 - MAX_RESOLUTION | 出力ビデオの高さ。16で割り切れる必要があります。(デフォルト: 480) |
| `length` | INT | いいえ | 1 - MAX_RESOLUTION | ビデオシーケンスのフレーム数。(デフォルト: 81) |
| `batch_size` | INT | いいえ | 1 - 4096 | 潜在出力のバッチサイズ。(デフォルト: 1) |
| `start_image` | IMAGE | はい | - | エンコードする開始画像または画像シーケンス。 |
| `clip_vision_output` | CLIPVISIONOUTPUT | いいえ | - | コンディショニングに追加するオプションのCLIPビジョンモデル出力。 |

**注記:** `strength`パラメータは、`tracks`が提供された場合にのみ効果があります。`tracks`が提供されていないか、`strength`が0.0の場合、トラックコンディショニングは適用されません。`start_image`はコンディショニング用の潜在画像とマスクを作成するために使用されます。提供されていない場合、このノードはコンディショニングを通過させるだけで、空の潜在を出力します。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修正されたポジティブコンディショニング。`concat_latent_image`、`concat_mask`、`clip_vision_output`を含む可能性があります。 |
| `negative` | CONDITIONING | 修正されたネガティブコンディショニング。`concat_latent_image`、`concat_mask`、`clip_vision_output`を含む可能性があります。 |
| `latent` | LATENT | `batch_size`、`length`、`height`、`width`入力によって形状が決まる次元を持つ空の潜在テンソル。 |
