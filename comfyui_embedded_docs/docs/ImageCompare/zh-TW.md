# 圖像比較

## 概述

Image Compare 節點提供一個視覺化介面，可使用可拖曳的滑桿並排比較兩張影像。它被設計為輸出節點，這表示它不會將資料傳遞給其他節點，而是直接在使用者介面中顯示影像以供檢視。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image_a` | 要比較的第一張影像。 | IMAGE | 否 | - |
| `image_b` | 要比較的第二張影像。 | IMAGE | 否 | - |
| `compare_view` | 在 UI 中啟用滑桿比較檢視的控制項。 | IMAGECOMPARE | 是 | - |

**注意：** 此節點是輸出節點。雖然 `image_a` 和 `image_b` 是選填的，但必須至少提供一張影像，節點才會有可見效果。對於任何未連接的影像輸入，節點會顯示空白區域。每個提供的影像批次會分別以 `comfy.compare.a` 和 `comfy.compare.b` 為前綴儲存到暫存空間，然後顯示在滑桿檢視中。

## 輸出

此節點是輸出節點，不會產生任何可供其他節點使用的資料輸出。其功能是在 ComfyUI 介面中顯示所提供的影像。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bc065572c5631ed80c0590aabae775c51d0f607895a87cb2cca78037ab9a6638`
