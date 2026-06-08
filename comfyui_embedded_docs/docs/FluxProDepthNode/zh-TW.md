此節點使用深度控制影像作為引導來生成影像。它接收控制影像和文字提示，然後建立一個同時遵循控制影像深度資訊與提示描述的新影像。該節點會連接外部 API 來執行影像生成過程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `control_image` | 用於引導影像生成的深度控制影像 | IMAGE | 是 | - |
| `prompt` | 影像生成的提示文字（預設值：空字串） | STRING | 否 | - |
| `prompt_upsampling` | 是否對提示進行上取樣。若啟用，會自動修改提示以產生更具創意的生成結果，但結果不具確定性（相同種子不會產生完全相同的結果）。（預設值：False） | BOOLEAN | 否 | - |
| `skip_preprocessing` | 是否跳過預處理；若 `control_image` 已為深度圖則設為 True，若為原始影像則設為 False。（預設值：False） | BOOLEAN | 否 | - |
| `guidance` | 影像生成過程的引導強度（預設值：15） | FLOAT | 否 | 1-100 |
| `steps` | 影像生成過程的步數（預設值：50） | INT | 否 | 15-50 |
| `seed` | 用於建立雜訊的隨機種子。（預設值：0） | INT | 否 | 0-18446744073709551615 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output_image` | 根據深度控制影像和提示生成的影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `34b80d7d63158b7dc4ad02da6b3a573b713d77efd0955d3477409f776f964462`
