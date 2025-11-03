> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/zh-TW.md)

此節點將 ControlNet 引導應用於 Stable Diffusion 3 的條件設定。它接收正向與負向條件輸入，以及 ControlNet 模型和圖像，然後透過可調整的強度和時機參數來施加控制引導，以影響生成過程。

**注意：** 此節點已被標記為棄用，可能在未來版本中移除。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `正向` | CONDITIONING | 是 | - | 要應用 ControlNet 引導的正向條件設定 |
| `負向` | CONDITIONING | 是 | - | 要應用 ControlNet 引導的負向條件設定 |
| `control_net` | CONTROL_NET | 是 | - | 用於引導的 ControlNet 模型 |
| `vae` | VAE | 是 | - | 過程中使用的 VAE 模型 |
| `影像` | IMAGE | 是 | - | ControlNet 將用作引導的輸入圖像 |
| `強度` | FLOAT | 是 | 0.0 - 10.0 | ControlNet 效果的強度（預設值：1.0） |
| `起始百分比` | FLOAT | 是 | 0.0 - 1.0 | ControlNet 開始應用的生成過程起始點（預設值：0.0） |
| `結束百分比` | FLOAT | 是 | 0.0 - 1.0 | ControlNet 停止應用的生成過程結束點（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `負向` | CONDITIONING | 已應用 ControlNet 引導的修改後正向條件設定 |
| `負向` | CONDITIONING | 已應用 ControlNet 引導的修改後負向條件設定 |