> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/ja.md)

## 概要

MultiGPU CFG Split ノードは、同じPCに入っている複数のGPUで拡散サンプリングを分担できるようにします。実際の速度向上はワークフローによって変わりますが、一般的なワークフローでは最大で約1.95倍の高速化が確認されています。

## 重要なポイント

異なる種類のGPUを混在させることはできません。使用するGPUは同じ型でそろっている必要があります。たとえば 2 x 5090 や 2 x 5080 のような構成です。

ComfyUI は起動時に、システムに入っている複数のGPUを自動で検出します。

## 対応GPU

Ampere以降のアーキテクチャを使った、同一GPU 2枚構成に対応しています。たとえば 2 x 3090 や 2 x RTX6000 Pro です。

## 対応モデル

* LTX-2.3  
* WAN 2.2  
* FLUX.2 Klein - Base Versions  
* Z-Image  
* Stable Diffusion 3.5 Large  
* Hunyuan Video  
* Qwen-Image-Edit-2511  
* Hunyuan-3D-v2.1  
* SDXL

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | はい | なし | サンプリング前に、MultiGPU CFG 分割用として準備するモデルです。 |
| `max_gpus` | INT | はい | 最小: 1<br>ステップ: 1<br>デフォルト: 2 | 負荷分散に使う同一GPUの最大数です。通常は、PCに入っている同型GPUの枚数に合わせて設定します。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `MODEL` | MODEL | MultiGPU CFG 分割用に準備され、すぐに高速サンプリングへ使えるモデルです。 |

## ノード配置とワークフローの注意

![image1.png](./asset/image1.png)  
`max_gpus` は、システムに入っている同型GPUの最大数に設定してください。

**ノードの配置場所:** MultiGPU CFG Split は、Model Load ノードと Sampling ノードの間に置く必要があります。Model Load ノードのモデル出力がほかのノードにもつながっている場合は、Sampling ノードに入る直前の最後のノードとして MultiGPU CFG Split を置いてください。

![image2.png](./asset/image2.png)

**ワークフロー要件:** このノードは CFG の段階で拡散処理を分割します。そのため、ワークフロー内の CFG は 1 より大きい必要があります。CFG = 1 が必要な distilled ワークフローでは、MultiGPU CFG Split を使っても複数GPUによる速度向上はほとんど期待できません。

## マルチGPU利用の確認方法

MultiGPU CFG Split を有効にしたワークフローを実行したら、Windows のタスクマネージャーを開き、パフォーマンスの項目を選んでください。  
![image3.png](./asset/image3.png)  
![image4.png](./asset/image4.png)  
ワークフローのサンプラーが動いている間、2枚のGPUの両方に動きが見えれば正常です。

## 既知の問題

TBD

## サンプルのマルチGPUワークフロー（Wan 2.2 FP8）

[https://drive.google.com/file/d/1VORVx7rMPSH9rY1HD2hCujcHa2vB9rzv/view?usp=drive\_link](https://drive.google.com/file/d/1VORVx7rMPSH9rY1HD2hCujcHa2vB9rzv/view?usp=drive_link)  

---
**Source fingerprint (SHA-256):** `7293ee785e29aea9a1a70a10444b99e89fb23c866505628ec57c209a2b8aaee0`
