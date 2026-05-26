> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/zh-TW.md)

## 概述

MultiGPU CFG Split 節點可讓同一台電腦中的多張 GPU 一起處理擴散取樣。實際加速幅度會依工作流程而不同，但在常見工作流程中，已測得最高約 1.95 倍的速度提升。

## 重要細節

不支援混用不同型號的 GPU，系統中安裝的 GPU 必須是相同類型，例如 2 張 5090，或 2 張 5080。

ComfyUI 會在啟動時自動偵測系統中已安裝的多張 GPU。

## 支援的 GPU

任何使用 Ampere 以上架構、且由兩張相同 GPU 組成的配置都可支援，例如 2 x 3090 或 2 x RTX6000 Pro。

## 支援的模型

* LTX-2.3  
* WAN 2.2  
* FLUX.2 Klein - Base Versions  
* Z-Image  
* Stable Diffusion 3.5 Large  
* Hunyuan Video  
* Qwen-Image-Edit-2511  
* Hunyuan-3D-v2.1  
* SDXL

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | 不適用 | 在開始取樣前，先準備給 MultiGPU CFG 拆分使用的模型。 |
| `max_gpus` | INT | 是 | 最小值：1<br>步長：1<br>預設值：2 | 可用來分攤負載的相同 GPU 最大數量。通常可設為系統中已安裝且型號一致的 GPU 數量。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `MODEL` | MODEL | 已準備好進行 MultiGPU CFG 拆分的模型，可直接用於加速取樣。 |

## 節點位置與工作流程說明

![image1.png](./asset/image1.png)  
`max_gpus` 應設定為系統中已安裝的相同 GPU 最大數量。

**節點放置位置：** MultiGPU CFG Split 需要放在模型載入節點與取樣節點之間。如果模型載入節點的模型輸出還連接了其他節點，那麼在進入取樣節點之前，MultiGPU CFG Split 應該是這條鏈上的最後一個節點。

![image2.png](./asset/image2.png)

**工作流程需求：** 這個節點是從 CFG 這一層來拆分擴散流程，因此工作流程中的 CFG 必須大於 1。若是必須使用 CFG = 1 的 distilled 工作流程，使用 MultiGPU CFG Split 在多張 GPU 上執行時通常不會帶來明顯的效能提升。

## 如何確認多 GPU 正在運作

執行啟用 MultiGPU CFG Split 的工作流程時，可以打開 Windows 工作管理員，並切換到「效能」分類。  
![image3.png](./asset/image3.png)  
![image4.png](./asset/image4.png)  
當工作流程中的取樣器正在執行時，你應該可以看到兩張已安裝的 GPU 都有活動。

## 已知問題

TBD

## 範例多 GPU 工作流程（Wan 2.2 FP8）

[https://drive.google.com/file/d/1VORVx7rMPSH9rY1HD2hCujcHa2vB9rzv/view?usp=drive\_link](https://drive.google.com/file/d/1VORVx7rMPSH9rY1HD2hCujcHa2vB9rzv/view?usp=drive_link)  

---
**Source fingerprint (SHA-256):** `7293ee785e29aea9a1a70a10444b99e89fb23c866505628ec57c209a2b8aaee0`
