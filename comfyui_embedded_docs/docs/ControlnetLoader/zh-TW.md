> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetLoader/zh-TW.md)

此節點會偵測位於 `ComfyUI/models/controlnet` 資料夾中的模型，同時也會從 extra_model_paths.yaml 檔案中設定的額外路徑讀取模型。有時您可能需要**重新整理 ComfyUI 介面**，才能讓它從相應的資料夾讀取模型檔案。

ControlNetLoader 節點旨在從指定路徑載入 ControlNet 模型。它在初始化 ControlNet 模型方面扮演著關鍵角色，這些模型對於應用控制機制來生成內容或根據控制信號修改現有內容至關重要。

## 輸入參數

| 欄位名稱          | Comfy 資料類型    | 描述說明                                                                       |
|-------------------|-------------------|---------------------------------------------------------------------------------|
| `control_net_name`| `COMBO[STRING]`   | 指定要載入的 ControlNet 模型名稱，用於在預定義的目錄結構中定位模型檔案。        |

## 輸出結果

| 欄位名稱        | Comfy 資料類型   | 描述說明                                                                         |
|-----------------|------------------|----------------------------------------------------------------------------------|
| `control_net`   | `CONTROL_NET`    | 返回已載入的 ControlNet 模型，準備好用於控制或修改內容生成過程。                  |