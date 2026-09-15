# BriaEraseByText

此節點使用 Bria 從影像中移除以純文字描述的物件。Bria 會以約 1 百萬像素重新渲染整個畫面，因此結果不會與輸入像素對齊。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 應從中移除指定物件的影像。 | IMAGE | 是 | - |
| `物件名稱` | 要移除的物件名稱，例如 'the lamp'。可以一次指定多個物件，例如 'the phone and the pencils'。即使指定的物件不在圖片中，仍會回傳並計費一張重新渲染的影像。長度必須至少為 1 個字元（預設：空）。 | STRING | 是 | - |
| `內容審核` | 審核設定。選擇是否顯示選用的審核控制項。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |

### 審核輸入

當 `moderation` 設為 `"true"` 時，會顯示這些參數。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | 啟用輸入影像的內容審核（預設：false）。 | BOOLEAN | 否 | true<br>false |
| `visual_output_moderation` | 啟用生成輸出影像的內容審核（預設：false）。 | BOOLEAN | 否 | true<br>false |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-----------|-----------|
| `IMAGE` | 已重新渲染並移除指定物件的影像。 | IMAGE |
| `structured_prompt` | 編輯後影像的結構化描述，可供 Bria FIBO Image Edit 進行後續編輯。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseByText/zh-TW.md)

---
**Source fingerprint (SHA-256):** `51ac362bea731251c99905172c41cdebb5165e7564c508f13aa43cf9072964ef`
