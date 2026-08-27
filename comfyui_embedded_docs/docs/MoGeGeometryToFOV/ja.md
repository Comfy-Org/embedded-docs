# MoGeGeometryToFOV

このノードは、MoGe ジオメトリオブジェクトに格納されたカメラ内部パラメータから、視野角と焦点距離を導出します。垂直・水平・対角のFOVを、度またはラジアンで返すことができます。垂直FOVの出力は、例えばSAM3DBody_Predictノードへの入力として使用できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `moge_geometry` | MoGeジオメトリオブジェクト。内部パラメータ行列と、画像・ポイント・深度データのうち少なくとも1つを含む必要があります。焦点距離変換に使用するピクセル高さを読み取るために使用されます。 | MOGE_GEOMETRY | はい | — |
| `axis` | FOVを計算する軸。"vertical"（fov_y）、"horizontal"（fov_x）、"diagonal"（デフォルト: "vertical"）。 | COMBO | はい | "vertical"<br>"horizontal"<br>"diagonal" |
| `unit` | FOVの出力単位（デフォルト: "degrees"）。 | COMBO | はい | "degrees"<br>"radians" |

注：`moge_geometry` に内部パラメータが含まれない場合（パノラマジオメトリにはありません）、または画像・ポイント・深度データのいずれも含まれない場合、ノードはエラーを発生させます。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `fov` | 選択した軸に沿った視野角。選択した単位（度またはラジアン）で返されます。 | FLOAT |
| `focal_pixels` | 垂直内部パラメータとピクセル高さから導出される、ピクセル単位のレンズ焦点距離。 | FLOAT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/ja.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`
