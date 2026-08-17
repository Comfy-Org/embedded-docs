# WanPhantomSubjectToVideo

WanPhantomSubjectToVideo ノードは、条件付け入力とオプションの参照画像を処理してビデオコンテンツを生成します。ビデオ生成用の潜在表現を作成し、入力画像が提供された場合は、そこから視覚的なガイダンスを組み込むことができます。このノードは、Wan ビデオモデル向けに時間次元の連結を施した条件付けデータを準備し、変更された条件付けとともに生成された潜在ビデオデータを出力します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | ビデオ生成を導くためのポジティブ条件付け入力 | CONDITIONING | はい | - |
| `negative` | 特定の特性を避けるためのネガティブ条件付け入力 | CONDITIONING | はい | - |
| `vae` | 画像が提供されたときにエンコードするための VAE モデル | VAE | はい | - |
| `width` | 出力ビデオの幅（ピクセル単位）（デフォルト: 832、16 で割り切れる必要があります） | INT | はい | 16 から MAX_RESOLUTION |
| `height` | 出力ビデオの高さ（ピクセル単位）（デフォルト: 480、16 で割り切れる必要があります） | INT | はい | 16 から MAX_RESOLUTION |
| `length` | 生成されるビデオのフレーム数（デフォルト: 81、4 で割り切れる必要があります） | INT | はい | 1 から MAX_RESOLUTION |
| `batch_size` | 同時に生成するビデオの数（デフォルト: 1） | INT | はい | 1 から 4096 |
| `images` | 時間次元の条件付けに使用するオプションの参照画像 | IMAGE | いいえ | - |

**注:** `images` が提供された場合、それらは指定された `width` と `height` に一致するように自動的にアップスケールされ、処理には最初の `length` フレームのみが使用されます。各画像は、VAE によってエンコードされる前に、最初の 3 つのカラーチャンネルに削減されます。`images` が提供されない場合、条件付け入力は変更されずにそのまま渡されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | 画像が提供された場合に時間次元の連結が施された、変更後のポジティブ条件付け | CONDITIONING |
| `negative_text` | 画像が提供された場合に時間次元の連結が施された、変更後のネガティブ条件付け | CONDITIONING |
| `negative_img_text` | 画像が提供された場合に時間次元の連結がゼロにされたネガティブ条件付け | CONDITIONING |
| `latent` | 16チャンネル、時間次元が ((length - 1) // 4) + 1、空間次元が height // 8 および width // 8 のゼロ埋めされた潜在ビデオ表現 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
