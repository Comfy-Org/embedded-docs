# Pad Image

使用純色或邊緣的鏡像副本為影像填充邊距。填充量可以設定為每側精確的像素數、尺寸倍數，或設為讓寬度與高度能被某個數字整除的最小填充量，這在儲存或平鋪之前相當實用。原始影像會保留其位置：`left` 與 `top` 填充加在其之前，`right` 與 `bottom` 填充則加在其之後。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要填充邊距的影像。 | IMAGE | 是 | - |
| `padding_type` | 要添加多少填充：`"pad dimensions"` 表示每側的精確數量，`"pad by multiplier"` 表示相對於輸入的輸出尺寸，`"pad to multiple"` 表示填充至下一個倍數。選擇某個選項後會顯示其參數。 | DYNAMIC_COMBO | 是 | `"pad dimensions"`<br>`"pad by multiplier"`<br>`"pad to multiple"` |
| `left` | 在左側添加的像素數。當 `padding_type` 為 `"pad dimensions"` 時可用（預設值：0）。 | INT | 是 | 0 至 16384 |
| `top` | 在上方添加的像素數。當 `padding_type` 為 `"pad dimensions"` 時可用（預設值：0）。 | INT | 是 | 0 至 16384 |
| `right` | 在右側添加的像素數。當 `padding_type` 為 `"pad dimensions"` 時可用（預設值：0）。 | INT | 是 | 0 至 16384 |
| `bottom` | 在下方添加的像素數。當 `padding_type` 為 `"pad dimensions"` 時可用（預設值：0）。 | INT | 是 | 0 至 16384 |
| `multiplier` | 相對於輸入的輸出尺寸，例如 1.5 會在每側增加 25%。填充會平均分配到相對的兩側。當 `padding_type` 為 `"pad by multiplier"` 時可用（預設值：1.0）。 | FLOAT | 是 | 1.0 至 8.0（步長 0.01） |
| `multiple` | 進行填充，使寬度與高度能被此數字整除。填充會平均分配到相對的兩側，多出的像素會分配給右側與下方。當 `padding_type` 為 `"pad to multiple"` 時可用（預設值：32）。 | INT | 是 | 1 至 16384 |
| `padding_style` | 填充區域要填入什麼：`"color"` 或 `"mirror image"`。選擇某個選項後會顯示其參數。 | DYNAMIC_COMBO | 是 | `"color"`<br>`"mirror image"` |
| `color` | 填充區域的填充顏色；alpha 會被忽略。當 `padding_style` 為 `"color"` 時可用（預設值：`"#000000"`）。 | COLOR | 是 | - |
| `feathering` | 在填充側將影像邊緣的這麼多像素與填充顏色混合。0 表示保留硬邊。當 `padding_style` 為 `"color"` 時可用（預設值：0）。 | INT | 是 | 0 至 16384 |

`"mirror image"` 會反射影像邊緣，而不是以顏色填入。邊緣像素不會重複，而當填充範圍比影像本身更寬或更高時，鏡像影像會重複以覆蓋其餘區域。當所有填充量計算結果皆為 0 時，會原樣返回輸入影像。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 填充後的影像，具有與輸入相同的批次維度與通道數。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PadImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9373cd6aa287befba74374b9b2a6c38b20344b5715e9aaa4cf49282ae930c91d`
