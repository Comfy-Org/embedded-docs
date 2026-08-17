# AutogrowNamesTestNode

このノードは、Autogrow入力機能のテスト用です。動的な数のfloat入力を受け取り、それぞれに特定の名前が付けられており、それらの値をカンマ区切りの単一の文字列に結合します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `autogrow` | 動的な入力グループです。リストにある「"a"」「"b"」「"c"」のいずれかの事前定義名を持つ複数のfloat入力を追加できます。このノードは、これらの名前付き入力の任意の組み合わせを受け入れます。 | FLOAT | はい | 該当なし |

**注記:** `autogrow` 入力は動的です。ワークフローに応じて、個々のfloat入力（「"a"」「"b"」「"c"」という名前）を必要に応じて追加または削除できます。ノードは指定されたすべての値を処理します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `output` | 指定されたすべてのfloat入力の値を、カンマで連結した単一の文字列です。 | STRING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/ja.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
