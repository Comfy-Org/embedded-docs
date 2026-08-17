# Reve 圖像編輯

Reve Image Edit 節點可讓您根據文字描述修改現有圖片。它使用 Reve API 來解讀您的指令，並將要求變更套用到您提供的圖片上。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|------|------|---------|------|------|
| `image` | 要編輯的圖片。 | IMAGE | 是 | - |
| `edit_instruction` | 描述如何編輯圖片的文字。最多 2560 個字元。（預設值：""） | STRING | 是 | 1 至 2560 個字元 |
| `model` | 用於編輯的模型版本。 | DYNAMIC_COMBO | 是 | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `upscale` | 放大生成的圖片。可能產生額外費用。（預設值："disabled"） | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"enabled"` |
| `remove_background` | 移除生成圖片的背景。可能產生額外費用。（預設值：false） | BOOLEAN | 否 | `true`<br>`false` |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果皆為非確定性。（預設值：0） | INT | 否 | 0 至 2147483647 |

### 模型輸入

由 `reve-edit@20250915` 與 `reve-edit-fast@20251030` 模型共用。

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|------|------|---------|------|------|
| `model.aspect_ratio` | 輸出圖片的長寬比。設為 `"auto"` 時，長寬比會自動決定。（預設值："auto"） | COMBO | 否 | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | 數值越高，產生圖片品質越好，但花費的點數越多。（預設值：1） | INT | 否 | 1 至 5 |

### 放大輸入

當 `upscale` 設為 `"enabled"` 時顯示。

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|------|------|---------|------|------|
| `upscale.upscale_factor` | 放大倍率（2 倍、3 倍或 4 倍）。（預設值：2） | INT | 否 | 2 至 4 |

**注意：** `upscale.upscale_factor` 參數僅在 `upscale` 設為 `"enabled"` 時出現。

## 輸出

| 輸出名 | 描述 | 資料型別 |
|--------|------|---------|
| `image` | 根據指令產生的已編輯圖片。 | IMAGE |

**注意：** 此節點已標記為已棄用。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`
