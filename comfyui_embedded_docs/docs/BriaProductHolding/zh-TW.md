# Bria Product Holding

此節點透過 Bria 將產品放到人物手中。人物的身分、姿勢與背景會保持不變，而場景會以約 1 百萬像素重新渲染，因此結果不會與輸入照片逐像素對齊。所有產品影像描述的都是同一件產品在不同角度或不同階段的樣貌。

## 輸入

當 `moderation` 選擇器設為 `"true"` 時，會顯示額外的審核選項。

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `person_image` | 手持產品的人物照片。影像上傳前會先移除 alpha 通道。 | IMAGE | 是 | - |
| `product_images` | 同一件產品的 1 至 3 張影像：產品本身、其包裝、另一個角度或搭配物件。批次輸入時每張影像各計一次，透明區域會被視為白色。 | AUTOGROW | 是 | 1 至 3 張圖像 |
| `instruction` | 選填的額外指示，會附加到 Bria 的內建指示中，例如使用哪隻手或標籤朝向哪一邊。預設值：`""`（空字串）。 | STRING | 是 | - |
| `aspect_ratio` | `"auto"` 會保持人物照片的取景，約 1 百萬像素。固定比例會回傳 0.6 至 1 百萬像素，例如 `"3:4"` 為 768x1024。預設值：`"auto"`。 | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"` |
| `seed` | 隨請求傳送給 Bria 的種子。預設值：42。 | INT | 是 | 1 至 2147483647 |
| `moderation` | 審核設定。設為 `"true"` 時，下方的審核旗標才會可用。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |

### Moderation "true" 輸入

此參數僅在 `moderation` 設為 `"true"` 時才會出現。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `visual_output_moderation` | 啟用對生成影像的內容審核。預設值：`False`。 | BOOLEAN | 否 | True / False |

**限制條件：**

* `product_images` 最多接受 3 張影像，當輸入為批次時會依每張影像分別計數。
* 產品影像中的透明像素會在上傳前合成到白色背景上。
* `person_image` 的 alpha 通道會在上傳前移除。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 已編輯的照片，產品已置於人物手中。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaProductHolding/zh-TW.md)

---
**Source fingerprint (SHA-256):** `91a4a4dde0e9d7fe2480130da87edf1f8ed9d4ae0c86f8a8d030c36987dcdb8e`
