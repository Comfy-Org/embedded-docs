# 解析度分桶

此節點會依解析度整理一批潛在影像及其對應的 conditioning 資料。它會將具有相同高度與寬度的項目分組在一起，為每個不重複的解析度建立各自的批次。此流程適合用來準備高效率訓練所需的資料，因為它能讓模型將多個相同大小的項目一起處理。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `latents` | 要依解析度分桶的 latent 字典列表。 | LATENT | 是 | N/A |
| `conditioning` | conditioning 列表的列表（長度必須與 `latents` 相符）。 | CONDITIONING | 是 | N/A |

**注意：** 兩個輸入都是列表類型輸入，表示節點會分別接收每個輸入的項目列表。`latents` 列表中的項目數量必須與 `conditioning` 列表中的項目數量完全一致；如果數量不符，節點會引發錯誤。每個 latent 字典可以包含一個樣本批次，而對應的 conditioning 列表必須包含與該批次相符數量的 conditioning 項目，因為批次中的每個樣本都會與自己的 conditioning 條目配對。Latent 樣本的形狀可能是影像的 (B, C, H, W) 或影片的 (B, T, C, H, W)；此節點只會依高度與寬度將它們分組。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `latents` | 批次化的 latent 字典列表，每個解析度桶一個。 | LATENT |
| `conditioning` | conditioning 列表的列表，每個解析度桶一個。 | CONDITIONING |

**注意：** 兩個輸出都是列表類型輸出。每個輸出列表會針對輸入中每個不重複的解析度（高度與寬度）包含一個項目，順序為這些解析度首次出現的順序。每個桶內的 latent 會沿著新的批次維度堆疊。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/zh-TW.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
