# WAN コンテキストウィンドウ（手動）

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | サンプリング中にコンテキストウィンドウを適用するモデル。 | MODEL | はい | - |
| `context_length` | コンテキストウィンドウの長さ（実フレーム数）。4n + 1 である必要があります。（デフォルト: 81） | INT | はい | 1 to 16384 (step 4) |
| `context_overlap` | コンテキストウィンドウのオーバーラップ（実フレーム数）。（デフォルト: 30） | INT | はい | 0 or greater |
| `context_schedule` | コンテキストウィンドウのステップ依存スケジューリングアルゴリズム。（デフォルト: "uniform_standard"） | COMBO | はい | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | コンテキストウィンドウのストライド。ユニフォームスケジュールにのみ適用されます。（デフォルト: 1） | INT | はい | 1 or greater |
| `closed_loop` | コンテキストウィンドウのループを閉じるかどうか。ループ式スケジュールにのみ適用されます。（デフォルト: False） | BOOLEAN | はい | True or False |
| `fuse_method` | コンテキストウィンドウを融合するために使用するメソッド。（デフォルト: "pyramid"） | COMBO | はい | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | FreeNoise ノイズシャッフリングを適用するかどうか。これによりウィンドウのブレンドが向上します。（デフォルト: True） | BOOLEAN | はい | True or False |
| `retain_first_frame` | すべてのコンテキストウィンドウで最初の I2V フレームを保持します（初期参照の保持に役立つ場合があります）。（デフォルト: False） | BOOLEAN | はい | True or False |
| `split_conds_to_windows` | 複数のコンディショニング（ConditionCombine によって作成されたもの）をリージョンインデックスに基づいて各ウィンドウに分割するかどうか。（デフォルト: False） | BOOLEAN | はい | True or False |

**注:** `context_stride` はユニフォームスケジュールにのみ影響し、`closed_loop` はループ式スケジュールにのみ適用されます。`context_length` は 4n + 1 のパターンに従う必要があります。このノードは、`context_length` と `context_overlap` を実フレームからモデル単位に変換してから適用し、`context_length` には最小 1、`context_overlap` には最小 0 を強制します。`context_stride`、`closed_loop`、`freenoise`、`split_conds_to_windows` は上級者向けオプションです。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `model` | 適用されたコンテキストウィンドウ設定を持つモデル。 | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/ja.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
