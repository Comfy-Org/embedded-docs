# 安定カスケード_ステージC_VAEエンコード

The StableCascade_StageC_VAEEncode ノードは、入力画像を VAE エンコーダーで処理し、Stable Cascade モデル用の潜在表現を生成します。まず、圧縮係数と VAE のダウンスケール比に基づいて画像をリサイズし、その後にリサイズされた画像をエンコードします。このノードは、ステージ C（実際のエンコード結果）とステージ B（ゼロ埋めされたプレースホルダー）の 2 つの潜在テンソルを出力します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `image` | 潜在空間にエンコードされる入力画像です。 | IMAGE | 必須 | - |
| `vae` | 画像のエンコードに使用する VAE モデルです。 | VAE | 必須 | - |
| `compression` | エンコード前に画像に適用される圧縮係数です。画像の寸法はこの値で除算され、その後 VAE のダウンスケール比が乗算されます。（デフォルト: 42） | INT | 任意 | 4-128 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `stage_c` | Stable Cascade モデルのステージ C 用にエンコードされた潜在表現です。 | LATENT |
| `stage_b` | ステージ B 用のプレースホルダー潜在表現です。現在は、入力画像サイズから計算された寸法を持つゼロ埋めテンソルを返します。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/ja.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
