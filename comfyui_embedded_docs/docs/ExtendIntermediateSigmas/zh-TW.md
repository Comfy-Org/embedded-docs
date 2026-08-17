# ExtendIntermediateSigmas

ExtendIntermediateSigmas 節點會擷取現有的 sigma 值序列，並在其間插入額外的中間 sigma 值。您可以指定要新增的額外步驟數、插值所用的間距方法，以及可選的起始與結束 sigma 邊界，以控制擴展在 sigma 序列中發生的位置。

## 輸入

| 參數 | 描述 | 資料類型 | 是否必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `sigmas` | 要擴展的輸入 sigma 序列，會在其中插入中間值 | SIGMAS | 是 | - |
| `steps` | 要在既有 sigma 之間插入的中間步驟數；使用 N 個步驟時，會在每個符合條件的配對之間插入 N-1 個中間 sigma 值（預設值：2） | INT | 是 | 1 至 100 |
| `start_at_sigma` | 擴展的較高 sigma 邊界 — 只擴展低於此值的 sigma（預設值：-1.0，表示無限大） | FLOAT | 是 | -1.0 至 20000.0 |
| `end_at_sigma` | 擴展的較低 sigma 邊界 — 只擴展高於此值的 sigma（預設值：12.0） | FLOAT | 是 | 0.0 至 20000.0 |
| `spacing` | 中間 sigma 值的間距插值方法：「linear」會均勻分佈，「cosine」與「sine」則套用曲線間距（預設值："linear"） | COMBO | 是 | `"linear"`<br>`"cosine"`<br>`"sine"` |

**注意：** 節點只會在符合以下條件的既有 sigma 配對之間插入中間 sigma：目前 sigma 同時小於或等於 `start_at_sigma`，且大於或等於 `end_at_sigma`。當 `start_at_sigma` 設為 -1.0 時，會視為無限大，因此只有 `end_at_sigma` 這個較低邊界會生效。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 已擴展的 sigma 序列，其中插入了額外的中間值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
