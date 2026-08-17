# WanFunInpaintToVideo

WanFunInpaintToVideo ノードは、開始画像と終了画像の間をインペイントしてビデオシーケンスを生成します。ポジティブおよびネガティブのコンディショニングに加え、オプションのフレーム画像を入力として、ビデオの潜在表現を生成します。このノードは、設定可能な寸法と長さのパラメータでビデオ生成を処理します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | ビデオ生成のためのポジティブコンディショニングプロンプト | CONDITIONING | 必須 | - |
| `negative` | ビデオ生成で回避するためのネガティブコンディショニングプロンプト | CONDITIONING | 必須 | - |
| `vae` | エンコード/デコード操作のためのVAEモデル | VAE | 必須 | - |
| `width` | 出力ビデオの幅（ピクセル単位）（デフォルト：832、ステップ：16） | INT | 必須 | 16 to MAX_RESOLUTION |
| `height` | 出力ビデオの高さ（ピクセル単位）（デフォルト：480、ステップ：16） | INT | 必須 | 16 to MAX_RESOLUTION |
| `length` | ビデオシーケンスのフレーム数（デフォルト：81、ステップ：4） | INT | 必須 | 1 to MAX_RESOLUTION |
| `batch_size` | 1回のバッチで生成するビデオの数（デフォルト：1） | INT | 必須 | 1 to 4096 |
| `clip_vision_output` | 追加のコンディショニングのためのオプションのCLIPビジョン出力 | CLIP_VISION_OUTPUT | 任意 | - |
| `start_image` | ビデオ生成のためのオプションの開始フレーム画像 | IMAGE | 任意 | - |
| `end_image` | ビデオ生成のためのオプションの終了フレーム画像 | IMAGE | 任意 | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | 処理済みのポジティブコンディショニング出力 | CONDITIONING |
| `negative` | 処理済みのネガティブコンディショニング出力 | CONDITIONING |
| `latent` | 生成されたビデオの潜在表現 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
