> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/ja.md)

以下が翻訳結果です。

Resolution Selector ノードは、選択したアスペクト比と目標とする総メガピクセル数に基づいて、画像のピクセル幅と高さを計算します。これは、Empty Latent Image ノードなど、他のノードで一貫した寸法を生成するのに便利です。出力される寸法は、常に最も近い8の倍数に丸められます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `aspect_ratio` | COMBO | はい | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` | 出力寸法のアスペクト比（デフォルト: `"SQUARE"`）。 |
| `megapixels` | FLOAT | はい | 0.1 - 16.0 | 目標とする総メガピクセル数。1.0 MP は正方形のアスペクト比で約 1024×1024 に相当します（デフォルト: 1.0）。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `width` | INT | 計算されたピクセル幅。8の倍数です。 |
| `height` | INT | 計算されたピクセル高さ。8の倍数です。 |