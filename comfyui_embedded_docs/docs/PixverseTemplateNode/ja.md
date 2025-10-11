> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/ja.md)

PixVerse Templateノードを使用すると、PixVerseの動画生成で利用可能なテンプレートから選択できます。このノードは、選択したテンプレート名を、PixVerse APIが動画作成に必要とする対応するテンプレートIDに変換します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `template` | STRING | はい | 複数のオプションが利用可能 | PixVerseの動画生成に使用するテンプレート。利用可能なオプションは、PixVerseシステム内で事前に定義されたテンプレートに対応します。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `pixverse_template` | INT | 選択したテンプレート名に対応するテンプレートID。他のPixVerseノードで動画生成に使用できます。 |