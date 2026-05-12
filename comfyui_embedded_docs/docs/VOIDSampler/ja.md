> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/ja.md)

以下が翻訳結果です。

## 概要

VOIDSamplerノードは、VOIDインペインティングモデル専用に設計された特殊なDDIMサンプリング手法を提供します。このノードは、標準のKSamplerが適用するノイズスケーリングを行わず、VOIDモデルのトレーニング時に使用されるものと同じノイズ除去プロセスを実装しています。このノードはSamplerCustomまたはSamplerCustomAdvancedノードと組み合わせて使用することを想定しており、RandomNoiseまたはVOIDWarpedNoiseSourceとペアリングする必要があります。

## 入力

このノードには設定可能な入力パラメーターはありません。固定のDDIMサンプリングアルゴリズムを適用する自己完結型のサンプラーです。

| パラメーター | データ型 | 必須 | 範囲 | 説明 |
|------------|----------|------|------|------|
| *入力なし* | - | - | - | このノードは入力パラメーターを受け付けません。 |

## 出力

| 出力名 | データ型 | 説明 |
|--------|----------|------|
| `SAMPLER` | SAMPLER | VOID DDIMアルゴリズムを実装したサンプラーオブジェクト。SamplerCustomまたはSamplerCustomAdvancedノードに接続して使用できます。 |