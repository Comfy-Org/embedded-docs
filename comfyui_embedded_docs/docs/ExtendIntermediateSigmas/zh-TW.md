# ExtendIntermediateSigmas

ExtendIntermediateSigmas 節點接受現有的 sigma 值序列，並在它們之間插入額外的中間 sigma 值。您可以指定要增加的額外步數、插值的間距方法，以及可選的開始和結束 sigma 邊界，以控制擴展在 sigma 序列中的發生位置。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `sigmas` | 要擴展的輸入 sigma 序列，會在中間插入值 | SIGMAS | 是 | - |
| `步驟數` | 控制每一對現有 sigma 之間插入的中間 sigma 值數量。兩個 sigma 之間的區間會被分成 `steps` 個部分，每對產生 `steps - 1` 個新值（預設為 2，即每對插入一個值） | INT | 是 | 1 至 100 |
| `起始 sigma` | 用於擴展的上限 sigma 邊界 - 只擴展低於此值的 sigma（預設為 -1.0，表示無限大） | FLOAT | 是 | -1.0 至 20000.0 |
| `結束 sigma` | 用於擴展的下限 sigma 邊界 - 只擴展高於此值的 sigma（預設為 12.0） | FLOAT | 是 | 0.0 至 20000.0 |
| `間距` | 用於在 sigma 值之間進行插值的間距方法（預設為 "linear"） | COMBO | 是 | `"linear"`<br>`"cosine"`<br>`"sine"` |

**注意：** 此節點只會在現有 sigma 配對之間插入中間 sigma，前提是目前的 sigma 小於或等於 `start_at_sigma`，且大於或等於 `end_at_sigma`。當 `start_at_sigma` 設定為 -1.0 時，會被視為無限大，表示只有 `end_at_sigma` 的下限邊界有效。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 已擴展的 sigma 序列，包含插入的額外中間值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
