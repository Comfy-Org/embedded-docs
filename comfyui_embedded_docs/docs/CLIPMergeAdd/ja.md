# CLIPマージ追加

The CLIPMergeAdd ノードは、2 つの CLIP モデルを結合し、2 番目のモデルから最初のモデルにパッチを追加します。最初の CLIP モデルのコピーを作成し、position ID と logit scale パラメータを除いて、2 番目のモデルからキーパッチを選択的に取り込みます。これにより、ベースモデルの構造を維持しながら、CLIP モデルのコンポーネントをマージできます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip1` | クローンされ、マージの基盤として使用されるベースの CLIP モデルです。 | CLIP | はい | - |
| `clip2` | ベースモデルに追加されるキーパッチを提供するセカンダリの CLIP モデルです。 | CLIP | はい | - |

注：`clip2` のキーパッチは強度 1.0 で追加されます。`.position_ids` または `.logit_scale` で終わるキーはマージから除外されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `CLIP` | ベースモデルの構造に、セカンダリモデルから追加されたパッチを含む、マージされた CLIP モデルです。 | CLIP |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/ja.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`
