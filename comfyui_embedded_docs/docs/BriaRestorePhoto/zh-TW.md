# BriaRestorePhoto

此節點透過 Bria API 修復老舊或損壞的照片。它會移除顆粒、刮痕與模糊，中和因年代造成的色偏，可能會裁掉相片卡紙裱框與攝影棚邊框，並重新繪製臉部。結果會以約 1 百萬像素重新渲染，因此不會與輸入像素對齊。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要修復的照片。上傳前會丟棄 Alpha 通道。 | IMAGE | 是 | - |
| `moderation` | 此請求的審核設定。選擇 `"true"` 會顯示兩個額外的布林切換開關；選擇 `"false"` 則不會傳送任何審核旗標。預設：`"false"`。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |

### 審核輸入

這些輸入只會在 `moderation` 設為 `"true"` 時出現。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | 對輸入影像啟用視覺內容審核。預設：false。 | BOOLEAN | 否 | true<br>false |
| `visual_output_moderation` | 對輸出影像啟用視覺內容審核。預設：false。 | BOOLEAN | 否 | true<br>false |

**注意：** 此節點會以約 1 百萬像素重新渲染整個畫面，因此結果不會與輸入像素對齊。若要放大影像，請改用 Bria Increase Resolution 節點，而非此節點。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | Bria 傳回的已修復照片。 | IMAGE |
| `structured_prompt` | 編輯後影像的結構化描述，可用於透過 Bria FIBO Image Edit 進行後續編輯。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRestorePhoto/zh-TW.md)

---
**Source fingerprint (SHA-256):** `387ec3e049464f185e27f79d160ade2a4170ab238853064c008892d84523fa68`
