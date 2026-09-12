# 載入 CLIP

CLIPLoader 節點會從檔案載入文字編碼器模型（CLIP、T5 或類似模型），使其可供其他需要將文字提示轉換為數值表示的節點使用。它支援多種模型架構，每種架構都需要特定的編碼器類型。

## 輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `clip_name` | 要載入的文字編碼器模型檔案名稱。此檔案必須位於 `ComfyUI/models/text_encoders/` 目錄中。 | STRING | Yes | List of files found in the `text_encoders` folder |
| `type` | 要載入的模型架構類型。這決定了使用哪一種特定的編碼器變體（預設：`"stable_diffusion"`）。 | COMBO | Yes | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"`<br>`"yue2"` |
| `device` | 要將模型載入到的裝置。`"default"` 會在可用時使用 GPU，而 `"cpu"` 則強制使用 CPU 載入。這是進階選項（預設：`"default"`）。 | COMBO | No | `"default"`<br>`"cpu"` |

### 支援的類型與編碼器對應關係

`type` 參數會為指定的模型架構選擇正確的編碼器。以下為常見的對應關係：

| Type | Encoder |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (226-token padding) |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (recommended) or t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL or Music3 Qwen/RVQ |

## 輸出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `CLIP` | 已載入的文字編碼器模型，可直接連接到其他節點，用於文字編碼與條件控制。 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6df608d500520d9414acd82d9fd509b1e211a8385202cefd5579e8a8f397bc64`
