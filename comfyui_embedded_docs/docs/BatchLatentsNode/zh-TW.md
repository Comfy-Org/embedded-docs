# 批次 latent

Batch Latents 節點將多個潛在輸入組合成單一批次。它接收可變數量的潛在樣本，並沿批次維度合併它們，使其能夠在後續節點中一起處理。這對於在單一操作中生成或處理多張影像非常有用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `latents` | 一組要組合成單一批次的潛在樣本。您必須至少提供一個潛在，並且最多可以添加 50 個。當您連接更多潛在時，節點會自動創建輸入插槽。 | LATENT | Yes | 1 to 50 inputs |

**注意：** 您必須至少提供一個潛在輸入，節點才能運作。當您連接更多潛在時，節點會自動創建輸入插槽，最多可達 50 個。

所有輸入的潛在都會在合併前重新調整形狀，以匹配第一個潛在的空間維度。每個潛在的 `batch_index` 中繼資料都會被帶到輸出；沒有 `batch_index` 的輸入會獲得從 0 開始的預設序列。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 包含所有輸入潛在合併為一個批次的單一潛在輸出。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`
