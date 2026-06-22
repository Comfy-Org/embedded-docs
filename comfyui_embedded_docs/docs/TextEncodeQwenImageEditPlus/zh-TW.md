# TextEncodeQwenImageEditPlus

TextEncodeQwenImageEditPlus 節點處理文字提示和可選圖像，為圖像生成或編輯任務生成條件數據。它使用專門的模板來分析輸入圖像，理解文字指令應如何修改它們，然後將此信息編碼以供後續生成步驟使用。該節點最多可處理三個輸入圖像，並在提供 VAE 時可選生成參考潛在變量。

## 輸入

| 參數 | 描述 | 數據類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於標記化和編碼的 CLIP 模型 | CLIP | 是 | - |
| `提示詞` | 描述所需圖像修改的文字指令（支援多行輸入和動態提示） | STRING | 是 | - |
| `vae` | 可選的 VAE 模型，用於從輸入圖像生成參考潛在變量 | VAE | 否 | - |
| `圖像1` | 第一個可選輸入圖像，用於分析和修改 | IMAGE | 否 | - |
| `圖像2` | 第二個可選輸入圖像，用於分析和修改 | IMAGE | 否 | - |
| `圖像3` | 第三個可選輸入圖像，用於分析和修改 | IMAGE | 否 | - |

**注意：** 當提供 VAE 時，節點會從所有輸入圖像生成參考潛在變量。該節點最多可同時處理三個圖像。圖像會自動調整為 384x384 像素以進行視覺語言處理，並調整為可被 8 整除的尺寸（目標面積為 1024x1024 像素）以進行 VAE 編碼。

## 輸出

| 輸出名稱 | 描述 | 數據類型 |
| --- | --- | --- |
| `CONDITIONING` | 編碼後的條件數據，包含文字標記和用於圖像生成的可選參考潛在變量 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/zh-TW.md)

---
**Source fingerprint (SHA-256):** `54889d9a3b70e41d623020f3fd5e3c798c72799492c67a9efd99f543c88bb968`
