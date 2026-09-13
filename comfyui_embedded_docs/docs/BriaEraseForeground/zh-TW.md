# BriaEraseForeground

此節點使用 Bria 移除影像的前景，並在原本位置生成新的背景。Bria 識別為前景的所有內容都會被移除，不僅限於人物，未經修改的像素則會保留。結果會以接近 1 百萬像素的標準尺寸重新渲染。

這是付費 API 節點，執行於 Bria 的服務，因此每次執行都會使用你的 Comfy API 憑證。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 要移除前景並以生成背景取代的影像。僅會傳送色彩通道；任何 alpha 通道都會在上傳前被捨棄。 | IMAGE | 是 | - |
| `內容審核` | 內容審核設定。選擇 `"false"` 會在不帶內容審核旗標的情況下傳送影像，選擇 `"true"` 則會顯示下方的內容審核切換選項。預設值：`"false"`。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |

### `"false"` 輸入

無額外輸入。請求會在不帶內容審核旗標的情況下傳送。

### `"true"` 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | 對輸入影像啟用內容審核。預設值：false。 | BOOLEAN | 是 | true<br>false |
| `visual_output_moderation` | 對生成的輸出影像啟用內容審核。預設值：false。 | BOOLEAN | 是 | true<br>false |

### 備註

- 輸出會以接近 1 百萬像素的標準尺寸重新渲染，因此傳回的影像尺寸可能與輸入不同。
- 此節點是付費 API 節點；每次執行費用約為 0.0572 USD。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 已擦除前景並在原本位置換上新生成背景的輸入影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseForeground/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4d8c3c5eed97c648b1191ec41931c97caa17e98a8edd1c054ed63e80cc671b05`
