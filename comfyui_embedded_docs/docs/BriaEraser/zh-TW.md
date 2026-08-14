# BriaEraser

Bria Eraser 使用 Bria API 從影像中移除物體或區域。您提供一張影像和一個遮罩，其中勾勒出要移除的區域；節點會將兩者上傳至 Bria、執行擦除工作、等待其完成，並傳回已編輯且遮罩區域已被擦除的影像。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 包含要移除之物體或區域的輸入影像。 | IMAGE | 是 | - |
| `mask` | 白色區域會被擦除，黑色區域會被保留。遮罩在傳送前會先二值化，因此部分塗繪的區域會被視為白色。必須與影像具有相同的外觀比例。 | MASK | 是 | - |
| `mask_type` | 選擇遮罩的建立方式。「manual」適用於手繪或筆刷遮罩；「automatic」適用於由分割模型（如 SAM）產生的遮罩。 | STRING | 是 | "manual"<br>"automatic" |
| `moderation` | 審核設定。設定為 "true" 以對輸入和/或輸出影像啟用內容審核。 | STRING | 是 | "false"<br>"true" |

注意：當 `moderation` 設為 "true" 時，會提供兩個額外的布林設定：

- `visual_input_moderation` — 對輸入影像套用視覺內容審核（預設：false）
- `visual_output_moderation` — 對輸出影像套用視覺內容審核（預設：false）

遮罩必須與影像的外觀比例相符，否則請求會失敗。遮罩在傳送至 API 前會先轉換為二值（黑白）遮罩，因此部分塗繪的區域會被視為白色並遭到擦除。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 已編輯的影像，其中遮罩的物體或區域已移除。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/zh-TW.md)

---
**Source fingerprint (SHA-256):** `557272ecb0e6487796184ce88217ff318de4a5728a82e903aeb3fa3a0d24a664`
