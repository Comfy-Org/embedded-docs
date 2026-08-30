# 載入 SAM3D 身體模型

此節點從偵測資料夾中儲存的檢查點檔案載入 SAM3D Body 模型，並為 3D 人體偵測用途做好準備。節點會載入模型權重、偵測並套用量化設定（如果存在），並將模型包裝以進行自動記憶體管理。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_file` | 要載入的 SAM3D Body 檢查點檔案。檔案必須放置在偵測資料夾中。 | COMBO | 是 | 偵測資料夾中所有可用的模型檔案 |

注意：模型檔案必須位於偵測資料夾中。如果檢查點的狀態字典鍵與 SAM3D Body 模型結構不符，載入將失敗並顯示錯誤。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `sam3d_body_model` | 已載入的 SAM3D Body 模型，已包裝以在 GPU 與 CPU 之間進行自動記憶體管理。手部偵測權重已移除，因此該模型專門用於人體偵測。 | SAM3D_BODY_MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Loader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c66a1639b5f19dafcfb1466d68908969a4d33ab0d01c30e8b31d1f1ce41fd782`
