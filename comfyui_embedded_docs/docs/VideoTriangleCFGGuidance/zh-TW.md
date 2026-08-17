# 影片三角 CFG 引導

VideoTriangleCFGGuidance 節點對影片模型套用三角形式的無分類器引導（CFG）縮放模式。它使用三角波函數隨時間調整條件引導強度，在最小 CFG 值與原始條件引導強度之間震盪，形成動態引導模式，有助於提升影片生成的一致性與品質。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用三角 CFG 引導的影片模型 | MODEL | 是 | - |
| `min_cfg` | 三角模式的最小 CFG 引導值（預設：1.0） | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用三角 CFG 引導的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
