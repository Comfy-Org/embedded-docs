# Patina Material Extract

從輸入影像的某個區域擷取可無縫平鋪的 PBR 材質，並由提示詞指引要取用的內容：牆面、地板或布料。它會回傳擷取出的基礎材質，以及最多五張材質貼圖，並可選擇使用 SeedVR 對貼圖進行放大。可用來將真實表面的照片轉換成可重複使用、可平鋪的材質。

## 輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image` | 要從中擷取材質的影像。 | IMAGE | 是 | - |
| `prompt` | 描述要從影像中擷取哪一種材質，例如 `"the wall"`。 | STRING | 是 | Multiline text |
| `image_size` | 輸出材質尺寸。設定為 `"custom"` 時會顯示 `width` 與 `height` 輸入。預設：`"1:1 (1024x1024)"`。 | DYNAMIC_COMBO | 是 | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | 產生 basecolor（albedo）貼圖。預設：True。 | BOOLEAN | 是 | true<br>false |
| `normal` | 產生 normal 貼圖。預設：True。 | BOOLEAN | 是 | true<br>false |
| `roughness` | 產生 roughness 貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `metalness` | 產生 metalness 貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `height` | 產生 height（displacement）貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `upscale_factor` | 對 PBR 貼圖進行無縫 SeedVR 放大。基礎材質不會被放大，而 4x 會將 2048 像素的貼圖放大成 8K。預設：0（關閉）。 | INT | 是 | 0 至 4 （步進值：2） |
| `seed` | 用於可重現生成的隨機種子。預設：42。 | INT | 是 | 0 至 2147483646 |
| `strength` | 對輸入影像的轉換程度。進階設定。預設：0.6。 | FLOAT | 是 | 0.01 至 1.0 （步進值：0.01） |
| `tiling_mode` | 平鋪方向：全方向、水平或垂直。進階設定。預設：`"both"`。 | COMBO | 是 | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | 材質生成的去噪步數。進階設定。預設：8。 | INT | 是 | 1 至 8 |
| `tile_size` | 潛空間中的貼圖區塊大小，其中 64 代表 512 像素、128 代表 1024 像素。進階設定。預設：128。 | INT | 是 | 32 至 256 （步進值：2） |
| `tile_stride` | 潛空間中的貼圖區塊步幅。進階設定。預設：64。 | INT | 是 | 16 至 128 （步進值：2） |
| `prompt_expansion` | 使用語言模型擴展提示詞，以獲得更豐富的材質細節。預設為關閉，因為擴展會將提示詞改寫成照片描述，容易使 metalness 貼圖變得模糊失真。進階設定。 | BOOLEAN | 是 | true<br>false |
| `safety_checker` | 對請求執行供應商的內容安全檢查。進階設定。預設：False。 | BOOLEAN | 是 | true<br>false |

### custom 影像尺寸輸入

當 `image_size` 設為 `"custom"` 時，會出現這些輸入。

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | 材質寬度（像素）。預設：1024。 | INT | 是 | 512 至 2048 （步進值：16） |
| `image_size.height` | 材質高度（像素）。預設：1024。 | INT | 是 | 512 至 2048 （步進值：16） |

**限制與行為：**

* 至少要啟用一張材質貼圖，否則執行會失敗。
* 提示詞為必填且不可為空；請盡可能精確地指出要擷取的區域。
* 8K 結果來自對 2048 像素渲染結果的貼圖進行 4 倍放大，而非單次 8K 生成。

## 輸出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `texture` | 擷取出的基礎材質，未套用任何貼圖。 | IMAGE |
| `basecolor` | basecolor（albedo）貼圖；若該貼圖已停用，則為 1x1 的佔位影像。 | IMAGE |
| `normal` | normal 貼圖；若該貼圖已停用，則為 1x1 的佔位影像。 | IMAGE |
| `roughness` | roughness 貼圖；若該貼圖已停用，則為 1x1 的佔位影像。 | IMAGE |
| `metalness` | metalness 貼圖；若該貼圖已停用，則為 1x1 的佔位影像。 | IMAGE |
| `height` | height（displacement）貼圖；若該貼圖已停用，則為 1x1 的佔位影像。 | IMAGE |
| `expanded_prompt` | 供應商實際使用的提示詞；僅在啟用 `prompt_expansion` 時才會與輸入不同。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialExtractNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `484b8eaa57388541e352cd88c8998c63aa0b2a99d98cd8e602252625064f16ba`
