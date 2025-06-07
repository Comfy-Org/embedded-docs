このドキュメントは、元の`Apply ControlNet(Advanced)`ノードに関するものです。最も古い`Apply ControlNet`ノードは`Apply ControlNet(Old)`に名前が変更されました。互換性のために、comfyui.orgからダウンロードした多くのワークフローフォルダで`Apply ControlNet(Old)`ノードを見ることができますが、検索やノードリストでは`Apply ControlNet(Old)`ノードを見つけることはできません。代わりに`Apply ControlNet`ノードを使用してください。

このノードは、与えられた画像とコンディショニングにControlNetを適用し、Depth、OpenPose、Canny、HEDなどのコントロールネットワークのパラメータと指定された強度に従って画像の属性を調整します。

ControlNetを使用するには、入力画像の前処理が必要です。ComfyUIの初期ノードには前処理器とControlNetモデルが含まれていないため、まずContrlNet前処理器[前処理器のダウンロード](https://github.com/Fannovel16/comfy_controlnet_preprocessors)と対応するControlNetモデルをインストールしてください。

## 入力

| パラメータ | データタイプ | 機能 |
| --- | --- | --- |
| `positive` | `CONDITIONING` | `CLIPテキストエンコーダー`または他のコンディショニング入力からの正のコンディショニングデータ |
| `negative` | `CONDITIONING` | `CLIPテキストエンコーダー`または他のコンディショニング入力からの負のコンディショニングデータ |
| `control_net` | `CONTROL_NET` | 適用するControlNetモデル、通常は`ControlNetローダー`から入力 |
| `image` | `IMAGE` | ControlNet適用のための画像、前処理器で処理が必要 |
| `vae` | `VAE` | Vaeモデル入力 |
| `strength` | `FLOAT` | ネットワーク調整の強度を制御、値の範囲は0~10。推奨値は0.5~1.5の間が適切です。値が低いほどモデルの自由度が高く、値が高いほど制約が厳しくなります。値が高すぎると奇妙な画像が生成される可能性があります。 |
| `start_percent` | `FLOAT` | 値0.000~1.000、ControlNetの適用を開始する時点をパーセンテージで決定、例えば0.2は拡散プロセスの20%時点でControlNetガイドが画像生成に影響を与え始めることを意味します |
| `end_percent` | `FLOAT` | 値0.000~1.000、ControlNetの適用を終了する時点をパーセンテージで決定、例えば0.8は拡散プロセスの80%時点でControlNetガイドが画像生成への影響を停止することを意味します |

## 出力

| パラメータ | データタイプ | 機能 |
| --- | --- | --- |
| `positive` | `CONDITIONING` | ControlNetによって処理された正のコンディショニングデータ、次のControlNetまたはKサンプラーノードに出力可能 |
| `negative` | `CONDITIONING` | ControlNetによって処理された負のコンディショニングデータ、次のControlNetまたはKサンプラーノードに出力可能 |

**T2IAdaptorスタイルモデル**を使用する場合は、代わりに`Apply Style Model`ノードを使用してください
