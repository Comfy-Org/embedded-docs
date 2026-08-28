# 指令式像素轉像素條件設定

InstructPixToPixConditioning 節點透過結合正向與負向文字提示及影像資料，為 InstructPix2Pix 影像編輯準備 conditioning 資料。它會將輸入影像經由 VAE 編碼器處理以建立潛在表示，並將這些潛在表示附加到正向與負向的 conditioning 資料上。此節點會自動處理影像尺寸，將其中心裁切至 8 像素的倍數，以確保與 VAE 編碼流程相容。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 包含所需影像特徵之文字提示與設定的正向 conditioning 資料 | CONDITIONING | 是 | - |
| `負向` | 包含不想要的影像特徵之文字提示與設定的負向 conditioning 資料 | CONDITIONING | 是 | - |
| `vae` | 用於將輸入影像編碼為潛在表示的 VAE 模型 | VAE | 是 | - |
| `像素` | 要處理並編碼至潛在空間的輸入影像 | IMAGE | 是 | - |

**注意：** 輸入影像的尺寸會自動透過中心裁切調整為寬與高皆為 8 像素的倍數，以確保與 VAE 編碼流程相容。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `正向` | 帶有附加潛在影像表示的正向 conditioning 資料 | CONDITIONING |
| `負向` | 帶有附加潛在影像表示的負向 conditioning 資料 | CONDITIONING |
| `潛在空間` | 與編碼後影像具有相同尺寸的空白潛在張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
