研究論文「Elucidating the Exposure Bias in Diffusion Models」で提案されたイプシロンスケーリング手法を実装します。この手法は、サンプリングプロセス中に予測ノイズをスケーリングすることで、サンプル品質を向上させます。拡散モデルにおける露出バイアスを軽減するために、一様なスケジュールを使用します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | イプシロンスケーリングを適用するモデル | MODEL | はい | - |
| `scaling_factor` | 予測ノイズのスケーリングに使用する係数（デフォルト：1.005） | FLOAT | いいえ | 0.5 - 1.5 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | イプシロンスケーリングが適用されたモデル | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/ja.md)
