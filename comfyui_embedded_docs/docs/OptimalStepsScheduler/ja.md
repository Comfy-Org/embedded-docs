# OptimalStepsScheduler

OptimalStepsScheduler ノードは、選択されたモデルタイプとステップ構成に基づいて、拡散モデルのノイズスケジュールシグマを計算します。`denoise` パラメータに応じてステップ数を調整し、要求されたステップ数に一致するようにノイズレベルを補間します。このノードは、拡散サンプリングプロセス中に使用されるノイズレベルを決定するシグマ値のシーケンスを返します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model_type` | ノイズレベル計算に使用する拡散モデルの種類 | COMBO | はい | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | 計算するサンプリングステップの総数（デフォルト: 20） | INT | はい | 3-1000 |
| `denoise` | ノイズ除去の強さを制御し、実効ステップ数を調整します（デフォルト: 1.0） | FLOAT | はい | 0.0-1.0 |

**注記:** `denoise` が 1.0 未満に設定されている場合、ノードは実効ステップ数を `steps * denoise` として計算します。`denoise` が 0.0 に設定されている場合、ノードは空のテンソルを返します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `sigmas` | 拡散サンプリングのノイズスケジュールを表すシグマ値のシーケンス | SIGMAS |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/ja.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
