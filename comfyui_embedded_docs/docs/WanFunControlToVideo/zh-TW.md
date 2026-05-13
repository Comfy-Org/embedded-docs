> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunControlToVideo/zh-TW.md)

此節點是為了支援阿里巴巴 Wan Fun Control 模型進行影片生成而新增的，並在[此提交](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82)之後加入。

- **目的：** 使用 Wan 2.1 Fun Control 模型，準備影片生成所需的條件資訊。

WanFunControlToVideo 節點是 ComfyUI 的擴充功能，旨在支援 Wan Fun Control 模型進行影片生成，目標是利用 WanFun 控制來創作影片。

此節點作為關鍵條件資訊的準備點，並初始化潛在空間的中心點，引導後續使用 Wan 2.1 Fun 模型的影片生成過程。節點名稱清楚說明了其功能：它接受各種輸入，並將其轉換為適合在 WanFun 框架內控制影片生成的格式。

該節點在 ComfyUI 節點層級中的位置表明，它在影片生成流程的早期階段運作，專注於在實際取樣或解碼影片幀之前處理條件訊號。

## 輸入

| 參數名稱            | 必要 | 資料類型           | 描述                                                                                                                               | 預設值 |
|:-------------------|:---------|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------|:-------------|
| positive           | 是      | CONDITIONING       | 標準的 ComfyUI 正向條件資料，通常來自「CLIP Text Encode」節點。正向提示詞描述了使用者期望生成影片中的內容、主題和藝術風格。 | N/A  |
| negative           | 是      | CONDITIONING       | 標準的 ComfyUI 負向條件資料，通常由「CLIP Text Encode」節點生成。負向提示詞指定了使用者希望在生成影片中避免的元素、風格或偽影。 | N/A  |
| vae                | 是      | VAE                | 需要一個與 Wan 2.1 Fun 模型系列相容的 VAE（變分自編碼器）模型，用於編碼和解碼影像/影片資料。 | N/A  |
| width              | 是      | INT                | 輸出影片幀的期望寬度（像素），預設值為 832，最小值為 16，最大值由 nodes.MAX_RESOLUTION 決定，步長為 16。 | 832  |
| height             | 是      | INT                | 輸出影片幀的期望高度（像素），預設值為 480，最小值為 16，最大值由 nodes.MAX_RESOLUTION 決定，步長為 16。 | 480  |
| length             | 是      | INT                | 生成影片的總幀數，預設值為 81，最小值為 1，最大值由 nodes.MAX_RESOLUTION 決定，步長為 4。 | 81   |
| batch_size         | 是      | INT                | 單一批次生成的影片數量，預設值為 1，最小值為 1，最大值為 4096。 | 1    |
| clip_vision_output | 否       | CLIP_VISION_OUTPUT | （可選）由 CLIP 視覺模型提取的視覺特徵，允許進行視覺風格和內容引導。 | None |
| start_image        | 否       | IMAGE              | （可選）影響生成影片開頭的初始影像。 | None |
| control_video      | 否       | IMAGE              | （可選）允許使用者提供預處理後的 ControlNet 參考影片，該影片將引導生成影片的運動和潛在結構。 | None |

## 輸出

| 參數名稱      | 資料類型           | 描述                                                                                                  |
|:-------------------|:-------------------|:-------------------------------------------------------------------------------------------------------------|
| positive           | CONDITIONING       | 提供增強的正面條件資料，包含編碼後的 start_image 和 control_video。 |
| negative           | CONDITIONING       | 提供同樣經過增強的負面條件資料，包含相同的 concat_latent_image。 |
| latent             | LATENT             | 一個字典，包含一個鍵值為「samples」的空潛在張量。 |