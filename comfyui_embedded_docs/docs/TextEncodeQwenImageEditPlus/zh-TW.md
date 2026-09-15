# TextEncodeQwenImageEditPlus

TextEncodeQwenImageEditPlus 節點會處理文字提示詞以及最多三張選用影像，以產生用於影像生成或編輯任務的條件資料。它使用專用範本，先要求模型描述輸入影像的關鍵特徵，接著說明使用者的文字指令應如何改變這些影像，因此編碼結果能同時理解影像與所請求的修改。當提供 VAE 時，此節點也會從輸入影像建立參考 latent。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於分詞與編碼的 CLIP 模型 | CLIP | 是 | - |
| `提示詞` | 描述所需影像修改的文字指令（支援多行輸入與動態提示詞） | STRING | 是 | - |
| `vae` | 選用的 VAE 模型，用於從輸入影像產生參考 latent | VAE | 否 | - |
| `圖像1` | 第一張選用輸入影像，用於分析與修改 | IMAGE | 否 | - |
| `圖像2` | 第二張選用輸入影像，用於分析與修改 | IMAGE | 否 | - |
| `圖像3` | 第三張選用輸入影像，用於分析與修改 | IMAGE | 否 | - |

**注意：** 當提供 VAE 時，此節點會從所有提供的輸入影像產生參考 latent。一次最多可處理三張影像。影像會縮放至目標區域 384x384 像素（保持長寬比）以進行視覺語言處理，並縮放至可被 8 整除的尺寸（目標區域為 1024x1024 像素）以進行 VAE 編碼。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 包含文字 token 與選擇性參考 latent 的編碼條件資料，用於影像生成 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
