> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageStitch/zh-TW.md)

此節點允許您以指定方向（上、下、左、右）拼接兩張圖片，並支援尺寸匹配和圖片間距設定。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 描述 |
|---------------|-----------|-------------|---------|--------|-------------|
| `image1` | IMAGE | 必填 | - | - | 要拼接的第一張圖片 |
| `image2` | IMAGE | 選填 | None | - | 要拼接的第二張圖片，如未提供則僅返回第一張圖片 |
| `direction` | STRING | 必填 | right | right/down/left/up | 拼接第二張圖片的方向：右側、下方、左側或上方 |
| `match_image_size` | BOOLEAN | 必填 | True | True/False | 是否調整第二張圖片尺寸以匹配第一張圖片的尺寸 |
| `spacing_width` | INT | 必填 | 0 | 0-1024 | 圖片間距的寬度，必須為偶數 |
| `spacing_color` | STRING | 必填 | white | white/black/red/green/blue | 拼接圖片間距的顏色 |

> 關於 `spacing_color`，當使用 "white/black" 以外的顏色時，如果 `match_image_size` 設為 `false`，填充區域將顯示為黑色

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 拼接後的圖片 |

## 工作流程示例

在以下工作流程中，我們使用 3 張不同尺寸的輸入圖片作為範例：

- image1: 500x300
- image2: 400x250  
- image3: 300x300

![工作流程](./asset/workflow.webp)

**第一個圖片拼接節點**

- `match_image_size`: false，圖片將以原始尺寸拼接
- `direction`: up，`image2` 將置於 `image1` 上方
- `spacing_width`: 20
- `spacing_color`: black

輸出圖片 1：

![輸出1](./asset/output-1.webp)

**第二個圖片拼接節點**

- `match_image_size`: true，第二張圖片將縮放以匹配第一張圖片的高度或寬度
- `direction`: right，`image3` 將出現在右側
- `spacing_width`: 20
- `spacing_color`: white

輸出圖片 2：

![輸出2](./asset/output-2.webp)