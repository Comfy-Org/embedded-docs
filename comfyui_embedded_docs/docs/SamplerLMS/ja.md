# サンプラーLMS

The SamplerLMS ノードは、拡散モデルで使用する最小平均二乗（LMS）サンプラーを作成します。サンプリングプロセスで使用できるサンプラーオブジェクトを生成し、LMS アルゴリズムの次数を制御して、数値的な安定性と精度を調整できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `order` | LMS サンプラーアルゴリズムの次数パラメータで、数値的手法の精度と安定性を制御します（デフォルト: 4、詳細パラメータ） | INT | はい | 1 〜 100 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `sampler` | サンプリングパイプラインで使用できる、設定済みの LMS サンプラーオブジェクト | SAMPLER |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/ja.md)

---
**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`
