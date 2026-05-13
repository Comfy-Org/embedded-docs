> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/zh-TW.md)

CLIPLoader 節點從檔案載入文字編碼器模型（CLIP、T5 或類似模型），使其可用於其他需要將文字提示轉換為數值表示的節點。它支援多種模型架構，每種架構都需要特定的編碼器類型。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip_name` | STRING | 是 | 在 `text_encoders` 資料夾中找到的檔案列表 | 要載入的文字編碼器模型檔案名稱。此檔案必須位於 `ComfyUI/models/text_encoders/` 或 `ComfyUI/models/clip/` 目錄中。 |
| `type` | STRING | 是 | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"` | 正在載入的模型架構類型。這決定了要使用的特定編碼器變體。預設值為 `"stable_diffusion"`。 |
| `device` | STRING | 否 | `"default"`<br>`"cpu"` | 載入模型的裝置。`"default"` 在可用時使用 GPU，而 `"cpu"` 則強制使用 CPU 載入。這是一個進階選項（預設值：`"default"`）。 |

### 支援的類型到編碼器對應關係

`type` 參數會為給定的模型架構選擇正確的編碼器。以下是常見的對應關係：

| 類型 | 編碼器 |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl（226 個標記填充） |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1（建議）或 t5 |
| omnigen2 | qwen vl 2.5 3B |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `clip` | CLIP | 已載入的文字編碼器模型，可連接到其他節點以進行文字編碼和條件設定。 |

---
**Source fingerprint (SHA-256):** `1051bfe5570dff81719682cb09938bae4c03e94e0e72f7a2be84867cccb48017`
