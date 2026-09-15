# 套用 ControlNet 修補（AliMama）

ControlNetInpaintingAliMamaApply 節點會透過將正向與負向條件與控制影像及遮罩結合，為影像修補任務套用 ControlNet 條件。它會處理輸入影像與遮罩，建立修改後的條件來引導生成過程，讓你可以控制影像中哪些區域要被修補。此節點支援強度調整與時間控制，以便在生成過程的不同階段微調 ControlNet 的影響力。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 引導生成朝向往目標內容的正向條件 | CONDITIONING | 是 | - |
| `負向` | 引導生成遠離不想要內容的負向條件 | CONDITIONING | 是 | - |
| `control_net` | 對生成提供額外控制的 ControlNet 模型 | CONTROL_NET | 是 | - |
| `vae` | 用於編碼與解碼影像的 VAE（變分自編碼器） | VAE | 是 | - |
| `影像` | 作為 ControlNet 控制指引的輸入影像 | IMAGE | 是 | - |
| `遮罩` | 定義影像中哪些區域應該進行修補的遮罩 | MASK | 是 | - |
| `強度` | ControlNet 效果的強度（預設：1.0，步長：0.01） | FLOAT | 是 | 0.0 至 10.0 |
| `起始百分比` | 進階參數。ControlNet 影響在生成過程中開始的時間點（以百分比表示）（預設：0.0，步長：0.001） | FLOAT | 是 | 0.0 至 1.0 |
| `結束百分比` | 進階參數。ControlNet 影響在生成過程中結束的時間點（以百分比表示）（預設：1.0，步長：0.001） | FLOAT | 是 | 0.0 至 1.0 |

**注意：** 當 ControlNet 啟用 `concat_mask` 時，遮罩會在處理前被反轉並套用到影像，且反轉後的遮罩會包含在傳送給 ControlNet 的額外串接資料中。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 已套用 ControlNet 以進行修補的修改後正向條件 | CONDITIONING |
| `negative` | 已套用 ControlNet 以進行修補的修改後負向條件 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
