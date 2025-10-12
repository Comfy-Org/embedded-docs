> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/ja.md)

Kling Single Image Video Effect Nodeは、単一の参照画像に基づいてさまざまな特殊効果を持つ動画を作成します。静的な画像を動的な動画コンテンツに変換するために、様々な視覚効果とシーンを適用します。このノードは、異なるエフェクトシーン、モデルオプション、動画の長さをサポートしており、目的の視覚的結果を達成することができます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | はい | - | 参照画像。URLまたはBase64エンコードされた文字列（data:imageプレフィックスなし）。ファイルサイズは10MBを超えず、解像度は300*300px以上、アスペクト比は1:2.5 ～ 2.5:1の間である必要があります。 |
| `effect_scene` | COMBO | はい | KlingSingleImageEffectsSceneからのオプション | 動画生成に適用する特殊効果シーンのタイプ |
| `model_name` | COMBO | はい | KlingSingleImageEffectModelNameからのオプション | 動画エフェクトの生成に使用する特定のモデル |
| `duration` | COMBO | はい | KlingVideoGenDurationからのオプション | 生成される動画の長さ |

**注意:** `effect_scene`、`model_name`、`duration`の具体的なオプションは、それぞれの列挙型クラス（KlingSingleImageEffectsScene、KlingSingleImageEffectModelName、KlingVideoGenDuration）で利用可能な値によって決定されます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `video_id` | VIDEO | エフェクトが適用された生成動画 |
| `duration` | STRING | 生成された動画の一意の識別子 |
| `duration` | STRING | 生成された動画の長さ |