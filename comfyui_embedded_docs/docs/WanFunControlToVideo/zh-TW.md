> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunControlToVideo/zh-TW.md)

此節點是為了支援阿里巴巴萬 Fun Control 模型進行影片生成而添加的，在[此提交](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82)後加入。

- **用途：** 使用 Wan 2.1 Fun Control 模型準備影片生成所需的條件資訊。

WanFunControlToVideo 節點是 ComfyUI 的擴充功能，旨在支援萬 Fun Control 模型進行影片生成，專門用於利用萬 Fun 控制來創建影片。

此節點作為必要條件資訊的準備點，並初始化潛在空間的中心點，引導後續使用 Wan 2.1 Fun 模型的影片生成過程。節點名稱清楚表明了其功能：接受各種輸入並將其轉換為適合在萬 Fun 框架內控制影片生成的格式。

該節點在 ComfyUI 節點層級中的位置表明它在影片生成流程的早期階段運作，專注於在實際取樣或解碼影片幀之前操作條件信號。

## 輸入參數

| 參數名稱            | 必填     | 資料類型           | 描述                                                  | 預設值 |
|:-------------------|:---------|:-------------------|:-----------------------------------------------------|:------|
| positive           | 是       | CONDITIONING       | 標準 ComfyUI 正向條件資料，通常來自 "CLIP Text Encode" 節點。正向提示詞描述使用者對生成影片內容、主題和藝術風格的設想。 | 無  |
| negative           | 是       | CONDITIONING       | 標準 ComfyUI 負向條件資料，通常由 "CLIP Text Encode" 節點生成。負向提示詞指定使用者希望在生成影片中避免的元素、風格或瑕疵。 | 無  |
| vae                | 是       | VAE                | 需要與 Wan 2.1 Fun 模型系列相容的 VAE（變分自編碼器）模型，用於編碼和解碼圖像/影片資料。 | 無  |
| width              | 是       | INT                | 輸出影片幀的期望寬度（像素），預設值為 832，最小值為 16，最大值由 nodes.MAX_RESOLUTION 決定，步長為 16。 | 832  |
| height             | 是       | INT                | 輸出影片幀的期望高度（像素），預設值為 480，最小值為 16，最大值由 nodes.MAX_RESOLUTION 決定，步長為 16。 | 480  |
| length             | 是       | INT                | 生成影片的總幀數，預設值為 81，最小值為 1，最大值由 nodes.MAX_RESOLUTION 決定，步長為 4。 | 81   |
| batch_size         | 是       | INT                | 單次批次生成的影片數量，預設值為 1，最小值為 1，最大值為 4096。 | 1    |
| clip_vision_output | 否       | CLIP_VISION_OUTPUT | （可選）由 CLIP 視覺模型提取的視覺特徵，允許進行視覺風格和內容引導。 | 無 |
| start_image        | 否       | IMAGE              | （可選）影響生成影片開頭的初始圖像。 | 無 |
| control_video      | 否       | IMAGE              | （可選）允許使用者提供預處理的 ControlNet 參考影片，該影片將引導生成影片的運動和潛在結構。| 無 |

## 輸出參數

| 參數名稱            | 資料類型           | 描述                                                  |
|:-------------------|:-------------------|:-----------------------------------------------------|
| positive           | CONDITIONING       | 提供增強的正面條件資料，包括編碼後的 `start_image` 和 `control_video`。 |
| negative           | CONDITIONING       | 提供同樣經過增強的負面條件資料，包含相同的 `concat_latent_image`。 |
| latent             | LATENT             | 包含帶有 "samples" 鍵的空潛在張量的字典。 |