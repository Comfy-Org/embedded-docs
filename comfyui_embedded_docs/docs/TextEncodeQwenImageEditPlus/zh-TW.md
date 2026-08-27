# TextEncodeQwenImageEditPlus

TextEncodeQwenImageEditPlus 節點處理文字提示詞和選用影像，以產生用於影像生成或編輯任務的 conditioning 資料。它使用專門的模板來分析輸入影像，並理解文字指令應如何修改這些影像，然後將此資訊編碼以供後續的生成步驟使用。此節點最多可處理三張輸入影像，並在提供 VAE 時選擇性地產生參考潛在變量。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於分詞與編碼的 CLIP 模型 | CLIP | 是 | - |
| `提示詞` | 描述所需影像修改的文字指令（支援多行輸入與動態提示詞） | STRING | 是 | - |
| `vae` | 選用的 VAE 模型，用於從輸入影像產生參考潛在變量 | VAE | 否 | - |
| `圖像1` | 第一張選用的輸入影像，用於分析與修改 | IMAGE | 否 | - |
| `圖像2` | 第二張選用的輸入影像，用於分析與修改 | IMAGE | 否 | - |
| `圖像3` | 第三張選用的輸入影像，用於分析與修改 | IMAGE | 否 | - |

**注意：** 當提供 VAE 時，節點會從所有提供的輸入影像產生參考潛在變量。一次最多可處理三張影像。影像會縮放至 384x384 像素的目標面積（保持長寬比）以進行視覺語言處理，並縮放至尺寸為 8 的倍數（目標面積為 1024x1024 像素）以進行 VAE 編碼。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 編碼後的 conditioning 資料，包含文字 token 與選用的參考潛在變量，用於影像生成 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
