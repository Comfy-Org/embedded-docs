# SeedVR2ProgressiveSampler

用於 SeedVR2 原生工作流程的順序時間區塊取樣器。此節點透過將長影片潛在變數分割成較小的時間區塊，依序對每個區塊進行取樣，並將結果混合在一起來處理長影片潛在變數。當使用 SeedVR2 模型處理會導致記憶體不足錯誤的序列時，此節點可作為標準 KSampler 的直接替代品。

## ## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於對輸入潛在變數進行去噪的模型 | MODEL | 是 | |
| `seed` | 用於產生雜訊的隨機種子（預設值：0） | INT | 是 | 0 到 0xffffffffffffffff |
| `steps` | 去噪過程中使用的步數（預設值：20） | INT | 是 | 1 到 10000 |
| `cfg` | 無分類器引導尺度，用於平衡創造力與對提示的遵循程度。數值越高，生成的影像越符合提示，但過高的數值會對品質產生負面影響（預設值：1.0） | FLOAT | 是 | 0.0 到 100.0 |
| `sampler_name` | 取樣時使用的演算法，會影響生成輸出的品質、速度和風格 | COMBO | 是 | 提供多種選項 |
| `scheduler` | 排程器控制雜訊如何逐步移除以形成影像 | COMBO | 是 | 提供多種選項 |
| `positive` | 描述您希望包含在影像中的屬性的條件設定 | CONDITIONING | 是 | |
| `negative` | 描述您希望從影像中排除的屬性的條件設定 | CONDITIONING | 是 | |
| `latent` | 要進行去噪的潛在影像 | LATENT | 是 | |
| `denoise` | 應用的去噪程度，較低的值將保持初始影像的結構，允許進行影像到影像的取樣（預設值：1.0） | FLOAT | 是 | 0.0 到 1.0 |
| `frames_per_chunk` | 每個時間區塊的像素幀數。必須是 4n+1 的值（1、5、9、13、17、21...）以符合 SeedVR2 的限制（預設值：21） | INT | 是 | 1 到 16384（步長為 4） |
| `temporal_overlap` | 相鄰區塊之間混合的潛在幀數，用於隱藏接縫；0 表示不進行混合（預設值：0） | INT | 是 | 0 到 16384 |
| `chunking_mode` | manual = 精確使用 `frames_per_chunk`；auto = 縮小區塊直到適合 VRAM（預設值："manual"） | COMBO | 是 | "manual"<br>"auto" |

**關於 `frames_per_chunk` 的說明：** 此參數必須是 4n+1 的像素幀數（1、5、9、13、17、21...）。如果提供了無效值，節點將引發錯誤。

**關於 `temporal_overlap` 的說明：** 重疊值會自動限制為最多比潛在區塊大小小一，以確保有效的區塊處理。

**關於 `chunking_mode` 的說明：** 當設定為 "auto" 時，如果當前區塊導致記憶體不足錯誤，節點將自動嘗試較小的區塊大小。如果所有嘗試都失敗，節點將引發錯誤。

## ## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `latent` | 去噪後的潛在輸出，從所有時間區塊連接回單一的壓縮 SeedVR2 潛在張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2ProgressiveSampler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a4574c3e619954b5569551b5b2ba112ecbff918dcebb5ba718a14e77701144a9`
