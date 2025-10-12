> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/ja.md)

Kling Dual Character Video Effect Nodeは、選択されたシーンに基づいて特殊効果を施した動画を作成します。2枚の画像を受け取り、1枚目の画像を左側、2枚目の画像を右側に配置した合成動画を生成します。選択されたエフェクトシーンに応じて、異なる視覚効果が適用されます。

## 入力パラメータ

| パラメータ名 | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `image_left` | IMAGE | はい | - | 左側の画像 |
| `image_right` | IMAGE | はい | - | 右側の画像 |
| `effect_scene` | COMBO | はい | 複数のオプションから選択可能 | 動画生成に適用する特殊効果シーンの種類 |
| `model_name` | COMBO | いいえ | 複数のオプションから選択可能 | キャラクター効果に使用するモデル（デフォルト: "kling-v1"） |
| `mode` | COMBO | いいえ | 複数のオプションから選択可能 | 動画生成モード（デフォルト: "std"） |
| `duration` | COMBO | はい | 複数のオプションから選択可能 | 生成される動画の長さ |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `duration` | VIDEO | デュアルキャラクター効果が適用された生成動画 |
| `duration` | STRING | 生成された動画の長さ情報 |