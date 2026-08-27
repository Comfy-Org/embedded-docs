# Pixal3DConditioning

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision モデル。 | CLIP_VISION | はい | — |
| `image` | ImageCropToMask で前処理済みの画像（Pixal3D では pad_factor=1.1）。 | IMAGE | はい | — |
| `camera_angle_x` | 水平方向の画角（度）。表示名は fov。画像ごとの FoV を設定するには MoGeGeometryToFOV（axis='horizontal'、unit='degrees'）を接続します（アップストリームのデフォルトと一致）。デフォルト: 49.13。 | FLOAT | はい | 1.0 – 170.0 |

注: `camera_angle_x` の値は内部でラジアンに変換され、投影変換行列のカメラ距離の計算に使用されます。指定されたビジョンモデルに NAF コンポーネントが含まれている場合、このノードはさらにシェイプステージとテクスチャステージ用の高解像度フィーチャマップを生成します。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `positive` | 画像由来のフィーチャマップと Trellis2 生成用の投影データを含むポジティブ conditioning。 | CONDITIONING |
| `negative` | ゼロ埋めされた特徴テンソルを含むネガティブ conditioning。classifier-free guidance に使用されます。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/ja.md)

---
**Source fingerprint (SHA-256):** `3eba711620f6c56a21bbf7df89f8d406ce6f90908298b1a295a1dbbddd042472`
