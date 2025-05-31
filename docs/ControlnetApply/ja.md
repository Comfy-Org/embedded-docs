> 
このドキュメントは、元の`Apply ControlNet(Advanced)`ノードに関するものです。最も古い`Apply ControlNet`ノードは`Apply ControlNet(Old)`に名前が変更されました。互換性のために、comfyui.orgからダウンロードした多くのワークフローフォルダで`Apply ControlNet(Old)`ノードを見ることができますが、検索やノードリストでは`Apply ControlNet(Old)`ノードを見つけることはできません。代わりに`Apply ControlNet`ノードを使用してください。

このノードは、与えられた画像とコンディショニングにControlNetを適用し、Depth、OpenPose、Canny、HEDなどのコントロールネットワークのパラメータと指定された強度に従って画像の属性を調整します。


ControlNetを使用するには、入力画像の前処理が必要です。ComfyUIの初期ノードには前処理器とControlNetモデルが含まれていないため、まずContrlNet前処理器[前処理器のダウンロード](https://github.com/Fannovel16/comfy_controlnet_preprocessors)と対応するControlNetモデルをインストールしてください。

### 入力タイプ
| パラメータ | データタイプ | 機能 |
| --- | --- | --- |
| `positive` | `CONDITIONING` | [CLIPテキストエンコーダー](/ja/comfyui-nodes/conditioning/clip-text-encode)または他のコンディショニング入力からの正のコンディショニングデータ |
| `negative` | `CONDITIONING` | [CLIPテキストエンコーダー](/ja/comfyui-nodes/conditioning/clip-text-encode)または他のコンディショニング入力からの負のコンディショニングデータ |
| `control_net` | `CONTROL_NET` | 適用するControlNetモデル、通常は[ControlNetローダー](/ja/comfyui-nodes/loaders/controlnet-loader)から入力 |
| `image` | `IMAGE` | ControlNet適用のための画像、前処理器で処理が必要 |
| `vae` | `VAE` | Vaeモデル入力 |
| `strength` | `FLOAT` | ネットワーク調整の強度を制御、値の範囲は0~10。推奨値は0.5~1.5の間が適切です。値が低いほどモデルの自由度が高く、値が高いほど制約が厳しくなります。値が高すぎると奇妙な画像が生成される可能性があります。 |
| `start_percent` | `FLOAT` | 値0.000~1.000、ControlNetの適用を開始する時点をパーセンテージで決定、例えば0.2は拡散プロセスの20%時点でControlNetガイドが画像生成に影響を与え始めることを意味します |
| `end_percent` | `FLOAT` | 値0.000~1.000、ControlNetの適用を終了する時点をパーセンテージで決定、例えば0.8は拡散プロセスの80%時点でControlNetガイドが画像生成への影響を停止することを意味します |

### 出力タイプ
| パラメータ | データタイプ | 機能 |
| --- | --- | --- |
| `positive` | `CONDITIONING` | ControlNetによって処理された正のコンディショニングデータ、次のControlNetまたはKサンプラーノードに出力可能 |
| `negative` | `CONDITIONING` | ControlNetによって処理された負のコンディショニングデータ、次のControlNetまたはKサンプラーノードに出力可能 |

> 
**T2IAdaptorスタイルモデル**を使用する場合は、代わりに`Apply Style Model`ノードを使用してください


## ComfyUI ControlNet 使用例
以下のページで例を確認してください:
- [ComfyUI OpenPose ControlNet 使用例](/ja/tutorial/advanced/how-to-use-openpose-controlnet-with-sd1.5)
- [ComfyUI Depth ControlNet 使用例](/ja/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5)
- [ComfyUI Canny ControlNet 使用例](/ja/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5)
- [ComfyUI Multi ControlNet 使用例](/ja/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui)

## 関連リソース

- モデルリソース: [ControlNetモデルリソースダウンロード](/ja/resource/controlnet-models)
- 前処理器プラグイン: [ComfyUI ControlNet Auxiliary Preprocessors](https://github.com/Fannovel16/comfyui_controlnet_aux)

## Apply ControlNet (OLD) ノードの説明
これはApply ControlNetノードの初期バージョンです。ノードオプションは更新されましたが、互換性のためにComfyUIで以前のバージョンノードを使用するワークフローをダウンロードすると、このノードとして表示されます。新しいApply ControlNetノードに切り替えることができます。

### Apply ControlNet (OLD) 入力タイプ
| パラメータ | データタイプ | 機能 |
| --- | --- | --- |
| `conditioning` | `CONDITIONING` | [CLIPテキストエンコーダー](/ja/comfyui-nodes/conditioning/clip-text-encode)または他のコンディショニング入力からのコンディショニングデータ |
| `control_net` | `CONTROL_NET` | 適用するControlNetモデル、通常は[ControlNetローダー](/ja/comfyui-nodes/loaders/controlnet-loader)から入力 |
| `image` | `IMAGE` | ControlNet適用のための画像、前処理器で処理が必要 |
| `strength` | `FLOAT` | ネットワーク調整の強度を制御、値の範囲は0~10。推奨値は0.5~1.5の間が適切です。値が低いほどモデルの自由度が高く、値が高いほど制約が厳しくなります。 |

### Apply ControlNet (OLD) 出力タイプ
| パラメータ | データタイプ | 機能 |
| --- | --- | --- |
| `conditioning` | `CONDITIONING` | ControlNetによって処理されたコンディショニングデータ、次のControlNetまたはKサンプラーノードに出力可能 |