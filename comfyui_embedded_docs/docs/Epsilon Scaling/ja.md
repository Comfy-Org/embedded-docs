# Epsilon Scaling

このノードは、研究論文「Elucidating the Exposure Bias in Diffusion Models」(arxiv.org/abs/2308.15321v6) で提案されたEpsilon Scaling法を実装しています。サンプリングプロセス中に予測されたノイズをスケーリングすることで露出バイアスを軽減し、生成画像の品質向上につなげます。この実装では、実用性と効果のバランスを考慮して、論文で推奨されている「一様スケジュール（uniform schedule）」を採用しています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | イプシロンスケーリングパッチが適用されるモデル。 | MODEL | はい | - |
| `scaling_factor` | 予測ノイズがスケーリングされる係数。1.0より大きい値は予測ノイズを減少させ、1.0より小さい値は予測ノイズを増加させます（デフォルト: 1.005）。 | FLOAT | はい | 0.5 - 1.5 (step: 0.001) |

注記: `scaling_factor` はゼロ除算を防ぐため、値がゼロにならないようにガードされています。UIでは最小値が0.5に設定されているため、通常の使用ではゼロになることはありません。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | サンプリングプロセスにイプシロンスケーリング関数が適用された、入力モデルのパッチ適用済みコピー。元のモデルは変更されません。 | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/ja.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
