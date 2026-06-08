# Tripo 文字轉模型節點

根據文字提示使用 Tripo API 同步生成 3D 模型。此節點接收文字描述，並建立具有可選紋理和材質屬性的 3D 模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | 用於生成 3D 模型的文字描述（多行輸入） | STRING | 是 | - |
| `負向提示詞` | 描述生成模型中應避免內容的文字（多行輸入） | STRING | 否 | - |
| `模型版本` | 用於生成的 Tripo 模型版本（預設：v2.5-20250123） | COMBO | 否 | 提供多個選項 |
| `風格` | 生成模型的樣式設定（預設："None"） | COMBO | 否 | 提供多個選項 |
| `紋理` | 是否為模型生成紋理（預設：True） | BOOLEAN | 否 | - |
| `PBR材質` | 是否生成 PBR（基於物理的渲染）材質（預設：True） | BOOLEAN | 否 | - |
| `圖片種子` | 影像生成的隨機種子（預設：42） | INT | 否 | - |
| `模型種子` | 模型生成的隨機種子（預設：42） | INT | 否 | - |
| `紋理種子` | 紋理生成的隨機種子（預設：42） | INT | 否 | - |
| `紋理品質` | 紋理生成的品質等級（預設："standard"） | COMBO | 否 | "standard"<br>"detailed" |
| `面數限制` | 生成模型中的最大面數，-1 表示無限制（預設：-1） | INT | 否 | -1 至 2000000 |
| `四邊形` | 是否生成四邊形幾何體而非三角形（預設：False） | BOOLEAN | 否 | - |
| `幾何品質` | 幾何體生成的品質等級（預設："standard"） | COMBO | 否 | "standard"<br>"detailed" |

**注意：** `prompt` 參數為必要參數，不可為空。若未提供提示詞，此節點將會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型任務 ID` | 生成的 3D 模型檔案（僅為向後相容性保留） | STRING |
| `GLB` | 模型生成過程的唯一任務識別碼 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f73316e0a50adfb6fe22ca6a20a2a5b36a6597abf0f4ddae9183d9e4a45cb46d`
