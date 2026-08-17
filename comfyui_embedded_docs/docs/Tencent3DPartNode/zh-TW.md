# Hunyuan3D：3D零件

此節點使用騰訊 Hunyuan3D API 自動分析 3D 模型，並根據模型結構識別或生成其組件。它處理模型並返回一個新的 FBX 檔案。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | FBX 格式的 3D 模型。模型應少於 30000 個面。 | FILE3D | 是 | FBX, Any |
| `seed` | 種子（seed）控制節點是否應重新執行；無論種子為何，結果都是不確定的。(預設值：0) | INT | 否 | 0 to 2147483647 |

**注意：** `model_3d` 輸入僅支援 FBX 格式的檔案。如果提供了其他 3D 檔案格式，節點將引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `FBX` | 處理後的 3D 模型，以 FBX 檔案形式返回。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `827b42559f4b2c341f08c58f53778d27c1c6afce607c36c8d1eae7c208c6a738`
