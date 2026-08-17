# SAM3 影片追蹤

使用 SAM3 的記憶型追蹤器在影片幀之間追蹤物件。此節點處理一系列影片幀，並在幀之間維持物件的身份，使用初始遮罩或文字提示來定義要追蹤的內容。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 作為批次影像的影片幀 | IMAGE | 是 | Batched video frames |
| `model` | 用於追蹤的 SAM3 模型 | MODEL | 是 | SAM3 model |
| `initial_mask` | 用於第一幀追蹤的遮罩（每個物件一個）。若未提供 `conditioning`，則此為必填。 | MASK | 否 | One mask per object |
| `conditioning` | 用於在追蹤過程中偵測新物件的文字條件。若未提供 `initial_mask`，則此為必填。 | CONDITIONING | 否 | Text conditioning |
| `detection_threshold` | 文字提示偵測的分數門檻（預設值：0.5）。 | FLOAT | 是 | 0.0 to 1.0 |
| `max_objects` | 最大追蹤物件數。初始遮罩計入此限制。0 表示使用內部上限 64（預設值：4）。 | INT | 是 | 0 to 64 |
| `detect_interval` | 每隔 N 幀執行一次偵測（1=每一幀）。數值越高越節省計算資源（預設值：1）。 | INT | 是 | 1 or higher |

**注意：** 必須提供 `initial_mask` 或 `conditioning`。若兩者皆省略，節點將引發錯誤。若同時提供兩者，初始遮罩定義從第一幀開始追蹤的物件，而文字提示則在追蹤過程中偵測額外的物件。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `track_data` | 包含所有影片幀之物件遮罩與中繼資料的追蹤資料，包括原始幀尺寸。 | SAM3_TRACK_DATA |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
