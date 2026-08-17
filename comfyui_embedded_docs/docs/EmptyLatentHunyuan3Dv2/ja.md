# EmptyLatentHunyuan3Dv2

EmptyLatentHunyuan3Dv2 ノードは、Hunyuan3Dv2 3D 生成モデル用に特別にフォーマットされた空白の潜在テンソルを作成します。Hunyuan3Dv2 アーキテクチャで必要とされる正しい次元と構造を持つ空の潜在空間を生成し、3D 生成ワークフローをゼロから開始できるようにします。このノードは、後続の 3D 生成プロセスの基礎となるゼロで満たされた潜在テンソルを生成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `resolution` | 潜在空間の解像度（デフォルト: 3072） | INT | はい | 1 - 8192 |
| `batch_size` | バッチ内の潜在画像の数（デフォルト: 1） | INT | はい | 1 - 4096 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `LATENT` | Hunyuan3Dv2 3D 生成用にフォーマットされた空のサンプルを含む潜在テンソルを返します | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/ja.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
