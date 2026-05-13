> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/zh-TW.md)

## 概述

TomePatchModel 節點將 Token Merging (ToMe) 應用於擴散模型，以降低推理過程中的計算需求。其運作原理是選擇性地合併注意力機制中的相似令牌，使模型能夠在維持影像品質的同時處理較少的令牌。此技術有助於在不顯著影響品質的情況下加速生成過程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要套用令牌合併的擴散模型 |
| `比例` | FLOAT | 否 | 0.0 - 1.0 | 要合併的令牌比例（預設值：0.3） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已套用令牌合併的修改後模型 |

---
**Source fingerprint (SHA-256):** `23d63ffa1b468a8a41533cc926125f4ef566b13edd1d95a6ef1ae63096a9d878`
