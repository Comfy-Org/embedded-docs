> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/zh-TW.md)

## 概述

對文字進行編碼並設定 PixArt Alpha 的解析度條件。此節點處理文字輸入並添加寬度和高度資訊，以建立專用於 PixArt Alpha 模型的條件資料。此節點不適用於 PixArt Sigma 模型。

## 輸入

| 參數 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `寬度` | INT | 輸入 | 1024 | 0 至 MAX_RESOLUTION | 用於解析度條件設定的寬度尺寸 |
| `高度` | INT | 輸入 | 1024 | 0 至 MAX_RESOLUTION | 用於解析度條件設定的高度尺寸 |
| `文字` | STRING | 輸入 | - | - | 要編碼的文字輸入，支援多行輸入和動態提示詞 |
| `clip` | CLIP | 輸入 | - | - | 用於分詞和編碼的 CLIP 模型 |

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 包含文字標記和解析度資訊的編碼條件資料 |