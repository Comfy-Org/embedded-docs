# MaskPreview

MaskPreview 節點會直接在 ComfyUI 介面中顯示遮罩資料的視覺預覽，而不會將其儲存到輸出目錄。這可讓您在流程中的任何時間點檢查確切的遮罩值。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `遮罩` | 要預覽的遮罩資料 | MASK | 是 | - |
| `filename_prefix` | 預覽檔案名稱的前綴（預設值："ComfyUI"） | STRING | 否 | - |
| `prompt` | 用於中繼資料的提示資訊（自動提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 用於中繼資料的額外 PNG 資訊（自動提供） | EXTRA_PNGINFO | 否 | - |

`prompt` 和 `extra_pnginfo` 輸入是隱藏的，會由 ComfyUI 系統自動提供；您不需要手動連接它們。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `mask` | 已預覽的遮罩資料，原樣返回以在流程中進一步使用 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
