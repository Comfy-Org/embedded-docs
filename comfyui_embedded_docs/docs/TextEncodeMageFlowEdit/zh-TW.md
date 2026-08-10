# TextEncodeMageFlowEdit

## 概述
此節點為 Mage-Flow-Edit 模型編碼一個編輯指令（提示詞）以及一張或多張參考影像。它將所有參考影像調整為目標輸出解析度，若提供了 VAE，則將其編碼為潛在空間，並將參考潛在變數附加到 conditioning 輸出。同時會生成一個具有正確取樣維度的空白潛在張量，確保其大小始終與輸出寬度和高度相符。

## 輸入
| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|------|------|----------|------|------|
| `clip` | 用於將文字提示詞進行分詞和編碼的 CLIP 模型。 | CLIP | 是 | |
| `prompt` | 要套用的編輯指令（正向提示詞）。 | STRING | 是 | 多行，啟用動態提示詞 |
| `negative_prompt` | 用於引導避免的負向提示詞。預設值：空字串（若為空白則內部使用一個空格）。顯示在介面的進階區段。 | STRING | 否 | 多行，啟用動態提示詞 |
| `vae` | 用於將參考影像編碼為潛在空間的 VAE 模型。若未提供，則 conditioning 輸出中不會加入參考潛在變數。 | VAE | 否 | |
| `images` | 要編輯的參考影像。所有參考影像在編碼前會調整為輸出解析度。 | IMAGE（自動增長） | 否 | 最多 16 張影像（命名為 `image_1`…`image_16`），至少 0 張 |
| `width` | 輸出寬度（像素）。若設為 0，則使用第一張參考影像的寬度。始終向下取整為 16 的倍數。預設值：0。 | INT | 是 | 0 至 8192（步長 16） |
| `height` | 輸出高度（像素）。與寬度的回退行為相同。預設值：0。 | INT | 是 | 0 至 8192（步長 16） |
| `batch_size` | 要產生的潛在樣本數量。預設值：1。 | INT | 是 | 1 至 4096 |

**關於參數相依性的說明：**
- 若 `width` 和/或 `height` 為 0 且未提供任何參考影像，則兩者均回退為 1024。
- 如果 `width` 或 `height` 中只有一個為 0，缺失的維度取自第一張參考影像，而顯式設定的維度保持不變。
- `vae` 參數為選用；僅當連接了 VAE 時，才會產生參考潛在變數並將其附加到 conditioning。
- `negative_prompt` 欄位為選用 – 若留空，則內部使用一個空格作為負向文字。
- 對於文字條件，每張參考影像都會調整大小，使其最長邊不超過 384 像素，與訓練預處理一致。而 VAE 編碼分支則會將所有參考影像調整到完整的輸出解析度。

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|-----------|------|----------|
| `positive` | 包含正向提示詞 token 的 conditioning 輸出；若提供了 VAE，則還包含編碼後的參考潛在變數。 | CONDITIONING |
| `negative` | 包含負向提示詞 token 的 conditioning 輸出；若提供了 VAE，則包含相同的參考潛在變數。 | CONDITIONING |
| `latent` | 一個形狀為 `[batch_size, 128, height÷16, width÷16]` 的空白潛在張量，用於取樣期間的初始雜訊。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMageFlowEdit/zh-TW.md)

---
**Source fingerprint (SHA-256):** `880d8856b7f6e656bc68ca953fbf892898d05bc5d65290ae3bf7a4405ee09be3`
