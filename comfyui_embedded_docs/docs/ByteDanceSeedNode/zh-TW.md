# ByteDance Seed

ByteDance Seed 使用 ByteDance 的 Seed 2.0 模型產生文字回應。提供文字提示，並可選擇性地加入一或多張圖片或影片以提供多模態上下文。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於產生回應的 Seed 模型。 | DYNAMIC_COMBO | 是 | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `prompt` | 傳送給模型的文字輸入。（預設值：""） | STRING | 是 | N/A |
| `seed` | `seed` 控制節點是否應重新執行；無論種子值為何，結果都具有不確定性。（預設值：0） | INT | 是 | 0 to 2147483647 |
| `system_prompt` | 用於決定模型行為的基礎指令。（預設值：""） | STRING | 否 | N/A |

### Seed 2.0 Pro、Seed 2.0 Lite 與 Seed 2.0 Mini 輸入

此設定由全部三個模型選項共用。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `temperature` | 控制隨機性。0.0 為確定性，數值越高越隨機。（預設值：1.0） | FLOAT | 是 | 0.0 to 2.0 |

### 參考輸入

`model` 選擇器提供這些可擴充插槽，用於連接圖片與影片，以提供模型多模態上下文。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可選的圖片，作為模型的上下文。最多 20 張圖片。可擴充插槽：連接 1 至 20 個項目（例如 `image_1`...`image_20`）。 | IMAGE | 否 | `image_1` to `image_20` |
| `videos` | 可選的影片，作為模型的上下文。最多 4 部影片。可擴充插槽：連接 1 至 4 個項目（例如 `video_1`...`video_4`）。 | VIDEO | 否 | `video_1` to `video_4` |

**注意：** `model` 選擇器決定用於產生回應的 Seed 模型。每個選項對應到特定的模型 ID：`"Seed 2.0 Pro"` → `seed-2-0-pro-260328`、`"Seed 2.0 Lite"` → `seed-2-0-lite-260228`、`"Seed 2.0 Mini"` → `seed-2-0-mini-260215`。

**關於限制的注意事項：** 每個請求最多支援 20 張圖片與 4 部影片。`prompt` 必須是非空字串。

**關於定價的注意事項：** 定價以 token 為基礎，並在節點 UI 中顯示為每 1K token 的近似範圍：Seed 2.0 Mini：$0.00025-$0.0009；Seed 2.0 Lite：$0.0003-$0.002；Seed 2.0 Pro：$0.0005-$0.003。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 由 Seed 模型產生的文字回應。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
