# LazyCache

LazyCache は、EasyCache のホームブリュー版であり、さらに簡単な実装を提供します。ComfyUI 内の任意のモデルで動作し、サンプリング中の計算を削減するキャッシュ機能を追加します。一般的には EasyCache よりも性能が劣りますが、まれに効果が高い場合もあり、ユニバーサルな互換性を備えています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | LazyCache を追加するモデル。 | MODEL | はい | - |
| `reuse_threshold` | キャッシュされたステップを再利用するためのしきい値（デフォルト: 0.2）。 | FLOAT | いいえ | 0.0 - 3.0 |
| `start_percent` | LazyCache の使用を開始するサンプリングステップの相対位置（デフォルト: 0.15）。 | FLOAT | いいえ | 0.0 - 1.0 |
| `end_percent` | LazyCache の使用を終了するサンプリングステップの相対位置（デフォルト: 0.95）。 | FLOAT | いいえ | 0.0 - 1.0 |
| `verbose` | 詳細情報をログに出力するかどうか（デフォルト: False）。 | BOOLEAN | いいえ | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | LazyCache 機能が追加されたモデル。 | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/ja.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
