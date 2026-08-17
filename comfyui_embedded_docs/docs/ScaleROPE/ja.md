# ROPEスケーリング

ScaleROPEノードは、モデルのRotary Position Embedding（ROPE）を変更し、そのX、Y、T（時間）コンポーネントに個別のスケーリング係数とシフト値を適用します。これは、モデルの位置エンコーディングの動作を調整するための高度で実験的なノードです。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | ROPEパラメータが変更されるモデルです。 | MODEL | はい | - |
| `scale_x` | ROPEのXコンポーネントに適用するスケーリング係数です（デフォルト：1.0）。 | FLOAT | はい | 0.0 - 100.0 (step 0.1) |
| `shift_x` | ROPEのXコンポーネントに適用するシフト値です（デフォルト：0.0）。 | FLOAT | はい | -256.0 - 256.0 (step 0.1) |
| `scale_y` | ROPEのYコンポーネントに適用するスケーリング係数です（デフォルト：1.0）。 | FLOAT | はい | 0.0 - 100.0 (step 0.1) |
| `shift_y` | ROPEのYコンポーネントに適用するシフト値です（デフォルト：0.0）。 | FLOAT | はい | -256.0 - 256.0 (step 0.1) |
| `scale_t` | ROPEのT（時間）コンポーネントに適用するスケーリング係数です（デフォルト：1.0）。 | FLOAT | はい | 0.0 - 100.0 (step 0.1) |
| `shift_t` | ROPEのT（時間）コンポーネントに適用するシフト値です（デフォルト：0.0）。 | FLOAT | はい | -256.0 - 256.0 (step 0.1) |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | 新しいROPEスケーリングおよびシフトパラメータが適用されたモデルです。 | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/ja.md)

---
**Source fingerprint (SHA-256):** `5d5ab0182b78c8c12ceaf44685a91e666ce15fa099fd194e3605bbdb9cc3c961`
