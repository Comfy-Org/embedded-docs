# EmptyAceStepLatentAudio

EmptyAceStepLatentAudio ノードは、指定された長さの空の潜在オーディオサンプルを作成します。ゼロで満たされた無音のオーディオ潜在変数のバッチを生成します。その長さは、入力された秒数とオーディオ処理パラメータに基づいて計算されます。このノードは、潜在表現を必要とするオーディオ処理ワークフローの初期化に役立ちます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `seconds` | オーディオの長さ（秒単位）。デフォルトは 120.0。 | FLOAT | はい | 1.0 - 1000.0 (step 0.1) |
| `batch_size` | バッチ内の潜在画像の数。デフォルトは 1。 | INT | はい | 1 - 4096 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `output` | ゼロが含まれる空の潜在オーディオサンプルを返します。出力には `samples` テンソルと、`type` フィールド（"audio" に設定）が含まれます。 | LATENT |

注：潜在の長さは、内部サンプルレート 44100 Hz を使用して `seconds` の値から導出され、`int(seconds × 44100 / 512 / 8)` フレームとして計算されます。結果の潜在テンソルは完全にゼロで満たされます。

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/ja.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
