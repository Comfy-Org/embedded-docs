# Ideogram P-Image

Ideogram & Pruna P-Image 使用 Ideogram 的快速文字轉影像模型，根據文字提示詞生成影像。該模型以卓越的文字排版和寫實照片感著稱。它也支援 Ideogram 4.0 結構化 JSON 描述，可精確控制文字字串、顏色和佈局。此節點會回傳生成的影像，以及實際用於生成該影像的最終提示詞。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 文字提示詞。也可接受 Ideogram 4.0 結構化 JSON 描述（精確的 #RRGGBB 十六進位顏色、精確的文字字串、邊界框佈局）— 設定 `prompt_upsampling` 為 OFF 以原樣使用。不可為空。（預設：""） | STRING | 是 | Any non-empty text |
| `quality` | 速度／價格／品質等級。MEDIUM 是日常使用的預設值；HIGH 適用於複雜提示詞、精細細節和困難文字；VERY_LOW/LOW 適用於大規模草稿。低於 MEDIUM 時，困難文字的渲染效果會較差。（預設："MEDIUM"） | COMBO | 是 | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | 輸出尺寸等級（確切像素取決於長寬比，例如 16:9 在 1K 下為 1280x720，在 2K 下為 2560x1440）。若要獲得清晰銳利的文字排版，建議使用 HIGH + 2K。（預設："1K"） | COMBO | 是 | "1K"<br>"2K" |
| `aspect_ratio` | 影像生成的長寬比。（預設："1:1"） | COMBO | 是 | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | 在生成前將短提示詞擴充為詳細的結構化描述（改寫後的提示詞會以 `final_prompt` 回傳）。當您提供自己的 JSON 描述或精確措辭時，請設為 OFF。（預設："AUTO"） | COMBO | 是 | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | 用於可重現生成的種子。當 `prompt_upsampling` 為 OFF 時，相同的種子與設定會回傳相同的影像；當為 ON/AUTO 時，每次執行的提示詞改寫都會不同 — 若要重現結果，請將其 `final_prompt` 輸出與 `prompt_upsampling` 設為 OFF 並使用相同的種子。（預設：42） | INT | No | 0 至 2147483647 |

**限制說明：** 提示詞必須至少包含一個非空白字元，否則節點會失敗。當您提供自己的結構化 JSON 描述或精確措辭時，請將 `prompt_upsampling` 設為 OFF。當 `prompt_upsampling` 為 ON 或 AUTO 時，提示詞會在生成前被改寫，因此相同的種子可能無法重現相同的影像；若要重現影像，請將其 `final_prompt` 輸出與 `prompt_upsampling` 設為 OFF 並搭配相同的種子。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 生成的影像，以影像批次的形式回傳。如果 Ideogram 的內容安全過濾器阻擋了生成，則會改為引發錯誤。 | IMAGE |
| `final_prompt` | 實際用於生成影像的提示詞（當 `prompt_upsampling` 執行時的改寫後結構化描述，否則為您提供的提示詞）。將它與 `prompt_upsampling` 設為 OFF 及相同的種子一起輸入，即可重現此影像。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6b014c2f097c49b5930f38869a4e2da0ebb19863763ae5817d6e566a36d2b8e8`
