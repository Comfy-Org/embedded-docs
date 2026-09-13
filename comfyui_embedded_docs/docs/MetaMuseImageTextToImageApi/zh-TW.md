# Meta Muse 圖片文字轉圖片

Meta Muse Image Text to Image 會使用 Meta 的 Muse Image 模型，根據文字提示生成圖像。此模型會在渲染前對提示進行推理，並可在規劃圖像時使用網頁搜尋、圖像搜尋與程式碼執行。此節點會呼叫 Muse Image API，並回傳生成的圖像（可能為單張或多張）。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要使用的模型。 | DYNAMIC_COMBO | 是 | `"muse-image-1.0"` |

在清單中選擇模型後，會顯示該模型支援的設定。目前唯一可用的模型是 `muse-image-1.0`；其設定如下所列。

### muse-image-1.0 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述圖像的提示。模型會在渲染前對提示進行推理，並可能使用其內建的網頁與圖像搜尋。 | STRING | 是 | 多行文字，最少 1 個字元 |
| `aspect_ratio` | 輸出的長寬比。圖像約以 2.5 百萬像素渲染（1:1 為 1600x1600，16:9 為 2048x1152）；`"auto"` 會讓模型根據提示選擇。 | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"5:4"`<br>`"4:5"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"`<br>`"2:1"`<br>`"1:2"` |
| `reasoning_strength` | 模型在渲染前進行思考、規劃與自我修正的程度。 | COMBO | 是 | `"high"`<br>`"low"` |
| `enable_web_search` | 允許模型在規劃圖像時搜尋網頁，以取得事實與即時資訊。 | BOOLEAN | 否 | True<br>False (預設：True) |
| `enable_image_search` | 允許模型在規劃圖像時搜尋參考圖像。 | BOOLEAN | 否 | True<br>False (預設：True) |
| `enable_shell` | 允許模型在規劃時執行程式碼，以精確配置版面、圖表與圖解；關閉時，數量與對齊會以近似方式處理。 | BOOLEAN | 否 | True<br>False (預設：True) |
| `seed` | 用來決定節點是否應重新執行的種子；API 沒有種子，因此無論此值為何，實際結果都是非確定性的。 | INT | 是 | 0 – 2147483647 (預設：42) |

注意：`prompt` 必須至少包含一個字元。當 `aspect_ratio` 設為 `"auto"` 時，不會將明確尺寸傳送給 API，模型會根據提示決定輸出尺寸。`seed` 參數僅控制節點何時重新執行；它不會傳送給 API，因此生成的結果是非確定性的。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | API 回傳的生成圖像，經解碼後以批次圖像形式提供。如果 API 回應包含多張圖像，會將它們合併為一個批次。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageTextToImageApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `59ebd72fab3db44a35ceac723606de4eabb5fe2b690d0b701db50e0e22a9e699`
