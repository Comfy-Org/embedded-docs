# Bria Guided Remove Background

此節點使用 Bria 從圖像中移除背景，保留 `prompt` 所描述的內容。原始像素會以完整解析度返回，並附加新的 alpha 通道，而非重新算繪，因此能保留細節與邊緣。若提示詞與任何內容都不相符，則會返回完全透明的圖像。若只需單純去背、不需任何引導，使用 Bria Remove Image Background 的成本更低。

## 輸入

`moderation` 選擇器設為 `"true"` 時，會顯示額外的審核選項。

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要去背的圖像。 | IMAGE | 是 | - |
| `prompt` | 要保留的內容，並可選擇性指定要移除或縮限的範圍，例如 'the person with the mat and the plant'、'the woman at her desk without the lamp' 或 'only the chair'。不得為空。若沒有任何內容符合提示詞，結果將完全透明。預設值：`""`（空字串）。 | STRING | 是 | 1 個字元以上 |
| `moderation` | 審核設定。設為 `"true"` 時，下方的視覺審核旗標將可使用。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |

### Moderation "true" 輸入

這些參數僅在 `moderation` 設為 `"true"` 時出現。`"false"` 選項不會新增任何輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | 對輸入圖像啟用內容審核。預設值：`False`。 | BOOLEAN | 否 | True / False |
| `visual_output_moderation` | 對生成的圖像啟用內容審核。預設值：`False`。 | BOOLEAN | 否 | True / False |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 去背後的圖像：原始像素加上新的 alpha 通道。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGuidedRemoveBackground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `210fa214a0d0d8ad19a15ea4f6baa9f13499bc4c3767e270f19f2a08d67e25ac`
