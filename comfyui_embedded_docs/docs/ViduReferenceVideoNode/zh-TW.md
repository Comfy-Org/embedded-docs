> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/zh-TW.md)

Vidu 參考影片節點可根據多個參考圖片和文字提示生成影片。它使用 AI 模型，基於提供的圖片和描述來創建一致的影片內容。此節點支援多種影片設定，包括持續時間、長寬比、解析度和動態控制。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"vidu_q1"`<br>`"vidu_q2"`<br>`"vidu_q3"`<br>`"vidu_q4"`<br>`"vidu_q5"`<br>`"vidu_q6"`<br>`"vidu_q7"`<br>`"vidu_q8"`<br>`"vidu_q9"`<br>`"vidu_q10"`<br>`"vidu_q11"`<br>`"vidu_q12"`<br>`"vidu_q13"`<br>`"vidu_q14"`<br>`"vidu_q15"`<br>`"vidu_q16"`<br>`"vidu_q17"`<br>`"vidu_q18"`<br>`"vidu_q19"`<br>`"vidu_q20"`<br>`"vidu_q21"`<br>`"vidu_q22"`<br>`"vidu_q23"`<br>`"vidu_q24"`<br>`"vidu_q25"`<br>`"vidu_q26"`<br>`"vidu_q27"`<br>`"vidu_q28"`<br>`"vidu_q29"`<br>`"vidu_q30"`<br>`"vidu_q31"`<br>`"vidu_q32"`<br>`"vidu_q33"`<br>`"vidu_q34"`<br>`"vidu_q35"`<br>`"vidu_q36"`<br>`"vidu_q37"`<br>`"vidu_q38"`<br>`"vidu_q39"`<br>`"vidu_q40"`<br>`"vidu_q41"`<br>`"vidu_q42"`<br>`"vidu_q43"`<br>`"vidu_q44"`<br>`"vidu_q45"`<br>`"vidu_q46"`<br>`"vidu_q47"`<br>`"vidu_q48"`<br>`"vidu_q49"`<br>`"vidu_q50"`<br>`"vidu_q51"`<br>`"vidu_q52"`<br>`"vidu_q53"`<br>`"vidu_q54"`<br>`"vidu_q55"`<br>`"vidu_q56"`<br>`"vidu_q57"`<br>`"vidu_q58"`<br>`"vidu_q59"`<br>`"vidu_q60"`<br>`"vidu_q61"`<br>`"vidu_q62"`<br>`"vidu_q63"`<br>`"vidu_q64"`<br>`"vidu_q65"`<br>`"vidu_q66"`<br>`"vidu_q67"`<br>`"vidu_q68"`<br>`"vidu_q69"`<br>`"vidu_q70"`<br>`"vidu_q71"`<br>`"vidu_q72"`<br>`"vidu_q73"`<br>`"vidu_q74"`<br>`"vidu_q75"`<br>`"vidu_q76"`<br>`"vidu_q77"`<br>`"vidu_q78"`<br>`"vidu_q79"`<br>`"vidu_q80"`<br>`"vidu_q81"`<br>`"vidu_q82"`<br>`"vidu_q83"`<br>`"vidu_q84"`<br>`"vidu_q85"`<br>`"vidu_q86"`<br>`"vidu_q87"`<br>`"vidu_q88"`<br>`"vidu_q89"`<br>`"vidu_q90"`<br>`"vidu_q91"`<br>`"vidu_q92"`<br>`"vidu_q93"`<br>`"vidu_q94"`<br>`"vidu_q95"`<br>`"vidu_q96"`<br>`"vidu_q97"`<br>`"vidu_q98"`<br>`"vidu_q99"`<br>`"vidu_q100"` | 用於影片生成的模型名稱（預設值："vidu_q1"） |
| `images` | IMAGE | 是 | - | 用作參考的圖片，用於生成具有一致主題的影片（最多 7 張圖片） |
| `prompt` | STRING | 是 | - | 用於影片生成的文字描述 |
| `duration` | INT | 否 | 5-5 | 輸出影片的持續時間，單位為秒（預設值：5） |
| `seed` | INT | 否 | 0-2147483647 | 影片生成的種子值（0 表示隨機）（預設值：0） |
| `aspect_ratio` | COMBO | 否 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | 輸出影片的長寬比（預設值："16:9"） |
| `resolution` | COMBO | 否 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"1440p"`<br>`"2160p"` | 支援的數值可能因模型和持續時間而異（預設值："1080p"） |
| `movement_amplitude` | COMBO | 否 | `"auto"`<br>`"low"`<br>`"medium"`<br>`"high"` | 畫面中物體的動態幅度（預設值："auto"） |

**限制與約束：**

- `prompt` 欄位為必填，不能為空
- 最多允許使用 7 張參考圖片
- 每張圖片的長寬比必須在 1:4 到 4:1 之間
- 每張圖片的最小尺寸必須為 128x128 像素
- 持續時間固定為 5 秒

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 基於參考圖片和提示生成的影片 |