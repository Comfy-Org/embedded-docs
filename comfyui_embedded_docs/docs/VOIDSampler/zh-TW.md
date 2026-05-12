> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/zh-TW.md)

## 概述

VOIDSampler 節點提供一種專門為 VOID 修復模型設計的 DDIM 取樣方法。它實作了與 VOID 模型訓練期間相同的去噪過程，且不包含標準 KSampler 所應用的噪聲縮放。此節點旨在與 SamplerCustom 或 SamplerCustomAdvanced 節點搭配使用，並應與 RandomNoise 或 VOIDWarpedNoiseSource 配對。

## 輸入

此節點沒有可設定的輸入參數。它是一個自包含的取樣器，採用固定的 DDIM 取樣演算法。

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| *無輸入* | - | - | - | 此節點不接受任何輸入參數。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `SAMPLER` | SAMPLER | 一個實作 VOID DDIM 演算法的取樣器物件，準備好連接到 SamplerCustom 或 SamplerCustomAdvanced 節點。 |