> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/zh-TW.md)

## 概述

使用 SAM3 的記憶體追蹤器在影片幀之間追蹤物體。此節點處理一系列影片幀，並透過使用初始遮罩或文字提示來定義要追蹤的內容，從而跨幀維持物體身份。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | 是 | 批次影片幀 | 作為批次圖像的影片幀 |
| `model` | MODEL | 是 | SAM3 模型 | 用於追蹤的 SAM3 模型 |
| `initial_mask` | MASK | 否 | 每個物體一個遮罩 | 第一幀要追蹤的物體遮罩（每個物體一個）。如果未提供 `conditioning`，則此為必要參數。 |
| `conditioning` | CONDITIONING | 否 | 文字條件設定 | 用於在追蹤過程中偵測新物體的文字條件設定。如果未提供 `initial_mask`，則此為必要參數。 |
| `detection_threshold` | FLOAT | 否 | 0.0 至 1.0（預設值：0.5） | 文字提示偵測的得分閾值 |
| `max_objects` | INT | 否 | 0 至無上限（預設值：0） | 最大追蹤物體數量（0=無上限）。初始遮罩計入此限制。 |
| `detect_interval` | INT | 否 | 1 至無上限（預設值：1） | 每 N 幀執行一次偵測（1=每幀）。較高的值可節省運算資源。 |

**注意：** 必須提供 `initial_mask` 或 `conditioning` 其中之一。如果兩者都省略，節點將引發錯誤。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `track_data` | SAM3TrackData | 包含所有影片幀中物體遮罩和元資料的追蹤資料 |