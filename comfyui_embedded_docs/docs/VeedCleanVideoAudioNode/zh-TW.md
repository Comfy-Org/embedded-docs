# VEED Clean Audio (in Video)

使用 VEED 移除影片中語音的背景噪音。只有音軌會改變：它會被替換為清理後的 48 kHz 單聲道語音，而畫面、解析度和幀率保持不變。它專為任何語言的語音而設計，音樂和音效會被移除而不是保留。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 帶有語音音軌的影片，長度短於 30 分鐘。影片必須有音軌。 | VIDEO | 是 | 最多 1799 秒 |
| `strength` | 語音下方移除多少噪音。較低值會在聲音背後保留更多室內底噪；字詞之間的停頓始終會完全清理，而高於預設值的數值變化不大。（預設值：0.874） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.001） |
| `loudness` | 是否將語音音量標準化。`"normalize"` 會將其設為 `target_lufs`；`"keep input level"` 則保持原本的音量。選取選項後會顯示其參數。（預設值：`"normalize"`） | DYNAMIC_COMBO | 是 | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | 清理後語音的整體響度，單位為 LUFS。峰值上限為 -1.1 dBTP，因此大聲的目標會提前停止（典型語音約為 -15 LUFS）。當 `loudness` 為 `"normalize"` 時可用（預設值：-19.0）。 | FLOAT | 是 | -40.0 至 -8.0 （步進值：0.1） |

當片段長於 1799 秒，或影片沒有音軌時，節點會停止並報錯。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `VIDEO` | 輸入影片，其音軌已替換為清理後的語音。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanVideoAudioNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b8ff533f3ce45691cccd3449596252b0216178fdef0e7e728ccccbc9a8712217`
