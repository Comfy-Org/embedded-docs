# MoGe レンダリング

以下に、英語ドキュメントを日本語に翻訳しました。

---

## 概要

このノードは、MoGe深度・法線推定ノードが生成した`MOGE_GEOMETRY`パケットを受け取り、標準的な画像形式にレンダリングします。深度マップ、カラー深度マップ、法線マップ、マスクのいずれかを出力できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `moge_geometry` | MoGe推定ノードからのジオメトリデータパケット。 | MOGE_GEOMETRY | はい | N/A |
| `output` | ジオメトリデータからレンダリングする画像の種類。DirectXとOpenGLの違いは、法線マップのグリーンチャンネルの規約を制御します。DirectX: 緑 = -Y（下方向）（Unreal）。OpenGL: 緑 = +Y（上方向）（Blender、Substance、Unity、glTF）。（デフォルト："depth"） | COMBO | はい | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**注意:** 選択した`output`モードにより、`moge_geometry`に含まれている必要があるデータが決まります。
- `depth`および`depth_colored`は深度データを必要とします。深度は0.1/99.9パーセンタイルのクリッピングを使用して、正規化された視差（1/depth）マップに変換されます。
- `normal_opengl`および`normal_directx`は法線データ、または法線を導出できるポイントデータを必要とします。いずれも存在しない場合、ノードはエラーを発生させます。
- `mask`はマスクデータを必要とします。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `IMAGE` | レンダリングされた画像をRGBテンソルのバッチとして出力します。内容は`output`モードに依存します。グレースケール深度マップ、カラー深度マップ、法線マップ、またはマスクです。 | IMAGE |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/ja.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
