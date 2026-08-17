# LTXV 裁剪引導

LTXVCropGuides 節點透過移除關鍵幀資訊並調整潛在維度來處理用於影片生成的 conditioning 與 latent 輸入。它會裁切潛在影像與雜訊遮罩，以排除關鍵幀區段，同時清除正向與負向 conditioning 輸入中的關鍵幀索引。這可為不需要關鍵幀引導的影片生成工作流程準備好資料。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 正向 conditioning 輸入，包含用於生成的引導資訊 | CONDITIONING | 是 | - |
| `negative` | 負向 conditioning 輸入，包含生成時應避免內容的引導資訊 | CONDITIONING | 是 | - |
| `latent` | 包含影像樣本與雜訊遮罩資料的潛在表示 | LATENT | 是 | - |

注意：如果正向 conditioning 中沒有關鍵幀索引，此節點會原封不動地回傳 positive、negative 與 latent 輸入。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 已清除關鍵幀索引與引導注意力項目的處理後正向 conditioning | CONDITIONING |
| `negative` | 已清除關鍵幀索引與引導注意力項目的處理後負向 conditioning | CONDITIONING |
| `latent` | 已裁切的潛在表示，其樣本與雜訊遮罩經過調整，且關鍵幀區段已被移除 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/zh-TW.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
