# SamplerEulerAncestral

## 概述

SamplerEulerAncestral 節點建立一個用於生成圖像的歐拉祖先取樣器。此取樣器採用特定的數學方法，將歐拉積分與祖先取樣技術相結合，以產生圖像變體。該節點允許您透過調整控制生成過程中隨機性和步長的參數來配置取樣行為。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制取樣過程的步長與隨機性（預設值：1.0）。這是一個進階參數。 | FLOAT | 否 | 0.0 - 100.0 |
| `s_noise` | 控制取樣過程中添加的噪聲量（預設值：1.0）。這是一個進階參數。 | FLOAT | 否 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 返回一個已配置的歐拉祖先取樣器，可用於取樣流程中。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4d167de55f003383ccbb4a53daa14496bd931589781d56b62bf282a811669670`
