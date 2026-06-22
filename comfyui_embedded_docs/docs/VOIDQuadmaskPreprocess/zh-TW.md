# VOIDQuadmaskPreprocess

## 概述

VOIDQuadmaskPreprocess 節點透過將遮罩轉換為特殊的四層級「四元遮罩」，為 VOID 修復（inpainting）準備遮罩。它接收輸入遮罩，可選擇性地對主要區域進行擴張，然後將遮罩值量化為四個不同層級，分別代表不同的語義區域（主要物體、重疊區域、受影響區域和背景）。最後，它會反轉並標準化遮罩，使輸出值落在 [0, 1] 範圍內，其中 1.0 表示要移除的區域，0.0 表示要保留的區域。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `mask` | 要進行預處理的輸入遮罩。 | MASK | 是 | 不適用 |
| `dilate_width` | 主要遮罩區域的擴張半徑。值為 0 表示不進行擴張。（預設值：0） | INT | 否 | 0 到 50（步長：1） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `quadmask` | 預處理後的四元遮罩，其值範圍為 [0, 1]，代表四個離散層級：1.0（要移除的主要物體）、約 0.75（主要物體與受影響區域的重疊）、約 0.50（受影響區域）和 0.0（要保留的背景）。 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/zh-TW.md)

---
**Source fingerprint (SHA-256):** `12dc5ab215b80d81289942457ce2ddffcb9ec41fc738a53ca5fbf1e9181ed439`
