> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/ja.md)

ImageRGBToYUV ノードは、RGB カラー画像を YUV 色空間に変換します。入力として RGB 画像を受け取り、それを Y（輝度）、U（青色投影）、V（赤色投影）の3つの個別のチャンネルに分離します。各出力チャンネルは、対応する YUV コンポーネントを表す個別のグレースケール画像として返されます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | はい | - | YUV 色空間に変換する入力 RGB 画像 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `Y` | IMAGE | YUV 色空間の輝度（明るさ）コンポーネント |
| `U` | IMAGE | YUV 色空間の青色投影コンポーネント |
| `V` | IMAGE | YUV 色空間の赤色投影コンポーネント |

---
**Source fingerprint (SHA-256):** `119cba119b62c7b46ffdd2c0feca932a9af1ec41c338fead23c21fdf76a6abb2`
