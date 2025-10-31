> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionEncode/zh-TW.md)

`CLIP Vision Encode` 節點是 ComfyUI 中的圖像編碼節點，用於透過 CLIP Vision 模型將輸入圖像轉換為視覺特徵向量。此節點是連接圖像與文字理解的重要橋樑，廣泛應用於各種 AI 圖像生成與處理工作流程中。

## 節點功能

- **圖像特徵提取**：將輸入圖像轉換為高維特徵向量
- **多模態橋接**：為圖像與文字的聯合處理提供基礎
- **條件生成**：為基於圖像的條件生成提供視覺條件

## 輸入參數

| 參數名稱        | 資料類型       | 描述                                                         |
| --------------- | ------------- | ------------------------------------------------------------ |
| `clip_vision`   | CLIP_VISION   | CLIP 視覺模型，通常透過 CLIPVisionLoader 節點載入            |
| `image`         | IMAGE         | 要進行編碼的輸入圖像                                         |
| `crop`          | Dropdown      | 圖像裁剪方式，選項：center（中心裁剪）、none（不裁剪）       |

## 輸出結果

| 輸出名稱            | 資料類型            | 描述                     |
| ------------------- | ------------------ | ------------------------ |
| CLIP_VISION_OUTPUT  | CLIP_VISION_OUTPUT | 編碼後的視覺特徵         |

此輸出物件包含：

- `last_hidden_state`：最後隱藏狀態
- `image_embeds`：圖像嵌入向量
- `penultimate_hidden_states`：倒數第二隱藏狀態
- `mm_projected`：多模態投影結果（如果可用）