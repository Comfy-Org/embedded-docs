# CFGガイダー

CFGGuider ノードは、画像生成におけるサンプリングプロセスを制御するためのガイダンスシステムを作成します。モデルと、ポジティブおよびネガティブのコンディショニング入力を取得し、classifier-free guidance スケールを適用して、望ましいコンテンツへ生成を導きつつ、不要な要素を回避します。このノードは、サンプリングノードが画像生成の方向を制御するために使用できるガイダーオブジェクトを出力します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | ガイダンスに使用されるモデル | MODEL | はい | - |
| `positive` | 望ましいコンテンツへ生成を導くポジティブコンディショニング | CONDITIONING | はい | - |
| `negative` | 不要なコンテンツから生成を遠ざけるネガティブコンディショニング | CONDITIONING | はい | - |
| `cfg` | コンディショニングが生成に与える影響の強さを制御する classifier-free guidance スケール（デフォルト: 8.0） | FLOAT | はい | 0.0 to 100.0 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `GUIDER` | 生成プロセスを制御するためにサンプリングノードに渡すことができるガイダーオブジェクト | GUIDER |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/ja.md)

---
**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`
