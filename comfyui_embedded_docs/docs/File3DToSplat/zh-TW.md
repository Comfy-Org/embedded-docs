# 取得 Splat

此節點將包含高斯點雲資料的 3D 檔案轉換為可在節點圖中使用的高斯點雲格式。支援 PLY、SPLAT、KSPLAT 和 SPZ 檔案格式，系統會根據檔案內容自動偵測檔案格式。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `3D 模型` | 一個高斯點雲 3D 檔案 | FILE3D | 是 | - |

輸入檔案必須是以下支援格式之一：PLY、SPLAT、KSPLAT 或 SPZ。PLY 檔案包含完整的球諧函數資料，而其他格式僅包含基礎顏色資訊。系統會根據檔案內容自動偵測格式。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `splat` | 一個包含位置、縮放、旋轉、不透明度和球諧函數資料的高斯點雲 | SPLAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/File3DToSplat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9f45210a1366e57a91de6e1251f0e2e09f39e6498dbec1db7bf9826ebedd167b`
