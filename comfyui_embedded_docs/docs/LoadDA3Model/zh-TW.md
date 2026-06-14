# 載入 Depth Anything 3

此節點從檔案載入 Depth Anything 3 模型，準備用於深度估計任務。它允許您選擇模型檔案，並可選擇指定模型權重的數值精度（資料類型）。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 要載入的 Depth Anything 3 模型檔案名稱。 | STRING | 是 | `geometry_estimation` 資料夾中可用的模型檔案列表 |
| `weight_dtype` | 模型權重的數值精度（資料類型）。"default" 選項使用模型的原始精度。（預設值："default"） | STRING | 否 | `"default"`<br>`"fp16"`<br>`"bf16"`<br>`"fp32"` |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `DA3_MODEL` | 已載入的 Depth Anything 3 模型，可用於深度估計工作流程。 | DA3_MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadDA3Model/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b1b3f4075cd9172bc1f274848b9300bca20d3cbd53b23d3c4a9f0986b36e409e`
