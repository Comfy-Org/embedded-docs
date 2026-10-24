# Krea 3 Image

Krea 3 Image 會使用 Krea 3 編輯影像，或在未連接任何影像時，根據文字提示生成新影像。最多可連接 8 張影像，並描述要變更什麼與要保留什麼，並在提示中以 `@Image1`、`@Image2` 等方式指稱它們。長寬比與解析度會設定輸出尺寸，而思考模式會以速度換取更詳細的規劃。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Krea 3 模型。選取模型後，會顯示其接受的參數。 | DYNAMIC_COMBO | 是 | `"Krea 3"` |

### Krea 3 輸入

當 `model` 設為 `Krea 3` 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.images` | 要編輯的影像，依連接順序編號。每張連接的影像都會計入 8 張的上限。留空則僅根據文字生成。 | IMAGE | 否 | 0 至 8 張影像 |
| `model.prompt` | 要變更什麼以及要保留什麼。請以 `@Image1`、`@Image2` 等方式，或以 image 1、image 2、... 來指稱影像。提示不能為空。 | STRING | 是 | - |
| `model.aspect_ratio` | 結果的長寬比。`"auto"` 會依第一張影像；若未連接影像，則依提示。(預設值：`"auto"`) | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"5:4"`<br>`"4:3"`<br>`"3:2"`<br>`"16:9"`<br>`"21:9"` |
| `model.resolution` | 輸出解析度。`"2K"` 比 `"1K"` 耗時更長，並產生更大的影像。(預設值：`"2K"`) | COMBO | 是 | `"1K"`<br>`"2K"` |
| `model.thinking_mode` | Krea 3 在規劃編輯時投入多少處理。建議使用 `"fast"`，而 `"high"` 會更詳細地規劃複雜編輯，但耗時更長。`"ultra"` 會產生多個候選並回傳最佳結果；它至少需要一張影像，一律輸出 2K，且不支援 `precise_edit`。(預設值：`"fast"`) | COMBO | 是 | `"fast"`<br>`"high"`<br>`"ultra"` |
| `model.precise_edit` | 保持編輯區域以外的所有內容不變。需要至少連接一張影像。(預設值：False) | BOOLEAN | 是 | false<br>true |
| `model.seed` | 請求的種子值（預設值：42）。Krea 會在生成前重寫提示，因此相同的種子不會重複產生相同的影像。 | INT | 是 | 0 至 2147483647 |

只有在至少連接三張影像時，才會接受像 `@Image3` 這樣的引用，否則節點會引發錯誤。參考影像會在傳送請求前上傳。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 生成或編輯後的影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea3ImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9e8d036f1ebca81b85e6ef42a015e7e2925bf467fa32e82180ee1b76dcc91c0b`
