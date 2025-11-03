> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/zh-TW.md)

SamplerCustomAdvanced 節點使用自定義噪聲、引導和採樣配置執行進階潛空間採樣。它透過具有可自定義噪聲生成和 sigma 調度表的引導採樣過程處理潛在圖像，產生最終的採樣輸出，並在可用時提供去噪版本。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `noise` | NOISE | 是 | - | 為採樣過程提供初始噪聲模式和種子的噪聲生成器 |
| `guider` | GUIDER | 是 | - | 引導採樣過程朝向期望輸出的引導模型 |
| `sampler` | SAMPLER | 是 | - | 定義生成過程中潛空間遍歷方式的採樣演算法 |
| `sigmas` | SIGMAS | 是 | - | 控制整個採樣步驟中噪聲水平的 sigma 調度表 |
| `latent_image` | LATENT | 是 | - | 作為採樣起點的初始潛在表示 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `output` | LATENT | 完成採樣過程後的最終採樣潛在表示 |
| `denoised_output` | LATENT | 輸出結果的去噪版本（如可用），否則返回與輸出相同的內容 |