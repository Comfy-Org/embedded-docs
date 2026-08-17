# 裁剪影片潛在空間

TrimVideoLatent 節點從影片潛在表示的開頭移除幀。它接受一個潛在影片樣本，並從開頭修剪掉指定數量的幀，傳回影片的其餘部分。這允許您透過移除初始幀來縮短影片序列。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 包含要修剪的影片幀的輸入潛在影片表示 | LATENT | 是 | - |
| `trim_amount` | 要從影片開頭移除的幀數（預設值：0） | INT | 是 | 0 to 99999 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 修剪後的潛在影片表示，已從開頭移除了指定數量的幀 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `33b7a899f2002e9a7008f2ca93de853c08dd0629a4c6867fb42aae4ec2eb864b`
