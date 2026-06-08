## 概述

LoraSave 節點可從模型差異中提取並儲存 LoRA（低秩適應）檔案。它能處理擴散模型差異、文字編碼器差異，或同時處理兩者，將其轉換為指定秩和類型的 LoRA 格式。產生的 LoRA 檔案會儲存至輸出目錄以供後續使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `檔名前綴` | 輸出檔案名稱的前綴（預設值："loras/ComfyUI_extracted_lora"） | STRING | 是 | - |
| `秩(rank)` | LoRA 的秩值，控制大小與複雜度（預設值：8） | INT | 是 | 1-4096 |
| `lora類型` | 要建立的 LoRA 類型（預設值："standard"） | COMBO | 是 | `"standard"`<br>`"locon"`<br>`"loha"`<br>`"lokr"`<br>`"dylora"` |
| `偏差差異` | 是否在 LoRA 計算中包含偏置差異（預設值：True） | BOOLEAN | 是 | - |
| `模型差異` | 要轉換為 LoRA 的 ModelSubtract 輸出 | MODEL | 否 | - |
| `文字編碼器差異` | 要轉換為 LoRA 的 CLIPSubtract 輸出 | CLIP | 否 | - |

**注意：** 節點運作時至少需提供 `model_diff` 或 `text_encoder_diff` 其中一項。若兩者皆省略，節點將不會產生任何輸出。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| - | 此節點會將 LoRA 檔案儲存至輸出目錄，但不會透過工作流程回傳任何資料 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fdf020915ee233cf68250dcdcf87e7862d13ccc4fa73d8da8245727fdac46015`
