# WeVisOne-VL Detect

WeVisOne-VL Detect 會根據文字提示在影像中尋找物件，並依所選任務傳回框、Alpha 遮罩、點或模型自身的答案。它涵蓋開放詞彙偵測與分割、指稱表達式、指向、計數與 OCR 定位，且會對批次中的每張影像執行一個提示。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 載入檢查點的 WeVisOne-VL 文字編碼器。 | CLIP | 是 | - |
| `image` | 要搜尋的影像或一批影像。 | IMAGE | 是 | - |
| `task` | 節點應傳回的內容。Segmentation 會傳回框加上 Alpha 遮罩；detection、referring、ocr 與 ocr_grounding 會傳回框；point 與 count_point 會傳回點；count_box 會以框進行計數；visual_prompt 會尋找與 `bboxes` 中參考框相似的物件；freeform 會原樣送出查詢，且只傳回文字（預設："segmentation"）。 | COMBO | 是 | `"segmentation"`<br>`"detection"`<br>`"referring"`<br>`"point"`<br>`"count_box"`<br>`"count_point"`<br>`"ocr"`<br>`"ocr_grounding"`<br>`"visual_prompt"`<br>`"freeform"` |
| `query` | 要以自然語言尋找的內容（例如「紅色馬克杯」）。`detection` 與 `point` 會每行讀取一個標籤，`count_box` 與 `count_point` 會計算你指定的主體，`ocr_grounding` 會尋找這段確切文字，`visual_prompt` 則改用 `bboxes`，而 `freeform` 會將其作為完整提示送出。`ocr` 會忽略它。 | STRING | 是 | - |
| `bboxes` | `visual_prompt` 用作要尋找物件範例的參考框。 | BOUNDING_BOX | 否 | - |
| `individual_masks` | 每個框傳回一個遮罩，依 `bboxes` 順序並逐幀傳回，而非每幀傳回一個合併遮罩（預設：false）。 | BOOLEAN | 否 | true<br>false |
| `max_length` | 模型可為其答案產生的最大 token 數（預設：4096）。 | INT | 是 | 1 至 32768 |

**注意：** 只有在模型以物件參考作答時，遮罩才會被填入；這正是 segmentation 任務所要求的。其他任務會傳回框、點或文字，並附帶空遮罩。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `masks` | 符合物件之 Alpha 遮罩，預設每幀一個，或在使用 `individual_masks` 時每個框一個。 | MASK |
| `bboxes` | 在每張影像中找到的框，儲存為 `x`、`y`、`width`、`height` 與 `label`。 | BOUNDING_BOX |
| `points` | 以像素為單位、格式為 `[{"x", "y", "label", "frame"}]` 的 JSON 點，由 `point` 與 `count_point` 任務填入。 | STRING |
| `text` | 模型的原始答案，每張影像一行。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeVisOneDetect/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0cef1dfcab790e145ace51401a84cdc10282835330cda5a3770f5b20a32d475e`
