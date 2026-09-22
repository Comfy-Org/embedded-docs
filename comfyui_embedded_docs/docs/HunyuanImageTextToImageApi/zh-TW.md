# Tencent HY Image: Text to Image

Tencent HY Image: Text to Image 節點會使用騰訊的 Hunyuan Image 模型，根據文字描述生成圖片。提示會傳送至 API，API 會在算繪前改寫並擴展提示，完成後的圖片會以圖片批次形式傳回。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於生成的模型。所選模型決定會顯示哪些額外輸入。 | DYNAMIC_COMBO | 是 | `"hy-image-3.5-preview"` |

### hy-image-3.5-preview 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成的圖片。模型會在算繪前改寫並擴展它。不得為空（預設：空）。 | STRING | 是 | 任意文字 |
| `aspect_ratio` | 輸出的長寬比。`"auto"` 讓模型根據提示挑選比例，且在 4K 時無法使用。當 `resolution` 為 `"custom"` 時忽略。 | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"`（預設：`"auto"`） |
| `resolution` | 圖片的像素面積：1K 約為 1024x1024，2K 約為 2048x2048，4K 約為 4096x4096。任何高於 2K 的內容會以 2K 算繪，並由模型放大。設為 `"custom"` 以使用 `width` 和 `height`，而非預設面積。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"`<br>`"custom"`（預設：`"2K"`） |
| `width` | 圖片的寬度，以像素為單位。僅當 `resolution` 為 `"custom"` 時使用。 | INT | 是 | 256-8192，間隔 16（預設：2048） |
| `height` | 圖片的高度，以像素為單位。僅當 `resolution` 為 `"custom"` 時使用。 | INT | 是 | 256-8192，間隔 16（預設：2048） |
| `seed` | 用於生成的種子。即使使用相同的 `seed`，不同次執行的結果仍會有所變化。 | INT | 是 | 0-2147483647（預設：42） |
| `watermark` | 是否在結果中加入 AI 生成的浮水印。這是進階參數。 | BOOLEAN | 否 | true<br>false（預設：false） |

`prompt` 不得為空。當 `resolution` 為 `"custom"` 時，`width` 和 `height` 都必須是 16 的倍數，且兩者的乘積不得超過 4096 x 4096 像素的面積限制（約 1670 萬像素）；任何長寬比皆可使用，不過超過約 6:1 後，模型會開始重複主體。`"auto"` 長寬比需要模型選擇尺寸，因此僅能在 2K 面積限制內運作：在 4K 時，請選擇明確的長寬比，或使用 `"custom"`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 生成的圖片。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageTextToImageApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1d4e70d688c5aa4e79b81447da559e201078454077da34769f2a4f544fbba63f`
