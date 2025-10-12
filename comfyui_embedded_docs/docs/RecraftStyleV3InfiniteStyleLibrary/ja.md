> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/ja.md)

このノードを使用すると、既存のUUIDを使用してRecraftのInfinite Style Libraryからスタイルを選択できます。提供されたスタイル識別子に基づいてスタイル情報を取得し、他のRecraftノードで使用するために返します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `style_id` | STRING | はい | 有効なUUID | Infinite Style LibraryからのスタイルのUUID。 |

**注意:** `style_id`入力は空にできません。空の文字列が提供された場合、ノードは例外を発生させます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | RecraftのInfinite Style Libraryから選択されたスタイルオブジェクト |
