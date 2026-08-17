# WanAnimateToVideo

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | 生成を望ましいコンテンツへ導くためのポジティブ conditioning です。 | CONDITIONING | 必須 | - |
| `negative` | 望ましくないコンテンツから生成を遠ざけるためのネガティブ conditioning です。 | CONDITIONING | 必須 | - |
| `vae` | 画像データのエンコードとデコードに使用される VAE モデルです。 | VAE | 必須 | - |
| `width` | 出力ビデオの幅（ピクセル単位）です（デフォルト: 832、ステップ: 16）。 | INT | 必須 | 16 to MAX_RESOLUTION |
| `height` | 出力ビデオの高さ（ピクセル単位）です（デフォルト: 480、ステップ: 16）。 | INT | 必須 | 16 to MAX_RESOLUTION |
| `length` | 生成するフレーム数です（デフォルト: 77、ステップ: 4）。 | INT | 必須 | 1 to MAX_RESOLUTION |
| `batch_size` | 1 バッチで生成するビデオの本数です（デフォルト: 1）。 | INT | 必須 | 1 to 4096 |
| `clip_vision_output` | ポジティブ conditioning とネガティブ conditioning の両方に追加の conditioning として使用される、オプションの CLIP vision モデル出力です。 | CLIP_VISION_OUTPUT | 任意 | - |
| `reference_image` | 生成の開始点として使用される参照画像です。指定しない場合は、黒画像（すべてゼロ）が使用されます。 | IMAGE | 任意 | - |
| `face_video` | 顔の表情のガイドを提供するビデオです。処理時に 512x512 にリサイズされ、-1.0 から 1.0 の範囲に正規化されます。 | IMAGE | 任意 | - |
| `pose_video` | ポーズとモーションのガイドを提供するビデオです。`length` より短い場合、最後のフレームでパディングされます。 | IMAGE | 任意 | - |
| `continue_motion_max_frames` | 前回のモーションから継続する最大フレーム数です。`continue_motion` の最後のこのフレーム数だけが使用されます（デフォルト: 5、ステップ: 4）。 | INT | 必須 | 1 to MAX_RESOLUTION |
| `background_video` | 生成されたコンテンツと合成する背景ビデオです。 | IMAGE | 任意 | - |
| `character_mask` | 選択的処理のためのキャラクター領域を定義するマスクです。マスクが 1 フレームのみの場合は、全フレームで繰り返されます。 | MASK | 任意 | - |
| `continue_motion` | ビデオを延長する際に時間的一貫性を維持するために使用される、以前のモーションシーケンスです。最後の `continue_motion_max_frames` フレームのみが使用されます。 | IMAGE | 任意 | - |
| `video_frame_offset` | すべての入力ビデオでシークするフレーム数です。チャンク単位で長いビデオを生成するために使用します。ビデオを延長するには、前のノードの `video_frame_offset` 出力に接続します（デフォルト: 0、ステップ: 1）。 | INT | 必須 | 0 to MAX_RESOLUTION |

**パラメータの制約:**

- `pose_video` が指定された場合、`length` に一致するように、短いポーズビデオは最後のフレームでパディングされます。ソースには、現在無効化されている `trim_to_pose_video` フラグがあり、これを有効にすると、ポーズビデオの長さに合わせて出力を短縮します。
- `face_video` は 512x512 にリサイズされ、-1.0 から 1.0 の範囲に正規化されます。
- `continue_motion` は、最後の `continue_motion_max_frames` フレームに制限されます。`continue_motion` を使用する場合、`video_frame_offset` は取得したフレーム数だけ減少しますが、0 未満にはなりません。
- 入力ビデオ（`face_video`、`pose_video`、`background_video`、`character_mask`）は、`video_frame_offset` によってオフセットされます。オフセットがこれらの長さ以上の場合、その入力は無視されます。ただし、単一フレームの `character_mask` は常に繰り返されるため例外です。
- `clip_vision_output` が指定された場合、ポジティブ conditioning とネガティブ conditioning の両方に適用されます。
- `reference_image` が指定されない場合、黒画像（すべてゼロ）が参照として使用されます。
- `continue_motion` が指定されない場合、モーション部分にはピクセル値 0.5 のグレーフレームが使用されます。
- `width` と `height` はステップ 16 を使用します。対応する潜在的な次元は `width / 8` と `height / 8` です。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | 変更されたポジティブ conditioning です。連結された潜在画像と連結されたマスクを常に含みます。`clip_vision_output`、`pose_video`、`face_video` が指定されている場合は、それらの値も追加されます。 | CONDITIONING |
| `negative` | 変更されたネガティブ conditioning です。連結された潜在画像と連結されたマスクを常に含みます。`clip_vision_output`、`pose_video`、`face_video` が指定されている場合は、それらの値も追加されます。なお、顔ビデオのピクセルは -1.0 に設定されます。 | CONDITIONING |
| `latent` | ゼロで初期化された空の潜在テンソルです。形状は `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]` です。 | LATENT |
| `trim_latent` | 参照画像の潜在フレームに対応する、先頭から切り取る潜在フレーム数です。 | INT |
| `trim_image` | 参照モーションフレームに対応する、先頭から切り取る画像フレーム数です。 | INT |
| `video_frame_offset` | チャンク単位のビデオ生成用に更新されたフレームオフセットです。調整後の入力オフセットに生成された長さを加えた値になります。 | INT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
