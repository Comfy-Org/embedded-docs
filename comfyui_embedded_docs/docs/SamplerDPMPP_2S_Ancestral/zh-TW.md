> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/zh-TW.md)

SamplerDPMPP_2S_Ancestral 節點會建立一個使用 DPM++ 2S Ancestral 採樣方法來生成圖像的採樣器。此採樣器結合了確定性與隨機性元素，能在保持一定一致性的同時產生多樣化的結果。它讓您能夠在採樣過程中控制隨機性和噪聲水平。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | 是 | 0.0 - 100.0 | 控制採樣過程中添加的隨機噪聲量（預設值：1.0） |
| `s_noise` | FLOAT | 是 | 0.0 - 100.0 | 控制採樣過程中應用的噪聲比例（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 返回一個已配置的採樣器物件，可在採樣流程中使用 |