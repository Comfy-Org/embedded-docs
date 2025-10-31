> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmppSde/zh-TW.md)

此節點專為 DPM++ SDE（隨機微分方程）模型生成取樣器而設計。它能適應 CPU 和 GPU 執行環境，根據可用硬體優化取樣器的實現。

## 輸入參數

| 參數名稱         | 資料類型     | 描述 |
|----------------|-------------|-------------|
| `eta`          | FLOAT       | 指定 SDE 求解器的步長，影響取樣過程的細緻度。|
| `s_noise`      | FLOAT       | 決定取樣過程中要應用的噪聲水平，影響生成樣本的多樣性。|
| `r`            | FLOAT       | 控制取樣過程中噪聲減少的比例，影響生成樣本的清晰度和品質。|
| `noise_device` | COMBO[STRING]| 選擇取樣器的執行環境（CPU 或 GPU），根據可用硬體優化性能。|

## 輸出參數

| 參數名稱    | 資料類型 | 描述 |
|----------------|-------------|-------------|
| `sampler`    | SAMPLER     | 使用指定參數配置生成的取樣器，已準備好用於取樣操作。 |