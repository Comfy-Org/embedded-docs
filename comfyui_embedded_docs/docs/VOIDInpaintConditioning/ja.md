> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/ja.md)

VOIDInpaintConditioning ノードは、CogVideoX モデルでインペインティングに必要なコンディショニングデータを準備します。ソース動画と前処理済みのクワッドマスクを受け取り、VAE を通じてエンコードし、モデルがマスク領域を補完するために使用する 32 チャンネルのコンディショニング信号に結合します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|----------|------|------|------|
| `positive` | CONDITIONING | はい | - | インペインティング潜在情報で拡張されるポジティブコンディショニング |
| `negative` | CONDITIONING | はい | - | インペインティング潜在情報で拡張されるネガティブコンディショニング |
| `vae` | VAE | はい | - | マスクとマスク済み動画を潜在空間にエンコードするために使用される VAE モデル |
| `video` | IMAGE | はい | - | [T, H, W, 3] 形式のソース動画フレーム |
| `quadmask` | MASK | はい | - | VOIDQuadmaskPreprocess から出力される [T, H, W] 形式の前処理済みクワッドマスク |
| `width` | INT | はい | 16 ～ MAX_RESOLUTION（ステップ：8） | 動画とマスクのリサイズ幅（デフォルト：672） |
| `height` | INT | はい | 16 ～ MAX_RESOLUTION（ステップ：8） | 動画とマスクのリサイズ高さ（デフォルト：384） |
| `length` | INT | はい | 1 ～ MAX_RESOLUTION（ステップ：1） | 処理するピクセルフレーム数。CogVideoX-Fun-V1.5（patch_size_t=2）の場合、latent_t は偶数である必要があります。奇数になる長さは切り捨てられます（例：49 → 45）（デフォルト：45） |
| `batch_size` | INT | はい | 1 ～ 64 | 出力ノイズ潜在のバッチサイズ（デフォルト：1） |

## 出力

| 出力名 | データ型 | 説明 |
|---------|----------|------|
| `positive` | CONDITIONING | インペインティング潜在情報が追加されたポジティブコンディショニング |
| `negative` | CONDITIONING | インペインティング潜在情報が追加されたネガティブコンディショニング |
| `latent` | LATENT | 形状 [batch_size, 16, latent_t, latent_h, latent_w] のゼロ埋めノイズ潜在テンソル |