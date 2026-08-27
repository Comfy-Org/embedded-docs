# Trellis2Conditioning

Trellis2Conditioning は、入力画像を TRELLIS.2 モデル用の条件付けデータに変換します。CLIP ビジョンモデルを使用して画像を 2 セットの特徴（512 および 1024 スケール）にエンコードし、それらをポジティブ条件付けペアとしてパッケージ化します。また、空の参照として機能する、対応するゼロ埋めのネガティブ条件付けペアも作成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | 画像を条件付け特徴にエンコードするために使用される CLIP ビジョンモデル。 | CLIP_VISION | はい | 利用可能な任意の CLIP ビジョンモデル |
| `image` | ImageCropToMask から前処理された画像（TRELLIS.2 の場合は pad_factor=1.0）。 | IMAGE | はい | 任意の画像 |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `positive` | 512 および 1024 スケールでエンコードされた画像特徴を含む条件付け。TRELLIS.2 モデルのポジティブ条件付けとして使用されます。 | CONDITIONING |
| `negative` | ポジティブ条件付けと同じ形状を持つゼロ埋めの条件付け。空のネガティブ参照として使用されます。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/ja.md)

---
**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`
