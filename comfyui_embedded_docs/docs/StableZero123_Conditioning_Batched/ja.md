# 安定ゼロ123条件付け（バッチ）

以下が日本語翻訳です。

---

StableZero123_Conditioning_Batched ノードは、Stable Zero123 モデルでオブジェクトの3Dビューを生成するために必要な条件付けデータを準備します。入力画像を CLIP ビジョンモデルと VAE でエンコードし、画像特徴量をバッチ内の各アイテムのカメラ仰角・方位角と組み合わせて、ポジティブ条件付けとネガティブ条件付け、および空の潜在テンソルを出力します。バッチ増分入力は、バッチ内の連続する各アイテムのカメラ角度を増減させます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 入力画像を画像埋め込みにエンコードするために使用される CLIP ビジョンモデル | CLIP_VISION | はい | - |
| `init_image` | 処理およびエンコードされる初期入力画像 | IMAGE | はい | - |
| `vae` | 画像ピクセルを潜在空間にエンコードするために使用される VAE モデル | VAE | はい | - |
| `width` | 処理画像のターゲット幅（デフォルト: 256） | INT | はい | 16 to MAX_RESOLUTION (step 8) |
| `height` | 処理画像のターゲット高さ（デフォルト: 256） | INT | はい | 16 to MAX_RESOLUTION (step 8) |
| `batch_size` | バッチ内で生成する条件付けサンプルの数（デフォルト: 1） | INT | はい | 1 to 4096 |
| `elevation` | 開始時のカメラ仰角（度）（デフォルト: 0.0） | FLOAT | はい | -180.0 to 180.0 (step 0.1) |
| `azimuth` | 開始時のカメラ方位角（度）（デフォルト: 0.0） | FLOAT | はい | -180.0 to 180.0 (step 0.1) |
| `elevation_batch_increment` | バッチ内の連続する各アイテムについて仰角に加算される値（デフォルト: 0.0、詳細パラメータ） | FLOAT | はい | -180.0 to 180.0 (step 0.1) |
| `azimuth_batch_increment` | バッチ内の連続する各アイテムについて方位角に加算される値（デフォルト: 0.0、詳細パラメータ） | FLOAT | はい | -180.0 to 180.0 (step 0.1) |

**注記：** `width` と `height` の値は 8 の倍数である必要があります（選択ステップが 8 のため自動的に適用されます）。これは、ノードがこれらの値を 8 で割って潜在次元を構築するためです。バッチ内の各アイテムについて、`elevation` と `azimuth` の値は `elevation_batch_increment` と `azimuth_batch_increment` だけ増加するため、連続するバッチアイテムには段階的なカメラ角度が適用されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | 画像埋め込み、カメラ埋め込み、および生成時に連結するために使用されるエンコード済み入力画像を組み合わせたポジティブ条件付け | CONDITIONING |
| `negative` | ゼロ初期化された画像埋め込みと連結用のゼロ潜在テンソルを使用するネガティブ条件付け | CONDITIONING |
| `latent` | 次元 (batch_size, 4, height/8, width/8) とバッチインデックス情報を持つ空の潜在テンソル | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/ja.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
