> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmppSde/zh-TW.md)

此節點專為生成 DPM++ SDE（隨機微分方程）模型的取樣器而設計。它會根據可用的硬體，自動適應 CPU 與 GPU 執行環境，並最佳化取樣器的實作方式。

## 輸入

| 參數 | 資料類型 | 說明 |
|---------------|-------------|-------------|
| `eta` | FLOAT | 指定 SDE 求解器的步長，影響取樣過程的細粒度。 |
| `s_noise` | FLOAT | 決定取樣過程中應用的雜訊程度，影響生成樣本的多樣性。 |
| `r` | FLOAT | 控制取樣過程中雜訊衰減的比例，影響生成樣本的清晰度與品質。 |
| `noise_device` | COMBO[STRING] | 選擇取樣器的執行環境（CPU 或 GPU），根據可用硬體最佳化效能。 |

## 輸出

| 參數 | 資料類型 | 說明 |
|---------------|-------------|-------------|
| `sampler` | SAMPLER | 根據指定參數配置所生成的取樣器，可用於取樣操作。 |