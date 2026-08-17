# WanInfiniteTalkToVideo

WanInfiniteTalkToVideo ノードは、オーディオから話しているヘッドのビデオクリップを生成します。ビデオ拡散モデルを、1人または2人の話者からのオーディオ特徴量に条件付けし、必要に応じて開始画像や前フレームをコンテキストとして使用し、パッチ適用済みモデル、条件付け、およびサンプリング用の潜在ビデオを返します。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `mode` | オーディオモード。`"single_speaker"` を選択すると1つのオーディオ入力を使用します。`"two_speakers"` を選択すると、以下にリストされている2人目の話者入力が追加されます。 | DYNAMIC_COMBO | はい | `"single_speaker"`<br>`"two_speakers"` |
| `model` | パッチ適用対象のベースビデオ拡散モデル。 | MODEL | はい | - |
| `model_patch` | オーディオ投影レイヤーを含むモデルパッチ。 | MODELPATCH | はい | - |
| `positive` | ビデオ生成をガイドするために使用されるポジティブ条件付け。 | CONDITIONING | はい | - |
| `negative` | ビデオ生成をガイドするために使用されるネガティブ条件付け。 | CONDITIONING | はい | - |
| `vae` | 画像と前フレームを潜在空間にエンコードするために使用されるVAE。 | VAE | はい | - |
| `width` | 生成するビデオの幅（ピクセル単位）。16の倍数で指定します。（デフォルト: 832） | INT | はい | 16 - MAX_RESOLUTION (step 16) |
| `height` | 生成するビデオの高さ（ピクセル単位）。16の倍数で指定します。（デフォルト: 480） | INT | はい | 16 - MAX_RESOLUTION (step 16) |
| `length` | 生成するフレーム数。（デフォルト: 81） | INT | はい | 1 - MAX_RESOLUTION (step 4) |
| `audio_encoder_output_1` | 1人目の話者に対するオーディオエンコーダ出力。条件付けに使用されるオーディオ特徴量が含まれます。 | AUDIOENCODEROUTPUT | はい | - |
| `start_image` | オプションの開始画像。ビデオの冒頭を初期化するために使用されます。`width` と `height` にリサイズされます。 | IMAGE | いいえ | - |
| `clip_vision_output` | オプションのCLIPビジョン出力。ポジティブ条件付けとネガティブ条件付けの両方に追加されます。 | CLIPVISIONOUTPUT | いいえ | - |
| `motion_frame_count` | モーションコンテキストとして使用する前フレームの数。（デフォルト: 9） | INT | はい | 1 - 33 (step 1) |
| `audio_scale` | オーディオ条件付けに適用されるスケーリング係数。（デフォルト: 1.0） | FLOAT | はい | -10.0 - 10.0 (step 0.01) |
| `previous_frames` | オプションの前ビデオフレーム。既存のシーケンスを拡張するために使用されます。ノードは最後の `motion_frame_count` フレームをモーションコンテキストとして使用します。 | IMAGE | いいえ | - |

### シングルスピーカー入力

`single_speaker` を選択しても、追加の入力は追加されません。

### ツースピーカー入力

これらの入力は、`mode` が `"two_speakers"` の場合に利用可能です。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | 2人目の話者に対するオーディオエンコーダ出力。指定する場合、`mask_1` と `mask_2` も指定する必要があります。 | AUDIOENCODEROUTPUT | いいえ | - |
| `mask_1` | 1人目の話者のマスク。2つのオーディオ入力を使用する場合に必要です。 | MASK | いいえ | - |
| `mask_2` | 2人目の話者のマスク。2つのオーディオ入力を使用する場合に必要です。 | MASK | いいえ | - |

**パラメータ制約：**

- `audio_encoder_output_2` が指定されている場合、`mask_1` と `mask_2` の両方も指定する必要があります。
- `mask_1` と `mask_2` の両方が指定されている場合、`audio_encoder_output_2` も指定する必要があります。
- `previous_frames` が指定されている場合、`motion_frame_count` で指定されたフレーム数以上のフレームを含む必要があります。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | オーディオ条件付けとサンプリングラッパーが適用されたパッチ適用済みモデル。 | MODEL |
| `positive` | 開始画像やCLIPビジョンコンテキストで変更される可能性のあるポジティブ条件付け。 | CONDITIONING |
| `negative` | 開始画像やCLIPビジョンコンテキストで変更される可能性のあるネガティブ条件付け。 | CONDITIONING |
| `latent` | 生成するビデオを表すゼロ初期化された潜在テンソル。 | LATENT |
| `trim_image` | 前フレームから拡張する際に先頭からトリミングするフレーム数。新しいシーケンスを開始する場合は0。 | INT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
