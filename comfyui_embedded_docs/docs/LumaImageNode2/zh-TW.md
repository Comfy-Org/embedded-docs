# Luma UNI-1 圖像

此節點使用 Luma UNI-1 模型，根據文字描述生成影像。它接收文字提示詞以及可選設定（如長寬比與樣式），然後將請求傳送至 Luma API 以建立影像。共有兩種模型變體可供使用：`uni-1` 與 `uni-1-max`。

## 輸入

### 通用輸入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `模型` | 用於生成的模型。選擇模型會顯示該模型的額外設定。 | DYNAMIC_COMBO | 是 | `"uni-1"`<br>`"uni-1-max"` |
| `提示` | 所需影像的文字描述。1 至 6000 個字元。(預設值："") | STRING | 是 | 1 至 6000 characters |
| `種子` | 種子（seed）控制節點是否應重新執行；無論種子為何，結果皆為非確定性。(預設值：0) | INT | 是 | 0 至 2147483647 |

### uni-1 與 uni-1-max 輸入

由 `uni-1` 與 `uni-1-max` 模型選項共用。選取任一模型時，即會顯示這些設定。

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | 輸出影像的長寬比。`"auto"` 會讓模型根據提示詞自動選擇。(預設值：`"auto"`) | COMBO | 是 | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | 樣式預設。`"auto"` 會根據提示詞自動選擇；`"manga"` 套用漫畫／動畫風格，且需要直式長寬比（2:3、9:16、1:2、1:3）。(預設值：`"auto"`) | COMBO | 是 | `"auto"`<br>`"manga"` |
| `web_search` | 在生成前搜尋網路以取得視覺參考。(預設值：False) | BOOLEAN | 是 | True / False |

### 參考輸入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `image_ref` | 可擴展插槽：可連接 1 至 9 個項目（例如 `image_1` 到 `image_9`）。最多 9 張參考影像，用於提供風格／內容引導。 | IMAGE | 否 | Up to 9 images |

**注意：** 若 `style` 設定為 `"manga"`，則 `aspect_ratio` 必須為 `"auto"` 或其中一種直式長寬比：`"2:3"`、`"9:16"`、`"1:2"`、`"1:3"`。若將 `"manga"` 樣式搭配任何其他長寬比使用，將會導致錯誤。`uni-1` 與 `uni-1-max` 的參考影像上限皆為 9 張。

## 輸出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `image` | 生成的影像，以張量表示。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `27254fe4627fd340426a68f651cab4513ffb6668cafc0accd17f2c442f7d3125`
