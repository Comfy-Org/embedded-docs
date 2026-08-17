# 套用 ControlNet (SD3)

此節點將 ControlNet 引導應用於 Stable Diffusion 3 conditioning。它接收正向與負向 conditioning 輸入，以及 ControlNet 模型和影像，然後以可調整的強度與時機參數套用控制引導，以影響生成過程。

**注意：** 此節點已標記為棄用，未來版本可能移除。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要套用 ControlNet 引導的正向 conditioning | CONDITIONING | 是 | - |
| `negative` | 要套用 ControlNet 引導的負向 conditioning | CONDITIONING | 是 | - |
| `control_net` | 用於引導的 ControlNet 模型 | CONTROL_NET | 是 | - |
| `vae` | 過程中使用的 VAE 模型 | VAE | 是 | - |
| `image` | ControlNet 將作為引導使用的輸入影像 | IMAGE | 是 | - |
| `strength` | ControlNet 效果的強度（預設值：1.0） | FLOAT | 是 | 0.0 - 10.0 |
| `start_percent` | 生成過程中 ControlNet 開始套用的起點（預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `end_percent` | 生成過程中 ControlNet 停止套用的終點（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

**注意：** 當 `strength` 設定為 0 時，此節點會回傳未變更的正向與負向 conditioning，且不套用 ControlNet。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `positive` | 套用 ControlNet 引導後的修改版正向 conditioning | CONDITIONING |
| `negative` | 套用 ControlNet 引導後的修改版負向 conditioning | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
