# ByteDanceVideoEnhanceNode

此節點使用 ByteDance vCube 來放大和修復影片。它可以將解析度提升至 8K，去除壓縮偽影和雜訊，增強色彩與銳利度，並可選擇性地進行影格插值以達成更高的影格率。影片會上傳至 vCube 服務，使用所選的增強預設進行處理，然後以增強後的影片檔案形式回傳。

## 輸入

### 通用輸入

這些輸入永遠可見。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 要增強的影片。來源解析度必須最高為 2560x1440 (2K)；輸出大小由解析度輸入設定。 | VIDEO | 是 | 最高 2560x1440 (2K) |
| `工具版本` | 'standard' 透過 10 種以上的增強演算法平衡速度與品質。'professional' 使用 30 種以上的演算法進行電影級修復，耗時約 3 倍，成本高 10 倍。 | DYNAMIC_COMBO | 是 | "standard"<br>"professional" |
| `解析度` | 輸出解析度。短邊會設為所選等級，長邊則維持來源長寬比。'source' 保留來源大小，'custom' 以像素設定短邊。寬或高超過約 2.2:1 的來源會以高一級解析度計費。 | DYNAMIC_COMBO | 是 | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | 輸出影格率。高於來源的影格率會啟用 AI 影格插值；較低的影格率則會丟棄影格。'source' 保留來源影格率，最高 120 fps。高於 30 fps 的影格率費用為 2 倍，高於 60 fps 為 4 倍。(預設值："source") | COMBO | 是 | "source" (預設)<br>最高 120 fps 的數值影格率 |
| `位元率等級` | 交付檔案的目標位元率，會依輸出解析度和影格率進行縮放。(預設值："medium") | COMBO | 是 | "low"<br>"medium"<br>"high" |

### 標準輸入

當 `tool_version` 設為 "standard" 時顯示。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `scene` | 針對內容調整的預設：'aigc' 用於 AI 生成素材，'common' 用於一般影片，'ugc' 用於壓縮的手機片段，'short_series' 用於包含臉部的戲劇，'old_film' 用於有刮痕或閃爍的檔案素材。(預設值："aigc") | COMBO | 是 | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 'hd' 套用較銳利的增強效果；'natural' 降低強度以呈現較柔和、較不銳利的外觀。(預設值："hd") | COMBO | 是 | "hd"<br>"natural" |

### 專業輸入

當 `tool_version` 設為 "professional" 時顯示。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `enhance_style` | 'hd' 套用較銳利的增強效果；'natural' 降低強度以呈現較柔和、較不銳利的外觀。(預設值："hd") | COMBO | 是 | "hd"<br>"natural" |

### 自訂解析度輸入

當 `resolution` 設為 "custom" 時顯示。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `short_side` | 輸出的短邊（像素）；長邊維持來源長寬比。(預設值：1080) | INT | 是 | 預設 1080；受限於 vCube 的最小和最大短邊限制 |

### 注意事項

- 來源影片必須最高為 2560x1440 (2K)。大於此大小的影片會被拒絕，必須在增強前縮小尺寸。
- 來源影片的長度限制為 vCube 服務支援的最大長度。
- 當 `tool_version` 為 "standard" 時，`scene` 和 `enhance_style` 皆可使用。當其為 "professional" 時，僅 `enhance_style` 可使用。
- 當 `resolution` 為 "custom" 時，需要 `short_side` 值。解析度預設和 "source" 不使用 `short_side`。
- 當 `resolution` 為 "source" 時，輸出保留來源解析度。
- 當 `fps` 為 "source" 時，輸出影格率與來源影格率相同，最高 120 fps。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 增強後的影片，以要求的解析度和影格率進行放大與修復。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`
