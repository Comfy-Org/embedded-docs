# モデルサンプリングフラックス

The ModelSamplingFlux ノードは、画像寸法に基づいてシフトパラメータを計算し、指定されたモデルに Flux モデルサンプリングを適用します。指定された幅・高さ・シフトパラメータに応じてモデルの動作を調整する専用のサンプリング構成を作成し、新しいサンプリング設定が適用された変更済みモデルを返します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | Flux サンプリングを適用するモデル | MODEL | はい | - |
| `max_shift` | サンプリング計算の最大シフト値（デフォルト: 1.15） | FLOAT | はい | 0.0 - 100.0 |
| `base_shift` | サンプリング計算のベースシフト値（デフォルト: 0.5） | FLOAT | はい | 0.0 - 100.0 |
| `width` | 対象画像の幅（ピクセル単位）（デフォルト: 1024） | INT | はい | 16 - MAX_RESOLUTION |
| `height` | 対象画像の高さ（ピクセル単位）（デフォルト: 1024） | INT | はい | 16 - MAX_RESOLUTION |

実効シフト値は、`width` と `height` から導出される潜在サイズに基づいて、`base_shift` と `max_shift` の間で補間されます。`step` 値は、`max_shift` と `base_shift` では 0.01、`width` と `height` では 8 です。`max_shift` と `base_shift` パラメータは、ユーザーインターフェースで高度なオプションとしてマークされています。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | Flux サンプリング構成が適用された変更済みモデル | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/ja.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
