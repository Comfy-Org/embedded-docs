# ExtendIntermediateSigmas

ExtendIntermediateSigmas 節點會接收一組現有的 sigma 值序列，並在這些值之間插入額外的中間 sigma 值。它讓您可以指定要新增多少個額外步驟、插值時使用的間距方法，以及選用的起始與結束 sigma 邊界，以控制在 sigma 序列中進行延伸的位置。

## 輸入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `sigmas` | 要以中間值延伸的輸入 sigma 序列 | SIGMAS | 是 | - |
| `步驟數` | 控制每對現有 sigma 之間插入的中間 sigma 值數量。兩個 sigma 之間的區間會被分割成 `steps` 等份，每對產生 `steps - 1` 個新值（預設：2，也就是每對插入一個值） | INT | 是 | 1 至 100 |
| `起始 sigma` | 延伸的上限 sigma 邊界。只有起始 sigma 小於或等於此值的 sigma 區間會被延伸。設為 -1.0 時會視為無限大，表示不套用上限。預設：-1.0 | FLOAT | 是 | -1.0 至 20000.0 |
| `結束 sigma` | 延伸的下限 sigma 邊界。只有起始 sigma 大於或等於此值的 sigma 區間會被延伸。預設：12.0 | FLOAT | 是 | 0.0 至 20000.0 |
| `間距` | 用於安排中間 sigma 值間距的插值方法（預設："linear"） | COMBO | 是 | `"linear"`<br>`"cosine"`<br>`"sine"` |

**注意：** 此節點只會為起始 sigma 小於或等於 `start_at_sigma` 且大於或等於 `end_at_sigma` 的 sigma 區間插入中間 sigma。當 `start_at_sigma` 設為 -1.0 時，會視為無限大，因此只會套用 `end_at_sigma` 這個下限邊界。

## 輸出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `sigmas` | 已插入額外中間值的延伸後 sigma 序列 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
