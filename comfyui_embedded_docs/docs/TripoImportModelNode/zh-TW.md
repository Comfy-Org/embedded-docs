# Tripo：匯入模型

此節點將外部 3D 模型檔案匯入 Tripo 系統，以便您可將其與 Tripo 的後處理節點（如紋理、骨架綁定和格式轉換）搭配使用。它會上傳您的模型並回傳一個任務 ID，其他 Tripo 節點可使用此 ID 來引用已匯入的模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 要匯入的 3D 模型（GLB / FBX / OBJ / STL，最大 150 MB）。OBJ 和 STL 檔案不包含嵌入的紋理。 | FILE3D | 是 | GLB<br>FBX<br>OBJ<br>STL<br>任何 3D 格式 |

**注意：** 建議使用 GLB 格式，因為僅當紋理直接嵌入檔案中時才能保留。OBJ 和 STL 檔案不支援嵌入紋理。不支援 GLTF (.gltf) 格式，因為它會引用外部檔案；請改用單一檔案 GLB。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model task_id` | 一個任務 ID，用於識別已匯入的模型，以便與 Tripo 後處理節點搭配使用 | MODEL_TASK_ID |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4fa13a108804f2a52190a85b5b5d58ff18190e9d182b556abada444788012fab`
