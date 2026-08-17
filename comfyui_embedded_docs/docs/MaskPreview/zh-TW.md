# MaskPreview

MaskPreview 節點會直接在 ComfyUI 介面中顯示遮罩資料的視覺預覽，方便您在工作流程期間檢視遮罩。它會顯示預覽，但不會將預覽儲存到 ComfyUI 的輸出目錄，並將遮罩原封不動地傳遞為輸出。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mask` | 要預覽的遮罩資料 | MASK | 是 | - |
| `filename_prefix` | 輸出檔名的前綴（預設："ComfyUI"） | STRING | 否 | - |
| `prompt` | 用於中繼資料的提示資訊（自動提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 用於中繼資料的額外 PNG 資訊（自動提供） | EXTRA_PNGINFO | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mask` | 已預覽的遮罩資料，原封不動地傳遞 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
