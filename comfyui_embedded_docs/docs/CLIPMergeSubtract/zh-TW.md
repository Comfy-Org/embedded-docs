# CLIPMergeSubtract

CLIPMergeSubtract 節點透過將第二個 CLIP 模型的權重從第一個模型中減去，來合併兩個 CLIP 模型。它會先複製第一個模型建立新的 CLIP 模型，再從第二個模型中減去關鍵修補程式（key patches），並以可調整的乘數控制減除強度。這允許透過從基礎模型中移除特定特徵，來進行精細調整的模型混合。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip1` | 將被複製並修改的基礎 CLIP 模型 | CLIP | 是 | - |
| `clip2` | 其關鍵修補程式將從基礎模型中減去的 CLIP 模型 | CLIP | 是 | - |
| `multiplier` | 控制減除操作的強度（預設值：1.0） | FLOAT | 是 | -10.0 到 10.0（步長：0.01） |

**注意：** 無論乘數值為何，此節點都會將 `.position_ids` 與 `.logit_scale` 參數排除在減除操作之外。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `clip` | 從第一個模型減去第二個模型權重後所得到的 CLIP 模型 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/zh-TW.md)

---
**Source fingerprint (SHA-256):** `62a8cf719c34d9e2b7321f6eeb03c881f0767fd36b80e25e74feff4c0a29045e`
