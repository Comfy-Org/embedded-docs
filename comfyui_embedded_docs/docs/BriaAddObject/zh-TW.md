# BriaAddObject

此節點使用 Bria 將以純文字描述的物件插入影像中。Bria 會以約 1 百萬像素重新渲染整個畫面，因此結果不會與輸入像素對齊。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 要加入所描述物件的影像。在影像上傳前會捨棄 alpha 通道。 | IMAGE | 是 | - |
| `指示` | 要加入什麼以及加在哪裡，例如 'Place a red vase with flowers on the table'。不得為空。預設值：""（空字串）。 | STRING | 是 | - |
| `種子` | Bria 在此不接受 seed，且每次呼叫都會重新構思編輯，因此重複執行可能產生不同結果。此值永遠不會被送出：它只會改變此節點的快取鍵，讓其他方面完全相同的圖形再次執行編輯，而不是傳回快取的結果。預設值：42。 | INT | 是 | 0 至 2147483647 |
| `內容審核` | 內容審核設定。選擇 "true" 以顯示下方的內容審核旗標。 | DYNAMIC_COMBO | 是 | "false"<br>"true" |

### 啟用內容審核的輸入

當 `moderation` 設為 "true" 時可用。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | 啟用輸入影像的內容審核。預設值：False。 | BOOLEAN | 否 | True / False |
| `visual_output_moderation` | 啟用生成輸出影像的內容審核。預設值：False。 | BOOLEAN | 否 | True / False |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 已編輯並加入所描述物件的影像。 | IMAGE |
| `structured_prompt` | 已編輯影像的結構化描述，可用於使用 Bria FIBO Image Edit 進行後續編輯。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaAddObject/zh-TW.md)

---
**Source fingerprint (SHA-256):** `41c9a3e511763372d8dc8be9da4f70158e53d5156a88eb3c66f81149efdbd566`
