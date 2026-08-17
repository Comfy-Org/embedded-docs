# VOIDSampler

## 概述

VOIDSampler 節點提供了一種專為 VOID 修復模型設計的專用 DDIM 取樣方法。它實作了與 VOID 模型訓練期間相同的去噪過程，但不包含標準 KSampler 所套用的雜訊縮放。此節點設計用於搭配 SamplerCustom 或 SamplerCustomAdvanced 節點使用，並應與 RandomNoise 或 VOIDWarpedNoiseSource 配對。

## 輸入

此節點沒有可設定的輸入參數。它是一個自包含的取樣器，套用固定的 DDIM 取樣演算法。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| *無輸入* | 此節點不接受任何輸入參數。 | - | - | - |

注意：VOID 模型是使用 diffusers CogVideoXDDIMScheduler 訓練的，該排程器在 alpha 空間中運作，其中輸入標準差約為 1。標準 KSampler 套用的雜訊縮放會乘以約 4500 倍，這與此訓練方式不相容。VOIDSampler 跳過該縮放，並直接使用 sigma 到 alpha 的轉換來實作 DDIM 更新規則。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `SAMPLER` | 一個實作 VOID DDIM 演算法的取樣器物件，可準備連接到 SamplerCustom 或 SamplerCustomAdvanced 節點。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
