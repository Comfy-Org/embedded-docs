# IdeogramPImage

Ideogram P-Image 使用 Ideogram 快速文字轉圖像模型，根據文字提示生成圖像，該模型以卓越的文字排版與照片級真實感聞名。它也支援 Ideogram 4.0 結構化 JSON 說明文字，可精確控制文字字串、顏色和版面配置。此節點會傳回生成的圖像，以及實際用於生成該圖像的最終提示。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 文字提示。也可接受 Ideogram 4.0 結構化 JSON 說明文字（精確顏色以 #RRGGBB 十六進位表示、精確文字字串、邊界框版面配置）— 將 `prompt_upsampling` 設為 OFF 以原樣使用。不可為空。（預設：""） | STRING | 是 | 任何文字 |
| `quality` | 速度/價格/品質等級。MEDIUM 是日常預設；HIGH 適用於複雜提示、精細細節和困難文字；VERY_LOW/LOW 適用於大量草稿。低於 MEDIUM 時，困難文字會呈現不佳。（預設："MEDIUM"） | STRING | 是 | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | 輸出尺寸等級（精確像素取決於長寬比，例如 16:9 在 1K 下為 1280x720，在 2K 下為 2560x1440）。如需清晰的文字排版，建議使用 HIGH 品質與 2K 解析度。（預設："1K"） | STRING | 是 | "1K"<br>"2K" |
| `aspect_ratio` | 圖像生成的長寬比。（預設："1:1"） | STRING | 是 | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | 在生成前將簡短提示擴展為詳細的結構化說明文字（改寫後的提示會作為 `final_prompt` 傳回）。當您提供自己的 JSON 說明文字或精確措辭時，請設為 OFF。（預設："AUTO"） | STRING | 是 | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | 用於可重現生成的種子。當 `prompt_upsampling` 為 OFF 時，相同的種子與設定會傳回相同的圖像；當為 ON/AUTO 時，提示改寫會因每次執行而異— 若要重現結果，請將其 `final_prompt` 輸出與 `prompt_upsampling` 設為 OFF 及相同種子一起重用。（預設：42） | INT | 否 | 0 到 2147483647 |

**關於限制的說明：** 提示必須包含至少一個非空白字元，否則節點將失敗。當您提供自己的結構化 JSON 說明文字或精確措辭時，請將 `prompt_upsampling` 設為 OFF。當 `prompt_upsampling` 為 ON 或 AUTO 時，提示會在生成前被改寫，因此相同的種子可能無法重現相同的圖像；若要重現圖像，請將其 `final_prompt` 輸出與 `prompt_upsampling` 設為 OFF 及相同種子一起重用。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 生成的圖像，以圖像批次形式傳回。如果 Ideogram 的內容安全篩選器阻擋了生成，則改為引發錯誤。 | IMAGE |
| `final_prompt` | 實際用於生成圖像的提示（當 `prompt_upsampling` 執行時為改寫後的結構化說明文字，否則為您的提示）。將其與 `prompt_upsampling` OFF 及相同種子一起回饋，即可重現此圖像。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7bd20aae508fee111ded32e87119ed6fc01c5ad5ba7d595e24391830a0f20bb7`
