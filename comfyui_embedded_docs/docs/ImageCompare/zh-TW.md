## 概述

影像比較節點提供一個視覺化介面，讓您透過可拖曳的滑桿來並排比較兩張影像。此節點被設計為輸出節點，意味著它不會將資料傳遞給其他節點，而是直接在使用者介面中顯示影像以供檢查。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image_a` | 要比較的第一張影像。 | IMAGE | 否 | - |
| `image_b` | 要比較的第二張影像。 | IMAGE | 否 | - |
| `compare_view` | 啟用使用者介面中滑桿比較視圖的控制項。 | IMAGECOMPARE | 是 | - |

**注意：** 此節點為輸出節點。雖然 `image_a` 和 `image_b` 為選填，但至少必須提供一張影像，節點才能產生可見效果。對於未連接的影像輸入，節點將顯示空白區域。

## 輸出

此節點為輸出節點，不會產生任何可供其他節點使用的資料輸出。其功能是在 ComfyUI 介面中顯示所提供的影像。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2bc980cd20aad3cf60300868599bbce8eaba1cdb21880d2b3f4cd628108d8139`
