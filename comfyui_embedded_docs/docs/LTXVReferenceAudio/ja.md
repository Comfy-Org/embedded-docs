# LTXV Reference Audio (ID-LoRA)

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | アイデンティティガイダンスでパッチされるモデル。 | MODEL | 必須 | - |
| `positive` | ポジティブ conditioning 入力。 | CONDITIONING | 必須 | - |
| `negative` | ネガティブ conditioning 入力。 | CONDITIONING | 必須 | - |
| `reference_audio` | 話者アイデンティティの転送元となる参照音声クリップ。約5秒を推奨（トレーニング時間）。これより短い、または長いクリップでは、音声アイデンティティ転送の品質が低下する可能性があります。 | AUDIO | 必須 | - |
| `audio_vae` | エンコード用の LTXV Audio VAE。 | VAE | 必須 | - |
| `identity_guidance_scale` | アイデンティティガイダンスの強さ。話者アイデンティティを増強するため、各ステップで参照なしの追加フォワードパスを実行します。無効にするには 0 に設定します（追加パスなし）。（デフォルト: 3.0） | FLOAT | 任意 | 0.0 - 100.0 |
| `start_percent` | アイデンティティガイダンスが有効な sigma 範囲の開始位置。（デフォルト: 0.0） | FLOAT | 任意 | 0.0 - 1.0 |
| `end_percent` | アイデンティティガイダンスが有効な sigma 範囲の終了位置。（デフォルト: 1.0） | FLOAT | 任意 | 0.0 - 1.0 |

注記: アイデンティティガイダンスは、`start_percent` と `end_percent` で定義された範囲内の sigma 値に対してのみ有効です。この範囲外では、デノイズ済み出力は変更されません。参照音声は、ポジティブ conditioning とネガティブ conditioning の両方に追加されます。参照音声のサンプルレートが audio VAE のサンプルレートと異なる場合、VAE に合わせて音声は自動的にリサンプリングされます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | アイデンティティガイダンス機能でパッチされたモデル。 | MODEL |
| `positive` | エンコードされた参照音声データを含むようになったポジティブ conditioning。 | CONDITIONING |
| `negative` | エンコードされた参照音声データを含むようになったネガティブ conditioning。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/ja.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
