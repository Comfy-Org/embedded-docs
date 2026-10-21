# VEED Lipsync 2.0

使用 VEED Lipsync 將影片中講者的嘴型重新同步到新的語音軌。可用於為片段配音或替換其對白，同時保留原始影像。輸出會保留影片解析度，影格率為 25 fps，長度與音訊相同，且每段影片僅支援一位講者。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的模型。選擇模型後會顯示其專屬參數：`video`、`audio` 和 `seed`。 | DYNAMIC_COMBO | 是 | `"lipsync-2.0"` |
| `video` | 一位正面朝向鏡頭的講者影像。若影片短於音訊，影片會正播與倒播直到音訊結束。 | VIDEO | 是 | - |
| `audio` | 新的語音，最長 600 秒。會設定影片長度。 | AUDIO | 是 | 最多 600 秒 |
| `seed` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果皆不具確定性。（預設值：42） | INT | 是 | 0 至 2147483647 |

當語音軌長度超過 600 秒，或 VEED 工作失敗時，節點會停止並顯示錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `VIDEO` | 重新同步後的影片：原始影像，嘴型已對應到新的語音。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedLipsyncNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1a1e854b6923b5bad0fd6f3a79e76c70231dee31a12e9cf0b22be6bdcc741168`
