> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/zh-TW.md)

{heading_overview}

LTXVCropGuides 節點透過移除關鍵影格資訊並調整潛在空間維度，為影片生成處理條件輸入和潛在輸入。它會裁剪潛在影像和噪聲遮罩以排除關鍵影格區段，同時清除正負條件輸入中的關鍵影格索引。這為不需要關鍵影格引導的影片生成工作流程準備資料。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `正向` | CONDITIONING | 是 | - | 包含生成引導資訊的正向條件輸入 |
| `負向` | CONDITIONING | 是 | - | 包含生成中應避免內容引導資訊的負向條件輸入 |
| `潛在空間` | LATENT | 是 | - | 包含影像樣本和噪聲遮罩資料的潛在表示 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `正向` | CONDITIONING | 已清除關鍵影格索引的處理後正向條件 |
| `負向` | CONDITIONING | 已清除關鍵影格索引的處理後負向條件 |
| `潛在空間` | LATENT | 包含調整後樣本和噪聲遮罩的裁剪潛在表示 |