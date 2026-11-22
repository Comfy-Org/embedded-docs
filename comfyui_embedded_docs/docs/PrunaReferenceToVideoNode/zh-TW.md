# Pruna P-Video-2 Pro Reference to Video

使用 Pruna P-Video-2 Pro Reference to Video，根據提示詞並以參考影像、影片和音訊為引導來生成影片。在提示詞中以編號指涉每個參考，模型會將其主體、風格或動態帶入結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要使用的 Pruna 影片模型。選擇模型後，下方會顯示其輸入。 | DYNAMIC_COMBO | 是 | `"p-video-2-pro-reference"` |

### P-Video-2 Pro Reference 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.images` | 可擴充的參考影像插槽（`image_1`、`image_2`、...），在提示詞中依連接順序以 `@Image1` 至 `@Image9` 指涉。最多 9 張影像，包含第一幀與最後一幀。 | AUTOGROW | 否 | 0 至 9 張影像 |
| `model.videos` | 可擴充的參考影片插槽（`video_1`、`video_2`、...），以 `@Video1` 至 `@Video3` 指涉。每段 2 至 15 秒，最高 60 fps，總計 15 秒。1080p 以上的影片會降採樣。 | AUTOGROW | 否 | 0 至 3 段影片 |
| `model.audios` | 可擴充的參考音訊插槽（`audio_1`、`audio_2`、...），以 `@Audio1` 至 `@Audio3` 指涉。總計最多 15 秒。 | AUTOGROW | 否 | 0 至 3 段音訊 |
| `提示詞` | 描述影片。以 `@Image1`、`@Video1` 或 `@Audio1` 指涉參考（預設：空）。最多 5000 個字元。 | STRING | 是 | 1 至 5000 個字元 |
| `model.first_frame` | 影片起始的影像。計入 9 張影像的限制。 | IMAGE | 否 | - |
| `model.last_frame` | 影片結束的影像。計入 9 張影像的限制。 | IMAGE | 否 | - |
| `keep_audio` | 將連接的音訊作為配樂，並生成與其相符的影片（預設：False）。需要正好一個音訊：較短音訊後會接上生成的聲音，較長音訊則會裁切至影片長度。 | BOOLEAN | 是 | `True`<br>`False` |
| `時長` | 影片長度，以秒為單位（預設：`"5"`）。 | COMBO | 是 | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"` |
| `解析度` | 輸出解析度（預設：`"768p"`）。1080p、2k 與 4k 會將生成的 768p 影片進行升頻。 | COMBO | 是 | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `模式` | `"cost"` 較便宜，`"speed"` 渲染較快（預設：`"speed"`）。 | COMBO | 是 | `"cost"`<br>`"speed"` |
| `aspect_ratio` | 輸出影片的長寬比（預設：`"16:9"`）。`"adaptive"` 會使用參考中最常見的比例；若開啟 `enhance_prompt`，則改由改寫後的提示詞選擇比例。 | COMBO | 是 | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `enhance_prompt` | 生成前以更多細節改寫提示詞；`"max"` 較慢（預設：`"turbo"`）。當提示詞以編號指涉參考時請保持開啟；第一幀或最後一幀一律使用 `"turbo"`。進階設定。 | COMBO | 是 | `"off"`<br>`"turbo"`<br>`"max"` |
| `seed` | 生成用的種子值（預設：42）。只有在 `model.enhance_prompt` 關閉時，相同種子值才能完全重現結果。 | INT | 是 | 0 至 2147483647<br>步進值：1 |

**備註：**

- 至少連接一個參考影像、影片、第一幀或最後幀，否則節點會停止並顯示錯誤。
- 最多允許 9 張影像（包含第一幀與最後幀），且影像、幀、影片與音訊合計最多 12 個參考。
- 參考影片與參考音訊各自總計上限為 15 秒，且每段參考影片長度必須為 2 至 15 秒，最高 60 fps。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `video` | 生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaReferenceToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d6e295b394984c924386ea6432532c7653b4512c646b1f86793be9b98583eef3`
