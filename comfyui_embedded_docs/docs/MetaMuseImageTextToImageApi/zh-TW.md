# MetaMuseImageTextToImageApi

Meta Muse Image Text to Image 會使用 Meta 的 Muse Image 模型，根據文字提示產生影像。模型在渲染前會先對提示進行推理，並在規劃影像時可使用網路搜尋、影像搜尋及程式碼執行。此節點會呼叫 Muse Image API，並傳回產生的單張或多張影像。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 是否必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要使用的模型。 | DYNAMIC_COMBO | 是 | `"muse-image-1.0"` |

在清單中選取模型會顯示該模型支援的設定。唯一可用的模型是 `muse-image-1.0`；其設定如下所示。

### muse-image-1.0 輸入

| 參數 | 說明 | 資料類型 | 是否必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述影像的提示。模型在渲染前會推理此提示，並可能使用其內建的網路與影像搜尋功能。 | STRING | 是 | 多行文字，至少 1 個字元 |
| `aspect_ratio` | 輸出的長寬比。影像以約 2.5 百萬像素渲染（1:1 為 1600x1600，16:9 為 2048x1152）；「auto」會讓模型根據提示自行選擇。 | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"5:4"`<br>`"4:5"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"`<br>`"2:1"`<br>`"1:2"` |
| `reasoning_strength` | 模型在渲染前思考、規劃及自我改進的程度。 | COMBO | 是 | `"high"`<br>`"low"` |
| `enable_web_search` | 讓模型在規劃影像時，於網路上搜尋事實和即時資訊。 | BOOLEAN | 否 | True<br>False（預設：True） |
| `enable_image_search` | 讓模型在規劃影像時搜尋參考影像。 | BOOLEAN | 否 | True<br>False（預設：True） |
| `enable_shell` | 讓模型在規劃時執行程式碼，以獲得精確的版面、圖表與示意圖；關閉時，數量與對齊方式會以近似方式處理。 | BOOLEAN | 否 | True<br>False（預設：True） |
| `seed` | 用來決定節點是否重新執行的種子；API 沒有種子概念，因此無論此值為何，實際結果皆為非確定性。 | INT | 是 | 0 – 2147483647（預設：42） |

注意：提示必須至少包含一個字元。當 `aspect_ratio` 設為 "auto" 時，不會傳送明確的尺寸給 API，模型會根據提示決定輸出尺寸。`seed` 參數僅控制節點何時重新執行；它不會傳送給 API，因此產生的結果是非確定性的。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | API 傳回的已生成影像，經解碼後以批次影像形式提供。如果 API 回應包含多張影像，則會合併為一個批次。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageTextToImageApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `59ebd72fab3db44a35ceac723606de4eabb5fe2b690d0b701db50e0e22a9e699`
