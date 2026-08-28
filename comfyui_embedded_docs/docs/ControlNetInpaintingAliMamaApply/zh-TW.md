# 套用 ControlNet 修補（AliMama）

ControlNetInpaintingAliMamaApply 節點透過將正條件與負條件結合控制影像與遮罩，套用 ControlNet 條件控制來執行修補（inpainting）任務。它會處理輸入影像與遮罩，以建立修改後的條件控制，進而引導生成過程，讓您能精確控制影像中要修補的區域。此節點支援強度調整與時間控制，可在生成過程的不同階段微調 ControlNet 的影響力。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 引導生成朝向期望內容的正條件 | CONDITIONING | 是 | - |
| `負向` | 引導生成遠離不希望內容的負條件 | CONDITIONING | 是 | - |
| `control_net` | 提供額外生成控制的 ControlNet 模型 | CONTROL_NET | 是 | - |
| `vae` | 用於編碼與解碼影像的 VAE（變分自編碼器） | VAE | 是 | - |
| `影像` | 作為 ControlNet 控制引導的輸入影像 | IMAGE | 是 | - |
| `遮罩` | 定義影像中應進行修補區域的遮罩 | MASK | 是 | - |
| `強度` | ControlNet 效果的強度（預設值：1.0，步進：0.01） | FLOAT | 是 | 0.0 至 10.0 |
| `起始百分比` | 進階參數。ControlNet 影響在生成過程中開始作用的起點（以百分比表示）（預設值：0.0，步進：0.001） | FLOAT | 是 | 0.0 至 1.0 |
| `結束百分比` | 進階參數。ControlNet 影響在生成過程中停止作用的終點（以百分比表示）（預設值：1.0，步進：0.001） | FLOAT | 是 | 0.0 至 1.0 |

**注意事項：** 當 ControlNet 啟用 `concat_mask` 時，遮罩會在處理前先被反轉並套用到影像上，且反轉後的遮罩會被包含在傳送至 ControlNet 的額外串接資料中。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `正向` | 套用 ControlNet 後、用於修補的修改後正條件 | CONDITIONING |
| `負向` | 套用 ControlNet 後、用於修補的修改後負條件 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
