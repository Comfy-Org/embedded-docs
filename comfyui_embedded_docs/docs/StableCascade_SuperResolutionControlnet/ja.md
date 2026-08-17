# 安定カスケード_超解像Controlnet

StableCascade_SuperResolutionControlnet ノードは、Stable Cascade の超解像処理用の入力を準備します。入力画像を受け取り、VAE を使用してエンコードし、ControlNet 入力を生成します。また、Stable Cascade パイプラインのステージ C およびステージ B 用のプレースホルダー潜在表現も生成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `image` | 超解像処理用に入力される画像です。 | IMAGE | はい | - |
| `vae` | 入力画像のエンコードに使用される VAE モデルです。 | VAE | はい | - |

注：VAE によるエンコード時には、入力画像の最初の3つのカラーチャンネルのみが使用されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `controlnet_input` | ControlNet 入力に適したエンコード済み画像表現です。 | IMAGE |
| `stage_c` | Stable Cascade 処理のステージ C 用のプレースホルダー潜在表現です。次元は入力画像サイズを16で割った値に基づきます。 | LATENT |
| `stage_b` | Stable Cascade 処理のステージ B 用のプレースホルダー潜在表現です。次元は入力画像サイズを2で割った値に基づきます。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/ja.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
