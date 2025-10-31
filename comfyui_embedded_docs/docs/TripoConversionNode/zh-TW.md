> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/zh-TW.md)

TripoConversionNode 使用 Tripo API 在不同檔案格式之間轉換 3D 模型。它接收來自先前 Tripo 操作的任務 ID，並將結果模型轉換為您所需的格式，提供多種匯出選項。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | 是 | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | 來自先前 Tripo 操作（模型生成、綁定或重新定位）的任務 ID |
| `format` | COMBO | 是 | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | 轉換後 3D 模型的目標檔案格式 |
| `quad` | BOOLEAN | 否 | True/False | 是否將三角形轉換為四邊形（預設值：False） |
| `face_limit` | INT | 否 | -1 到 500000 | 輸出模型中的最大面數，使用 -1 表示無限制（預設值：-1） |
| `texture_size` | INT | 否 | 128 到 4096 | 輸出紋理的像素大小（預設值：4096） |
| `texture_format` | COMBO | 否 | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | 匯出紋理的格式（預設值：JPEG） |

**注意：** `original_model_task_id` 必須是來自先前 Tripo 操作（模型生成、綁定或重新定位）的有效任務 ID。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| *無命名輸出* | - | 此節點以非同步方式處理轉換，並透過 Tripo API 系統返回結果 |