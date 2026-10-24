# VEED Remove Video Background

使用 VEED 將主體從影片中去背，並回傳影格與 Alpha 遮罩。可將這兩個輸出用於合成，或將它們送至 Join Image with Alpha 與 Save WEBM，以輸出透明影片。若要在任何背景下獲得最佳邊緣，請選擇 `"standard"`；若重視速度，請選擇 `"fast"`；若素材是對綠幕拍攝，請選擇 `"green screen"`。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的分割模型：`"standard"` 適用於任何背景，可提供最佳邊緣，輸出最高可達 3840x2160；`"fast"` 可更快取得結果，最高可達 1920x1080；`"green screen"` 可去背綠幕背景，最高可達 3840x2160。較大的影片會被縮小。選取某個選項後會顯示其參數。 | DYNAMIC_COMBO | 是 | `"standard"`<br>`"fast"`<br>`"green screen"` |
| `video` | 要從中將主體去背的影片。最多 60 秒。 | VIDEO | 是 | 最多 60 秒 |
| `refine_foreground_edges` | 讓頭髮、毛髮與細節的邊緣更乾淨。關閉此選項可降低費用。適用於 `"standard"` 與 `"fast"`（預設：True）。 | BOOLEAN | 是 | false<br>true |
| `subject_is_person` | 當主體是物件或動物時請關閉。適用於 `"standard"` 與 `"fast"`（預設：True）。 | BOOLEAN | 是 | false<br>true |
| `spill_suppression_strength` | 從主體移除綠色溢色的強度。若仍有綠色斑點殘留，請提高此值；若主體顏色偏移，請降低此值。適用於 `"green screen"`（預設：0.8）。 | FLOAT | 是 | 0.0 至 1.0（步長 0.01） |

影片片段上限為 60 秒；較長的影片會回報錯誤並遭到拒絕。在背景被移除的位置，遮罩值為 1，因此若你想保留主體，請在 Image Composite Masked 之前先使用 Invert Mask。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `images` | 已移除背景的影片影格。 | IMAGE |
| `mask` | 逐影格標示背景被移除的位置為 1。 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedRemoveVideoBackgroundNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1bf52a380ab09437a5a57f70215856d4ea0055f78ce8b42fe2a2b87d686e8d26`
