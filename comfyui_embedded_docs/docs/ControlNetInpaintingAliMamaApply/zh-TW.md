# 套用 ControlNet 修補（AliMama）

此節點透過將正向與負向條件結合控制影像和遮罩，為修復（inpainting）任務套用 ControlNet 條件。它處理影像和遮罩以建立修改後的條件，引導生成過程，讓使用者精確控制要修復的區域。此節點也支援強度與時間控制，可調整 ControlNet 在生成期間的影響。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 正向條件，引導生成朝向想要的內容。 | CONDITIONING | 是 | - |
| `negative` | 負向條件，引導生成遠離不想要的內容。 | CONDITIONING | 是 | - |
| `control_net` | 提供對生成額外控制的 ControlNet 模型。 | CONTROL_NET | 是 | - |
| `vae` | 用於編碼和解碼影像的 VAE。 | VAE | 是 | - |
| `image` | 作為 ControlNet 控制引導的輸入影像。 | IMAGE | 是 | - |
| `mask` | 定義影像中應修復區域的遮罩。 | MASK | 是 | - |
| `strength` | ControlNet 效果的強度（預設：1.0）。 | FLOAT | 是 | 0.0 to 10.0 |
| `start_percent` | 進階選項。ControlNet 影響開始的生成流程比例（預設：0.0）。 | FLOAT | 是 | 0.0 to 1.0 |
| `end_percent` | 進階選項。ControlNet 影響停止的生成流程比例（預設：1.0）。 | FLOAT | 是 | 0.0 to 1.0 |

**注意：** 當所選的 ControlNet 啟用 `concat_mask` 時，遮罩值會被反轉（1 - mask），反轉後的遮罩會調整尺寸後套用於影像，且反轉遮罩會包含在傳遞給 ControlNet 的額外串接資料中。若停用 `concat_mask`，則不會使用 `mask` 輸入。

## 輸出

| 輸出名 | 描述 | 資料型別 |
| --- | --- | --- |
| `positive` | 套用 ControlNet 於修復後修改的正向條件。 | CONDITIONING |
| `negative` | 套用 ControlNet 於修復後修改的負向條件。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
