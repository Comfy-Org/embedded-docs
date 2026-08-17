# 画像ヒストグラム

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `image` | 解析する入力画像。ノードはバッチ内の最初の画像を処理します。 | IMAGE | はい | N/A |

## 出力

すべての出力ヒストグラムには、0 から 255 までの各輝度レベルに対応する 256 個の値が含まれます。

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `rgb` | 赤、緑、青の各チャンネルにおける平均ピクセル強度を表す複合ヒストグラム。 | HISTOGRAM |
| `luminance` | ITU-R BT.709 標準輝度式を使用して計算された、画像の知覚輝度のヒストグラム。 | HISTOGRAM |
| `red` | 赤色チャンネルにおけるピクセル強度の分布を示すヒストグラム。 | HISTOGRAM |
| `green` | 緑色チャンネルにおけるピクセル強度の分布を示すヒストグラム。 | HISTOGRAM |
| `blue` | 青色チャンネルにおけるピクセル強度の分布を示すヒストグラム。 | HISTOGRAM |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/ja.md)

---
**Source fingerprint (SHA-256):** `5020f5cedd325250a207a00950011f4b6dc19ddfe4d172665ffca4982731dd5e`
