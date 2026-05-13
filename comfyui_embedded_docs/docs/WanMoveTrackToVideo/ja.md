> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/ja.md)

WanMoveTrackToVideo ノードは、動画生成用のコンディショニングと潜在空間データを準備し、オプションで動き追跡情報を組み込みます。開始画像シーケンスを潜在表現にエンコードし、オブジェクトトラックからの位置データをブレンドして、生成される動画の動きをガイドします。このノードは、修正されたポジティブおよびネガティブコンディショニングと、動画モデル用に準備された空の潜在テンソルを出力します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | はい | - | 修正されるポジティブコンディショニング入力。 |
| `negative` | CONDITIONING | はい | - | 修正されるネガティブコンディショニング入力。 |
| `vae` | VAE | はい | - | 開始画像を潜在空間にエンコードするために使用されるVAEモデル。 |
| `tracks` | TRACKS | いいえ | - | オブジェクトのパスを含むオプションの動き追跡データ。 |
| `strength` | FLOAT | いいえ | 0.0 - 100.0 | トラックコンディショニングの強度。（デフォルト：1.0） |
| `width` | INT | いいえ | 16 - MAX_RESOLUTION | 出力動画の幅。16で割り切れる必要があります。（デフォルト：832） |
| `height` | INT | いいえ | 16 - MAX_RESOLUTION | 出力動画の高さ。16で割り切れる必要があります。（デフォルト：480） |
| `length` | INT | いいえ | 1 - MAX_RESOLUTION | 動画シーケンスのフレーム数。（デフォルト：81） |
| `batch_size` | INT | いいえ | 1 - 4096 | 潜在出力のバッチサイズ。（デフォルト：1） |
| `start_image` | IMAGE | はい | - | エンコードする開始画像または画像シーケンス。 |
| `clip_vision_output` | CLIPVISIONOUTPUT | いいえ | - | コンディショニングに追加するオプションのCLIPビジョンモデル出力。 |

**注意:** `strength` パラメータは、`tracks` が指定された場合にのみ効果があります。`tracks` が指定されていない場合、または `strength` が 0.0 の場合は、トラックコンディショニングは適用されません。`start_image` はコンディショニング用の潜在画像とマスクを作成するために使用されます。これが指定されていない場合、ノードはコンディショニングをそのまま通過させ、空の潜在データを出力します。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | `concat_latent_image`、`concat_mask`、`clip_vision_output` を潜在的に含む、修正されたポジティブコンディショニング。 |
| `negative` | CONDITIONING | `concat_latent_image`、`concat_mask`、`clip_vision_output` を潜在的に含む、修正されたネガティブコンディショニング。 |
| `latent` | LATENT | `batch_size`、`length`、`height`、`width` の入力によって形状が決定される空の潜在テンソル。 |

---
**Source fingerprint (SHA-256):** `9677addf5b94b42efd3015f51380c1fa9b16d4a5105cc7f24de0be34c0042bbc`
