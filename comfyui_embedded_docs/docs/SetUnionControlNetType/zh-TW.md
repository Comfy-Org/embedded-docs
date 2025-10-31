> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/zh-TW.md)

SetUnionControlNetType 節點允許您指定用於條件控制的控制網路類型。它接收現有的控制網路，並根據您的選擇設定其控制類型，創建一個具有指定類型配置的控制網路修改副本。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `control_net` | CONTROL_NET | 是 | - | 需要設定新類型設定的控制網路 |
| `type` | STRING | 是 | `"auto"`<br>所有可用的 UNION_CONTROLNET_TYPES 鍵值 | 要應用的控制網路類型。使用 "auto" 進行自動類型檢測，或從可用選項中選擇特定的控制網路類型 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `control_net` | CONTROL_NET | 已應用指定類型設定的修改後控制網路 |