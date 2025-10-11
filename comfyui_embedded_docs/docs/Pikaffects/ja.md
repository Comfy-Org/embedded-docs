> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/ja.md)

Pikaffectsノードは、入力画像にさまざまなビジュアルエフェクトを適用して動画を生成します。このノードはPikaの動画生成APIを使用し、静止画像を、溶ける、爆発する、浮遊するなどの特定のエフェクトが適用されたアニメーション動画に変換します。ノードを使用するには、PikaサービスにアクセスするためのAPIキーと認証トークンが必要です。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | はい | - | Pikaffectを適用する参照画像。 |
| `pikaffect` | COMBO | はい | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" | 画像に適用する特定のビジュアルエフェクト（デフォルト: "Cake-ify"）。 |
| `prompt_text` | STRING | はい | - | 動画生成を導くテキストによる説明。 |
| `negative_prompt` | STRING | はい | - | 生成される動画で避けるべき内容のテキストによる説明。 |
| `seed` | INT | はい | 0 ～ 4294967295 | 再現可能な結果を得るためのランダムシード値。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 適用されたPikaffectを持つ生成された動画。 |