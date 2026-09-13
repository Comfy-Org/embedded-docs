# ByteDance vCube 影片增強

此節點使用 ByteDance vCube 對影片進行解析度提升與修復。可將解析度提升至最高 8K，移除壓縮失真與雜訊，增強色彩與銳利度，並可選擇性地進行補幀以提高影格率。影片會上傳至 vCube 服務，使用所選的增強預設集進行處理，並以增強後的影片檔案回傳。

## 輸入

### 通用輸入

這些輸入永遠可見。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 要增強的影片。來源解析度必須最高為 2560x1440 (2K)；輸出尺寸由 `resolution` 輸入決定。 | VIDEO | 是 | 最高 2560x1440 (2K) |
| `工具版本` | 'standard' 以 10+ 種增強演算法平衡速度與品質。'professional' 使用 30+ 種演算法進行電影級修復，耗時約 3 倍，成本高 10 倍。 | DYNAMIC_COMBO | 是 | "standard"<br>"professional" |
| `解析度` | 輸出解析度。短邊會設為所選等級，長邊則依來源長寬比調整。'source' 保留來源尺寸，'custom' 以像素設定短邊。寬度或高度超過約 2.2:1 的來源會以高一階的解析度等級計費。 | DYNAMIC_COMBO | 是 | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | 輸出影格率。高於來源的影格率會啟用 AI 補幀；低於來源的影格率則會捨棄影格。'source' 保留來源影格率，最高 120 fps。高於 30 fps 的影格率成本為 2 倍，高於 60 fps 為 4 倍。（預設值："source"） | COMBO | 是 | "source" (預設)<br>數值影格率最高 120 fps |
| `位元率等級` | 交付檔案的目標位元率，會依輸出解析度與影格率調整。（預設值："medium"） | COMBO | 是 | "low"<br>"medium"<br>"high" |

### 標準輸入

當 `tool_version` 設為 "standard" 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `scene` | 針對內容調整的預設集：'aigc' 適用於 AI 生成影片，'common' 適用於一般影片，'ugc' 適用於壓縮過的手機短片，'short_series' 適用於有人臉的戲劇，'old_film' 適用於有刮痕或閃爍的檔案影片。（預設值："aigc"） | COMBO | 是 | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 'hd' 套用更銳利的增強；'natural' 降低增強強度，呈現較柔和、較不銳利的樣貌。（預設值："hd"） | COMBO | 是 | "hd"<br>"natural" |

### 專業輸入

當 `tool_version` 設為 "professional" 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `enhance_style` | 'hd' 套用更銳利的增強；'natural' 降低增強強度，呈現較柔和、較不銳利的樣貌。（預設值："hd"） | COMBO | 是 | "hd"<br>"natural" |

### 自訂解析度輸入

當 `resolution` 設為 "custom" 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `short_side` | 輸出的短邊像素值；長邊會依來源長寬比調整。（預設值：1080） | INT | 是 | 預設 1080；受 vCube 最小與最大短邊限制所規範 |

### 備註

- 來源影片必須最高為 2560x1440 (2K)。大於此尺寸的影片會遭拒絕，必須先縮小後再增強。
- 來源影片長度限制為 vCube 服務支援的最大長度。
- 當 `tool_version` 為 "standard" 時，`scene` 與 `enhance_style` 皆可使用。當其為 "professional" 時，僅可使用 `enhance_style`。
- 當 `resolution` 為 "custom" 時，必須提供 `short_side` 值。解析度預設集與 "source" 不會使用 `short_side`。
- 當 `resolution` 為 "source" 且來源短邊至少達到最小短邊限制時，輸出會保留來源解析度。
- 當 `fps` 為 "source" 時，輸出影格率會與來源影格率相符，最高 120 fps。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 增強後的影片，會依要求的解析度與影格率進行解析度提升與修復。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`
