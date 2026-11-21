# Rodin 3D Gen-2.5 - テキストから3D生成

## 概要

Rodin Gen-2.5 API を使用して、テキストプロンプトから 3D モデルを生成します。生成速度と出力品質のバランスを取るため、異なる品質モード（Fast、Regular、Extreme-High）から選択できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 3D モデル用のテキストプロンプトです。 | STRING | はい | 1～1024 文字 |
| `mode` | 生成品質と速度のモードです。「Fast」は最速で、「Extreme-High」は最も高品質ですが時間がかかります。 | COMBO | はい | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | 生成される 3D モデルのマテリアルスタイルです。 | COMBO | はい | `"PBR"`<br>`"Matte"`<br>`"Shiny"` |
| `geometry_file_format` | 出力される 3D モデルのファイル形式です。 | COMBO | はい | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `texture_mode` | テクスチャ生成モードです。「None」はテクスチャを生成せず、「Generated」は標準テクスチャを生成し、「Generated+HD」は高精細テクスチャを生成します。 | COMBO | はい | `"None"`<br>`"Generated"`<br>`"Generated+HD"` |
| `seed` | 再現性のある結果を得るための乱数シードです。同じ入力で同じシードを使用すると、同じ出力が生成されます。 | INT | はい | 0～2147483647 |
| `TAPose` | 生成されるモデルに T ポーズ（腕を広げた姿勢）を適用するかどうか。 | BOOLEAN | はい | True または False |
| `hd_texture` | モデル用の高精細テクスチャを生成するかどうか。 | BOOLEAN | はい | True または False |
| `texture_delight` | モデルにテクスチャ delight（テクスチャ品質の向上）を適用するかどうか。 | BOOLEAN | はい | True または False |
| `addon_highpack` | 標準モデルに加えて、高ポリゴンバージョンのモデルを生成するかどうか。 | BOOLEAN | はい | True または False |
| `bbox_width` | ワールド単位でのバウンディングボックスの幅です。 | INT | はい | 1～1000 |
| `bbox_height` | ワールド単位でのバウンディングボックスの高さです。 | INT | はい | 1～1000 |
| `bbox_length` | ワールド単位でのバウンディングボックスの長さです。 | INT | はい | 1～1000 |
| `height_cm` | 生成されるモデルの高さ（センチメートル）です。 | INT | はい | 1～300 |

**注:** `prompt` パラメータは 1～1024 文字の長さである必要があります。`seed` パラメータは指定しない場合、デフォルトで 0（ランダム）になります。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `model_file` | 指定された形式で生成された 3D モデルファイルです。 | FILE3DANY |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/ja.md)

---
**Source fingerprint (SHA-256):** `95d5faa36298f09f0ae4dcda95dfd8913ebb393bb5934ae2c4622acfe79c85d6`
