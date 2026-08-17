# FluxDisableGuidance

このノードは、FluxおよびFlux系モデルにおけるガイダンス埋め込み機能を完全に無効化します。条件付けデータを入力として受け取り、ガイダンスコンポーネントを`None`に設定して削除し、変更済みの条件付けデータを返します。これにより、生成プロセスにおけるガイダンスベースの条件付けが効果的にオフになります。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `conditioning` | ガイダンスを除去するために処理する条件付けデータ | CONDITIONING | 必須 | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `conditioning` | ガイダンスが無効化された、変更済みの条件付けデータ | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/ja.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
