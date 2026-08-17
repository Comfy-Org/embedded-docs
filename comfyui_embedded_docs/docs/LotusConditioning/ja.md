# LotusConditioning

LotusConditioning ノードは、Lotus モデル用に事前計算されたコンディショニング埋め込みを提供します。null コンディショニングを備えた凍結エンコーダーを使用し、推論や大きなテンソルファイルの読み込みを必要とせずに、参照実装と同等の結果を得るためにハードコードされたプロンプト埋め込みを返します。このノードは、生成パイプラインで直接使用できる固定コンディショニングテンソルを出力します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| *入力なし* | このノードは入力パラメータを受け付けません。 | - | - | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `conditioning` | Lotus モデル用に事前計算されたコンディショニング埋め込みで、固定のプロンプト埋め込みと空の辞書を含みます。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/ja.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`
