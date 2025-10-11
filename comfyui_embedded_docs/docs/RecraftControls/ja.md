> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftControls/ja.md)

Recraft生成をカスタマイズするためのコントロールを作成します。このノードを使用すると、Recraft画像生成プロセスで使用されるカラー設定を構成できます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `colors` | COLOR | いいえ | - | メイン要素のカラー設定 |
| `background_color` | COLOR | いいえ | - | 背景色の設定 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `recraft_controls` | CONTROLS | カラー設定を含む構成済みのRecraftコントロール |