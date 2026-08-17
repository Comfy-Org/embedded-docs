# WanDancerVideo

WanDancerVideo は、WanDancer モデルによるビデオ生成のために、コンディショニングデータと空の潜在テンソルを準備します。ポジティブコンディショニングとネガティブコンディショニングを受け取り、オプションで開始画像、マスク、CLIPビジョン埋め込み、オーディオ特徴量を組み合わせて、生成されるビデオを制御します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | ビデオ生成をガイドするポジティブコンディショニング。 | CONDITIONING | はい |  |
| `negative` | ビデオ生成をガイドするネガティブコンディショニング。 | CONDITIONING | はい |  |
| `vae` | 開始画像を潜在空間にエンコードするために使用されるVAE。 | VAE | はい |  |
| `width` | 生成されるビデオの幅（ピクセル単位）（デフォルト: 480）。 | INT | はい | 16 to MAX_RESOLUTION (step: 16) |
| `height` | 生成されるビデオの高さ（ピクセル単位）（デフォルト: 832）。 | INT | はい | 16 to MAX_RESOLUTION (step: 16) |
| `length` | 生成されるビデオのフレーム数。WanDancer では 149 に保ってください（デフォルト: 149）。 | INT | はい | 1 to MAX_RESOLUTION (step: 4) |
| `clip_vision_output` | 最初のフレーム用のCLIPビジョン埋め込み。 | CLIP_VISION_OUTPUT | いいえ |  |
| `clip_vision_output_ref` | 参照画像用のCLIPビジョン埋め込み。 | CLIP_VISION_OUTPUT | いいえ |  |
| `start_image` | エンコードされる初期画像（複数可）。任意のフレーム数を指定できます。 | IMAGE | いいえ |  |
| `mask` | 開始画像に対するイメージコンディショニングマスク。白の領域は保持され、黒の領域は生成されます。ローカル生成に使用されます。 | MASK | いいえ |  |
| `audio_encoder_output` | オーディオエンコーダーの出力。オーディオコンディショニング付き生成のためのオーディオ特徴量、FPS、オーディオ注入スケールを提供します。 | AUDIO_ENCODER_OUTPUT | いいえ |  |

**パラメータの制約に関する注意事項：**
- `start_image` が指定された場合、`width` × `height` にリサイズされ、`length` フレームに制限された上でエンコードされ、連結マスクとともに両方のコンディショニングに添付される潜在テンソルになります。
- `mask` は、`start_image` も指定されている場合にのみ有効です。マスク内の白い領域は保持され、黒い領域は生成されます。`mask` が指定されていない場合、開始画像の領域はコンディショニングのガイドとして使用され、残りのフレームが生成されます。
- `clip_vision_output_ref` は、`clip_vision_output` が指定されている場合にのみ適用されます。
- `audio_encoder_output` は、オーディオ特徴量、FPS、オーディオ注入スケール（デフォルト: 1.0）を両方のコンディショニングに添付します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | 追加データ（連結潜在テンソル、CLIPビジョン、オーディオ）が添付されたポジティブコンディショニング。 | CONDITIONING |
| `negative` | 追加データ（連結潜在テンソル、CLIPビジョン、オーディオ）が添付されたネガティブコンディショニング。 | CONDITIONING |
| `latent` | 指定されたビデオの長さ、高さ、幅に一致する次元を持つ空の潜在テンソル。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/ja.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
