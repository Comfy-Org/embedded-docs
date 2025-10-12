> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/ja.md)

このノードは、RecraftのAPIで使用するためのリアルな画像スタイル設定を作成します。realistic_imageスタイルを選択し、さまざまなサブスタイルオプションから選択して出力の外観をカスタマイズすることができます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `サブスタイル` | STRING | はい | 複数のオプションが利用可能 | realistic_imageスタイルに適用する特定のサブスタイル。"None"に設定すると、サブスタイルは適用されません。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | realistic_imageスタイルと選択されたサブスタイル設定を含むRecraftスタイル設定オブジェクトを返します。 |