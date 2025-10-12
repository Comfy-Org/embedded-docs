> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerCFGpp/ja.md)

SamplerEulerCFGppノードは、出力を生成するためのEuler CFG++サンプリング手法を提供します。このノードは、ユーザーの好みに基づいて選択可能な2つの異なる実装バージョンのEuler CFG++サンプラーを提供します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `バージョン` | STRING | はい | `"regular"`<br>`"alternative"` | 使用するEuler CFG++サンプラーの実装バージョン |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 設定済みのEuler CFG++サンプラーインスタンスを返します |
