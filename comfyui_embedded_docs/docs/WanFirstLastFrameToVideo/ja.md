# WanFirstLastFrameToVideo

WanFirstLastFrameToVideo ノードは、開始フレームと終了フレームをテキストプロンプトと組み合わせて、ビデオ用の条件付けを作成します。最初と最後のフレームをエンコードし、マスクを適用して生成プロセスを導き、利用可能な場合には CLIP vision 特徴量を組み込むことで、ビデオ生成用の潜在表現を生成します。このノードは、指定された開始点と終了点の間で一貫性のあるシーケンスを生成するために、ビデオモデル向けのポジティブおよびネガティブ条件付けの両方を準備します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `positive` | ビデオ生成を導くためのポジティブなテキスト条件付け | CONDITIONING | 必須 | - |
| `negative` | ビデオ生成を導くためのネガティブなテキスト条件付け | CONDITIONING | 必須 | - |
| `vae` | 画像を潜在空間にエンコードするために使用される VAE モデル | VAE | 必須 | - |
| `width` | 出力ビデオの幅（デフォルト: 832、ステップ: 16） | INT | 必須 | 16 to MAX_RESOLUTION |
| `height` | 出力ビデオの高さ（デフォルト: 480、ステップ: 16） | INT | 必須 | 16 to MAX_RESOLUTION |
| `length` | ビデオシーケンス内のフレーム数（デフォルト: 81、ステップ: 4） | INT | 必須 | 1 to MAX_RESOLUTION |
| `batch_size` | 同時に生成するビデオの数（デフォルト: 1） | INT | 必須 | 1 to 4096 |
| `clip_vision_start_image` | 開始画像から抽出された CLIP vision 特徴量 | CLIP_VISION_OUTPUT | 任意 | - |
| `clip_vision_end_image` | 終了画像から抽出された CLIP vision 特徴量 | CLIP_VISION_OUTPUT | 任意 | - |
| `start_image` | ビデオシーケンスの開始フレーム画像 | IMAGE | 任意 | - |
| `end_image` | ビデオシーケンスの終了フレーム画像 | IMAGE | 任意 | - |

**注記:** `start_image` と `end_image` の両方が指定された場合、ノードはこれら2つのフレーム間を遷移するビデオシーケンスを作成します。処理前に、`start_image` は最初の `length` フレームにトリミングされ、`end_image` は最後の `length` フレームにトリミングされます。どちらか一方だけが指定された場合は、欠落している側は中間グレーのフレームで埋められます。マスクは、開始フレームと終了フレームが存在する場所では 0 に、それ以外では 1 に設定されます。`clip_vision_start_image` と `clip_vision_end_image` はオプションです。両方が指定された場合は、それらの CLIP vision 特徴量が連結され、ポジティブおよびネガティブ条件付けの両方に適用されます。一方のみが指定された場合は、その特徴量のみが使用されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `positive` | ビデオフレームエンコードと CLIP vision 特徴量が適用されたポジティブ条件付け | CONDITIONING |
| `negative` | ビデオフレームエンコードと CLIP vision 特徴量が適用されたネガティブ条件付け | CONDITIONING |
| `latent` | 指定されたビデオパラメータに一致する次元を持つ空の潜在テンソル | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
