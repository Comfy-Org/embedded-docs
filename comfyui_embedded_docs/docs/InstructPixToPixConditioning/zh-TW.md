# 指令式像素轉像素條件設定

InstructPixToPixConditioning 節點透過將輸入影像與正向和負向文字提示條件結合，為 InstructPix2Pix 影像編輯準備條件資料。它使用 VAE 將影像編碼為潛在表示，將該潛在表示附加到兩個條件集合，並建立一個維度相符的零填充潛在表示。如果影像的寬度或高度不是 8 像素的倍數，則會在編碼前自動裁切影像。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 包含所需影像特徵之文字提示和設定的正向條件資料。 | CONDITIONING | 是 | - |
| `negative` | 包含非所需影像特徵之文字提示和設定的負向條件資料。 | CONDITIONING | 是 | - |
| `vae` | 用於將輸入影像編碼為潛在表示的 VAE 模型。 | VAE | 是 | - |
| `pixels` | 待處理並編碼到潛在空間的輸入影像。 | IMAGE | 是 | - |

**注意：** 輸入影像會在寬度和高度上自動裁切為 8 像素的倍數（向下取整），以確保與 VAE 編碼過程的相容性。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 附加了編碼後影像潛在表示的正向條件資料。 | CONDITIONING |
| `negative` | 附加了編碼後影像潛在表示的負向條件資料。 | CONDITIONING |
| `latent` | 與編碼後影像具有相同維度的零填充潛在張量。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
