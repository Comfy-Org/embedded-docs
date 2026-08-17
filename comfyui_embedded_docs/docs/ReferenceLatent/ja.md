# 参照潜在変数

このノードは、編集モデルのガイドとなる潜在変数を設定します。コンディショニングデータとオプションの潜在変数入力を受け取り、参照潜在変数情報を含むようにコンディショニングを変更します。モデルが対応している場合、複数のReferenceLatentノードを連結して、複数の参照画像を設定できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `conditioning` | 参照潜在変数情報で変更されるコンディショニングデータ | CONDITIONING | はい | - |
| `latent` | 編集モデルの参照として使用するオプションの潜在変数データ | LATENT | いいえ | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `output` | 参照潜在変数情報を含む、変更されたコンディショニングデータ | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/ja.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
