# CLIPマージ減算

CLIPMergeSubtract ノードは、2 つの CLIP モデルをマージし、一方のモデルの重みをもう一方のモデルから減算します。最初のモデルをクローンした後、2 番目のモデルからキーパッチを減算して新しい CLIP モデルを作成します。乗数（multiplier）は調整可能で、減算の強さを制御できます。これにより、ベースモデルから特定の特性を除去して、微調整されたモデルブレンドが可能になります。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip1` | クローンされ、変更されるベースの CLIP モデル | CLIP | はい | - |
| `clip2` | ベースモデルから減算されるキーパッチを持つ CLIP モデル | CLIP | はい | - |
| `multiplier` | 減算操作の強さを制御します（デフォルト: 1.0） | FLOAT | はい | -10.0 ～ 10.0（ステップ: 0.01） |

**注:** このノードは、乗数（multiplier）の値に関係なく、`.position_ids` および `.logit_scale` パラメータを減算操作から除外します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `clip` | 最初のモデルから 2 番目のモデルの重みを減算した結果の CLIP モデル | CLIP |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/ja.md)

---
**Source fingerprint (SHA-256):** `62a8cf719c34d9e2b7321f6eeb03c881f0767fd36b80e25e74feff4c0a29045e`
