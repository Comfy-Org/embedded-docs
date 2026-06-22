# Reve 圖像混合

Reve 圖像重混節點使用 Reve API 來生成新圖像。它將一張或多張參考圖像與文字提示相結合，根據提供的描述創建新的重混圖像。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `參考圖像` | 作為重混基礎的一張或多張參考圖像。您可以添加 1 到 6 張圖像。 | IMAGE | 是 | 1 到 6 張圖像 |
| `提示詞` | 所需圖像的文字描述。您可以包含 XML `<img>` 標籤來按索引引用特定圖像（例如 `<img>0</img>`、`<img>1</img>`）。（預設值：空） | STRING | 是 | 1 到 2560 個字元 |
| `模型` | 用於重混的模型版本。每個模型選項都包含可配置的長寬比和測試時縮放設定。 | COMBO | 是 | `reve-remix@20250915`<br>`reve-remix-fast@20251030` |
| `放大` | 控制是否對生成的圖像進行放大。啟用時，您可以選擇放大倍數。 | COMBO | 否 | `"disabled"`<br>`"enabled"` |
| `去背` | 啟用時，嘗試移除生成圖像的背景。 | BOOLEAN | 否 | `true`<br>`false` |
| `種子` | 種子值。更改此值將導致節點重新執行，但無論種子如何，結果都是非確定性的。（預設值：0） | INT | 否 | 0 到 2147483647 |

**注意：** `model` 參數是一個動態組合，包含 `aspect_ratio`（選項："auto"、"16:9"、"9:16"、"3:2"、"2:3"、"4:3"、"3:4"、"1:1"）和 `test_time_scaling` 的嵌套設定。`upscale` 參數設定為 "enabled" 時，會顯示嵌套的 `upscale_factor` 設定。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `image` | 由 Reve 重混過程生成的新圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e64dccddfd55ebaa7e28bf17c2a5ff1a0c130db1475e307940b75106c788f687`
