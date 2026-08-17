# PiD コンディショニング

潜在イメージと劣化シグマ値を CONDITIONING データに添付します。これは PiD（Pixel-in-Detail）デコードやアップスケーリングに使用され、処理前に潜在イメージをどの程度劣化させるかを制御できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 潜在イメージと劣化シグマを添付する CONDITIONING データです。 | CONDITIONING | はい | - |
| `latent` | CONDITIONING に添付する潜在イメージ（VAEEncode または KSampler から取得したもの）です。 | LATENT | はい | - |
| `latent_format` | 潜在イメージの形式です。Flux1（16チャンネル）と Flux2（128チャンネル）の潜在イメージは、「flux」ではチャンネル次元から自動検出されます。SD3（16チャンネル）、SDXL（4チャンネル）、QwenImage（16チャンネル）の場合は手動で選択してください（デフォルト："flux"）。 | COMBO | はい | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | 0 はクリーンな潜在イメージです。破損した潜在出力のノイズを除去するには、値を増やします（デフォルト：0.0）。 | FLOAT | はい | 0.0 から 1.0（ステップ：0.01） |

注：`latent_format` が "flux" の場合、ノードは潜在イメージのチャンネル次元に基づいて、Flux1（16チャンネル）か Flux2（128チャンネル）かを自動的に検出します。処理対象の潜在イメージが5次元の場合、最後の次元に沿った最初のスライスのみが使用されます。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 潜在イメージと劣化シグマ値が添付された元の CONDITIONING データです。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/ja.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
