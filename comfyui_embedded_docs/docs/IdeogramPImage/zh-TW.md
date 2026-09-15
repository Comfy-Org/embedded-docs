# Ideogram & Pruna P-Image

Ideogram & Pruna P-Image 會使用 Ideogram 的快速文字轉圖像模型，根據文字提示生成影像；該模型以強大的文字排版與照片級真實感著稱。它也支援 Ideogram 4.0 結構化 JSON 描述，可精確控制文字字串、顏色與版面配置。此節點會傳回生成的影像，以及該影像實際生成時所使用的最終提示。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 文字提示。也接受 Ideogram 4.0 結構化 JSON 描述（以 #RRGGBB 十六進位值表示的精確顏色、精確文字字串、邊界框版面配置）——將 `prompt_upsampling` 設為 OFF 以逐字使用。不得為空。（預設值：""） | STRING | 是 | 任何非空文字 |
| `quality` | 速度/價格/品質等級。MEDIUM 是日常使用的預設值；HIGH 適用於複雜提示、精細細節與困難文字；VERY_LOW/LOW 適用於大規模草稿。困難文字在低於 MEDIUM 時渲染效果不佳。（預設值："MEDIUM"） | COMBO | 是 | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | 輸出尺寸等級（實際像素依長寬比而定，例如 16:9 在 1K 下為 1280x720，在 2K 下為 2560x1440）。若要有清晰銳利的文字排版，建議使用 HIGH + 2K。（預設值："1K"） | COMBO | 是 | "1K"<br>"2K" |
| `aspect_ratio` | 影像生成的長寬比。（預設值："1:1"） | COMBO | 是 | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | 在生成前將短提示擴展為詳細的結構化描述（改寫後的提示會以 `final_prompt` 傳回）。當你提供自己的 JSON 描述或精確用語時，請設為 OFF。（預設值："AUTO"） | COMBO | 是 | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | 用於可重現生成的種子。當 `prompt_upsampling` 為 OFF 時，相同種子與設定會傳回相同影像；當為 ON/AUTO 時，提示改寫每次執行會有所不同——若要重現某個結果，請以其 `final_prompt` 輸出搭配 `prompt_upsampling` OFF 及相同種子重新使用。（預設值：42） | INT | 否 | 0 至 2147483647 |

**限制條件備註：** `prompt` 必須包含至少一個非空白字元，否則此節點會失敗。當你提供自己的結構化 JSON 描述或精確用語時，請將 `prompt_upsampling` 設為 OFF。當 `prompt_upsampling` 為 ON 或 AUTO 時，提示會在生成前被改寫，因此相同種子可能無法重現相同影像；若要重現某張影像，請以其 `final_prompt` 輸出搭配 `prompt_upsampling` OFF 及相同種子重新使用。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 生成的影像，以一批影像的形式傳回。如果 Ideogram 的內容安全篩選器阻擋生成，則會改為拋出錯誤。 | IMAGE |
| `final_prompt` | 影像實際生成時所用的提示（當 `prompt_upsampling` 執行時，為改寫後的結構化描述；否則為你的提示）。將其搭配 `prompt_upsampling` OFF 及相同種子再次輸入，即可重現此影像。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6b014c2f097c49b5930f38869a4e2da0ebb19863763ae5817d6e566a36d2b8e8`
