# Comfy Cloud MiniMax Music 3 文字轉音訊 [BETA]

此節點會在 Comfy Cloud GPU 上執行 MiniMax Music 3 工作流程，並回傳一首生成的歌曲。`prompt` 用於描述風格、配器與情緒；`lyrics` 會以演唱方式呈現，而非僅作描述，若 `lyrics` 留空，曲目會是純音樂。此為 Beta 節點，並依 GPU 秒數計費。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 歌曲描述：風格、配器與情緒。提交前會移除開頭與結尾的空白字元。 | STRING | 是 | 1 到 4096 個字元 |
| `歌詞` | 要演唱的歌詞。留空則為純音樂。 | STRING | 否 | 0 到 4096 個字元 |
| `種子` | 控制生成結果的隨機種子（預設值：42）。 | INT | 是 | 0 到 9223372036854775807 |
| `最長時長` | 曲目最長可持續的秒數（預設值：120.0）。模型可以提前結束歌曲。 | FLOAT | 是 | 0.04 到 360.0（步長 0.04） |
| `音訊品質` | 輸出位元率。`"V0"` 是可變位元率，且為三者中最高品質（預設值：`"V0"`）。 | COMBO | 是 | `"V0"`<br>`"128k"`<br>`"320k"` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `AUDIO` | 生成的歌曲。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxMusic3TextToAudioNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `defc8d97071f2eaef4b00c6df721f4d10756e4867fefa22c1db7b8c3aafb6b7b`
