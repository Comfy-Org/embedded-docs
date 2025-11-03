> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmas/zh-TW.md)

SplitSigmas 節點專為根據指定步驟將 sigma 值序列分割成兩部分而設計。此功能對於需要對 sigma 序列的初始部分和後續部分進行不同處理或操作的任務至關重要，從而實現對這些值更靈活且具針對性的操控。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
|----------|----------|------|
| `sigmas` | `SIGMAS` | `sigmas` 參數代表待分割的 sigma 值序列。它對於確定分割點及產生的兩個 sigma 值序列至關重要，會影響節點的執行過程與結果。 |
| `step`   | `INT`    | `step` 參數指定了 sigma 序列應被分割的索引位置。它在定義兩個輸出 sigma 序列之間的分界點方面扮演關鍵角色，會影響節點的功能特性與輸出結果。 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
|----------|----------|------|
| `sigmas` | `SIGMAS` | 該節點會輸出兩個 sigma 值序列，每個序列代表原始序列在指定步驟處分割後的一部分。這些輸出對於後續需要對 sigma 值進行差異化處理的操作至關重要。 |