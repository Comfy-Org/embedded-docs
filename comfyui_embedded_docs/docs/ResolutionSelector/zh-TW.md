# 解析度選擇器

Resolution Selector 節點會根據所選的長寬比，以及以百萬像素為單位的目標總解析度，計算像素寬度與高度。此節點適合用來為其他節點（例如 Empty Latent Image 節點）產生一致的尺寸。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `長寬比` | 輸出尺寸的長寬比（預設：`"1:1 (Square)"`）。 | COMBO | 是 | `"1:1 (Square)"`<br>`"2:3 (Portrait Photo)"`<br>`"3:2 (Photo)"`<br>`"3:4 (Portrait Standard)"`<br>`"4:3 (Standard)"`<br>`"9:16 (Portrait Widescreen)"`<br>`"16:9 (Widescreen)"`<br>`"21:9 (Ultrawide)"` |
| `百萬像素` | 目標總百萬像素。對於正方形，1.0 MP ≈ 1024x1024（預設：1.0）。 | FLOAT | 是 | 0.1 - 16.0 （步進值：0.1） |
| `預覽` | 計算後輸出解析度的即時預覽。此唯讀小工具會自動更新，且不接受使用者輸入。 | RESOLUTION_PREVIEW | 否 | N/A |
| `倍數` | 用來將計算結果調整為最接近的倍數，以設定所選解析度（預設：8）。 | INT | 否 | 8 - 128 （步進值：4） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `width` | 計算出的像素寬度乘以所選倍數。 | INT |
| `height` | 計算出的像素高度乘以所選倍數。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dd4c7f977ed69a873a48da4b01c5c8f0b6563cfd743740235fc0ad5762579697`
