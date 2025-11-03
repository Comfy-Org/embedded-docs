> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNETLoader/zh-TW.md)

UNETLoader 節點專為透過名稱載入 U-Net 模型而設計，便於在系統中使用預訓練的 U-Net 架構。

此節點會偵測位於 `ComfyUI/models/diffusion_models` 資料夾中的模型。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
|----------|--------------|-------------|
| `unet_name` | COMBO[STRING] | 指定要載入的 U-Net 模型名稱。此名稱用於在預定義的目錄結構中定位模型，實現不同 U-Net 模型的動態載入。 |
| `weight_dtype` | ... | 🚧  fp8_e4m3fn fp9_e5m2  |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
|----------|-------------|-------------|
| `model`   | MODEL     | 返回已載入的 U-Net 模型，使其可在系統中用於進一步處理或推論。 |