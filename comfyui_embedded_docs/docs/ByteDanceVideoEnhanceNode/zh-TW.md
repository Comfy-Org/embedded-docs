# ByteDanceVideoEnhanceNode

此節點使用 ByteDance vCube 對影片進行放大與修復。可將解析度提升至 8K，移除壓縮偽影與雜訊、增強色彩與銳利度，並可選擇進行影格補插以獲得更高的幀率。影片會上傳至 vCube 服務，以所選的增強預設進行處理，最後回傳增強後的影片檔案。

## 輸入

### 通用輸入

這些輸入參數一律可見。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要增強的影片。來源解析度最高必須為 2560x1440（2K）；輸出尺寸由解析度輸入決定。 | VIDEO | 是 | 最高 2560x1440（2K） |
| `tool_version` | 「standard」在速度與品質之間取得平衡，搭載 10 種以上的增強演算法；「professional」則使用 30 種以上演算法進行電影級修復，耗時約 3 倍，成本為 10 倍。 | DYNAMIC_COMBO | 是 | "standard"<br>"professional" |
| `resolution` | 輸出解析度。短邊設為所選等級，長邊依來源影片長寬比自動決定。「source」保留來源尺寸，「custom」以像素設定短邊。來源影片的寬高比若超過約 2.2:1，將以更高一個解析度等級計費。 | DYNAMIC_COMBO | 是 | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | 輸出幀率。高於來源幀率時會啟用 AI 影格補插；低於來源幀率時則會捨棄影格。「source」保留來源幀率，最高可達 120 fps。幀率高於 30 fps 費用為 2 倍，高於 60 fps 費用為 4 倍。（預設值："source"） | COMBO | 是 | "source" (default)<br>數值幀率，最高 120 fps |
| `bitrate_level` | 輸出檔案的目標位元率，會依輸出解析度與幀率進行縮放。（預設值："medium"） | COMBO | 是 | "low"<br>"medium"<br>"high" |

### 標準輸入

當 `tool_version` 設為「standard」時顯示。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `scene` | 依內容調校的預設模式：「aigc」適用於 AI 生成素材，「common」適用於一般影片，「ugc」適用於壓縮過的手機片段，「short_series」適用於包含人臉的戲劇，「old_film」適用於有刮痕或閃爍的檔案素材。（預設值："aigc"） | COMBO | 是 | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 「hd」套用較銳利的增強效果；「natural」降低強度，呈現較柔和、較少銳利化的外觀。（預設值："hd"） | COMBO | 是 | "hd"<br>"natural" |

### 專業輸入

當 `tool_version` 設為「professional」時顯示。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `enhance_style` | 「hd」套用較銳利的增強效果；「natural」降低強度，呈現較柔和、較少銳利化的外觀。（預設值："hd"） | COMBO | 是 | "hd"<br>"natural" |

### 自訂解析度輸入

當 `resolution` 設為「custom」時顯示。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `short_side` | 輸出短邊的像素長度；長邊依來源影片長寬比自動決定。（預設值：1080） | INT | 是 | 預設值 1080；受限於 vCube 的最小與最大短邊限制 |

### 注意事項

- 來源影片最高必須為 2560x1440（2K）。大於此尺寸的影片會被拒絕，必須先縮小尺寸再進行增強。
- 來源影片的時長不得超過 vCube 服務支援的最大時長。
- 當 `tool_version` 為「standard」時，`scene` 與 `enhance_style` 皆可使用；當其為「professional」時，僅 `enhance_style` 可使用。
- 當 `resolution` 為「custom」時，必須提供 `short_side` 值。解析度預設選項與「source」不使用 `short_side`。
- 當 `resolution` 為「source」時，輸出將保持來源解析度。
- 當 `fps` 為「source」時，輸出幀率與來源幀率相同，最高可達 120 fps。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 增強後的影片，已按要求的解析度與幀率進行放大與修復。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`
