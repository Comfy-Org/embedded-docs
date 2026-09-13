# BriaRelight

此節點使用 Bria 改變影像的光線氛圍與方向。影像會由 Bria 重新渲染，因此結果不會與輸入像素對齊；整個畫面會以約 1 百萬像素重新生成。

## 輸入

### 通用輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image` | 要改變光線的影像。上傳影像前會先移除任何 alpha 通道。 | IMAGE | 是 | - |
| `light_type` | 要套用的光線氛圍。 | COMBO | 是 | `"midday"`<br>`"blue hour light"`<br>`"low-angle sunlight"`<br>`"sunrise light"`<br>`"spotlight on subject"`<br>`"overcast light"`<br>`"soft overcast daylight lighting"`<br>`"cloud-filtered lighting"`<br>`"fog-diffused lighting"`<br>`"moonlight lighting"`<br>`"starlight nighttime"`<br>`"soft bokeh lighting"`<br>`"harsh studio lighting"` |
| `light_direction` | 光線來源的方向。硬光氛圍（例如 midday、spotlight on subject 與 harsh studio lighting）對其反應最為明顯。 | COMBO | 是 | `"front"`<br>`"side"`<br>`"bottom"`<br>`"top-down"` |
| `moderation` | 審核設定。選擇 `"true"` 會顯示審核選項，選擇 `"false"` 則不啟用這些選項。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |

### 審核輸入

當 `moderation` 設為 `"true"` 時會顯示這些選項。

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | 對輸入影像啟用內容審核。預設：false。 | BOOLEAN | No | `true`<br>`false` |
| `visual_output_moderation` | 對生成的輸出影像啟用內容審核。預設：false。 | BOOLEAN | No | `true`<br>`false` |

注意：Bria 會以約 1 百萬像素重新渲染整個畫面，因此結果不會與輸入像素對齊。

## 輸出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `image` | Bria 傳回的打光調整後影像。 | IMAGE |
| `structured_prompt` | 編輯後影像的結構化描述，可用於後續以 Bria FIBO Image Edit 進行編輯。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRelight/zh-TW.md)

---
**Source fingerprint (SHA-256):** `21fbe2186c99a7e8d99d5659ac25c3ab1a757492916dba4135487d4b293cb4f6`
