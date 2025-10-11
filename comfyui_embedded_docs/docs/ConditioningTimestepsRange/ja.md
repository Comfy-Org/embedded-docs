> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/ja.md)

ConditioningTimestepsRangeノードは、生成プロセス中にコンディショニング効果が適用されるタイミングを制御するための3つの異なるタイムステップ範囲を作成します。開始パーセンテージと終了パーセンテージの値を受け取り、タイムステップの全範囲（0.0から1.0）を3つのセグメントに分割します：指定されたパーセンテージ間のメイン範囲、開始パーセンテージ前の範囲、および終了パーセンテージ後の範囲です。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `start_percent` | FLOAT | はい | 0.0 - 1.0 | タイムステップ範囲の開始パーセンテージ（デフォルト: 0.0） |
| `end_percent` | FLOAT | はい | 0.0 - 1.0 | タイムステップ範囲の終了パーセンテージ（デフォルト: 1.0） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `TIMESTEPS_RANGE` | TIMESTEPS_RANGE | start_percentとend_percentで定義されるメインのタイムステップ範囲 |
| `BEFORE_RANGE` | TIMESTEPS_RANGE | 0.0からstart_percentまでのタイムステップ範囲 |
| `AFTER_RANGE` | TIMESTEPS_RANGE | end_percentから1.0までのタイムステップ範囲 |