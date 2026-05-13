> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/zh-TW.md)

使用控制影像（canny）生成影像。此節點接收一張控制影像，並根據提供的提示詞，在遵循控制影像中偵測到的邊緣結構的同時，生成一張新的影像。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | 是 | - | 用於 Canny 邊緣偵測控制的輸入影像 |
| `prompt` | STRING | 否 | - | 影像生成的提示詞（預設：空字串） |
| `prompt_upsampling` | BOOLEAN | 否 | - | 是否對提示詞進行上取樣。若啟用，會自動修改提示詞以產生更具創意的生成結果，但結果不具確定性（相同的種子不會產生完全相同的結果）。（預設：False） |
| `canny_low_threshold` | FLOAT | 否 | 0.01 - 0.99 | Canny 邊緣偵測的低閾值；若 `skip_preprocessing` 為 True 則忽略此參數（預設：0.1） |
| `canny_high_threshold` | FLOAT | 否 | 0.01 - 0.99 | Canny 邊緣偵測的高閾值；若 `skip_preprocessing` 為 True 則忽略此參數（預設：0.4） |
| `skip_preprocessing` | BOOLEAN | 否 | - | 是否跳過預處理；若 `control_image` 已經是 Canny 邊緣處理過的影像則設為 True，若為原始影像則設為 False。（預設：False） |
| `guidance` | FLOAT | 否 | 1 - 100 | 影像生成過程的引導強度（預設：30） |
| `steps` | INT | 否 | 15 - 50 | 影像生成過程的步數（預設：50） |
| `seed` | INT | 否 | 0 - 18446744073709551615 | 用於建立雜訊的隨機種子。（預設：0） |

**注意：** 當 `skip_preprocessing` 設為 True 時，`canny_low_threshold` 和 `canny_high_threshold` 參數將被忽略，因為控制影像被假定為已經處理過的 Canny 邊緣影像。此時 `control_image` 會直接作為預處理後的影像使用。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output_image` | IMAGE | 根據控制影像和提示詞生成的影像 |

---
**Source fingerprint (SHA-256):** `dedf55a2b2c183519d7f5be0d9a96abbe40716a247f574fc0d50f10f715949a7`
