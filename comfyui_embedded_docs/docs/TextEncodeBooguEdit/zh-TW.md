# TextEncodeBooguEdit

此節點為使用 Boogu 進行影像編輯準備條件化輸入。它處理參考影像以產生正向和負向條件化輸出。參考影像被使用兩次：來自影像的視覺標記僅添加到正向條件化中以增強編輯指令，而 VAE 參考潛在空間則同時添加到正向和負向條件化中，使其在 CFG 下相互抵消，從而保留原始影像的識別特徵。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用於文字編碼的 CLIP 模型 | CLIP | 是 | |
| `prompt` | 描述所需編輯的文字提示 | STRING | 是 | |
| `negative_prompt` | 描述編輯中應避免內容的文字提示 | STRING | 否 | |
| `vae` | 用於將參考影像編碼為潛在空間的 VAE 模型 | VAE | 否 | |
| `images` | 要編輯的參考影像。Boogu 專注於每個樣本一個參考；允許更多。 | IMAGE | 否 | 最多 16 張影像 |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 包含文字提示（含視覺標記）和參考潛在空間的條件化 | CONDITIONING |
| `negative` | 包含負向文字提示和參考潛在空間的條件化 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeBooguEdit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `170979acf5b2e9f25f96231a4b23a4376cfddcd4bda2fdd6e03528417e6931b0`
