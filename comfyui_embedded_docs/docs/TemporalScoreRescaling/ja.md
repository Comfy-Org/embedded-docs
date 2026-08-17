# TSR - 時間的スコアリスケーリング

このノードは、拡散モデルにTemporal Score Rescaling（TSR）を適用します。デノイジング処理中に予測されたノイズまたはスコアを再スケーリングすることでモデルのサンプリング動作を変更し、生成出力の多様性を調整できます。これは、CFG（Classifier-Free Guidance）後処理関数として実装されています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | TSR関数でパッチされる拡散モデル。 | MODEL | はい | - |
| `tsr_k` | 再スケーリングの強さを制御します。kが低いほど画像生成でより詳細な結果が得られ、kが高いほど滑らかな結果が得られます。k = 1に設定すると再スケーリングが無効になります。（デフォルト: 0.95） | FLOAT | いいえ | 0.01 - 100.0 |
| `tsr_sigma` | 再スケーリングがどの程度早く有効になるかを制御します。値が大きいほど早く有効になります。（デフォルト: 1.0） | FLOAT | いいえ | 0.01 - 100.0 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `patched_model` | 入力モデル。そのサンプリングプロセスにTemporal Score Rescaling関数が適用されたものです。 | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/ja.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
