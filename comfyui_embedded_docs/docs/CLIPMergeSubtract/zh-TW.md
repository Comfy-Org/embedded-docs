> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/zh-TW.md)

## 概述

CLIPMergeSubtract 節點透過從一個 CLIP 模型中減去另一個模型的權重來執行模型合併。它會先複製第一個模型來建立新的 CLIP 模型，然後從中減去第二個模型的關鍵修補程式，並透過可調整的乘數來控制減去強度。這使得能夠透過從基礎模型中移除特定特徵來進行精細的模型混合。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip1` | CLIP | 是 | - | 將被複製並修改的基礎 CLIP 模型 |
| `clip2` | CLIP | 是 | - | 其關鍵修補程式將從基礎模型中減去的 CLIP 模型 |
| `乘數` | FLOAT | 是 | -10.0 至 10.0 | 控制減去操作的強度（預設值：1.0） |

**注意：** 無論乘數值為何，此節點都會從減去操作中排除 `.position_ids` 和 `.logit_scale` 參數。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `clip` | CLIP | 從第一個模型中減去第二個模型權重後所產生的 CLIP 模型 |

---
**Source fingerprint (SHA-256):** `3136cf509fcbfa291af8f820928a6cc14de7a586f953af0ada9bea949b437d86`
