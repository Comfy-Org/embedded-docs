# VEED Clean Audio

使用 VEED 移除語音中的背景雜訊。它專為任何語言的語音而設計：人聲底下的雜訊會被清除、停頓會被徹底清理，而音樂與音效會被移除而非保留。輸出為 48 kHz 單聲道音訊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio` | 語音錄音，長度需短於 30 分鐘。 | AUDIO | 是 | 最多 1799 秒 |
| `strength` | 控制人聲下方雜訊的移除程度。較低值會保留較多人聲背後的室內底噪；字詞之間的停頓一律會徹底清理，而高於預設值時，效果變化不大。（預設值：0.874） | FLOAT | 是 | 0.0 至 1.0（步進 0.001） |
| `loudness` | 是否將輸出音量正規化。`"normalize"` 會將輸出設為 `target_lufs`；`"keep input level"` 會維持原本音量。選取選項後會顯示其參數。（預設值：`"normalize"`） | DYNAMIC_COMBO | 是 | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | 輸出的整體響度（LUFS）。峰值上限為 -1.1 dBTP，因此響度目標偏大時會提早停止（一般語音約為 -15 LUFS）。當 `loudness` 為 `"normalize"` 時可用（預設值：-19.0）。 | FLOAT | 是 | -40.0 至 -8.0（步進 0.1） |

當錄音長度超過 1799 秒時，此節點會停止並顯示錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `AUDIO` | 清理後的語音，為 48 kHz 單聲道音訊。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanAudioNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c85949385109a5d320e52619e9df17c245b19f8f16cc1a0b69a37ae2e7bb5b6d`
