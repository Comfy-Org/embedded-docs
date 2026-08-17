# EasyCache

EasyCache ノードは、サンプリングプロセス中に以前に計算されたステップを再利用することでパフォーマンスを向上させる、モデル向けのネイティブキャッシュシステムを実装しています。サンプリングのタイムライン上でキャッシュの使用を開始および停止するタイミングのしきい値を設定可能な状態で、モデルに EasyCache 機能を追加します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | EasyCache を追加するモデル。 | MODEL | はい | - |
| `reuse_threshold` | キャッシュされたステップを再利用するためのしきい値（デフォルト: 0.2）。 | FLOAT | はい | 0.0 - 3.0 |
| `start_percent` | EasyCache の使用を開始するサンプリングステップの相対位置（デフォルト: 0.15）。 | FLOAT | はい | 0.0 - 1.0 |
| `end_percent` | EasyCache の使用を終了するサンプリングステップの相対位置（デフォルト: 0.95）。 | FLOAT | はい | 0.0 - 1.0 |
| `verbose` | 詳細な情報をログに記録するかどうか（デフォルト: False）。 | BOOLEAN | はい | - |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `model` | EasyCache が適用されたモデル。 | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/ja.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
