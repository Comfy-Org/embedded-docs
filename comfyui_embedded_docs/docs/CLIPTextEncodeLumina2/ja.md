# CLIP Text Encode for Lumina2

The CLIP Text Encode for Lumina2ノードは、CLIPモデルを使用してシステムプロンプトとユーザープロンプトをエンコードし、拡散モデルが特定の画像を生成するためのガイドとなる埋め込みを生成します。定義済みのシステムプロンプトとカスタムテキストプロンプトを組み合わせ、それらをCLIPモデルで処理して、画像生成用のコンディショニングデータを作成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `system_prompt` | Lumina2には2種類のシステムプロンプトがあります。「superior」は優れた画像とテキストの整合性を持つ画像を生成し、「alignment」は最も高い画像とテキストの整合性を持つ高品質な画像を生成します。 | COMBO | はい | `"superior"`<br>`"alignment"` |
| `user_prompt` | エンコードするテキストです。複数行入力と動的プロンプトに対応しています。 | STRING | はい | N/A |
| `clip` | テキストのエンコードに使用されるCLIPモデルです。 | CLIP | はい | N/A |

**注：** `clip`入力は必須であり、Noneにすることはできません。`clip`入力が無効な場合、ノードはチェックポイントに有効なCLIPまたはテキストエンコーダモデルが含まれていない可能性があることを示すエラーを発生させます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `CONDITIONING` | 拡散モデルをガイドするために使用される、埋め込みテキストを含むコンディショニングです。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/ja.md)

---
**Source fingerprint (SHA-256):** `0c7540e6232c93b0f76c4903f5646e00a639ccb0b7720f70b5ac727513358a02`
