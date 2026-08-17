# CLIPTextEncodeKandinsky5

CLIPTextEncodeKandinsky5 ノードは、Kandinsky 5 モデルで使用するテキストプロンプトを準備します。2 つの別々のテキスト入力を受け取り、提供された CLIP モデルを使用してトークン化し、それらを単一の conditioning 出力に結合します。この出力は、画像生成プロセスを導くために使用されます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip` | テキストプロンプトのトークン化とエンコードに使用される CLIP モデル。 | CLIP | はい |  |
| `clip_l` | 主要なテキストプロンプト。この入力は複数行テキストと動的プロンプトをサポートします。 | STRING | はい |  |
| `qwen25_7b` | 二次的なテキストプロンプト。この入力は複数行テキストと動的プロンプトをサポートします。 | STRING | はい |  |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `CONDITIONING` | 両方のテキストプロンプトから生成された結合 conditioning データ。画像生成のために Kandinsky 5 モデルに入力する準備ができています。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/ja.md)

---
**Source fingerprint (SHA-256):** `d988c47ab9a5f01549a3ae01b365d39e9fa2464bb69ea018ec20151939dcfc56`
