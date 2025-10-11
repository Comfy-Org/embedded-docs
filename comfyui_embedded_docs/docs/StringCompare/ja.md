> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/ja.md)

StringCompareノードは、2つのテキスト文字列を様々な比較方法で比較します。一方の文字列がもう一方で始まるか、終わるか、または両方の文字列が完全に等しいかをチェックできます。比較は、大文字と小文字の違いを考慮するかどうかを選択して実行できます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | はい | - | 比較する最初の文字列 |
| `string_b` | STRING | はい | - | 比較対象の2番目の文字列 |
| `mode` | COMBO | はい | "Starts With"<br>"Ends With"<br>"Equal" | 使用する比較方法 |
| `case_sensitive` | BOOLEAN | いいえ | - | 比較時に大文字と小文字を区別するかどうか（デフォルト: true） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | BOOLEAN | 比較条件が満たされた場合はtrue、それ以外の場合はfalseを返します |