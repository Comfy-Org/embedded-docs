# SetFirstSigma

SetFirstSigma ノードは、シグマ値のシーケンスを変更し、シーケンスの最初のシグマ値をカスタム値に置き換えます。既存のシグマシーケンスと新しいシグマ値を入力として受け取り、最初の要素のみを変更し、他のすべてのシグマ値は変更しない新しいシグマシーケンスを返します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `sigmas` | 変更対象のシグマ値の入力シーケンス | SIGMAS | はい | - |
| `sigma` | シーケンスの最初の要素として設定する新しいシグマ値（デフォルト: 136.0） | FLOAT | はい | 0.0 to 20000.0 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `sigmas` | 最初の要素がカスタムシグマ値に置き換えられた、変更後のシグマシーケンス | SIGMAS |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/ja.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
