> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/zh-TW.md)

`CLIPSave` 節點專為以 SafeTensors 格式儲存 CLIP 文字編碼器模型而設計。此節點是先進模型合併工作流程的一部分，通常與 `CLIPMergeSimple` 和 `CLIPMergeAdd` 等節點結合使用。儲存的檔案使用 SafeTensors 格式以確保安全性和相容性。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 預設值 | 描述 |
|-----------|-----------|----------|---------------|-------------|
| clip | CLIP | 是 | - | 要儲存的 CLIP 模型 |
| filename_prefix | STRING | 是 | "clip/ComfyUI" | 儲存檔案的前綴路徑 |
| prompt | PROMPT | 隱藏 | - | 工作流程提示資訊（用於元數據） |
| extra_pnginfo | EXTRA_PNGINFO | 隱藏 | - | 額外的 PNG 資訊（用於元數據） |

## 輸出結果

此節點沒有定義輸出類型。它會將處理後的檔案儲存到 `ComfyUI/output/` 資料夾中。

### 多檔案儲存策略

該節點根據 CLIP 模型類型儲存不同組件：

| 前綴類型 | 檔案後綴 | 描述 |
|------------|-------------|-------------|
| `clip_l.` | `_clip_l` | CLIP-L 文字編碼器 |
| `clip_g.` | `_clip_g` | CLIP-G 文字編碼器 |
| 空前綴 | 無後綴 | 其他 CLIP 組件 |

## 使用說明

1. **檔案位置**：所有檔案均儲存在 `ComfyUI/output/` 目錄中
2. **檔案格式**：模型以 SafeTensors 格式儲存以確保安全
3. **元數據**：包含工作流程資訊和 PNG 元數據（如果可用）
4. **命名慣例**：使用指定的前綴加上根據模型類型的適當後綴