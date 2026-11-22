# Creatify Boreal-H3 Video

Creatify Boreal-H3 Video 會依照文字提示產生帶有聲音的影片，使用 Creatify 專為影片廣告打造、經後訓練的 H3 模型。連接第一幀可讓靜態影像動起來，並可選擇連接最後一幀，讓鏡頭結束於所選影像。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述影片的文字提示。必須包含至少一個非空白字元。 | STRING | 是 | 任意非空文字 |
| `first_frame` | 影片起始的影像。連接此項時，請將 `aspect_ratio` 保持為 `"auto"`，讓影片依循該影像。 | IMAGE | 否 | - |
| `last_frame` | 影片結束的影像。需要已連接的 `first_frame`。 | IMAGE | 否 | - |
| `resolution` | 輸出影片的解析度（預設：`"768p"`）。 | COMBO | 是 | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | 輸出影片的長寬比。連接第一幀時，`"auto"` 會依循第一幀；在該情況下請保持為 `"auto"`（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | 影片長度，以秒為單位（預設：5）。在 `"2k"` 時，最大值為 14 秒。 | INT | 是 | 1 至 15（步進值：1） |
| `prompt_enhancement` | Creatify 在渲染前如何改寫提示：`"auto"` 與 `"ads"` 會將其轉為影片廣告提示，並可加入口播台詞；`"general"` 會將其改寫為適用於其他影片的提示；`"none"` 則依原樣渲染（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | `seed` 控制節點是否重新執行。不會傳送 `seed` 給 Boreal-H3，因此以相同輸入重新執行可能產生不同的影片（預設：42）。 | INT | 是 | 0 至 2147483647 |

**限制：** 使用 `first_frame` 時，長寬比一律取自該影像，因此任何其他 `aspect_ratio` 值都會引發錯誤。沒有 `first_frame` 的 `last_frame` 會被拒絕，且在 `"2k"` 時，`duration` 超過 14 秒也會被拒絕。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 產生的含聲音影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3VideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `535bcbeced69cffd4d0edca04f30dd00dac4ec728cd8eb638b4f9d9af8448336`
