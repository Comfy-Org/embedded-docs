# EmptyARVideoLatent

EmptyARVideoLatent ノードは、動画生成用の空の潜在表現を作成します。指定された寸法、アスペクト比、長さを持つゼロのテンソルを提供することで、動画生成プロセスを初期化するために使用されます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `width` | 動画フレームの幅（ピクセル単位）（デフォルト: 832） | INT | はい | 16 から 8192（ステップ: 16） |
| `height` | 動画フレームの高さ（ピクセル単位）（デフォルト: 480） | INT | はい | 16 から 8192（ステップ: 16） |
| `length` | 動画のフレーム数（デフォルト: 81） | INT | はい | 1 から 1024（ステップ: 4） |
| `batch_size` | 1回のバッチで生成する動画の数（デフォルト: 1） | INT | はい | 1 から 64 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `LATENT` | ゼロで満たされた潜在テンソルで、指定された寸法、長さ、バッチサイズを持つ空の動画潜在空間を表します。テンソルの形状は [batch_size, 16, lat_t, height/8, width/8] で、lat_t は length から計算されます。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/ja.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`
