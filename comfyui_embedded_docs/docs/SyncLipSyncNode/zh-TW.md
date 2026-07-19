# SyncLipSyncNode

此節點使用 sync.so API 將影片中的嘴部動作與新的語音音訊重新同步。它會自動處理特寫、側面及遮擋情況，同時保留說話者的表情。費用會根據輸出時長而變化。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要重新同步的說話者影片素材。最高可達 4K (4096x2160)；24/25/30 fps 的固定影格率效果最佳。 | VIDEO | 是 | - |
| `audio` | 用於同步嘴部的語音音訊。 | AUDIO | 是 | - |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果皆為非確定性（預設值：42）。 | INT | 是 | 0 到 2147483647 |
| `model` | sync.so 生成模型。 | COMBO | 是 | 請參閱下方 |

`model` 參數是一個動態組合，包含以下子參數：

| 子參數 | 描述 | 資料類型 | 必要 | 範圍 |
|---------------|-------------|-----------|----------|-------|
| `sync_mode` | 如何處理影片與音訊之間的時長不匹配；此設定也會決定輸出長度（預設值："bounce"）。 | COMBO | 是 | `"bounce"`<br>`"cut_off"`<br>`"loop"`<br>`"silence"`<br>`"remap"` |
| `speaker_selection` | 當畫面中有多人時，要對哪張臉進行唇形同步（預設值："default"）。 | COMBO | 是 | `"default"`<br>`"auto-detect"`<br>`"coordinates"` |
| `speaker_frame` | 用於定位說話者的影片影格。僅在 `speaker_selection` 設為 "coordinates" 時使用（預設值：0）。 | INT | 否 | 0 到 1000000 |
| `speaker_x` | 說話者臉部的 X 像素座標。僅在 `speaker_selection` 設為 "coordinates" 時使用（預設值：0）。 | INT | 否 | 0 到 4096 |
| `speaker_y` | 說話者臉部的 Y 像素座標。僅在 `speaker_selection` 設為 "coordinates" 時使用（預設值：0）。 | INT | 否 | 0 到 4096 |

**同步模式選項：**
- `bounce`：影片向前播放，然後向後播放，直到音訊結束（輸出長度 = 音訊長度）
- `loop`：影片重新開始播放，直到音訊結束（輸出長度 = 音訊長度）
- `remap`：影片被時間拉伸以匹配音訊（輸出長度 = 音訊長度）
- `cut_off`：較長的軌道會被裁剪（輸出長度 = 較短的長度）
- `silence`：不裁剪任何內容；較短的軌道會被填充靜音（輸出長度 = 較長的長度）

**說話者選擇選項：**
- `default`：讓模型決定要對哪張臉進行唇形同步
- `auto-detect`：偵測並跟隨正在說話的人
- `coordinates`：定位到由 `speaker_frame` 選擇的影格中，像素座標 (`speaker_x`, `speaker_y`) 處的臉部

**限制條件：**
- 影片解析度不得超過 4K (4096x2160)。超過此限制的影片將會引發錯誤。
- 音訊時長不得超過 600 秒（10 分鐘）。
- `speaker_frame`、`speaker_x` 和 `speaker_y` 參數僅在 `speaker_selection` 設為 "coordinates" 時使用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 重新同步後的影片，嘴部動作與提供的音訊相匹配。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncLipSyncNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b41f8c9bf0d55059f081a66af20636ec96462c3fd9caeb685cab10278f84678a`
