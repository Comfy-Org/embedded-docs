> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/zh-TW.md)

使用控制影像（canny）生成影像。此節點接收一個控制影像，並根據提供的提示詞生成新影像，同時遵循控制影像中偵測到的邊緣結構。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | 是 | - | 用於 canny 邊緣偵測控制的輸入影像 |
| `prompt` | STRING | 否 | - | 影像生成的提示詞（預設：空字串） |
| `prompt_upsampling` | BOOLEAN | 否 | - | 是否對提示詞進行上採樣。如果啟用，會自動修改提示詞以實現更具創意的生成，但結果具有不確定性（相同種子不會產生完全相同的結果）。（預設：False） |
| `canny_low_threshold` | FLOAT | 否 | 0.01 - 0.99 | Canny 邊緣偵測的低閾值；如果 skip_processing 為 True 則忽略此參數（預設：0.1） |
| `canny_high_threshold` | FLOAT | 否 | 0.01 - 0.99 | Canny 邊緣偵測的高閾值；如果 skip_processing 為 True 則忽略此參數（預設：0.4） |
| `skip_preprocessing` | BOOLEAN | 否 | - | 是否跳過預處理；如果 control_image 已經是 canny 化影像則設為 True，如果是原始影像則設為 False。（預設：False） |
| `guidance` | FLOAT | 否 | 1 - 100 | 影像生成過程的引導強度（預設：30） |
| `steps` | INT | 否 | 15 - 50 | 影像生成過程的步驟數（預設：50） |
| `seed` | INT | 否 | 0 - 18446744073709551615 | 用於創建噪聲的隨機種子。（預設：0） |

**注意：** 當 `skip_preprocessing` 設為 True 時，`canny_low_threshold` 和 `canny_high_threshold` 參數將被忽略，因為控制影像被假定為已經處理過的 canny 邊緣影像。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output_image` | IMAGE | 基於控制影像和提示詞生成的影像 |