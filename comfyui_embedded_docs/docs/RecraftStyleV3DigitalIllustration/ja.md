> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/ja.md)

このノードは、Recraft APIで使用するスタイルを設定し、特に「digital_illustration」（デジタルイラストレーション）スタイルを選択します。オプションのサブスタイルを選択することで、生成される画像の芸術的な方向性をさらに細かく調整することができます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `サブスタイル` | STRING | いいえ | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` | 特定のタイプのデジタルイラストレーションを指定するためのオプションのサブスタイルです。選択されない場合は、基本の「digital_illustration」スタイルが使用されます。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | 選択された「digital_illustration」スタイルとオプションのサブスタイルを含む、設定済みのスタイルオブジェクトです。他のRecraft APIノードに渡す準備ができています。 |
