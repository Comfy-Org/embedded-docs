# BriaReplaceObject

使用 Bria 的文字導引影像編輯，將影像中的物件替換為純文字所描述的另一個物件。Bria 會以約 1 百萬像素重新渲染整個畫面，因此結果不會與輸入影像像素對齊。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 包含要替換物件的影像。影像上傳前會移除 alpha 通道。 | IMAGE | 是 | - |
| `instruction` | 要將什麼替換成什麼，例如「Replace the red apple with a green pear」。長度必須至少為 1 個字元。 | STRING | 是 | 多行文字；預設：""（空） |
| `seed` | Bria 在此不使用 `seed`，且每次呼叫都會重新構思編輯，因此重複執行可能產生不同結果。此值永遠不會被傳送：它只會改變此節點的快取鍵，因此一個在其他方面相同的圖形會再次執行編輯，而不是傳回快取結果。 | INT | 是 | 0 至 2147483647，步長 1；預設：42；啟用產生後控制 |

### 審核輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `moderation` | 審核設定。選取 "true" 會顯示下方的審核子選項；否則不會顯示。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |
| `visual_input_moderation` | 啟用輸入影像的審核。僅當 `moderation` 設為 "true" 時可用。 | BOOLEAN | 否 | `true` / `false`；預設：false |
| `visual_output_moderation` | 啟用所產生輸出影像的審核。僅當 `moderation` 設為 "true" 時可用。 | BOOLEAN | 否 | `true` / `false`；預設：false |

注意：`instruction` 會在傳送請求前進行驗證，且必須至少包含 1 個字元。`seed` 值不會傳送給 Bria；它只影響此節點要重新執行編輯，或傳回快取結果。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 已套用所描述物件替換的編輯後影像。 | IMAGE |
| `structured_prompt` | 編輯後影像的結構化描述，可用於使用 Bria FIBO Image Edit 進行後續編輯。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceObject/zh-TW.md)

---
**Source fingerprint (SHA-256):** `75a45d5c0d6cde96a1e961db627edc1a59c07cc37b974402745cefc62864cc26`
