# BriaReplaceImageBackground

此節點會將影像的背景替換為由 Bria 產生的新背景。新背景可以用提示詞描述，或由參考影像引導。主體的像素會保留，並在其周圍產生背景。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 將要替換背景的輸入影像。 | IMAGE | 是 | |
| `背景` | 使用提示詞描述新背景，或使用參考影像引導。 | DYNAMIC_COMBO | 是 | `"prompt"`<br>`"reference images"` |
| `original_quality` | 傳回輸入的確切像素尺寸，而不是將結果縮放為約 1 百萬像素。大型輸入接著會傳回大型影像。（預設：false） | BOOLEAN | 否 | `true`<br>`false` |
| `種子` | 相同的 `seed` 通常會傳回相同背景；自動提示詞精煉仍可能使其有所不同。（預設：42） | INT | 否 | 0 至 2147483647 |
| `內容審核` | 審核設定。（預設：`"false"`） | DYNAMIC_COMBO | 否 | `"false"`<br>`"true"` |

### 提示輸入

當 `background` 設為 `"prompt"` 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 新背景的描述。諸如 #FF5733 的十六進位色碼會產生純色背景。長度必須至少為 1 個字元。 | STRING | 是 | |
| `mode` | `high_control` 最緊密遵循提示詞，`base` 是平衡的預設選項，而 `fast` 以細節換取速度。 | COMBO | 是 | `"high_control"`<br>`"base"`<br>`"fast"` |
| `refine_prompt` | 重寫提示詞以獲得更好的結果，這也會翻譯非英文提示詞。將其關閉可完全依原樣傳送提示詞。（預設：true） | BOOLEAN | 否 | `true`<br>`false` |

### 參考影像輸入

當 `background` 設為 `"reference images"` 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `ref_images` | 可擴充插槽：連接 1 到 10 張引導新背景的影像；它們不需要具有相同尺寸。每個參考都會改變結果，因此少量一致的參考勝過大量互相衝突的參考。批次輸入中的每張影像各計一次。 | IMAGE | 是 | 1 至 10 images |
| `enhance_ref_images` | 對參考影像進行額外處理以獲得更好的結果。（預設：true） | BOOLEAN | 否 | `true`<br>`false` |

### 審核輸入

當 `moderation` 設為 `"true"` 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | 啟用提示內容的審核。（預設：false） | BOOLEAN | 否 | `true`<br>`false` |
| `visual_input_moderation` | 啟用視覺輸入的審核。（預設：false） | BOOLEAN | 否 | `true`<br>`false` |
| `visual_output_moderation` | 啟用視覺輸出的審核。（預設：false） | BOOLEAN | 否 | `true`<br>`false` |

**注意：** `ref_images` 輸入最多接受 10 張影像；提供超過 10 張會傳回錯誤。`prompt` 欄位必須包含至少 1 個字元。當 `original_quality` 為 false 時，輸入影像會在處理前縮小至約 1 百萬像素。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-----------|-----------|
| `image` | 具有新背景的影像。 | IMAGE |
| `refined_prompt` | Bria 產生時所依據的提示詞；在參考影像路徑中為空。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceImageBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `62c29d61983c9656d2ea2954518404c62d76961c3deba0e10d63e787d0b0b106`
