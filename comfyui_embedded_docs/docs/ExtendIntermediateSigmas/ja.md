# ExtendIntermediateSigmas

The `ExtendIntermediateSigmas` ノードは、既存のシグマ値のシーケンスを受け取り、その間に追加の中間シグマ値を挿入します。追加するステップ数、補間の間隔方法、および拡張を行うシグマシーケンスの範囲を制御するオプションの開始・終了シグマ境界を指定できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `sigmas` | 中間値で拡張する入力シグマシーケンス | SIGMAS | はい | - |
| `steps` | 既存のシグマ間に挿入する中間ステップ数。N ステップの場合、対象となる各ペア間に N-1 個の中間シグマ値が挿入されます（デフォルト: 2） | INT | はい | 1 ～ 100 |
| `start_at_sigma` | 拡張の上限シグマ境界。この値以下のシグマのみが拡張対象となります（デフォルト: -1.0。無限大を意味します） | FLOAT | はい | -1.0 ～ 20000.0 |
| `end_at_sigma` | 拡張の下限シグマ境界。この値以上のシグマのみが拡張対象となります（デフォルト: 12.0） | FLOAT | はい | 0.0 ～ 20000.0 |
| `spacing` | 中間シグマ値の間隔を決定する補間方法。"linear" は等間隔に配置し、"cosine" と "sine" は曲線的な間隔を適用します（デフォルト: "linear"） | COMBO | はい | `"linear"`<br>`"cosine"`<br>`"sine"` |

**注記:** このノードは、現在のシグマが `start_at_sigma` 以下かつ `end_at_sigma` 以上である既存のシグマペア間にのみ、中間シグマを挿入します。`start_at_sigma` が -1.0 の場合、無限大として扱われるため、`end_at_sigma` の下限境界のみが適用されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `sigmas` | 追加の中間値が挿入された拡張シグマシーケンス | SIGMAS |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/ja.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
