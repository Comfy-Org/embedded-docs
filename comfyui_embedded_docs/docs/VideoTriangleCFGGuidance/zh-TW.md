# 影片三角 CFG 引導

VideoTriangleCFGGuidance 節點會對影片模型套用三角形的無分類器引導（CFG）縮放模式。它使用在 `min_cfg` 與模型原始條件縮放值之間振盪的三角波來改變條件縮放。這會產生動態的引導模式，有助於提升影片生成的一致性與品質。

## 輸入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | 要套用三角形 CFG 引導的影片模型。 | MODEL | 是 | - |
| `min_cfg` | 三角形模式的最小 CFG 縮放值。此參數顯示於節點介面的進階區段中（預設值：1.0）。 | FLOAT | 是 | 0.0 - 100.0 (step: 0.5, round: 0.01) |

## 輸出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | 已套用三角形 CFG 引導的修改後模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
