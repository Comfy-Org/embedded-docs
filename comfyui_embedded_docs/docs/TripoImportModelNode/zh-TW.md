# Tripo：匯入模型

此節點將外部 3D 模型匯入 Tripo，以便其他 Tripo 後處理節點（如 Texture、Rig 和 Convert）可以使用它。節點會上傳模型並回傳一個識別所匯入模型的任務 ID。建議使用 GLB 格式，因為只有嵌入檔案中的紋理才能被保留，且對匯入模型進行紋理處理需要紋理提示詞。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 要匯入的 3D 模型（GLB / FBX / OBJ / STL，最大 150 MB）。OBJ 和 STL 檔案不包含嵌入的紋理。 | FILE3D | 是 | GLB<br>FBX<br>OBJ<br>STL<br>任何 3D 格式 |

**注意：** 僅支援 GLB、FBX、OBJ 和 STL 格式。不支援 GLTF (.gltf) 格式，因為它會引用外部檔案；請改用單一檔案 GLB。模型檔案必須為 150 MB 或更小。建議使用 GLB，因為紋理僅在嵌入檔案時才能在匯入後保留。OBJ 和 STL 檔案不攜帶嵌入紋理。對匯入模型進行紋理處理需要紋理提示詞。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model task_id` | 一個任務 ID，用於識別已匯入的模型，以便與 Tripo 後處理節點搭配使用 | MODEL_TASK_ID |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4fa13a108804f2a52190a85b5b5d58ff18190e9d182b556abada444788012fab`
