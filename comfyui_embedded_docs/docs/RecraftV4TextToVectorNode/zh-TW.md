# Recraft V4 文字轉向量圖

Recraft V4 Text to Vector 節點使用 Recraft V4 與 V4.1 模型，根據文字描述生成可縮放向量圖形（SVG）插圖。它會連線至 Recraft API，根據你的提示詞生成一個或多個 SVG 檔案，並可套用現有的向量風格，或從參考影像建立新的向量風格——當使用參考影像時，所建立的風格會以 `style_id` 回傳以供重複使用。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於生成的模型。recraftv4_styles 模型專為風格一致的生成而打造，且一律需要 `style_id` 或 `style_references`。選取模型會變更可用的 `size` 選項。 | DYNAMIC_COMBO | 是 | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"`<br>`"recraftv4_styles_vector"`<br>`"recraftv4_styles_pro_vector"` |
| `prompt` | 用於影像生成的提示詞。最多 10,000 個字元。 | STRING | 是 | N/A |
| `negative_prompt` | 此輸入會被忽略：Recraft V4 與 V4.1 模型不支援負向提示詞。 | STRING | 是 | N/A |
| `n` | 要生成的影像數量（預設：1）。 | INT | 是 | 1 到 6 |
| `seed` | 用來決定節點是否應重新執行的種子；無論種子為何，實際結果皆非確定性（預設：0）。 | INT | 是 | 0 到 18446744073709551615 |
| `recraft_controls` | 透過 Recraft Controls 節點對生成提供的選用額外控制項。 | CUSTOM | 否 | N/A |
| `style_id` | 要套用的 Recraft V4 向量風格 UUID，例如來自 Recraft V4 Create Style 節點，或來自先前執行之 `style_id` 輸出。不能與 `style_references` 合併使用。 | STRING | 否 | N/A |
| `style_match` | 遵循風格的程度：`precise` 會詳細重現該風格，`flexible` 則符合整體外觀。僅在提供風格時使用（預設："precise"）。 | COMBO | 否 | `"precise"`<br>`"flexible"` |

### recraftv4_1_vector、recraftv4_1_utility_vector、recraftv4 與 recraftv4_styles_vector 輸入

這些模型共用相同的 `size` 選項。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成影像的尺寸。預設為 `"1024x1024"`。 | COMBO | 是 | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### recraftv4_1_pro_vector、recraftv4_1_utility_pro_vector、recraftv4_pro 與 recraftv4_styles_pro_vector 輸入

這些模型共用相同的 `size` 選項。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成影像的尺寸。預設為 `"2048x2048"`。 | COMBO | 是 | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

### 參考輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `style_references` | 用於即時建立向量風格的參考影像，會在生成費用之外另行計費。所建立的風格會以 `style_id` 回傳以供重複使用。不能與 `style_id` 合併使用。 | IMAGE | 否 | 可增長的插槽：連接 1..N 張參考影像（最多可達節點上限） |

**注意：** `size` 參數是動態輸入，其可用選項會根據所選的 `model` 變更。`seed` 值不保證能從外部 API 獲得可重現的結果。`recraftv4_styles_vector` 與 `recraftv4_styles_pro_vector` 模型一律需要風格：請提供 `style_id`，或連接至少一張 `style_references` 影像。`style_id` 與 `style_references` 不能一起使用——同時提供兩者會引發錯誤，且 `style_id` 必須是有效的 UUID。風格參考影像的數量有限，且其總編碼大小不得超過 10 MB。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的可縮放向量圖形（SVG）影像。 | SVG |
| `style_id` | Recraft API 回傳的風格 UUID。當提供參考影像時，所建立的風格會在此回傳以供重複使用；否則為空字串。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `182a40b206b164cf2e96c7344d23e4906b7d61b90e3000743a3fd31941e08539`
