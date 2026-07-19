# 跳過層引導 DiT

透過使用另一組帶有跳層的 CFG 負面條件，增強對詳細結構的引導。此通用版本的 SkipLayerGuidance 可用於所有 DiT 模型，其靈感來自於 Perturbed Attention Guidance。原始的實驗性實作是為 SD3 所建立。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要應用跳層引導的模型 | MODEL | 是 | - |
| `雙層` | 要跳過的雙區塊層號，以逗號分隔（預設："7, 8, 9"） | STRING | 是 | - |
| `單層` | 要跳過的單區塊層號，以逗號分隔（預設："7, 8, 9"） | STRING | 是 | - |
| `縮放` | 引導縮放因子（預設：3.0） | FLOAT | 是 | 0.0 - 10.0 |
| `起始百分比` | 開始應用引導的百分比（預設：0.01） | FLOAT | 是 | 0.0 - 1.0 |
| `結束百分比` | 結束應用引導的百分比（預設：0.15） | FLOAT | 是 | 0.0 - 1.0 |
| `重新縮放比例` | 重新縮放因子，用於調整輸出幅度（預設：0.0，表示不重新縮放） | FLOAT | 是 | 0.0 - 10.0 |

**注意：** 如果 `double_layers` 和 `single_layers` 皆為空（不包含任何層號），則此節點會傳回原始模型，不應用任何引導。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用跳層引導的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cf494fbeb33e7bc3b3f798e9e9b025623afad4ea6340ef628caa776c7d42ba12`
