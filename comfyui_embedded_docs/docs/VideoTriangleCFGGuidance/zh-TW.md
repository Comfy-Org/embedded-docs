# 影片三角 CFG 引導

VideoTriangleCFGGuidance 節點將三角無分類器引導（CFG）縮放模式應用於影片模型。它使用一個在 `min_cfg` 與模型原始條件縮放之間振盪的三角波，隨著時間改變條件縮放。這會產生動態引導模式，有助於提升影片生成的一致性和品質。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用三角 CFG 引導的影片模型 | MODEL | 是 | - |
| `min_cfg` | 三角模式的最小 CFG 縮放值（預設值：1.0）。此參數顯示在節點介面的進階區段中。 | FLOAT | 是 | 0.0 - 100.0 (step: 0.5, round: 0.01) |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用三角 CFG 引導的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
