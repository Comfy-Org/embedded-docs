# ByteDance Seedance 2.0 首末幀轉影片

此節點使用 ByteDance Seedance 2.5 或 Seedance 2.0 模型，從必填的起始幀（first frame）影像與可選的結束幀（last frame）影像生成影片。起始幀定義影片片段的開頭，結束幀（若提供）定義結尾，文字提示則描述動態。所選模型會控制可用的解析度、時長與輸出格式選項。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片生成的模型。Seedance 2.5 是最新模型，支援最長 30 秒的影片及 mp4/mov 輸出；Seedance 2.0 提供最高品質與 1080p/4k；Fast 專為速度最佳化；Mini 是最快、成本最低的生成。選取模型後，下方會顯示其專屬輸入。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | 影片的起始幀影像。`first_frame` 與 `first_frame_asset_id` 必須提供其中一個。 | IMAGE | 否 | - |
| `last_frame` | 影片的結束幀影像。 | IMAGE | 否 | - |
| `first_frame_asset_id` | Seedance asset_id 用作起始幀。與 `first_frame` 影像輸入互斥。預設為空字串。 | STRING | 否 | - |
| `last_frame_asset_id` | Seedance asset_id 用作結束幀。與 `last_frame` 影像輸入互斥。預設為空字串。 | STRING | 否 | - |
| `seed` | Seed 控制節點是否應重新執行；無論 seed 為何，結果皆非確定性。預設為 0。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在影片中加入浮水印。預設為 False。 | BOOLEAN | 否 | - |

### Seedance 2.5 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示。將台詞放在雙引號中，以引導生成的對話內容。預設為空字串。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。預設為 "720p"。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `duration` | 輸出影片的時長（秒）(4-30)。預設為 5。 | INT | 是 | 4 to 30 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設為 True。 | BOOLEAN | 是 | - |
| `output_format` | 輸出影片的容器格式。預設為 "mp4"。 | COMBO | 是 | `"mp4"` |

### Seedance 2.0 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示。預設為空字串。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比。預設為 "adaptive"。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的時長（秒）(4-15)。預設為 7。 | INT | 是 | 4 to 15 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設為 True。 | BOOLEAN | 是 | - |

### Seedance 2.0 Fast 與 Seedance 2.0 Mini 共用

這兩個模型提供與 Seedance 2.0 相同的輸入，但僅提供 480p 與 720p 解析度。

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示。預設為空字串。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比。預設為 "adaptive"。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的時長（秒）(4-15)。預設為 7。 | INT | 是 | 4 to 15 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設為 True。 | BOOLEAN | 是 | - |

**限制與約束：**

*   `prompt` 為必填項，且必須包含至少一個非空白字元（忽略開頭與結尾的空白）。
*   您必須提供恰好一個起始幀來源：`first_frame` 影像或 `first_frame_asset_id`。同時提供兩者會引發錯誤，兩者都不提供也會引發錯誤。
*   `last_frame` 影像與 `last_frame_asset_id` 互斥。兩者皆可省略。
*   Asset ID 必須參照狀態為 Active 的現有 Seedance 資產。若資產未啟用或不是 Image 資產，則會引發錯誤。
*   本機影像的長寬比必須介於 0.4 至 2.5 之間（2:5 至 5:2）。
*   對於 Seedance 2.0 模型，本機影像必須至少為 300x300 像素。系統會自動將影像調整為所選解析度與比例對應的完整支援輸出尺寸，並以 "adaptive" 比例提交請求。當 `ratio` 為 "adaptive" 時，輸出長寬比會根據起始幀自身的長寬比推導，並貼合至最接近的支援比例。當使用 asset ID 而非本機影像時，會直接套用所選的 `ratio` 值。
*   對於 Seedance 2.5，以及任何使用 asset ID 的模型，影像會自動縮小至最大邊長 6000 像素，且每個維度必須介於 300 至 6000 像素之間。
*   Seedance 2.5 始終保留起始幀自身的長寬比，因此此模型不顯示 `ratio` 輸入。
*   時長限制因模型而異：Seedance 2.5 支援 4 至 30 秒，而 Seedance 2.0、2.0 Fast 與 2.0 Mini 支援 4 至 15 秒。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `output` | 生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d87265eb75d67f7d80f76474fc699f7ca87b6edbddda36733d5e440708b074a2`
