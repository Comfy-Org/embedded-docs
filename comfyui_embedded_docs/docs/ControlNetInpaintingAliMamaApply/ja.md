# ControlNetインペインティングAliMamaを適用

このノードは、ポジティブおよびネガティブのコンディショニングと、制御画像およびマスクを組み合わせることで、インペインティングタスク向けのControlNetコンディショニングを適用します。画像とマスクを処理して修正済みのコンディショニングを生成し、生成プロセスをガイドすることで、どの領域をインペイントするかを正確に制御できます。また、生成中のControlNetの影響を調整するための強度とタイミングの制御にも対応しています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | 生成を望ましいコンテンツへ導くポジティブコンディショニング。 | CONDITIONING | はい | - |
| `negative` | 生成を不要なコンテンツから遠ざけるネガティブコンディショニング。 | CONDITIONING | はい | - |
| `control_net` | 生成に対する追加の制御を提供するControlNetモデル。 | CONTROL_NET | はい | - |
| `vae` | 画像のエンコードおよびデコードに使用されるVAE。 | VAE | はい | - |
| `image` | ControlNetの制御ガイダンスとして使用される入力画像。 | IMAGE | はい | - |
| `mask` | 画像のどの領域をインペイントするかを定義するマスク。 | MASK | はい | - |
| `strength` | ControlNet効果の強さ（デフォルト: 1.0）。 | FLOAT | はい | 0.0 to 10.0 |
| `start_percent` | 詳細オプション。ControlNetの影響が生成プロセスのどの時点で開始されるかを示す割合（デフォルト: 0.0）。 | FLOAT | はい | 0.0 to 1.0 |
| `end_percent` | 詳細オプション。ControlNetの影響が生成プロセスのどの時点で終了するかを示す割合（デフォルト: 1.0）。 | FLOAT | はい | 0.0 to 1.0 |

**注記:** 選択したControlNetで `concat_mask` が有効な場合、マスク値が反転され（1 - mask）、反転されたマスクのリサイズ版が画像に適用され、反転マスクがControlNetに渡される追加の連結データに含まれます。`concat_mask` が無効な場合、`mask` 入力は使用されません。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | インペインティング用にControlNetが適用された修正済みポジティブコンディショニング。 | CONDITIONING |
| `negative` | インペインティング用にControlNetが適用された修正済みネガティブコンディショニング。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/ja.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
