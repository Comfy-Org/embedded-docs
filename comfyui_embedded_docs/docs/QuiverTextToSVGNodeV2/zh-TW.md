# Quiver Text to SVG

使用 Quiver AI 從文字提示生成可縮放向量圖形（SVG）。選用的參考影像與樣式指示可引導生成。

選取 `model` 會顯示下列模型特定參數，而參考影像的數量上限也取決於所選模型。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於 SVG 生成的模型。 | DYNAMIC_COMBO | 是 | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `prompt` | 所需 SVG 輸出的文字描述。必須包含至少一個非空白字元（預設：空）。 | STRING | 是 | 任意文字 |
| `instructions` | 額外的樣式或格式指引。選用的進階參數（預設：空）。 | STRING | 否 | 任意文字 |
| `reference_images` | 可擴充插槽：連接一或多個選用的參考影像（`ref_1`、`ref_2`、...），以引導生成。影像數量上限取決於所選模型。 | IMAGE | 否 | 最多 14<br>最多 4 |
| `width` | 輸出 SVG 畫布（viewBox）的寬度，單位為使用者單位。同時設定 `width` 與 `height` 可控制輸出尺寸與長寬比；將任一項保留為 0 可讓模型選擇，通常會得到方形畫布。進階參數（預設：0）。 | INT | 是 | 0 到 8192 |
| `height` | 輸出 SVG 畫布（viewBox）的高度，單位為使用者單位。同時設定 `width` 與 `height` 可控制輸出尺寸與長寬比；將任一項保留為 0 可讓模型選擇，通常會得到方形畫布。進階參數（預設：0）。 | INT | 是 | 0 到 8192 |
| `seed` | 用於決定節點是否應重新執行的種子；無論 `seed` 值為何，實際結果皆不具確定性。此參數具有「生成後控制」功能（預設：42）。 | INT | 是 | 0 到 2147483647 |

### 模型特定輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 模型在繪製前投入多少推理。較高等級可提升細節，但會消耗更多 token。僅由 `"arrow-2"` 與 `"arrow-2-telos"` 模型使用（預設：`"high"`）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | 隨機性控制。較高的值會增加隨機性。`"arrow-2-telos"` 模型不使用。進階參數（預設：1.0）。 | FLOAT | 是 | 0.0 到 2.0（步長 0.1） |
| `top_p` | 核取樣（nucleus sampling）參數。`"arrow-2-telos"` 模型不使用。進階參數（預設：1.0）。 | FLOAT | 是 | 0.05 到 1.0（步長 0.05） |
| `presence_penalty` | Token 存在懲罰。`"arrow-2-telos"` 模型不使用。進階參數（預設：0.0）。 | FLOAT | 是 | -2.0 到 2.0（步長 0.1） |

**注意：** `reference_images` 的數量上限為 14，適用於 `"arrow-2"`、`"arrow-2-telos"` 與 `"arrow-1.1-max"`；而 `"arrow-1.1"` 與 `"arrow-preview"` 則為 4。將 `width` 或 `height` 保留為 0，可讓模型選擇畫布尺寸。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `SVG` | 生成的 SVG 輸出。 | SVG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `809d2e5bd62386723e36b7649af2f8dda40b437dc39bac9236529db5b52d32e9`
