# SamplerDPMAdaptative

SamplerDPMAdaptative 節點實作了一個自適應 DPM（擴散機率模型）取樣器，會在取樣過程中自動調整步長。它使用基於容差的誤差控制來決定最佳步長，在計算效率與取樣精度之間取得平衡。此自適應方法有助於維持品質，同時可能減少所需的步驟數量。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `order` | 取樣器方法的階數（預設值：3） | INT | 是 | 2-3 |
| `rtol` | 誤差控制的相對容差（預設值：0.05） | FLOAT | 是 | 0.0-100.0 |
| `atol` | 誤差控制的絕對容差（預設值：0.0078） | FLOAT | 是 | 0.0-100.0 |
| `h_init` | 初始步長（預設值：0.05） | FLOAT | 是 | 0.0-100.0 |
| `pcoeff` | 步長控制的比例係數（預設值：0.0） | FLOAT | 是 | 0.0-100.0 |
| `icoeff` | 步長控制的積分係數（預設值：1.0） | FLOAT | 是 | 0.0-100.0 |
| `dcoeff` | 步長控制的微分係數（預設值：0.0） | FLOAT | 是 | 0.0-100.0 |
| `accept_safety` | 步驟接受的安全係數（預設值：0.81） | FLOAT | 是 | 0.0-100.0 |
| `eta` | 隨機性參數（預設值：0.0） | FLOAT | 是 | 0.0-100.0 |
| `s_noise` | 雜訊縮放因子（預設值：1.0） | FLOAT | 是 | 0.0-100.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 傳回配置好的 DPM 自適應取樣器實例 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/zh-TW.md)

---
**Source fingerprint (SHA-256):** `07b2e5b9f21ec101eabccc6be245d043e64a996a14db10434b03eaae0a91b1d8`
