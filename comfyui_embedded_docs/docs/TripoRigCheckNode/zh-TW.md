# Tripo：骨架綁定檢查

此節點會將已完成的 Tripo 3D 模型任務 ID 傳送至 Tripo API，並檢查該模型是否可以進行骨骼綁定。它會等待檢查完成，然後傳回是/否結果，以及 Tripo 為該模型建議的骨架類型。

<Note>
Tripo 僅在其伺服器上保留任務紀錄 7 天（自 2026年12月1日起生效）。超過此期限的任務 ID 將無法再解析，因此在該期限之後重新執行已儲存的工作流程時，會在此節點失敗。若要繼續，請重新執行先前的 Tripo 節點以建立新的任務 ID，或使用 **Tripo：匯入模型** 重新匯入您已下載的模型。
</Note>

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 要分析的模型之 Tripo 任務 ID。它會識別先前透過 Tripo 任務生成、匯入或以其他方式建立的模型。 | MODEL_TASK_ID | 是 | N/A |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `riggable` | 模型是否可進行骨骼綁定。 | BOOLEAN |
| `rig_type` | 建議的骨架：biped、quadruped、hexapod、octopod、avian、serpentine 或 aquatic；當模型不可進行骨骼綁定時為 'others'。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigCheckNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3aa0bc194e887804b92ca1f9f2b12997c73e111fb282c5de96e55f664c21545e`
