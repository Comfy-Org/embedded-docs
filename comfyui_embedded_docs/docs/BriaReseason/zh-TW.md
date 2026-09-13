# BriaReseason

此節點使用 Bria 將影像移至另一個季節。整個場景會重新渲染，因此景色可能不僅限於季節本身的變化。Bria 會以約 1 百萬像素重新渲染整個畫面，因此結果不會與輸入像素對齊。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要移至另一個季節的影像。影像傳送前會移除任何 alpha 通道。 | IMAGE | 是 | - |
| `season` | 要套用的季節。 | COMBO | 是 | `"spring"`<br>`"summer"`<br>`"autumn"`<br>`"winter"` |
| `moderation` | 內容審核設定。選擇是否為此請求設定內容審核選項。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |

### 內容審核輸入

當 `moderation` 設為 `"true"` 時，會顯示這些選項。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | 啟用輸入影像的內容審核（預設值：false）。 | BOOLEAN | 否 | true<br>false |
| `visual_output_moderation` | 啟用生成輸出影像的內容審核（預設值：false）。 | BOOLEAN | 否 | true<br>false |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 在所選季節中重新渲染的影像。 | IMAGE |
| `structured_prompt` | 編輯後影像的結構化描述，用於使用 Bria FIBO Image Edit 進行後續編輯。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReseason/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3bb9ee1c00c91759cc6f972e2ba8708ae73a186f4b66bf6669937e561efad0a4`
