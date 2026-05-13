> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/ja.md)

WanInfiniteTalkToVideo ノードは、音声入力からビデオシーケンスを生成します。このノードは、1人または2人の話者から抽出された音声特徴量を条件として、ビデオ拡散モデルを使用し、トーキングヘッドビデオの潜在表現を生成します。新しいシーケンスを生成することも、モーションコンテキストとして以前のフレームを使用して既存のシーケンスを拡張することもできます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `mode` | COMBO | はい | `"single_speaker"`<br>`"two_speakers"` | 音声入力モード。`"single_speaker"` は1つの音声入力を使用します。`"two_speakers"` は2人目の話者と対応するマスクの入力を有効にします。 |
| `model` | MODEL | はい | - | ベースとなるビデオ拡散モデル。 |
| `model_patch` | MODELPATCH | はい | - | 音声投影レイヤーを含むモデルパッチ。 |
| `positive` | CONDITIONING | はい | - | 生成をガイドするポジティブ条件付け。 |
| `negative` | CONDITIONING | はい | - | 生成をガイドするネガティブ条件付け。 |
| `vae` | VAE | はい | - | 画像を潜在空間にエンコードし、潜在空間からデコードするために使用されるVAE。 |
| `width` | INT | いいえ | 16 - MAX_RESOLUTION | 出力ビデオの幅（ピクセル単位）。16で割り切れる必要があります。（デフォルト: 832） |
| `height` | INT | いいえ | 16 - MAX_RESOLUTION | 出力ビデオの高さ（ピクセル単位）。16で割り切れる必要があります。（デフォルト: 480） |
| `length` | INT | いいえ | 1 - MAX_RESOLUTION | 生成するフレーム数。（デフォルト: 81） |
| `clip_vision_output` | CLIPVISIONOUTPUT | いいえ | - | 追加の条件付けのためのオプションのCLIPビジョン出力。 |
| `start_image` | IMAGE | いいえ | - | ビデオシーケンスを初期化するためのオプションの開始画像。 |
| `audio_encoder_output_1` | AUDIOENCODEROUTPUT | はい | - | 最初の話者の特徴量を含むプライマリ音声エンコーダ出力。 |
| `motion_frame_count` | INT | いいえ | 1 - 33 | シーケンスを拡張する際にモーションコンテキストとして使用する過去のフレーム数。（デフォルト: 9） |
| `audio_scale` | FLOAT | いいえ | -10.0 - 10.0 | 音声条件付けに適用されるスケーリング係数。（デフォルト: 1.0） |
| `previous_frames` | IMAGE | いいえ | - | 拡張元となるオプションの以前のビデオフレーム。 |
| `audio_encoder_output_2` | AUDIOENCODEROUTPUT | いいえ | - | 2番目の音声エンコーダ出力。`mode` が `"two_speakers"` に設定されている場合に必須です。 |
| `mask_1` | MASK | いいえ | - | 最初の話者のマスク。2つの音声入力を使用する場合に必須です。 |
| `mask_2` | MASK | いいえ | - | 2番目の話者のマスク。2つの音声入力を使用する場合に必須です。 |

**パラメータ制約:**

* `mode` が `"two_speakers"` に設定されている場合、パラメータ `audio_encoder_output_2`、`mask_1`、`mask_2` が必須になります。
* `audio_encoder_output_2` が指定された場合、`mask_1` と `mask_2` の両方も指定する必要があります。
* `mask_1` と `mask_2` が指定された場合、`audio_encoder_output_2` も指定する必要があります。
* `previous_frames` が指定された場合、`motion_frame_count` で指定された数以上のフレームが含まれている必要があります。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model` | MODEL | 音声条件付けが適用されたパッチ済みモデル。 |
| `positive` | CONDITIONING | 追加コンテキスト（開始画像、CLIPビジョンなど）で変更される可能性のあるポジティブ条件付け。 |
| `negative` | CONDITIONING | 追加コンテキストで変更される可能性のあるネガティブ条件付け。 |
| `latent` | LATENT | 潜在空間で生成されたビデオシーケンス。 |
| `trim_image` | INT | シーケンスを拡張する際に、モーションコンテキストの先頭からトリミングする必要があるフレーム数。 |

---
**Source fingerprint (SHA-256):** `6bb976da5cac0b61edb7d4c9d206c7c7ea9ffc0e982034c23c7f2e891e972888`
