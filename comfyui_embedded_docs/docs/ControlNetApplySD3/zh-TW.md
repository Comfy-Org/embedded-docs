# 套用 ControlNet (SD3)

此節點將 ControlNet 引導套用於 Stable Diffusion 3 條件。它接收正向和負向條件輸入，以及 ControlNet 模型和圖像，然後以可調整的強度和時序參數套用控制引導，以影響生成過程。

**注意：** 此節點已被標記為已棄用，未來版本中可能會移除。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 要套用 ControlNet 引導的正向條件 | CONDITIONING | 是 | - |
| `負向` | 要套用 ControlNet 引導的負向條件 | CONDITIONING | 是 | - |
| `control_net` | 用於引導的 ControlNet 模型 | CONTROL_NET | 是 | - |
| `vae` | 在此過程中使用的 VAE 模型 | VAE | 是 | - |
| `影像` | ControlNet 將用作引導的輸入圖像 | IMAGE | 是 | - |
| `強度` | ControlNet 效果的強度（預設值：1.0）。當設為 0.0 時，節點不會套用 ControlNet，並原樣回傳條件。 | FLOAT | 是 | 0.0 - 10.0 |
| `起始百分比` | 生成過程中 ControlNet 開始套用的起點（預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `結束百分比` | 生成過程中 ControlNet 停止套用的終點（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

**注意：** 當 `strength` 設為 0.0 時，不會套用 ControlNet 引導，輸入條件會原樣傳遞到兩個輸出。

**注意：** 如果相同的條件在其他地方重複使用且已包含控制資訊，新的 ControlNet 會在前一個之後連結，因此可以依序套用多個 ControlNet。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `正向` | 已套用 ControlNet 引導的修改後正向條件 | CONDITIONING |
| `負向` | 已套用 ControlNet 引導的修改後負向條件 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
