# UltraTex Conditioning

使用 UltraTex LoRA 對 FLUX.2 Klein 9B 進行條件化，將參考影像的外觀繪製到網格上，每個視圖一張影像。使用 Render Mesh 以 `world normal` 模式渲染這些視圖，視圖由 Create Camera Orbit 的 4 個視圖加上頂部與底部產生，然後使用 Bake Texture From Views 烘焙結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `conditioning` | 文字條件。UltraTex 是以空提示詞訓練的。 | CONDITIONING | 是 | - |
| `vae` | 用於編碼法線、視圖和參考的 VAE。 | VAE | 是 | - |
| `normals` | Render Mesh `world normal` 影像：6 個標準視圖，或 4 個側面視圖。 | IMAGE | 是 | - |
| `masks` | 相同視圖的 Render Mesh 遮罩，每個視圖一個。 | MASK | 是 | - |
| `reference` | 物件應呈現的外觀，從前方相機側所見。 | IMAGE | 是 | - |
| `reference_mask` | 參考的物件遮罩，物件部分為白色。預設：全白。 | MASK | 否 | - |
| `extra_views` | 更多參考：從其他視圖看到的物件，每個都與其視圖綁定，就像參考與前方綁定一樣。預設：`"off"`。 | DYNAMIC_COMBO | 是 | `"off"`<br>`"on"` |

### 額外視圖「on」輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `right` | 從右側視圖看到的物件。 | IMAGE | 否 | - |
| `back` | 從後側視圖看到的物件。 | IMAGE | 否 | - |
| `left` | 從左側視圖看到的物件。 | IMAGE | 否 | - |
| `top` | 從頂部視圖看到的物件。 | IMAGE | 否 | - |
| `bottom` | 從底部視圖看到的物件。 | IMAGE | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 攜帶視圖網格、參考潛在表示，以及 UltraTex 所需的 token 遮罩的條件。 | CONDITIONING |

注意：`normals` 必須包含 6 個標準視圖（Create Camera Orbit 的 `count` 為 4，且 `poles` 為頂部和底部）或 4 個側面視圖，而 `masks` 的數量必須與視圖數量相符。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UltraTexConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5b05f5151d4c12394ef893db69538adaef86e9cbdbb118a37c20919758520b6f`
