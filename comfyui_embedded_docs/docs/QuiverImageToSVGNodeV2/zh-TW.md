# Quiver Image to SVG

使用 Quiver AI 將點陣影像向量化為可縮放向量圖形（SVG）。影像會傳送至 Quiver AI 的 API，並傳回向量化結果。

選擇 `model` 會顯示下列模型專用參數。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於 SVG 向量化的模型。 | DYNAMIC_COMBO | 是 | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `image` | 要向量化的輸入影像。 | IMAGE | 是 | N/A |
| `auto_crop` | 自動裁切至主要主體。進階參數（預設：False）。 | BOOLEAN | 是 | `True`<br>`False` |
| `target_size` | 在向量化前對輸入影像套用的正方形縮放，單位為像素。0 會保留來源尺寸，這比強制縮放更能乾淨地向量化；任何其他低於 128 的值都會被限制為 128。這不會設定輸出畫布；請使用 `width` 和 `height` 來設定。進階參數（預設：0）。 | INT | 是 | 0 至 4096 |
| `width` | 輸出 SVG 畫布（viewBox）的寬度，單位為使用者單位。同時設定 `width` 和 `height` 可控制輸出尺寸與長寬比；將任一項保留為 0 會讓模型自行選擇，這通常會產生正方形畫布。進階參數（預設：0）。 | INT | 是 | 0 至 8192 |
| `height` | 輸出 SVG 畫布（viewBox）的高度，單位為使用者單位。同時設定 `width` 和 `height` 可控制輸出尺寸與長寬比；將任一項保留為 0 會讓模型自行選擇，這通常會產生正方形畫布。進階參數（預設：0）。 | INT | 是 | 0 至 8192 |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子值為何，實際結果都是不確定的。此參數具有「生成後控制」功能（預設：42）。 | INT | 是 | 0 至 2147483647 |

### 模型專用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 模型在繪製前投入的推理量。較高等級可提升細節，但會消耗更多 token。僅供 `"arrow-2"` 和 `"arrow-2-telos"` 模型使用（預設：`"high"`）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | 隨機性控制。較高的值會增加隨機性。`"arrow-2-telos"` 模型不使用。進階參數（預設：1.0）。 | FLOAT | 是 | 0.0 至 2.0 （步進值：0.1） |
| `top_p` | 核取樣參數。`"arrow-2-telos"` 模型不使用。進階參數（預設：1.0）。 | FLOAT | 是 | 0.05 至 1.0 （步進值：0.05） |
| `presence_penalty` | token 存在懲罰。`"arrow-2-telos"` 模型不使用。進階參數（預設：0.0）。 | FLOAT | 是 | -2.0 至 2.0 （步進值：0.1） |

**注意：** `target_size` 會在向量化前套用，且不會變更輸出畫布。將 `width` 或 `height` 保留為 0，可讓模型選擇畫布尺寸。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `SVG` | 向量化後的 SVG 輸出。 | SVG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `186769b09bef2d2dbbfc26102f375ff80f8b324a24cd593da20afcea9cc2095b`
