# SeedVR2TemporalMerge

此節點將取樣的 SeedVR2 潛在時間區塊重新組合成單一完整長度的潛在表示。它使用重疊區域上的漢寧窗交叉淡入淡出來創建平滑過渡，或在未指定重疊時執行純粹的串接。

## ## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `latents` | 按順序排列的取樣時間區塊。 | LATENT | 是 | 潛在列表 |
| `temporal_overlap` | 分割 SeedVR2 潛在節點的 temporal_overlap 輸出。0 = 純粹串接。（預設值：0） | INT | 是 | 0 至 16384 |

**注意：** `temporal_overlap` 值必須大於或等於 0。序列中的最後一個區塊可能比其他區塊擁有更少的時間幀。所有區塊除了時間軸（T）之外必須具有匹配的維度，且第一個區塊必須是 5 維（B、C、T、H、W）。

## ## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `latent` | 重新組合後的完整長度潛在表示。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/zh-TW.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
