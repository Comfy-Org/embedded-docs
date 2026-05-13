> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/zh-TW.md)

## 概述

LTXVCropGuides 節點透過移除關鍵幀資訊並調整潛在維度，處理用於影片生成的條件與潛在輸入。它會裁切潛在影像與雜訊遮罩，以排除關鍵幀部分，同時清除正向與負向條件輸入中的關鍵幀索引。這可為不需要關鍵幀引導的影片生成工作流程準備資料。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 包含生成引導資訊的正向條件輸入 |
| `negative` | CONDITIONING | 是 | - | 包含生成時應避免內容引導資訊的負向條件輸入 |
| `latent` | LATENT | 是 | - | 包含影像樣本與雜訊遮罩資料的潛在表示 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已清除關鍵幀索引與引導注意力條目的處理後正向條件 |
| `negative` | CONDITIONING | 已清除關鍵幀索引與引導注意力條目的處理後負向條件 |
| `latent` | LATENT | 已裁切的潛在表示，包含調整後的樣本與雜訊遮罩，其中關鍵幀部分已被移除 |

---
**Source fingerprint (SHA-256):** `029309c260e09221cc9a046897589d99498f6e8ad984ef6052e50be9a0ea7b6d`
