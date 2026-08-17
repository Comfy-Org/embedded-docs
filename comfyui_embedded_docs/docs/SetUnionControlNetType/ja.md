# Union ControlNetタイプを設定

SetUnionControlNetType ノードは、conditioning に使用するコントロールネットワークのコントロールタイプを設定できます。既存のコントロールネットワークを受け取り、その変更されたコピーを作成し、選択したコントロールタイプをそのコピーに保存するため、元のネットワークは変更されません。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `control_net` | 選択したコントロールタイプでコピーおよび変更するコントロールネットワーク | CONTROL_NET | はい | - |
| `type` | コピーしたコントロールネットワークに適用するコントロールタイプ。コントロールタイプを未設定のままにするには「auto」を選択し、利用可能なユニオンコントロールネットワークタイプから特定のタイプを選択します（デフォルト: "auto"） | COMBO | はい | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/scribble/ted"`<br>`"canny/softedge"`<br>`"normal/bms"`<br>`"seg"`<br>`"inpaint"`<br>`"lineart"`<br>`"s4"`<br>`"tile/color"`<br>`"blur"`<br>`"identity"` |

注：`type` が "auto" の場合、コピーしたコントロールネットワーク上のコントロールタイプリストはクリアされます。特定のタイプを選択した場合、コピーしたコントロールネットワークには対応するタイプ番号が保存されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `control_net` | 選択したコントロールタイプが適用された、コントロールネットワークの変更済みコピー | CONTROL_NET |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/ja.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
