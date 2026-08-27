# EmptyTrellis2LatentStructure

このノードは、Trellis2モデル用の空の潜在構造を作成します。すべての値はゼロに設定されます。指定されたバッチ内のアイテム数に合わせた、32チャネル、解像度16×16×16の空白の3D潜在テンソルを生成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `batch_size` | バッチ内の潜在画像の数（デフォルト: 1）。 | INT | はい | 1 から 4096 |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `LATENT` | 空のTrellis2潜在構造。サンプルは形状 (batch_size, 32, 16, 16, 16) のゼロで埋められたテンソルで、潜在タイプは "trellis2" に設定されています。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/ja.md)

---
**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`
