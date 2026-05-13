> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/zh-TW.md)

# TextEncodeQwenImageEditPlus 節點文檔

TextEncodeQwenImageEditPlus 節點處理文字提示和可選圖像，為圖像生成或編輯任務生成條件數據。它使用專門的模板來分析輸入圖像，理解文字指令應如何修改它們，然後將此信息編碼以供後續生成步驟使用。該節點最多可處理三個輸入圖像，並在提供 VAE 時可選生成參考潛在變量。

## 輸入

| 參數 | 數據類型 | 必要 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 用於標記化和編碼的 CLIP 模型 |
| `prompt` | STRING | 是 | - | 描述所需圖像修改的文字指令（支援多行輸入和動態提示） |
| `vae` | VAE | 否 | - | 可選的 VAE 模型，用於從輸入圖像生成參考潛在變量 |
| `image1` | IMAGE | 否 | - | 第一個可選輸入圖像，用於分析和修改 |
| `image2` | IMAGE | 否 | - | 第二個可選輸入圖像，用於分析和修改 |
| `image3` | IMAGE | 否 | - | 第三個可選輸入圖像，用於分析和修改 |

**注意：** 當提供 VAE 時，節點會從所有輸入圖像生成參考潛在變量。該節點最多可同時處理三個圖像。圖像會自動調整為 384x384 像素以進行視覺語言處理，並調整為可被 8 整除的尺寸（目標面積為 1024x1024 像素）以進行 VAE 編碼。

## 輸出

| 輸出名稱 | 數據類型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 編碼後的條件數據，包含文字標記和用於圖像生成的可選參考潛在變量 |

---
**Source fingerprint (SHA-256):** `54889d9a3b70e41d623020f3fd5e3c798c72799492c67a9efd99f543c88bb968`
