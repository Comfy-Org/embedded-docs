# Recraft ベクトル化画像

入力画像から SVG ベクターグラフィックを生成します。このノードは各画像を Recraft API に送信し、結果を単一の SVG 出力に結合することで、ラスター画像をスケーラブルなベクター形式に変換します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `画像` | SVG 形式に変換する入力画像です。複数画像のバッチ処理をサポートします。 | IMAGE | はい | - |
| `version` | ベクター化バージョン：`v1` は標準バージョン、`v1_pro`（Vectorizer Pro）は滑らかな曲線、直線、鋭い角を備えたよりクリーンな SVG を生成し、レタリングや複雑な形状に最適です（デフォルト: "v1"）。 | COMBO | いいえ | "v1"<br>"v1_pro" |
| `shape_stacking` | SVG 内で形状をどのように重ねるか：`hierarchical` は形状を互いの上に階層的に重ねます。`cut_out` は形状が決して重ならないようにし、プロッター、ビニールカッター、スクリーン印刷向けです（デフォルト: "hierarchical"）。 | COMBO | いいえ | "hierarchical"<br>"cut_out" |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `SVG` | 生成されたベクターグラフィック出力で、処理されたすべての画像を単一の SVG ドキュメントに結合します。 | SVG |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/ja.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`
