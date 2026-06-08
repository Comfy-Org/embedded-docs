使用控制影像（canny）生成影像。此節點接收一張控制影像，並根據提供的提示詞，在遵循控制影像中偵測到的邊緣結構的同時，生成一張新的影像。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `control_image` | 用於 Canny 邊緣偵測控制的輸入影像 | IMAGE | 是 | - |
| `prompt` | 影像生成的提示詞（預設：空字串） | STRING | 否 | - |
| `prompt_upsampling` | 是否對提示詞進行上取樣。若啟用，會自動修改提示詞以產生更具創意的生成結果，但結果不具確定性（相同的種子不會產生完全相同的結果）。（預設：False） | BOOLEAN | 否 | - |
| `canny_low_threshold` | Canny 邊緣偵測的低閾值；若 `skip_preprocessing` 為 True 則忽略此參數（預設：0.1） | FLOAT | 否 | 0.01 - 0.99 |
| `canny_high_threshold` | Canny 邊緣偵測的高閾值；若 `skip_preprocessing` 為 True 則忽略此參數（預設：0.4） | FLOAT | 否 | 0.01 - 0.99 |
| `skip_preprocessing` | 是否跳過預處理；若 `control_image` 已經是 Canny 邊緣處理過的影像則設為 True，若為原始影像則設為 False。（預設：False） | BOOLEAN | 否 | - |
| `guidance` | 影像生成過程的引導強度（預設：30） | FLOAT | 否 | 1 - 100 |
| `steps` | 影像生成過程的步數（預設：50） | INT | 否 | 15 - 50 |
| `seed` | 用於建立雜訊的隨機種子。（預設：0） | INT | 否 | 0 - 18446744073709551615 |

**注意：** 當 `skip_preprocessing` 設為 True 時，`canny_low_threshold` 和 `canny_high_threshold` 參數將被忽略，因為控制影像被假定為已經處理過的 Canny 邊緣影像。此時 `control_image` 會直接作為預處理後的影像使用。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output_image` | 根據控制影像和提示詞生成的影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dedf55a2b2c183519d7f5be0d9a96abbe40716a247f574fc0d50f10f715949a7`
