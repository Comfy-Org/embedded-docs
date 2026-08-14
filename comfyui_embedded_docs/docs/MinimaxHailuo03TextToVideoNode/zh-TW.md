# MinimaxHailuo03TextToVideoNode

此節點使用 MiniMax H3 模型，根據文字提示產生影片。它會將文字連同解析度、時間長度與寬高比等影片設定傳送至 MiniMax API，並將產生的影片作為輸出回傳。

## 輸入
| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於影片產生的模型。（預設值："MiniMax H3"）此選項同時包含所產生影片的文字提示、解析度、時間長度與寬高比設定。 | COMBO | 是 | `"MiniMax H3"` |
| `隨機種子` | 隨機種子。使用相同種子的相同請求會產生相似但不保證完全相同的結果。（預設值：42） | INT | 是 | 0 至 4294967295 |
| `浮水印` | 是否在影片中加入 AIGC 浮水印。（預設值：false） | BOOLEAN | 否 | true<br>false |

注意：`model` 選項中包含的文字提示必須至少包含一個非空白字元。此節點顯示的預估價格是根據所選的影片時間長度計算。

## 輸出
| 輸出名 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `VIDEO` | 根據提供的文字提示所產生的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9478576dd02ed407a39c95c7227eb8e1482db8b77adc814691fbd807e4cc2893`
