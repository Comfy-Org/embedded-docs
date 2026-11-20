# HeyGen Decision (Choice)

針對你連接的文字、影像、音訊或影片，從你自己提供的選項中挑選一個，並取回所選的選項、其位置與信心分數。將 `choice` 連接到 Branch 節點（其輸入帶有相同的選項名稱），或依 `option_index` 進行路由。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型。`heygen-decision-1-turbo` 比 `heygen-decision-1` 更快且成本更低（預設：`"heygen-decision-1"`）。 | COMBO | 是 | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | 選項所回答的問題，最多 5000 個字元（預設："What style is the image?"）。 | STRING | 是 | 1 至 5000 個字元 |
| `options` | 每行一個選項，會完全依照輸入內容使用，每個選項最多 128 個字元。針對不符合任何選項的輸入，新增例如 `other` 的選項（預設：`photo`、`illustration`、`3d render`、`anime`、`sketch`、`other`）。 | STRING | 是 | 2 至 255 個選項 |
| `images` | 要分類的影像，總共最多 4 張，批次中的每個影格都會計入。這些影像會依序跨各個插槽編號為 `image_1` 至 `image_4`。 | IMAGE | 否 | 最多 4 張影像 |
| `audio_1` | 要分類的音訊，最多 30 分鐘。 | AUDIO | 否 | 最多 30 分鐘 |
| `video_1` | 要分類的影片，最多 60 秒。 | VIDEO | 否 | 最多 60 秒 |
| `text` | 問題所針對的文字，例如提示詞或 LLM 回應，最多 20000 個字元。 | STRING | 否 | 最多 20000 個字元 |

請提供 2 至 255 個選項，不得重複，且不得僅有字母大小寫不同，否則節點會引發錯誤。至少連接一個要分類的輸入，並在問題中依插槽名稱指名它們，例如「`image_1` 中顯示的是哪個季節？」。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `choice` | 所選的選項，內容與 `options` 中的寫法完全一致。 | STRING |
| `option_index` | 所選選項在 `options` 中的位置，從 0 開始。 | INT |
| `confidence` | 對此選擇的信心分數，介於 0 與 1 之間。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionChoice/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dd21b3b8021b8917e7ee4d120471974634ae6771ff17b0f49e9460f82a2fbe78`
