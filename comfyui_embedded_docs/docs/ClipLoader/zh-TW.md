# 載入 CLIP

CLIPLoader 節點會從檔案載入文字編碼器模型（CLIP、T5 或類似模型），使其可供其他需要將文字提示轉換為數值表示形式的節點使用。它支援多種模型架構，每種架構都需要特定的編碼器類型。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_name` | 要載入的文字編碼器模型檔案名稱。此檔案必須位於 `ComfyUI/models/text_encoders/` 目錄中。 | COMBO | 是 | 在 `text_encoders` 資料夾中找到的檔案清單 |
| `type` | 要載入之模型的架構類型。這決定了要使用哪個特定的編碼器變體（預設：`"stable_diffusion"`）。 | COMBO | 是 | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"` |
| `device` | 要載入模型的裝置。`"default"` 使用預設裝置（通常為可用的 GPU），而 `"cpu"` 則強制使用 CPU 載入。這是進階選項（預設：`"default"`）。 | COMBO | 否 | `"default"`<br>`"cpu"` |

### 支援的類型與編碼器對應表

`type` 參數會為給定的模型架構選擇正確的編碼器。以下為節點描述中列出的常見對應關係：

| 類型 | 編碼器 |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl（226 個 token 的填充） |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1（建議）或 t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL 或 Music3 Qwen/RVQ |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `clip` | 已載入的文字編碼器模型，可直接連接到其他節點進行文字編碼與條件化處理。 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7c1586d01410d319468f7c8c153ef0717280804add868ba57bff0c6539fb5dd9`
