# MiniMax H3 Image

使用 MiniMax H3 Image 從文字生成影像，或編輯與組合最多 16 張參考影像。提示詞會依連接順序以 `@Image1`、`@Image2` 等方式指稱這些參考影像。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | `MiniMax-H3-Image`，或使用執行速度更快的 `MiniMax-H3-Image-Highspeed`。預設：`"MiniMax-H3-Image"`。 | COMBO | 是 | `"MiniMax-H3-Image"`<br>`"MiniMax-H3-Image-Highspeed"` |
| `prompt` | 要生成的內容，或如何編輯參考影像。連接參考影像時，最多可達 8,000 個字元。預設：空。 | STRING | 是 | 1 至 8000 個字元 |
| `size` | `2K` 與 `4K` 會依長寬比推導尺寸；`custom` 則設定確切的寬度與高度。預設：`"2K"`。 | DYNAMIC_COMBO | 是 | `"2K"`<br>`"4K"`<br>`"custom"` |
| `enhance_prompt` | MiniMax 會在生成前將提示詞改寫為詳細的場景描述。影像編輯一律會進行增強。關閉時，請選擇固定長寬比或自訂尺寸。預設：True。 | BOOLEAN | 否 | True<br>False |
| `seed` | 控制此節點是否重新執行；無論種子值為何，結果都是不確定的。預設：42。 | INT | 否 | 0 至 2147483647 |
| `images` | 要編輯或組合的參考影像，在提示詞中依連接順序以 `@Image1` 至 `@Image16` 指稱。 | AUTOGROW | 否 | 最多 16 張影像 |

### 尺寸 "2K" 與 "4K" 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | 使用 `auto` 時，MiniMax 會從提示詞中挑選比例，或在有連接參考影像時依循該參考影像。關閉 `enhance_prompt` 的文字轉圖片需要固定比例。預設：`"auto"`。 | COMBO | 是 | 有多個選項可用 |

### 尺寸 "custom" 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `width` | 輸出寬度（像素）。預設：2048。 | INT | 是 | 512 至 7680（步進值：16） |
| `height` | 輸出高度（像素）。預設：2048。 | INT | 是 | 512 至 7680（步進值：16） |

注意：使用自訂尺寸時，寬度乘以高度必須介於 655,360 至 20,000,000 像素之間，且長寬比最多為 3:1。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `image` | 生成或編輯後的影像，格式為 PNG。 | IMAGE |
| `revised_prompt` | 提示詞增強開啟時，MiniMax 所使用的改寫後提示詞。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxH3ImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `723eb4c2d3b303ece041f98bd5b773c669affb9a7b3da0c08ffcac4ee89f8e11`
