# Patina Material

從文字描述生成完整、可無縫平鋪的 PBR 材質：包含基礎貼圖，以及最多五張材質貼圖，並可選擇使用 SeedVR 對貼圖進行放大。輸入影像可作為 image-to-image 傳遞來驅動結果，而帶有遮罩的輸入影像則會使其轉為 inpaint 傳遞。可用於製作可直接用於遊戲或 3D 的表面，無需掃描真實材質。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 要生成的材質或貼圖描述。 | STRING | 是 | 多行文字 |
| `image_size` | 輸出貼圖尺寸。`"custom"` 會顯示 `width` 與 `height` 輸入。預設：`"1:1 (1024x1024)"`。 | DYNAMIC_COMBO | 是 | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | 生成 basecolor（albedo）貼圖。預設：True。 | BOOLEAN | 是 | true<br>false |
| `normal` | 生成 normal 貼圖。預設：True。 | BOOLEAN | 是 | true<br>false |
| `roughness` | 生成 roughness 貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `metalness` | 生成 metalness 貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `height` | 生成 height（displacement）貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `upscale_factor` | 對 PBR 貼圖進行無縫 SeedVR 放大。基礎貼圖不會被放大，4x 會將 2048 像素的貼圖放大為 8K。預設：0（關閉）。 | INT | 是 | 0 至 4（步長 2） |
| `seed` | 用於可重現生成的種子。預設：42。 | INT | 是 | 0 至 2147483646 |
| `tiling_mode` | 平鋪方向：全方位、水平或垂直。進階設定。預設：`"both"`。 | COMBO | 是 | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | 貼圖生成的去噪步數。進階設定。預設：8。 | INT | 是 | 1 至 8 |
| `tile_size` | 潛空間中的圖塊大小，其中 64 表示 512 像素，128 表示 1024 像素。進階設定。預設：128。 | INT | 是 | 32 至 256（步長 2） |
| `tile_stride` | 潛空間中的圖塊步幅。進階設定。預設：64。 | INT | 是 | 16 至 128（步長 2） |
| `image` | 可選的來源影像。單獨使用時會執行 image-to-image；與遮罩一起使用時則執行 inpaint 傳遞。 | IMAGE | 否 | - |
| `mask` | 可選的 inpaint 遮罩，需要輸入影像。白色區域會被重新生成，黑色區域會被保留。 | MASK | 否 | - |
| `strength` | 對輸入影像的轉換程度。僅在連接影像時使用。進階設定。預設：0.6。 | FLOAT | 是 | 0.01 至 1.0（步長 0.01） |
| `prompt_expansion` | 使用語言模型擴展提示詞，以獲得更豐富的貼圖細節。預設為關閉，因為擴展會將提示詞重新框架為照片，並往往會沖淡 metalness 貼圖。進階設定。 | BOOLEAN | 是 | true<br>false |
| `safety_checker` | 對請求執行供應商的內容安全檢查。進階設定。預設：False。 | BOOLEAN | 是 | true<br>false |

### 自訂影像尺寸輸入

當 `image_size` 設為 `"custom"` 時，這些輸入會顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | 貼圖寬度（像素）。預設：1024。 | INT | 是 | 512 至 2048（步長 16） |
| `image_size.height` | 貼圖高度（像素）。預設：1024。 | INT | 是 | 512 至 2048（步長 16） |

**限制與行為：**

* 允許不啟用任何材質貼圖：此時節點僅回傳基礎貼圖，而每個貼圖輸出都會保持為 1x1 佔位符。
* 遮罩需要輸入影像；單獨使用遮罩會引發錯誤。
* 8K 結果來自對 2048 像素渲染的貼圖進行 4x 放大，而非來自單次 8K 生成。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `texture` | 材質的基礎貼圖，未套用任何貼圖。 | IMAGE |
| `basecolor` | basecolor（albedo）貼圖，或當該貼圖停用時的 1x1 佔位符。 | IMAGE |
| `normal` | normal 貼圖，或當該貼圖停用時的 1x1 佔位符。 | IMAGE |
| `roughness` | roughness 貼圖，或當該貼圖停用時的 1x1 佔位符。 | IMAGE |
| `metalness` | metalness 貼圖，或當該貼圖停用時的 1x1 佔位符。 | IMAGE |
| `height` | height（displacement）貼圖，或當該貼圖停用時的 1x1 佔位符。 | IMAGE |
| `expanded_prompt` | 供應商實際使用的提示詞，僅在啟用 `prompt_expansion` 時才會與輸入不同。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4e8305fa56a29dce72c54de12ae05207e8de39a1fea1f4753906c26e8af60383`
