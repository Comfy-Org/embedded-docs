# 套用 ControlNet (SD3)

## 概述

此節點將 ControlNet 引導應用於 Stable Diffusion 3 的條件設定。它接收正向與負向條件設定輸入，以及 ControlNet 模型和影像，接著以可調整的強度與時間參數來應用控制引導，以影響生成過程。

**注意：** 此節點已被標記為已棄用，可能在未來版本中移除。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 要套用 ControlNet 引導的正向條件設定 | CONDITIONING | 是 | - |
| `負向` | 要套用 ControlNet 引導的負向條件設定 | CONDITIONING | 是 | - |
| `control_net` | 用於引導的 ControlNet 模型 | CONTROL_NET | 是 | - |
| `vae` | 過程中使用的 VAE 模型 | VAE | 是 | - |
| `影像` | ControlNet 將用作引導的輸入影像 | IMAGE | 是 | - |
| `強度` | ControlNet 效果的強度（預設值：1.0） | FLOAT | 是 | 0.0 - 10.0 |
| `起始百分比` | ControlNet 開始應用的生成過程起點（預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `結束百分比` | ControlNet 停止應用的生成過程終點（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `負向` | 已套用 ControlNet 引導的修改後正向條件設定 | CONDITIONING |
| `負向` | 已套用 ControlNet 引導的修改後負向條件設定 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7bd24b19c159374bc86a773be9b563760bfae7e10d3333596788dbc52ef2f294`
