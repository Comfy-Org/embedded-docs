> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageStitch/zh-TW.md)

此節點允許您在指定方向（上、下、左、右）上將兩張圖片拼接在一起，並支援尺寸匹配和圖片間距功能。

## 輸入

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 說明 |
|---------------|-----------|-------------|---------|--------|-------------|
| `image1` | IMAGE | 必要 | - | - | 要拼接的第一張圖片 |
| `image2` | IMAGE | 可選 | None | - | 要拼接的第二張圖片，若未提供則僅回傳第一張圖片 |
| `direction` | STRING | 必要 | right | right/down/left/up | 拼接第二張圖片的方向：右、下、左或上 |
| `match_image_size` | BOOLEAN | 必要 | True | True/False | 是否將第二張圖片調整大小以匹配第一張圖片的尺寸 |
| `spacing_width` | INT | 必要 | 0 | 0-1024 | 圖片之間的間距寬度，必須為偶數 |
| `spacing_color` | STRING | 必要 | white | white/black/red/green/blue | 拼接圖片之間間距的顏色 |

> 對於 `spacing_color`，當使用「white/black」以外的顏色時，若 `match_image_size` 設為 `false`，則填充區域將以黑色顯示

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 拼接後的圖片 |

## 工作流程範例

在下方的工作流程中，我們使用 3 張不同尺寸的輸入圖片作為範例：

- image1：500x300
- image2：400x250
- image3：300x300

![工作流程](./asset/workflow.webp)

**第一個圖片拼接節點**

- `match_image_size`：false，圖片將以原始尺寸進行拼接
- `direction`：up，`image2` 將放置在 `image1` 上方
- `spacing_width`：20
- `spacing_color`：black

輸出圖片 1：

![輸出1](./asset/output-1.webp)

**第二個圖片拼接節點**

- `match_image_size`：true，第二張圖片將被縮放以匹配第一張圖片的高度或寬度
- `direction`：right，`image3` 將出現在右側
- `spacing_width`：20
- `spacing_color`：white

輸出圖片 2：

![輸出2](./asset/output-2.webp)