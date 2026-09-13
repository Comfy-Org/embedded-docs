# Tripo: 骨架模型

此節點會取得現有的 Tripo 3D 模型，並建立其骨架綁定版本，也就是讓模型取得骨架，以便製作動畫。您需提供要進行骨架綁定之模型的任務 ID、選擇綁定版本、骨架類型、骨骼命名風格與輸出檔案格式，節點會將工作傳送至 Tripo，等待完成後回傳下載的結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `原始模型任務ID` | 要進行骨架綁定之原始 3D 模型的任務 ID。這通常是先前 Tripo 模型生成節點所產生的 ID。 | MODEL_TASK_ID | 是 | - |
| `model_version` | 要使用的綁定模型版本。v1.0：僅限人形（雙足）角色，內含 90 多種動畫預設。v2.5：非人形生物（四足、六足、八足、鳥類、蛇形、水生）。預設：`v1.0-20240301`。 | COMBO | 否 | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | 骨架類型。"auto" 會先執行 Tripo 的免費綁定檢查，並使用建議的類型。預設："auto"。 | COMBO | 否 | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | 骨骼命名：Tripo 原生或 Mixamo 相容。Tripo 無法將其動畫預設重新定位到使用 mixamo 規格製作的 v1.0 綁定上；如需使用 Tripo: Retarget rigged model，請選擇 tripo。預設："tripo"。 | COMBO | 否 | "tripo"<br>"mixamo" |
| `out_format` | 輸出檔案格式；結果會出現在對應的輸出上。預設："glb"。 | COMBO | 否 | "glb"<br>"fbx" |

**注意：** v1.0 模型版本（`v1.0-20240301`）僅支援雙足骨架。若此版本搭配非雙足的 `rig_type`，節點會引發錯誤，並指示您改用 `v2.5-20260210`。

**注意：** 當 `rig_type` 為 "auto" 時，Tripo 會先檢查模型是否能進行綁定，並挑選建議的骨架類型。若 Tripo 回報模型無法綁定，節點會失敗並產生錯誤。

**注意：** 節點預期 Tripo 回傳 GLB 或 FBX 檔案。若 Tripo 回傳任何其他檔案類型，節點會引發錯誤。

**注意：** 只有與 `out_format` 相符的輸出會被填入：當 `out_format` 為 "glb" 時為 `GLB`，當 `out_format` 為 "fbx" 時為 `FBX`。另一個 3D 輸出會是空的。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 產生的綁定模型檔案名稱（任務 ID 加上格式副檔名）。僅為向後相容而保留。 | STRING |
| `rig task_id` | 用於追蹤綁定生成流程的任務 ID。 | RIG_TASK_ID |
| `GLB` | 綁定後的模型，格式為 GLB 3D 檔案。當 `out_format` 為 "glb" 時填入。 | FILE3DGLB |
| `FBX` | 綁定後的模型，格式為 FBX 3D 檔案。當 `out_format` 為 "fbx" 時填入。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b9c1b6d27b6278bcee4fc22e11c11e65cd22ea92cab3fc6c74f84d3deb2024d6`
