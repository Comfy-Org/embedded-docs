> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/zh-TW.md)

SamplerSASolver 節點為擴散模型實作了一種自定義採樣演算法。它採用預測器-校正器方法，具有可配置的階數設定和隨機微分方程（SDE）參數，用於從輸入模型生成樣本。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 用於採樣的擴散模型 |
| `eta` | FLOAT | 是 | 0.0 - 10.0 | 控制步長縮放因數（預設值：1.0） |
| `sde_start_percent` | FLOAT | 是 | 0.0 - 1.0 | SDE 採樣的起始百分比（預設值：0.2） |
| `sde_end_percent` | FLOAT | 是 | 0.0 - 1.0 | SDE 採樣的結束百分比（預設值：0.8） |
| `s_noise` | FLOAT | 是 | 0.0 - 100.0 | 控制採樣過程中添加的噪聲量（預設值：1.0） |
| `predictor_order` | INT | 是 | 1 - 6 | 求解器中預測器元件的階數（預設值：3） |
| `corrector_order` | INT | 是 | 0 - 6 | 求解器中校正器元件的階數（預設值：4） |
| `use_pece` | BOOLEAN | 是 | - | 啟用或停用 PECE（預測-評估-校正-評估）方法 |
| `simple_order_2` | BOOLEAN | 是 | - | 啟用或停用簡化的二階計算 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 已配置的採樣器物件，可與擴散模型一起使用 |