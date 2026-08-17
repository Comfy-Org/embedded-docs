# VOIDSampler

## 概要

VOIDSampler ノードは、VOID インペインティングモデル専用に設計された特殊な DDIM サンプリング手法を提供します。このノードは、VOID モデルのトレーニング時に使用されるものと同じデノイジング処理を実装しており、標準の KSampler が適用するノイズスケーリングは行いません。このノードは SamplerCustom または SamplerCustomAdvanced ノードと組み合わせて使用することを想定しており、RandomNoise または VOIDWarpedNoiseSource とペアで使用する必要があります。

## 入力

このノードには設定可能な入力パラメータはありません。固定の DDIM サンプリングアルゴリズムを適用する自己完結型のサンプラーです。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| *入力なし* | このノードは入力パラメータを受け付けません。 | - | - | - |

注：VOID モデルは diffusers の CogVideoXDDIMScheduler を使用してトレーニングされており、このスケジューラは入力の標準偏差が約 1 となるアルファ空間で動作します。標準の KSampler が適用するノイズスケーリングは約 4500 倍の乗算を行うため、このトレーニングとは互換性がありません。VOIDSampler はそのスケーリングを省略し、シグマからアルファへの変換を使用して DDIM 更新ルールを直接実装します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `SAMPLER` | VOID DDIM アルゴリズムを実装したサンプラーオブジェクト。SamplerCustom または SamplerCustomAdvanced ノードに接続可能です。 | SAMPLER |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/ja.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
