> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetLoader/zh-TW.md)

此節點會偵測位於 `ComfyUI/models/controlnet` 資料夾中的模型，也會讀取在 extra_model_paths.yaml 檔案中設定的其他路徑中的模型。有時，您可能需要**重新整理 ComfyUI 介面**，以便讓它從對應的資料夾中讀取模型檔案。

ControlNetLoader 節點旨在從指定路徑載入 ControlNet 模型。它在初始化 ControlNet 模型中扮演關鍵角色，這些模型對於對生成的內容應用控制機制，或根據控制訊號修改現有內容至關重要。

## 輸入

| 欄位               | Comfy 資料類型    | 說明                                                                           |
|-------------------|-------------------|-----------------------------------------------------------------------------------|
| `control_net_name`| `COMBO[STRING]`    | 指定要載入的 ControlNet 模型名稱，用於在預定義的目錄結構中定位模型檔案。 |

## 輸出

| 欄位            | Comfy 資料類型   | 說明                                                              |
|----------------|---------------|--------------------------------------------------------------------------|
| `control_net`  | `CONTROL_NET` | 回傳已載入的 ControlNet 模型，準備好用於控制或修改內容生成流程。 |