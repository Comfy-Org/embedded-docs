# SAM3 影片追蹤

使用 SAM3 的記憶體式追蹤器跨影片幀追蹤物件。此節點會處理一系列影片幀，並在幀之間維持物件身分，使用初始遮罩或文字提示來定義要追蹤的內容，並可透過文字條件在追蹤過程中偵測新物件。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 以批次影像形式提供的影片幀 | IMAGE | 是 | Batched video frames |
| `model` | 用於追蹤的 SAM3 模型 | MODEL | 是 | SAM3 model |
| `初始 mask` | 要追蹤的第一幀遮罩（每個物件一個） | MASK | 否 | One mask per object |
| `條件` | 用於在追蹤期間偵測新物件的文字條件 | CONDITIONING | 否 | Text conditioning |
| `偵測閾值` | 文字提示偵測的分數閾值（預設值：0.5） | FLOAT | 否 | 0.0 至 1.0 （步進值：0.01） |
| `最大物件數` | 最大追蹤物件數。初始遮罩會計入此上限。0 會使用內部上限 64。（預設值：4） | INT | 否 | 0 至 64 |
| `偵測間隔` | 每 N 幀執行偵測（1=每一幀）。較高的值可節省運算。（預設值：1） | INT | 否 | 1 or higher |

**注意：** 必須提供 `initial_mask` 或 `conditioning` 其中一個。如果兩者都省略，節點會引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `track_data` | 包含所有影片幀中物件遮罩與中繼資料的追蹤資料 | SAM3_TRACK_DATA |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
