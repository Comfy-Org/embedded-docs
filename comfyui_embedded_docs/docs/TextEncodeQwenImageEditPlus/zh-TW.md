# TextEncodeQwenImageEditPlus

### TextEncodeQwenImageEditPlus 節點

TextEncodeQwenImageEditPlus 節點處理文字提示和可選影像，以產生用於影像生成或編輯任務的 conditioning 資料。它使用專門的模板來分析輸入影像，並理解文字指令應如何修改它們，然後將此資訊編碼以供後續生成步驟使用。此節點最多可處理三個輸入影像，並在提供 VAE 時可選地生成參考潛在變量。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於分詞和編碼的 CLIP 模型 | CLIP | 是 | - |
| `prompt` | 描述所需影像修改的文字指令（支援多行輸入和動態提示） | STRING | 是 | - |
| `vae` | 可選的 VAE 模型，用於從輸入影像生成參考潛在變量 | VAE | 否 | - |
| `image1` | 第一個可選輸入影像，用於分析和修改 | IMAGE | 否 | - |
| `image2` | 第二個可選輸入影像，用於分析和修改 | IMAGE | 否 | - |
| `image3` | 第三個可選輸入影像，用於分析和修改 | IMAGE | 否 | - |

**注意：** 當提供 VAE 時，此節點會從所有輸入影像生成參考潛在變量。此節點最多可同時處理三個影像。影像會自動縮放至約 384×384 像素的目標面積（保持長寬比）以進行視覺語言處理，並縮放至約 1024×1024 像素的目標面積且尺寸可被 8 整除，以進行 VAE 編碼。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 包含文字標記和可選參考潛在變量的編碼後 conditioning 資料，用於影像生成 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
