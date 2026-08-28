# LTXV 裁剪引導

LTXVCropGuides 節點透過移除關鍵幀資訊並調整潛在維度來處理影片生成的 conditioning 與 latent 輸入。它會裁切潛在影像與雜訊遮罩以排除關鍵幀區段，同時清除正向與負向 conditioning 輸入中的關鍵幀索引與引導注意力條目。這會為不需要關鍵幀引導的影片生成工作流程準備資料。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 包含生成引導資訊的正向 conditioning 輸入。其關鍵幀索引決定從 latent 中裁切多少幀。 | CONDITIONING | 是 | - |
| `負向` | 包含生成時要避免之內容的負向 conditioning 輸入。其關鍵幀資料會與正向 conditioning 一併清除。 | CONDITIONING | 是 | - |
| `潛在空間` | 包含影像樣本與雜訊遮罩資料的 latent 表示。當正向 conditioning 中存在關鍵幀時，會從樣本與雜訊遮罩中移除最後一個關鍵幀所對應的幀。 | LATENT | 是 | - |

注意：只有在正向 conditioning 包含關鍵幀索引時才會進行裁切。若未偵測到任何關鍵幀，則正向與負向 conditioning 以及 latent 都會原封不動地通過。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `正向` | 已處理的正向 conditioning，其關鍵幀索引與引導注意力條目已清除 | CONDITIONING |
| `負向` | 已處理的負向 conditioning，其關鍵幀索引與引導注意力條目已清除 | CONDITIONING |
| `潛在空間` | 已裁切的 latent 表示，包含調整後的樣本與雜訊遮罩，且已移除關鍵幀區段 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/zh-TW.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
