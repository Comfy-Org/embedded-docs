# Patina Material

產生完整且可無縫平鋪的 PBR 材質，內容包含基礎貼圖加上最多五張材質貼圖，並可選擇使用 SeedVR 對貼圖進行放大。輸入影像可作為圖生圖（image-to-image）流程來驅動結果，而帶有遮罩的輸入影像則會使其變成內補（inpaint）流程。使用此節點即可製作可直接用於遊戲或 3D 的表面，無需掃描真實材質。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 要生成之材質或貼圖的描述。 | STRING | 是 | Multiline text |
| `image_size` | 輸出貼圖尺寸。設定為 `"custom"` 時會顯示 `width` 與 `height` 輸入。預設：`"1:1 (1024x1024)"`。 | DYNAMIC_COMBO | 是 | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | 生成 basecolor（albedo）貼圖。預設：True。 | BOOLEAN | 是 | true<br>false |
| `normal` | 生成 normal 貼圖。預設：True。 | BOOLEAN | 是 | true<br>false |
| `roughness` | 生成 roughness 貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `metalness` | 生成 metalness 貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `height` | 生成 height（displacement）貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `upscale_factor` | 對 PBR 貼圖進行無縫 SeedVR 放大。基礎貼圖不會被放大，4x 會將 2048 像素的貼圖放大為 8K。預設：0（關閉）。 | INT | 是 | 0 至 4 （步進值：2） |
| `seed` | 用於可重現生成的隨機種子。預設：42。 | INT | 是 | 0 至 2147483646 |
| `tiling_mode` | 平鋪方向：全方位、水平或垂直。進階設定。預設：`"both"`。 | COMBO | 是 | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | 用於貼圖生成的去雜訊步數。進階設定。預設：8。 | INT | 是 | 1 至 8 |
| `tile_size` | 潛空間中的圖塊大小，其中 64 代表 512 像素，128 代表 1024 像素。進階設定。預設：128。 | INT | 是 | 32 至 256 （步進值：2） |
| `tile_stride` | 潛空間中的圖塊步幅。進階設定。預設：64。 | INT | 是 | 16 至 128 （步進值：2） |
| `image` | 選用的來源影像。單獨使用時會執行圖生圖；與遮罩一起使用時會執行內補流程。 | IMAGE | 否 | - |
| `mask` | 選用的內補遮罩，需搭配輸入影像。白色區域會重新生成，黑色區域則會保留。 | MASK | 否 | - |
| `strength` | 輸入影像的轉換程度。僅在連接影像時使用。進階設定。預設：0.6。 | FLOAT | 是 | 0.01 至 1.0 （步進值：0.01） |
| `prompt_expansion` | 使用語言模型擴展提示詞，以獲得更豐富的貼圖細節。預設關閉，因為擴展會將提示詞重新詮釋為照片，且往往會使 metalness 貼圖變得平淡。進階設定。 | BOOLEAN | 是 | true<br>false |
| `safety_checker` | 對請求執行供應商的內容安全檢查。進階設定。預設：False。 | BOOLEAN | 是 | true<br>false |

### custom 影像尺寸輸入

當 `image_size` 設為 `"custom"` 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | 貼圖寬度（像素）。預設：1024。 | INT | 是 | 512 至 2048 （步進值：16） |
| `image_size.height` | 貼圖高度（像素）。預設：1024。 | INT | 是 | 512 至 2048 （步進值：16） |

**限制與行為：**

* 必須至少啟用一張材質貼圖，否則執行會失敗。
* 遮罩需要搭配輸入影像；單獨提供遮罩會引發錯誤。
* 8K 結果是將 2048 像素渲染的貼圖放大 4x 而得，並非來自單次 8K 生成。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `texture` | 材質的基礎貼圖，未套用任何材質貼圖。 | IMAGE |
| `basecolor` | basecolor（albedo）貼圖；若停用該貼圖，則為 1x1 的佔位影像。 | IMAGE |
| `normal` | normal 貼圖；若停用該貼圖，則為 1x1 的佔位影像。 | IMAGE |
| `roughness` | roughness 貼圖；若停用該貼圖，則為 1x1 的佔位影像。 | IMAGE |
| `metalness` | metalness 貼圖；若停用該貼圖，則為 1x1 的佔位影像。 | IMAGE |
| `height` | height（displacement）貼圖；若停用該貼圖，則為 1x1 的佔位影像。 | IMAGE |
| `expanded_prompt` | 供應商實際使用的提示詞；僅在啟用 `prompt_expansion` 時才會與輸入不同。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4e8305fa56a29dce72c54de12ae05207e8de39a1fea1f4753906c26e8af60383`
