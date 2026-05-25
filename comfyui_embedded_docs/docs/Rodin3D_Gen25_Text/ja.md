> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/ja.md)

## 概要

Rodin Gen-2.5 APIを使用して、テキストプロンプトから3Dモデルを生成します。生成速度と出力品質のバランスを調整するために、異なる品質モード（Fast、Regular、Extreme-High）から選択できます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | はい | 最大2500文字 | 生成したい3Dモデルを説明するテキストプロンプト。 |
| `mode` | COMBO | はい | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` | 生成品質と速度のモード。"Fast"が最も速く、"Extreme-High"は最高品質ですが時間がかかります。 |
| `material` | COMBO | はい | `"PBR"`<br>`"Matte"`<br>`"Shiny"` | 生成される3Dモデルのマテリアルスタイル。 |
| `geometry_file_format` | COMBO | はい | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` | 出力3Dモデルのファイル形式。 |
| `texture_mode` | COMBO | はい | `"None"`<br>`"Generated"`<br>`"Generated+HD"` | テクスチャ生成モード。"None"はテクスチャなし、"Generated"は標準テクスチャ、"Generated+HD"は高精細テクスチャを生成します。 |
| `seed` | INT | はい | 0 ～ 2147483647 | 再現可能な結果を得るためのランダムシード。同じシードと入力で同じ出力が得られます。 |
| `TAPose` | BOOLEAN | はい | True / False | 生成モデルにTポーズ（腕を伸ばした姿勢）を適用するかどうか。 |
| `hd_texture` | BOOLEAN | はい | True / False | モデルに高精細テクスチャを生成するかどうか。 |
| `texture_delight` | BOOLEAN | はい | True / False | モデルにテクスチャデライト（テクスチャ品質の向上）を適用するかどうか。 |
| `addon_highpack` | BOOLEAN | はい | True / False | 標準モデルに加えて高ポリゴンバージョンのモデルを生成するかどうか。 |
| `bbox_width` | INT | はい | 1 ～ 1000 | ワールド単位でのバウンディングボックスの幅。 |
| `bbox_height` | INT | はい | 1 ～ 1000 | ワールド単位でのバウンディングボックスの高さ。 |
| `bbox_length` | INT | はい | 1 ～ 1000 | ワールド単位でのバウンディングボックスの奥行き。 |
| `height_cm` | INT | はい | 1 ～ 300 | 生成されるモデルの高さ（センチメートル）。 |

**注記:** `prompt`パラメータは1文字以上2500文字以下である必要があります。`seed`パラメータは指定がない場合、デフォルトで0（ランダム）になります。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model_file` | FILE3DANY | 指定された形式で生成された3Dモデルファイル。 |

---
**Source fingerprint (SHA-256):** `79fbaf466e9af88cdfdac0f9136a2df17ba4bc2e5bb65a35b9ad2b1181da94db`
