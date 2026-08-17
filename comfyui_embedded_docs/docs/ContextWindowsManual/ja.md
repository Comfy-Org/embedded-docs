# コンテキストウィンドウ（手動）

Context Windows (Manual) ノードを使用すると、サンプリング中にモデルへ適用するコンテキストウィンドウを手動で設定できます。指定した長さ、重複、スケジューリングパターンで重複するコンテキストセグメントを作成し、セグメント間の連続性を維持しながらデータを管理可能なチャンクに分割して処理します。このノードは、ノイズシャッフリング、コンディショニング保持、ノイズ潜在変数保持、因果ウィンドウ修正など、コンテキストウィンドウの適用方法を制御する高度なオプションを提供します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | サンプリング中にコンテキストウィンドウを適用するモデル。 | MODEL | はい | - |
| `context_length` | コンテキストウィンドウの長さ（デフォルト：16）。 | INT | いいえ | 1+ |
| `context_overlap` | コンテキストウィンドウの重複量（デフォルト：4）。 | INT | いいえ | 0+ |
| `context_schedule` | コンテキストウィンドウのステップ依存スケジューリングアルゴリズム（デフォルト：STATIC_STANDARD）。 | COMBO | いいえ | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | コンテキストウィンドウのストライド。ユニフォームスケジュールにのみ適用されます（デフォルト：1）。 | INT | いいえ | 1+ |
| `closed_loop` | コンテキストウィンドウのループを閉じるかどうか。ループスケジュールにのみ適用されます（デフォルト：False）。 | BOOLEAN | いいえ | - |
| `fuse_method` | コンテキストウィンドウを融合する方法（デフォルト：PYRAMID）。 | COMBO | いいえ | `"PYRAMID"`<br>`"LIST_STATIC"` |
| `dim` | コンテキストウィンドウを適用する次元（デフォルト：0）。 | INT | いいえ | 0-5 |
| `freenoise` | FreeNoise ノイズシャッフリングを適用するかどうか。ウィンドウのブレンドが改善されます（デフォルト：False）。 | BOOLEAN | いいえ | - |
| `cond_retain_index_list` | 各ウィンドウのコンディショニングテンソルに保持する潜在インデックスのリスト。concat 方式の I2V モデル（例：Wan I2V、HunyuanVideo I2V、Cosmos I2V、SVD）では、エンコードされた開始画像は c_concat コンディショニングチャンネルに格納されます。これを `'0'` に設定すると、すべてのウィンドウのサブ位置 0 にその開始画像の内容が保持されます（デフォルト：""）。 | STRING | いいえ | - |
| `split_conds_to_windows` | ConditionCombine によって作成された複数のコンディショニングを、リージョンインデックスに基づいて各ウィンドウに分割するかどうか（デフォルト：False）。 | BOOLEAN | いいえ | - |
| `latent_retain_index_list` | 各ウィンドウについて、ノイズ潜在変数自体に保持する潜在インデックスのリスト。参照コンテンツ（例：開始画像）が別のコンディショニングチャンネルではなく、ノイズ潜在変数に直接格納されるワークフロー（例：LTXV、AnimateDiff などの inplace 方式の I2V）で使用します。cond_retain_index_list とは独立しています（デフォルト：""）。 | STRING | いいえ | - |
| `causal_window_fix` | 0 番目以外のインデックスが付いたコンテキストウィンドウに因果修正フレームを追加するかどうか（デフォルト：True）。 | BOOLEAN | いいえ | - |

**パラメータの制約：**

- `context_stride` はユニフォームスケジュールが選択されている場合にのみ使用されます
- `closed_loop` はループスケジュールにのみ適用されます
- `dim` は 0 以上 5 以下である必要があります
- `cond_retain_index_list` は、整数インデックスのカンマ区切りリストを文字列として指定します（例："0,1,2"）
- `latent_retain_index_list` は、整数インデックスのカンマ区切りリストを文字列として指定し（例："0,1,2"）、`cond_retain_index_list` とは独立しています

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | サンプリング中にコンテキストウィンドウが適用されたモデル。 | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/ja.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
