# 取樣影片影格

`VideoFrameSample` 節點使用四種策略之一從影片中提取固定數量的影格。對於連續策略「head」和「tail」，輸出為延遲影片參考（影格不會被解碼）；對於非連續策略「uniform」和「random」，僅會解碼選定的影格。

## 輸入
| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|------|------|----------|------|------|
| `影片` | 輸入影片。 | VIDEO | 是 | – |
| `影格數量` | 要取樣的影格數量（預設：16）。 | INT | 是 | 1 – 9999 |
| `策略` | 取樣策略（預設："uniform"）。 | COMBO | 是 | `"uniform"`<br>`"head"`<br>`"tail"`<br>`"random"` |
| `隨機種子` | 隨機種子，僅在「random」策略中使用（預設：0）。 | INT | 是 | 0 – 18446744073709551615 |

- `num_frames` 會自動限制為輸入影片的總影格數。
- 除非 `strategy` 設為 `"random"`，否則 `seed` 參數不會產生任何效果。

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|----------|------|----------|
| `影片` | 取樣後的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoFrameSample/zh-TW.md)

---
**Source fingerprint (SHA-256):** `727504a9cf7fe5505c33da071cb8f21a38e1b7c0f964c5da172d9cedfc2f2300`
