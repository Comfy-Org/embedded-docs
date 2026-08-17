# LTXV 空のラテントオーディオ

LTXV Empty Latent Audio ノードは、空（ゼロで埋められた）潜在オーディオテンソルのバッチを作成します。提供された Audio VAE モデルの設定を使用して、チャンネル数や周波数ビンなど、潜在空間の正しい次元を決定します。オーディオ潜在変数の数は、Audio VAE モデルを使用してフレーム数とフレームレートから計算されます。この空の潜在変数は、ComfyUI 内でのオーディオ生成や操作ワークフローの開始点として機能します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `frames_number` | フレーム数。デフォルト: 97。 | INT | はい | 1 から 1000 |
| `frame_rate` | 1秒あたりのフレーム数。浮動小数点数または整数を受け入れます。デフォルト: 25.0。 | FLOAT (または INT) | はい | 1.0 から 1000.0 |
| `batch_size` | バッチ内の潜在オーディオサンプルの数。デフォルト: 1。 | INT | はい | 1 から 4096 |
| `audio_vae` | 設定を取得するための Audio VAE モデル。 | VAE | はい | 該当なし |

**注:** `audio_vae` 入力は必須です。提供されない場合、ノードはエラーを発生させます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `Latent` | 入力された Audio VAE に一致するように構成された、(batch_size, z_channels, num_audio_latents, audio_freq) 構造の空の潜在オーディオテンソル。出力には "audio" に設定された `type` フィールドも含まれます。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/ja.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
