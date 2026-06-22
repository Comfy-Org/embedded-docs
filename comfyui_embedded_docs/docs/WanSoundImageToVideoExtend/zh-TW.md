# 萬聲圖像轉影片擴展

WanSoundImageToVideoExtend 節點透過生成額外影格來擴展現有的影片潛在表示，可選擇性地由音訊、參考影像和控制影片引導。它接收起始的影片潛在表示，並產生更長的影片序列，利用提供的條件設定和音訊提示來影響新內容。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正面提示` | 正向條件提示，引導影片應包含的內容 | CONDITIONING | 是 | - |
| `負面提示` | 負向條件提示，指定影片應避免的內容 | CONDITIONING | 是 | - |
| `VAE` | 用於編碼和解碼影片影格的變分自編碼器 | VAE | 是 | - |
| `長度` | 要生成的影片序列總影格數（預設值：77，步長：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `影片潛在空間` | 作為擴展起點的初始影片潛在表示 | LATENT | 是 | - |
| `音訊編碼器輸出` | 可選的音訊嵌入，可根據聲音特徵影響影片生成 | AUDIOENCODEROUTPUT | 否 | - |
| `參考圖片` | 可選的參考影像，為影片生成提供視覺引導 | IMAGE | 否 | - |
| `控制影片` | 可選的控制影片，可引導生成影片的動作和風格 | IMAGE | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `負面提示` | 已套用影片上下文的處理後正向條件 | CONDITIONING |
| `潛在空間` | 已套用影片上下文的處理後負向條件 | CONDITIONING |
| `latent` | 包含擴展影片序列的生成影片潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fc9aee5d51e96b864da7d75f592f07691be8b970346998b209b3ad8a72308ecb`
