> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/ja.md)

Epsilon Scalingメソッドを、研究論文「Elucidating the Exposure Bias in Diffusion Models」に基づいて実装します。このメソッドは、サンプリングプロセス中に予測されたノイズをスケーリングすることで、サンプルの品質を向上させます。拡散モデルにおけるエクスポージャーバイアスを軽減するために、均一なスケジュールを使用します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | はい | - | Epsilon Scalingを適用するモデル |
| `scaling_factor` | FLOAT | いいえ | 0.5 - 1.5 | 予測ノイズのスケーリングに使用する係数（デフォルト: 1.005） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model` | MODEL | Epsilon Scalingが適用されたモデル |
