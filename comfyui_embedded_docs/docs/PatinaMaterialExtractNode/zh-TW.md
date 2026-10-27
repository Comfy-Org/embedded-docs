# Patina Material Extract

從輸入影像的某個區域擷取可無縫拼接的 PBR 材質，並由提示詞指定要擷取的內容：牆面、地板或布料。它會傳回擷取出的基礎紋理，以及最多五張材質貼圖，並可選擇使用 SeedVR 對這些貼圖進行放大。可用來將真實表面的照片轉換成可重複使用、可拼接的材質。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要從中擷取紋理的影像。 | IMAGE | 是 | - |
| `prompt` | 描述要從影像中擷取哪種紋理，例如 `"the wall"`。 | STRING | 是 | 多行文字 |
| `image_size` | 輸出紋理尺寸。`"custom"` 會顯示 `width` 和 `height` 輸入。預設：`"1:1 (1024x1024)"`。 | DYNAMIC_COMBO | 是 | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | 產生 basecolor（albedo）貼圖。預設：True。 | BOOLEAN | 是 | true<br>false |
| `normal` | 產生法線貼圖。預設：True。 | BOOLEAN | 是 | true<br>false |
| `roughness` | 產生粗糙度貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `metalness` | 產生金屬度貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `height` | 產生高度（置換）貼圖。預設：False。 | BOOLEAN | 是 | true<br>false |
| `upscale_factor` | 對 PBR 貼圖進行無縫 SeedVR 放大。基礎紋理不會被放大；4x 會將 2048 像素的貼圖變成 8K 貼圖。預設：0（關閉）。 | INT | 是 | 0 至 4 （步進值：2） |
| `seed` | 用於可重現生成的種子。預設：42。 | INT | 是 | 0 至 2147483646 |
| `strength` | 輸入影像的轉換程度。進階設定。預設：0.6。 | FLOAT | 是 | 0.01 至 1.0 （步進值：0.01） |
| `tiling_mode` | 拼接方向：全方向、水平或垂直。進階設定。預設：`"both"`。 | COMBO | 是 | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | 紋理生成的去噪步數。進階設定。預設：8。 | INT | 是 | 1 至 8 |
| `tile_size` | 潛在空間中的圖磚尺寸；其中 64 表示 512 像素，128 表示 1024 像素。進階設定。預設：128。 | INT | 是 | 32 至 256 （步進值：2） |
| `tile_stride` | 潛在空間中的圖磚步幅。進階設定。預設：64。 | INT | 是 | 16 至 128 （步進值：2） |
| `prompt_expansion` | 使用語言模型擴展提示詞，以取得更豐富的紋理細節。預設關閉，因為擴展會將提示詞重新詮釋為照片，且往往會沖淡金屬度貼圖。進階設定。 | BOOLEAN | 是 | true<br>false |
| `safety_checker` | 對請求執行供應商的內容安全檢查。進階設定。預設：False。 | BOOLEAN | 是 | true<br>false |

### 自訂影像尺寸輸入

當 `image_size` 設為 `"custom"` 時，會出現這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | 紋理寬度（像素）。預設：1024。 | INT | 是 | 512 至 2048 （步進值：16） |
| `image_size.height` | 紋理高度（像素）。預設：1024。 | INT | 是 | 512 至 2048 （步進值：16） |

**限制與行為：**

* 允許不啟用任何材質貼圖：此時節點只會傳回基礎紋理，且每個貼圖輸出都會保持為 1x1 的預留位置。
* 提示詞為必填且不得為空；請盡可能精確地指出要擷取的區域。
* 8K 結果是將 2048 像素渲染結果的貼圖放大 4x 而得，並非來自單次 8K 生成。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `texture` | 擷取出的基礎紋理，未套用任何貼圖。 | IMAGE |
| `basecolor` | basecolor（albedo）貼圖；當該貼圖停用時，則為 1x1 預留位置。 | IMAGE |
| `normal` | 法線貼圖；當該貼圖停用時，則為 1x1 預留位置。 | IMAGE |
| `roughness` | 粗糙度貼圖；當該貼圖停用時，則為 1x1 預留位置。 | IMAGE |
| `metalness` | 金屬度貼圖；當該貼圖停用時，則為 1x1 預留位置。 | IMAGE |
| `height` | 高度（置換）貼圖；當該貼圖停用時，則為 1x1 預留位置。 | IMAGE |
| `expanded_prompt` | 供應商實際使用的提示詞；只有在啟用 `prompt_expansion` 時，才會與輸入不同。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialExtractNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `484b8eaa57388541e352cd88c8998c63aa0b2a99d98cd8e602252625064f16ba`
