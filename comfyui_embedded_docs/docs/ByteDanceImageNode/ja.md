> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/ja.md)

ByteDance Imageノードは、テキストプロンプトに基づいてAPI経由でByteDanceモデルを使用して画像を生成します。異なるモデルの選択、画像サイズの指定、シードやガイダンススケールなどの様々な生成パラメータの制御が可能です。このノードはByteDanceの画像生成サービスに接続し、作成された画像を返します。

## 入力

| パラメータ | データ型 | 入力タイプ | デフォルト | 範囲 | 説明 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedream_3 | Text2ImageModelNameオプション | モデル名 |
| `prompt` | STRING | STRING | - | - | 画像生成に使用するテキストプロンプト |
| `size_preset` | STRING | COMBO | - | RECOMMENDED_PRESETSラベル | 推奨サイズを選択します。カスタムを選択すると、以下の幅と高さを使用します |
| `width` | INT | INT | 1024 | 512-2048（ステップ64） | 画像のカスタム幅。`size_preset`が`Custom`に設定されている場合にのみ有効です |
| `height` | INT | INT | 1024 | 512-2048（ステップ64） | 画像のカスタム高さ。`size_preset`が`Custom`に設定されている場合にのみ有効です |
| `seed` | INT | INT | 0 | 0-2147483647（ステップ1） | 生成に使用するシード（オプション） |
| `guidance_scale` | FLOAT | FLOAT | 2.5 | 1.0-10.0（ステップ0.01） | 値を高くすると、画像がプロンプトにより忠実になります（オプション） |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 画像に「AI生成」の透かしを追加するかどうか（オプション） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | ByteDance APIから生成された画像 |
