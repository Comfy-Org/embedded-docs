# SeedVR2TemporalMerge

此節點重新組合先前由 Split SeedVR2 Latent 節點分割的潛在影片資料時間區塊。它在重疊區域使用漢寧窗交叉淡入淡出，以在區塊之間建立平滑過渡，或在未指定重疊時執行簡單的串接。

## 輸入
| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `latents` | 按序列順序排列的已取樣時間區塊。 | LATENT | 是 | 潛在變數列表 |
| `temporal_overlap` | Split SeedVR2 Latent 的 `temporal_overlap` 輸出。0 = 純串接。 | INT | 是 | 0 至 16384（預設值：0） |

**注意：** `temporal_overlap` 參數必須從 Split SeedVR2 Latent 節點的 `temporal_overlap` 輸出接線。所有輸入潛在變數必須具有相同的批次大小、通道數、高度和寬度。只有最後一個區塊的時間維度可能比其他區塊短。

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `latent` | 重新組合後的完整長度潛在變數。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/zh-TW.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
