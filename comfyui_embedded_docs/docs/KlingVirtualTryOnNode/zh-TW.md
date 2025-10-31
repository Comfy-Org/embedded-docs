> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/zh-TW.md)

{heading_overview}
Kling 虛擬試穿節點。輸入人體圖像和服裝圖像，在人物身上試穿服裝。您可以將多件服裝物品圖片合併為一張白色背景的圖像。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `human_image` | IMAGE | 是 | - | 要試穿服裝的人體圖像 |
| `cloth_image` | IMAGE | 是 | - | 要在人體上試穿的服裝圖像 |
| `model_name` | STRING | 是 | `"kolors-virtual-try-on-v1"` | 要使用的虛擬試穿模型（預設："kolors-virtual-try-on-v1"） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | IMAGE | 顯示人物試穿服裝物品後的最終圖像 |